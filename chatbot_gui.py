import wx
from wx.adv import Animation, AnimationCtrl
from typing import Callable
from threading import RLock
from concurrent.futures import ThreadPoolExecutor
import time
import pyttsx3

# define event id for sending a command to GUI from a thread
ID_COMMAND = wx.NewId()


# define result event
def evt_command(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_COMMAND, func)


# result event class
class CommandEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, task: str, data: str):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_COMMAND)

        # the task to perform and the data needed for the task
        self.task = task
        self.data = data


# main wx frame object
class Main(wx.Frame):
    def __init__(self, parent, title: str, gui: 'ChatbotGUI', gif_path: str, show_timestamp: bool = False):
        # init parent
        wx.Frame.__init__(self, parent, -1, title=title)

        # a reference to the chatbot GUI
        self.gui = gui

        # keeps track of the show_timestamp
        self.show_timestamp = show_timestamp

        # grid for splitting the screen into two parts, the gif and I/O elements
        self.grid = wx.BoxSizer(wx.HORIZONTAL)

        # user & AI message history
        self.user_message_history = []
        self.ai_message_history = []

        # panel for all of the I/O elements
        self.io_panel = wx.Panel(self)

        # the sizer for the panel I/O elements
        self.io_sizer = wx.BoxSizer(wx.VERTICAL)

        # chat bot animation asset
        self.chatbot_gif = Animation(gif_path)

        # animation controller for the chat bot gif
        self.chatbot_control = AnimationCtrl(self, -1, self.chatbot_gif)

        #
        # I/O elements
        #
        
        # input chat label
        self.input_chat_top_label = wx.StaticText(self.io_panel, label="Your History:")

        # Your chat history 
        self.input_chat = wx.TextCtrl(self.io_panel, size=wx.Size(400, 290), style=wx.TE_READONLY | wx.TE_MULTILINE)

        # input chat label
        self.input_chat_label = wx.StaticText(self.io_panel, label="Talk to AI:")

        # input chat text box
        self.input_box = wx.TextCtrl(self.io_panel, style=wx.TE_PROCESS_ENTER, size=wx.Size(400, 20))

        # input chat enter button
        self.chat_button = wx.Button(self.io_panel, label="Send your Text to AI Bot")

        # input chat label
        self.output_chat_label = wx.StaticText(self.io_panel, label="AI Response History:")

        # AI chat History
        self.output_chat = wx.TextCtrl(self.io_panel, size=wx.Size(400, 290), style=wx.TE_READONLY | wx.TE_MULTILINE)

        # ai status label
        self.ai_status_label = wx.StaticText(self.io_panel, label="Current AI Status:")

        # ai status box
        self.status_box = wx.TextCtrl(self.io_panel, style=wx.TE_READONLY)

        #
        #   Add and size elements
        #

        # add elements to the I/O sizer
        self.io_sizer.Add(self.input_chat_top_label, 0, wx.EXPAND | wx.LEFT | wx.TOP, 5)
        self.io_sizer.Add(self.input_chat, 0, wx.EXPAND | wx.ALL, 5)
        self.io_sizer.Add(self.input_chat_label, 0, wx.EXPAND | wx.LEFT | wx.TOP, 5)
        self.io_sizer.Add(self.input_box, 0, wx.EXPAND | wx.ALL, 5)
        self.io_sizer.Add(self.chat_button, 0, wx.EXPAND | wx.ALL, 5)
        self.io_sizer.Add(self.output_chat_label, 0, wx.EXPAND | wx.LEFT | wx.TOP, 5)
        self.io_sizer.Add(self.output_chat, 0, wx.EXPAND | wx.ALL, 5)
        self.io_sizer.Add(self.ai_status_label, 0, wx.EXPAND | wx.LEFT | wx.TOP, 5)
        self.io_sizer.Add(self.status_box, 0, wx.EXPAND | wx.ALL, 5)

        # add elements to the main grid sizer
        self.grid.Add(self.io_panel, 0, wx.EXPAND | wx.ALL)
        self.grid.Add(self.chatbot_control)

        # size and fit the sizers
        self.io_panel.SetSizerAndFit(self.io_sizer)
        self.SetSizerAndFit(self.grid)

        #
        #   Bind buttons to functions
        #
        self.Bind(wx.EVT_TEXT_ENTER, self.on_send_press)
        self.Bind(wx.EVT_BUTTON, self.on_send_press, self.chat_button)

        # bind the event handler for commands
        evt_command(self, self.on_command)

    # function for handling command events
    def on_command(self, event: CommandEvent):
        # process send command
        if event.task == "send":
            # send ai message to chat
            self.send_ai_message(event.data)
        # process gif commands
        if event.task == "gif":
            # start gif and set status to speaking
            if event.data == "start":
                self.status_box.SetValue("Speaking...")
                self.start_animation()
            # stop gif and set status to waiting
            else:
                self.status_box.SetValue("Waiting...")
                self.stop_animation()
        # process thinking commands
        if event.task == "thinking":
            # set status to thinking
            if event.data == "start":
                self.status_box.SetValue("Thinking...")
            # set status to waiting
            else:
                self.stop_animation("Waiting...")

    def start_animation(self, event=None):
        self.chatbot_control.Play()

    def stop_animation(self, event=None):
        self.chatbot_control.Stop()

    # updates the user and AI message histories
    def update_message_history(self):
        # variables to store the aggregated text
        user_text = ""
        ai_text = ""

        # aggregate user messages
        for message in self.user_message_history:
            user_text += message + "\n"

        # aggregate ai messages
        for message in self.ai_message_history:
            ai_text += str(message) + "\n"

        # update the chats
        self.input_chat.SetValue(user_text)
        self.output_chat.SetValue(ai_text)

    # send a ai message
    def send_ai_message(self, text: str):
        # add the message to message history
        self.ai_message_history.insert(0, self.get_timestamp() + "AI> " + str(text))

        # update the message history
        self.update_message_history()

    # clears the user and AI chat history
    def clear_chat(self):
        self.user_message_history = []
        self.ai_message_history = []
        self.update_message_history()        
        
    # closes program
    def exit_bot(self):
        self.Close()

    # function handling "send" button press
    def on_send_press(self, event):
        # read the text box
        text = self.input_box.GetValue()
        if text == "":
            return

        # clear the text box
        self.input_box.SetValue("")

        # add the message to message history
        self.user_message_history.insert(0, self.get_timestamp() + "You> " + text)

        # update the message history
        self.update_message_history()

        # call the message handler function for the ChatBot GUI
        self.gui.call_on_message(text)

    # returns time stamp
    def get_timestamp(self) -> str:
        if self.show_timestamp:
            return "[" + time.strftime("%H:%M:%S", time.localtime()) + "] "
        else:
            return ""


