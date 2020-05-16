from linepy import *
import json, time, random

#line = Lineline(authToken='AUTH TOKEN')

line = LineClient(id = 'Email 1', passwd = 'Password')
#If you want to login into multiple people at once, uncomment the next line
#line = LineClient(id = 'Email 2', passwd = 'Password')


line.log("Auth Token : " + str(line.authToken))

channel = LineChannel(line)
line.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(line)


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
                try:
#Tagall, with many lists, and end count the length of JML(# of members in group)
                                if text.lower() == 'tagall':
                                        group = line.getGroup(msg.to)
                                        line_Ids1 = [contact.mid for contact in group.members]
                                        if len(line_Ids1) >= 1:
                                                line.mention(msg.to, line_Ids1[0:10])
                                                print("List 1 printed")

                                        if len(line_Ids1) > 10: 
                                                    line_Ids2 = line_Ids1[10:19]
                                                    line.mention(msg.to, line_Ids2)
                                                    print("List 2 printed")
                                        if len(line_Ids1) > 19:
                                                        line_Ids3 = line_Ids1[19: 28]
                                                        line.mention(msg.to, line_Ids3)
                                                        print("List 3 printed")
                                        if len(line_Ids1) > 28:
                                                            line_Ids4 = line_Ids1[28:38]
                                                            line.mention(msg.to, line_Ids4)
                                                            print("List 4 printed")
                                        if len(line_Ids1) > 38:
                                                                line_Ids5 = line_Ids1[38:48]
                                                                line.mention(msg.to, line_Ids5)
                                                                print("List 5 printed")
                                        if len(line_Ids1) > 48:
                                                                line_Ids6 = line_Ids1[48:58]
                                                                line.mention(msg.to, line_Ids6)
                                                                print("List 6 printed")
                                        if len(line_Ids1) > 58:
                                                                line_Ids7 = line_Ids1[58:68]
                                                                line.mention(msg.to, line_Ids7)
                                                                print("List 7 printed")
                                                 
                except Exception as e:
                    line.log("[SEND_MESSAGE] ERROR : " + str(e))

            

            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))





