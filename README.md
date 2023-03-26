how to vid https://youtu.be/E0B9bbG-nVI



(1)--------(CLI Expo MetaHuman)= In this session, we worked on creating a multi-screen menu with buttons labeled "Page 1" through "Page 10" using React Native and React Navigation. We started by modifying the given code to create a grid of buttons that, when pressed, should navigate to the corresponding pages. We then implemented the logic to handle navigation and created the corresponding pages with text that indicates the page number.

Initially, we encountered some issues with the navigation logic and setting up the proper structure for React Navigation. We resolved these issues by using the createStackNavigator and configuring the navigation stack to include all the pages.

Finally, we combined all the necessary components and navigation logic into a single file, creating a functional multi-screen menu. The resulting application displays a grid of buttons on the home screen, and pressing any of the buttons navigates to the respective page, displaying the correct page number.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
(2)-------(navigate to pages) =  I initially received an error related to conflicting imports in the React Native project. After analyzing the code, I identified that the Ionicons import statement was causing the conflict. I removed the import and combined the imports from the two conflicting files. This fixed the import conflict issue.

Next, I encountered an error that stated "Unable to resolve module ../screens/TabOneScreen". To resolve this, I updated the file paths in the import statement to match the correct file locations for TabOneScreen, Page1, and Page2. This resolved the module resolution error.

However, after making these changes, a new error surfaced: "Rendered more hooks than during the previous render". This error occurs when there is a mismatch in the number of hooks rendered between different renders. To fix this error, I modified the code to ensure that hooks are always rendered in the same order and not used conditionally. I achieved this by updating the RootLayout function to use the React.Fragment component, rendering both the SplashScreen and RootLayoutNav components. I also updated the components to accept a visible prop to control their visibility based on the state of the loaded variable.

By making these changes, I was able to resolve the "Rendered more hooks than during the previous render" error, and the React Native project should now be functioning correctly.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
(3)------------(Animated GIF for React Native) = I had a project to create a React Native app that could record audio and upload it to a server. I started by creating a new React Native project and installing the necessary packages, including react-native-audio-recorder-player and axios.

Next, I created the AudioRecorderScreen component, which consisted of a button to start recording audio, a button to stop recording, and a button to upload the recorded audio to the server using Axios.

After that, we encountered an issue with the Axios package not being recognized, so we had to install it again. Once that was resolved, we tested the app and successfully recorded and uploaded audio.

I then added a new screen, CameraHubScreen, which allowed the user to access their device's camera and take a photo. This screen used the react-native-camera package.

Finally, I modified the WisperTalk component to include text input for the user to type a message and a button to send it. The messages were stored in an array and displayed in a ScrollView.

Overall, we were able to successfully create an app that allowed the user to record audio, take photos, and send messages, while also integrating with a server using Axios.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
(4)------------ (rebiuld react envirment after crash) = In the project, I started by setting up a new Expo CLI project with a clean slate. I then created the desired folder structure, which included folders named "papers" and "whisper-backend" in the main directory, as well as an App.js file and two files within the "pages" folder: "AudioRecorderScreen.js" and "HomeScreen.js".

During the testing phase, I encountered an error related to the missing @react-navigation/native package. I resolved this issue by installing the required package and its dependencies. Afterward, I proceeded to install the expo-sharing package and demonstrated how to import and use it in the project.

Next, I installed the expo-av package and showed how to import and use the Audio module for audio playback and recording. While testing the project, I faced another bundling error related to the expo-av package. I successfully resolved this issue by reinstalling the package and its dependencies.

I also installed the axios package to make HTTP requests in the project and provided an example of how to import and use it for a simple GET request. Finally, I guided the process of committing the project to the specified GitHub repository.

Overall, the project involved setting up the Expo CLI environment, addressing bundling errors, and installing and using various packages like @react-navigation/native, expo-sharing, expo-av, and axios. The project was successfully committed to a GitHub repository for version control and collaboration.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
(5)-----------------(Flask back-end for storing files.) = In this session, I have implemented a Flask-based backend to store incoming files and texts. Initially, I have created a Flask application called app.py and set up a route to handle incoming file uploads. I also configured an uploaded_files folder to store the uploaded files.

To store incoming texts, I have added another route called /send_text in the app.py file. The Flask server receives the incoming text and saves it in the uploaded_files folder as a userText.txt document.

Next, I have updated the WisperTalk.js file to send texts to the Flask server. I added an async function called sendTextToServer to handle the communication between the React Native app and the Flask server using the fetch API. I also made sure that the handleSend function is an async function, so it can properly use the await keyword when calling sendTextToServer.

After that, I helped integrate the Flask server with the AudioRecorderScreen.js page. I modified the sendAudioToWhisper function to send the recorded .wav file to the Flask server and store it in the uploaded_files folder. I then updated the app.py file to handle incoming audio files and concatenate them to an existing .wav file each time a new recording is received.





(1) for flask start server  "env\Scripts\activate" // this activates the server for conunication 

(2) activate the expo server. "expo start" // this activates the server for expo CLI 


https://youtu.be/E0B9bbG-nVI