# main program class, controls the GUI and interactions with the GUI
class ChatbotGUI:
    def __init__(self, title: str, gif_path: str, show_timestamps: bool = True, default_voice_options: dict = None):
        # app object
        self.app = wx.App()

        # main frame
        self.frame = Main(None, title, self, gif_path, show_timestamps)

        # mutex to prevent out - of - order responses
        self.__thinking = RLock()

        # mutex to prevent ai from talking over itself
        self.__talking = RLock()

        # thread pool for executing speech and processing threads
        self.__pool = ThreadPoolExecutor(max_workers=8)

        # set default_voice_options to the default if no defaults are provided
        if default_voice_options is None:
            self.default_voice_options = {
                "rate": 100,
                "volume": 0.8,
                "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
            }
        else:
            self.default_voice_options = {
                "rate": default_voice_options.get("rate", 100),
                "volume": default_voice_options.get("rate", 0.8),
                "voice": default_voice_options.get(
                    "id",
                    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                )
            }

    # clear's chat history
    def clear(self):
        self.frame.clear_chat()
        
    # exits application
    def exit(self):
        self.frame.exit_bot()

    # starts gif
    def start_gif(self):
        self.frame.start_animation(None)

    # starts gif
    def stop_gif(self):
        self.frame.stop_animation(None)

    # function for sending the chatbot message processing to a thread
    def process_and_send_ai_message(self, ai_response_generator: Callable[[str], str], text: str,
                                    callback: Callable[[], None] = None, voice_options: dict = None):
        # submit the process to the thread pool
        self.__pool.submit(self.__process_and_send, ai_response_generator, text, callback, voice_options)

    # thread function used to process the
    def __process_and_send(self, ai_response_generator: Callable[[str], str], text: str,
                           callback: Callable[[], None] = None, voice_options: dict = None):
        # block other processing threads until this one is finished
        with self.__thinking:
            # put up thinking indicator
            wx.PostEvent(self.frame, CommandEvent("thinking", "start"))

            # generate the ai response
            response = ai_response_generator(text)

            # remove thinking indicator
            wx.PostEvent(self.frame, CommandEvent("thinking", "stop"))

            # send the ai message
            self.send_ai_message(response, callback, voice_options)

    # function for submitting messages
    def send_ai_message(self, text: str, callback: Callable[[], None] = None, voice_options: dict = None):
        # submit the function to the thread pool
        self.__pool.submit(self.__send_ai_message, text, callback, voice_options)

    # thread function used to submit ai messages
    def __send_ai_message(self, text: str, callback: Callable[[], None] = None, voice_options: dict = None):
        # if no speech options are provided then set defaults
        if voice_options is None:
            voice_options = self.default_voice_options

        # acquire permission to perform text to speech
        with self.__talking:
            # Code based on https://www.geeksforgeeks.org/text-to-speech-changing-voice-in-python/

            # send the message in chat via command event
            wx.PostEvent(self.frame, CommandEvent("send", text))

            # initialize tts engine
            converter = pyttsx3.init()

            # set properties given provided options
            converter.setProperty('rate', voice_options.get("rate", self.default_voice_options.get("rate")))
            converter.setProperty('volume', voice_options.get("volume", self.default_voice_options.get("volume")))
            converter.setProperty('voice', voice_options.get("voice", self.default_voice_options.get("voice")))

            # start gif by sending command event
            wx.PostEvent(self.frame, CommandEvent("gif", "start"))

            # say the text
            converter.say(text)
            converter.runAndWait()

            # stop the gif by sending the command event
            wx.PostEvent(self.frame, CommandEvent("gif", "stop"))

        # run the callback if provided
        if callback is not None:
            callback()

    # handles passing incoming user messages to the on_message handler
    def call_on_message(self, text: str):
        if getattr(self, "on_message", None) is None:
            print("Please define the 'on_message' function!")
            return

        # call the on_message handler
        getattr(self, "on_message")(self, text)

    # used to easily define the on_message handler function
    def event(self, coroutine):
        # handle general on_connect, and on_disconnect handlers
        if coroutine.__name__ == "on_message":
            # replaces the existing coroutine with the provided one
            setattr(self, coroutine.__name__, coroutine)
            return True
        return False

    # run the chat bot GUI
    def run(self) -> None:
        self.frame.Show()
        self.app.MainLoop()
