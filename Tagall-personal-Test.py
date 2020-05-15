from linepy import *
import json, time, random

#line = Lineline(authToken='AUTH TOKEN')

line = LineClient(id = 'Email', passwd = 'Password')


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
                if msg.text != None:
                    if msg.toType == 2:
                        may = line.getProfile().mid
                        if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            pilih = ['tag','tag?','tag? tag?','tag, tag','tag, tag']
                            rslt = random.choice(pilih)
                            line.sendText(msg.to, str(rslt))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            elif op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            line.sendChatChecked(receiver, msg_id)
                            contact = line.getContact(sender)
                            try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                            except Exception as e:
                                    #Tagall, with many lists, and end count the length of JML(# of members in group)
                                if text.lower() == 'tagall':
                                        group = line.getGroup(msg.to)
                                        line_Ids1 = [contact.mid for contact in group.members]
                                        if len(line_Ids1) > 1:
                                                line_Ids1[0:19]
                                                line.mention(msg.to, line_Ids1)
                                                line_Ids2 = line_Ids1[20:39]
                                                line.mention(msg.to, line_Ids2)
                                                line_Ids3 = line_Ids1[40:59]
                                                line.mention(msg.to, line_Ids3)
                                                line_Ids4 = line_Ids1[60:79]
                                                line.mention(msg.to, line_Ids4)
                                                line_Ids5 = line_Ids1[80:99]
                                                line.mention(msg.to, line_Ids5)
                                                 
                except Exception as e:
                    line.log("[SEND_MESSAGE] ERROR : " + str(e))

            

            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))





