from linepy import *
#Says to import everything from the package Linepy
import json

#line = Lineline(authToken='AUTH TOKEN')

line = LineClient(id = 'Mail', passwd = 'paswword')
#If you want to login into different accounts, uncomment the next line, and recomment the first, or vise versa to save one accounts login info.
#line = LineClient(id = 'ENTER YOUR SECOND EMAIL IF APPLIES, otheriwise, leave as a comment or delete', passwd = 'Password')


line.log("Auth Token : " + str(line.authToken))
#logs the authentication Token

channel = LineChannel(line)
line.log("Channel Access Token : " + str(channel.channelAccessToken))
#logs the channels access token

poll = LinePoll(line)
#creates a new instance for the selfbot
#while true runs forever since it says while this is true, do this, so having true there, it will constantly run.
while True:
    try:
        ops = poll.singleTrace(count=50)
        for op in ops:
            if op.type == 26:
                msg = op.message
            elif op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                #all of this just gets the users ids who made the command, and checks if the ID matches the login, send message, and send message from the reciever.
                try:
                                if text.lower() == 'tagall':
                                    #if looks at the command sent, and if it is Tagall, lower the capitals to lowercase
                                        group = line.getGroup(msg.to)
                                        #gets group members IDs, than indicates where the message gets sent.
                                        line_Ids1 = [contact.mid for contact in group.members]
                                        #stores the Line Ids into a list from (group.members, meaning the people in the gorup that the IDs were pulled from)
                                        if len(line_Ids1) >= 1:
                                                 #This if statement checks if the size of the room is greater than or equal to 1, making it always true, so it will always perform what is inside of it
                                                line.mention(msg.to, line_Ids1[0:10])
                                                #send a message that mentions to the IDs from 0 to 10 from the main list, and only 0-10.
                                                print("List 1 printed")
                                                #this prints just in case there is an error def mention, so you can see what needs to be changed in the numbers 0:10, etc.
                                                #The same applies for the following if statements
                                        if len(line_Ids1) > 10: 
                                                line.mention(msg.to, line_Ids1[10:19])
                                                print("List 2 printed")
                                        if len(line_Ids1) > 19:
                                                line.mention(msg.to, line_Ids1[19: 28])
                                                print("List 3 printed")
                                        if len(line_Ids1) > 28:
                                                line.mention(msg.to, line_Ids1[28:38])
                                                print("List 4 printed")
                                        if len(line_Ids1) > 38:
                                                line.mention(msg.to, line_Ids1[38:48])
                                                print("List 5 printed")
                                        if len(line_Ids1) > 48:
                                                line.mention(msg.to, line_Ids1[48:58])
                                                print("List 6 printed")
                                        if len(line_Ids1) > 58:
                                                line.mention(msg.to, line_Ids1[58:68])
                                                print("List 7 printed")
                                        if len(line_Ids1) > 68:
                                                line.mention(msg.to, line_Ids1[68:78])
                                                print("List 8 printed")
                                        if len(line_Ids1) > 78:
                                                line.mention(msg.to, line_Ids1[78:88])
                                                print("List 9 printed")
                                        if len(line_Ids1) > 88:
                                                line.mention(msg.to, line_Ids1[88:98])
                                                print("List 10 printed")
                                                #if you want to extend the number of people that can be mentioned, copy and paste the list and change 88:98 to 98:108.
                                                #In python, lists start at 0, not 1. so 0 to 10 is 11 people.
                                                 
                except Exception as e:
                    line.log("[SEND_MESSAGE] ERROR : " + str(e))
                    #This sends an error message

            

            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))





