import wikipedia
# this used wiki to find data for you and print it to the consle 


# a function must be created above where you call it from










def main():
    
    print("fetch bot")
    print("_" * 100, "\n")
    #ask user what they would like to research
    # then use input to get the tipc and assigne it to a string variable
    users_main_topic_choice = input("\n what do you want me to go get?")
    print ("researching " + users_main_topic_choice)
    print("_" * 100, "\n")
    # now do it
    # creat a variable for resruch results
    raw_Research_results = wikipedia.page(users_main_topic_choice)
    
    
    print("\n\n \t\t ###### research on ************ " + users_main_topic_choice + "###\n")
    print("\n\n\t\t summary of data")
    print(raw_Research_results.summary)
    print("_" * 100, "\n")
    # next one.................
    print("\n\n\t\t **************expanded content*************")
    print(raw_Research_results.content)
    raw = raw_Research_results.content
    print("_" * 100, "\n")
    print(raw)
    print("_" * 100, "\n")
    print("what do you wana do with all the data?")
   
    


if __name__ == "__main__":
    main()
    





##
# c.send(message)     Sends a message to the chatroom
# c.go_away()             Goes “away” in the chatroom, as the bot will not go “away” by default
# c.come_back()        Comes back from the chat room, after being away
# c.kick_user(user)   Kicks a user from the chatroom
# c.ban_user(user[, time=3600[, reason="Misbehaving in chat"]])  Bans a user from the chatroom.   
# 
# 
# ##