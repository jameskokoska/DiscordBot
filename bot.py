#Message formatting:
#":emoji: " + message.author.mention + ", Result."
#:no_entry_sign: " + message.author.mention + ", Error message."

print("Loading bot please wait...")
version = "Test bot v 1.4.1"
colours = ["black", "blue", "green", "light blue", "orange", "purple", "red", "pink", "white", "yellow"]

import discord
import random
import asyncio
import wikipedia
from PyDictionary import PyDictionary
import os

#Custom Modules
import helpText
import morseCommand
import AI

client = discord.Client()

@client.event
async def on_ready():
    print("Client bot connected!")
    print(version)
    print("Username: " + client.user.name)
    print("ID: " + client.user.id)

    #looping game - Playing... + splash
    splashes = ["discord", "with fire", "Tic Tac Toe", "fun games", "... studying instead!", ", working, sleeping", "pew pew games", "physics bridge designer",
                "sports", "at the movies", "steam games", "dsicord.py", "with python", "changing splash text", "with math", "with physics", "with chemistry", "with numbers",
                "Lorem ipsum dolor...", "with English subtitles", "in French", "in a theatre near you", "possum", "Pokemon Go", "cards", "to win", "it cool", "in theatres",
                "in the snow", "in the rain", "in the leaves", "outside", "avi files", "mp4 files", "mp3 files", "music", "dumb", "dvds on Windows 10", "games", "Jeopardy",
                "Wheel of Fortune", "gameshows", "Deal or No Deal", "chess", "checkers", "battleship", "Blu-ray on PC", "marbles", "with matter", "with experiments",
                "latent heat", "with chromosomes", "beat frequencies", "with the Doppler effect", "different frequencies", "with vectors", "with scalars", "flash games",
                "the lottery", "losing the lottery", "penny football", "with splashes", "high, winning low", "low, winning high", "discord.Game(name=splash)",
                "jokes", "asyncio", "randomly", "alone", "videos", "with sine waves", "with cosine waves", "with i", "with n\u00F70", "right now", "at different db",
                "in the sun", "for keeps", "the stock market", "your friend", "the victim", "in the Hunger Games", "with LEGO", "with Megablocks", "the radio",
                "with dark matter", "pool", "a movie", "at the beach", "in the sand", "on Netflix", "on TV", "in " + random.choice(colours), "minesweeper", "pinball"]
    importantSplash = [version, "//help"]
    print(str(len(splashes)) + " splashes loaded!")
    topics = ["Talk about games!", "Talk about school!", "Talk about math!", "Talk about physics!", "Talk about video games!", "Talk about anything!",
              "Talk about everything!", "Does anyone even read this!?"]

    splashTime = 0
    while True:
        await asyncio.sleep(20)
        splashTime += 1
        if splashTime == 3:
            splashTime = 0
            splash = random.choice(importantSplash)
        else:
            splash = random.choice(splashes)
        await client.change_presence(game=discord.Game(name=splash))
        await asyncio.sleep(10)

        await client.edit_channel(client.get_channel(id="256572058434011137"), topic = random.choice(topics))

        #pres = discord.utils.get(discord.Status, name="idle")
        #await client.change_presence(status=pres)


@client.event
async def on_member_join(member):
    server = member.server
    fmt = "\U0001F3AE \U0001F38A Welcome {0.mention} to {1.name}! Type //rules to get started!"
    await client.send_message(server, fmt.format(member, server))

    colourRole = discord.utils.find(lambda c: c.name == "colour-" + random.choice(colours), server.roles)
    await client.add_roles(member, colourRole)

@client.event
async def on_member_remove(member):
    await client.send_message(member.server, "\U0001F6AA Goodbye " + member.mention + "!")

@client.event
async def on_message(message):
    tempMessage = 0
    error = ""

    if message.content.startswith("//"):
        await client.send_typing(message.channel)
        message = message
        await client.delete_message(message)

        if message.author.top_role.name == "No Bot":
            error = "You have been banned from using the bot."
            tempMessage = 5
            msg = await client.send_message(message.channel, ":no_entry_sign: " + message.author.mention + ", " + error)
            await asyncio.sleep(tempMessage)
            await client.delete_message(msg)
            return

        elif message.content.startswith("//editme"):
            msg = await client.send_message(message.author, "10")
            await asyncio.sleep(3)
            await client.edit_message(msg, "40")

        # we do not want the bot to reply to itself
        elif message.author == client.user:
            return

        if message.content.startswith("//hello"):
            msg = "Hello " + message.author.mention
            await client.send_message(message.channel, msg, tts=True)

        elif message.content.startswith("//ask"):
            if message.author.top_role.name == "Admin":
                adminState = True
            else:
                adminState = False
            if "?" not in message.content:
                await client.send_message(message.channel, "**Question: **" + str((message.content[6:] + "?").capitalize()) + " **Response:** " + AI.answer(message.content[6:],adminState))
            else:
                await client.send_message(message.channel, "**Question: **" + str((message.content[6:]).capitalize()) + " **Response:** " + AI.answer(message.content[6:],adminState))

        #elif message.content.startswith("//chat"):
        #    await client.send_message(message.channel, message.author.mention + ": " + str((message.content[7:]).capitalize()) + "\n" +
        #    str(ChatBot.talk(message.content[7:])).capitalize())

        elif message.content.startswith("//petition"):
            votes = 7
            if len(message.content[11:]) != 0:
                msg = await client.send_message(message.channel, ":ballot_box_with_check: Petition: **" + message.content[11:] + "** - created by: " + message.author.mention + ". React with thumbs on this message to vote @here! (" + str(votes) + " votes to pass or fail)")
                await client.add_reaction(msg, "\U0001F44D")
                await client.add_reaction(msg, "\U0001F44E")
                count = [0,0]
                #[upvotes,downvotes]
                alreadyVoted = [[],[]]
                upvotedDisplay = await client.send_message(message.channel, "**0** \U0001F44D")
                downvotedDisplay = await client.send_message(message.channel, "**0** \U0001F44E")
                await asyncio.sleep(1)
                while count[0] <= votes - 1 and count[1] <= votes - 1:
                    res = await client.wait_for_reaction(message=msg)
                    if res.user != client.user:
                        await client.remove_reaction(msg, res.reaction.emoji, res.user)
                    if (res.user not in alreadyVoted[0]) and (res.user not in alreadyVoted[1]) and (res.user != client.user):
                        if res.reaction.emoji == "\U0001F44D":
                            count[0] += 1
                            alreadyVoted[0].append(res.user)
                        if res.reaction.emoji == "\U0001F44E": 
                            count[1] += 1
                            alreadyVoted[1].append(res.user)
                        displayVotedUp = ', '.join(str(votee) for votee in alreadyVoted[0])
                        await client.edit_message(upvotedDisplay, "**" + str(len(alreadyVoted[0])) + "** \U0001F44D " + displayVotedUp)
                        displayVotedDown = ', '.join(str(votee) for votee in alreadyVoted[1])
                        await client.edit_message(downvotedDisplay, "**" + str(len(alreadyVoted[1])) + "** \U0001F44E " + displayVotedDown)
                if count[0] >= votes:
                    await client.send_message(message.channel, ":ballot_box_with_check: Voting done! - sent to an admin for review.")
                    adminChannel = client.get_channel("256589191444430848")
                    await client.send_message(adminChannel,  ":ballot_box_with_check: Petition created by: " + message.author.mention + " passed voting! - **" + message.content[11:] + "**")
                else:
                    await client.send_message(message.channel, ":x: Voting failed!") 
            else:
                msg = await client.send_message(message.channel, "Please enter something into the petition.")
                await asyncio.sleep(5)
                await client.delete_message(msg)

        elif message.content.startswith("//vote"):
            #http://discordpy.readthedocs.io/en/latest/api.html#discord.Client.get_reaction_users
            voteEmoticion = "\u2714"
            unvoteEmoticon = "\u2716"
            if len(message.content[7:]) != 0:
                msg = await client.send_message(message.channel, ":ballot_box_with_check: Vote: **" + message.content[7:] + "** - created by: " + message.author.mention + ". @here, Click vote reactions to vote!")
                await asyncio.sleep(0.5)
                await client.add_reaction(msg, voteEmoticion)
                await client.add_reaction(msg, unvoteEmoticon)
            else:
                msg = await client.send_message(message.channel, ":no_entry_sign: " + message.author.mention + ", Please enter something into the vote.")
                await asyncio.sleep(5)
                await client.delete_message(msg)

        elif message.content.startswith("//deleteme"):
            tempMessage = 0.1
            msg = await client.send_message(message.channel, "You saw nothin.")

        elif message.content.startswith("//roll"):
            limit = int(message.content[6:])
            result = str(random.randint(1, limit))
            msg = await client.send_message(message.channel, result)
            tempMessage = 5

        elif message.content.startswith("//help detail"):
            await client.send_message(message.channel, helpText.help() + version + "\n" + message.author.mention)

        elif message.content.startswith("//help"):
            await client.send_message(message.channel, helpText.helpSimple() + version + "\n" + message.author.mention)

        elif message.content.startswith("//choose"):
            if len(message.content[9:]) == 0:
                error = "Invalid format! //choose <option 1 2 3...>"
                tempMessage = 5
                return
            else:
                given = message.content[9:]
                choices = given.split(", ")
                msg = await client.send_message(message.channel, "Options:" + message.content[8:] + ", I have chosen: **" + random.choice(choices) + "**")

        elif message.content.startswith("//salt" or "//salty"):
            msg = await client.send_file(message.channel, "salt.png")
            tempMessage = 30

        elif message.content.startswith("//wiki"):
            try:
                page = wikipedia.page(message.content[7:])
                emb = discord.Embed()
                emb.title = ":newspaper: " + str(page.title)
                emb.description = str(wikipedia.summary(message.content[7:]))[:500] + "..." + " \n*Read more here: " + str(page.url) + "*"
                await client.send_message(message.channel, embed=emb)
            except wikipedia.exceptions.DisambiguationError as exception:
                emb = discord.Embed()
                emb.title = "Couldn't find any Wikipedia pages, try these:"
                emb.description = ", ".join(exception.options)
                msg = await client.send_message(message.channel, embed=emb)
                tempMessage = 30
        
        elif message.content.startswith("//define"):
            dictionary=PyDictionary()
            if dictionary.meaning(message.content[9:]) == None:
                error = "Sorry I can't seem to find a definition for that."
                tempMessage = 5
            else:
                emb = discord.Embed()
                emb.title = str(":abc: Definition: " + message.content[9:])
                emb.description = str(dictionary.meaning(message.content[9:]))
                await client.send_message(message.channel, embed=emb)
        
        elif message.content.startswith("//antonym"):
            dictionary=PyDictionary()
            if dictionary.meaning(message.content[9:]) == None:
                error = "Sorry I can't seem to find an antonym for that."
                tempMessage = 5
            else:
                emb = discord.Embed()
                emb.title = str(":ab: Antonym: " + message.content[10:])
                emb.description = ", ".join(dictionary.antonym(message.content[10:]))
                await client.send_message(message.channel, embed=emb)
        
        elif message.content.startswith("//synonym"):
            dictionary=PyDictionary()
            if dictionary.meaning(message.content[9:]) == None:
                error = "Sorry I can't seem to find an synonym for that."
                tempMessage = 5
            else:
                emb = discord.Embed()
                emb.title = str(":abcd: Synonym: " + message.content[10:])
                emb.description = ", ".join(dictionary.synonym(message.content[10:]))
                await client.send_message(message.channel, embed=emb)

        elif message.content.startswith("//french"):
            dictionary=PyDictionary()
            if dictionary.meaning(message.content[9:]) == None:
                error = "Sorry I can't seem to translate that. (one word please)"
                tempMessage = 5
            else:
                emb = discord.Embed()
                emb.title = str(":symbols: Engligh: " + message.content[9:])
                emb.description = "**French:** " + str(dictionary.translate(message.content[9:],'fr'))
                await client.send_message(message.channel, embed=emb)


        elif message.content.startswith("//pepper" or "//peppery"):
            msg = await client.send_file(message.channel, "pepper.png")
            tempMessage = 30

        elif message.content.startswith("//spam"):
            #right click spam channel for id
            arguments = message.content.split()
            conString = ""
            if message.channel.name == "spam": #or message.channel.id == "id"
                try:
                    int(arguments[1])
                except:
                    error = "Invalid format! //spam <amount> <message...>"
                    tempMessage = 5
                    return
                for word in arguments[2:]:
                    conString = conString + " " + word
                if int(arguments[1]) <= 10:
                    for x in range(int(arguments[1])):
                        await client.send_message(message.channel, conString)
                elif int(arguments[1]) > 10:
                    error = "I can't spam that much!"
                    tempMessage = 5
            else:
                error = "You may only use this in the spam text channel."
                tempMessage = 5

        elif message.content.startswith("//morse"):
            decoded = (str(message.content[8:]))
            decoded = decoded.lower()
            msg = await client.send_message(message.channel, "```" + morseCommand.encode(decoded) + "```" + message.author.mention)

        elif message.content.startswith("//demorse"):
            encoded = (str(message.content[10:]) + " ")
            msg = await client.send_message(message.channel, "```" + morseCommand.decode(encoded) + "```" + message.author.mention)

        elif message.content.startswith("//flip" or "//flipr"):
            if message.content.startswith("//flip "):
                unflip = (str(message.content[7:]))[::-1]
            else:
                unflip = (str(message.content[8:]))
            unflip = unflip.lower()
            msg = await client.send_message(message.channel, morseCommand.flip(unflip))

        elif message.content.startswith('//repeat'):
            try:
                if message.content.startswith('//repeat init'):
                    if message.author.top_role.name == 'Admin':
                        global stored
                        stored = []
                        msg = await client.send_message(message.channel, '```Initialized!```' + message.author.mention)
                        tempMessage = 3
                    else:
                        msg = await client.send_message(message.channel, '```Insufficient permissions!```' + message.author.mention)
                        tempMessage = 3
                elif message.content.startswith('//repeat save'):
                    found = False
                    if len(stored) > 0:
                        for mes in range(len(stored)):
                            if stored[mes][0] == message.author.mention:
                                stored[mes][1] = message.content[14:]
                                msg = await client.send_message(message.channel, '```Message recorded!```' + message.author.mention)
                                tempMessage = 3
                                found = True
                        if found == False:
                            stored.append([message.author.mention, message.content[14:]])
                            msg = await client.send_message(message.channel, '```Message recorded!```' + message.author.mention)
                            tempMessage = 3
                            found = True
                    else:
                        stored.append([message.author.mention, message.content[14:]])
                        msg = await client.send_message(message.channel, '```Message recorded!```' + message.author.mention)
                        tempMessage = 3
                        found = True
                elif message.content.startswith('//repeat call'):
                    found = False
                    for mes in range(len(stored)):
                        if stored[mes][0] == message.author.mention:
                            if len(stored[mes][1]) == 0:
                                msg = await client.send_message(message.channel, '``` ```**Message from: **' + message.author.mention)
                            else:
                                msg = await client.send_message(message.channel, '```' + stored[mes][1] + '```**Message from: **' + message.author.mention)
                            found = True
                    if found == False:
                        msg = await client.send_message(message.channel, '```No messages found!```' + message.author.mention)
                        tempMessage = 3
                        found = True
                else:
                    msg = await client.send_message(message.channel, '```Invalid subcommand!```' + message.author.mention)
                    tempMessage = 3
            except:
                msg = await client.send_message(message.channel, '```Not initialized!```' + message.author.mention)
                tempMessage = 3

        elif message.content.startswith("//anon"):
            mes = message.content[7:]
            msg = await client.send_message(message.channel, mes + "\n**~Anonymous :speech_balloon:**")

        elif message.content.startswith("//reverse"):
            mes = str(message.content[:9:-1])
            msg = await client.send_message(message.channel, "```" + mes + "```")

        elif message.content.startswith("//colour list"):
            msg = await client.send_message(message.channel, message.author.mention + " colours: " +", ".join(colours))
            tempMessage = 10

        elif message.content.startswith("//colour"):
            for colour in colours:
                await asyncio.sleep(0.1)
                removeRole = discord.utils.find(lambda d: d.name == "colour-" + colour, message.channel.server.roles) #thanks Khang, lambda master
                await client.remove_roles(message.author, removeRole)
            await asyncio.sleep(0.5)
            userColour = message.content[9:]
            colourRole = discord.utils.find(lambda r: r.name == "colour-" + userColour, message.channel.server.roles)
            await client.add_roles(message.author, colourRole)

        elif message.content.startswith("//hexcolour"):
            hx = str(message.content[12:18])
            hx = hx.upper()
            digs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
            valid = True
            for dig in hx:
                if dig not in digs:
                    valid = False
            while len(hx) < 6:
                hx = "0" + hx
            if valid == False:
                msg = await client.send_message(message.channel, "```Invalid colour!```" + message.author.mention)
                await asyncio.sleep(3)
                await client.delete_message(msg)
            else:
                hxint = int("0x" + hx, 16)
                newrole = discord.utils.get(message.server.roles, name = "#" + hx)
                if newrole not in message.server.roles:
                    await asyncio.sleep(0.2)
                    await client.create_role(server=message.server, name="#" + hx, colour=discord.Colour(hxint), mentionable=False, hoist=False)
                for rol in message.author.roles:
                    if str(rol)[0] == "#":
                        rolefound = 0
                        for mem in message.server.members:
                            if rol in mem.roles:
                                rolefound += 1
                        if rolefound <= 1:
                            await asyncio.sleep(0.2)
                            await client.delete_role(server=message.server, role=rol)
                        await asyncio.sleep(0.2)
                        await client.remove_roles(message.author, rol)
                for rol in message.server.roles:
                    if str(rol) == "#" + hx:
                        await asyncio.sleep(0.2)
                        await client.add_roles(message.author, rol)

        elif message.content.startswith("//notify on"):
            try:
                topic = message.content[12:]
                topicRole = discord.utils.find(lambda r: r.name == "notify-" + topic, message.channel.server.roles)
                await client.add_roles(message.author, topicRole)
                msg = await client.send_message(message.channel, ":bell: " + message.author.mention + ", you have been opted in to receive notifications for " + topic)
                tempMessage = 5
            except:
                error = "Something went wrong."
                tempMessage = 5


        elif message.content.startswith("//notify off"):
            try:
                topic = message.content[13:]
                topicRole = discord.utils.find(lambda r: r.name == "notify-" + topic, message.channel.server.roles)
                await client.remove_roles(message.author, topicRole)
                msg = await client.send_message(message.channel, ":no_bell: " + message.author.mention + ", you have been opted out of receiving receive notifications for " + topic)
                tempMessage = 5
            except:
                error = "Something went wrong."
                tempMessage = 5

        elif message.content.startswith("//notify list"):
            msg = await client.send_message(message.channel, ":bellhop: " + message.author.mention + " //notify <on/off> <channel> - Channel Options: rocket league, minecraft, announcements")
            tempMessage = 10

            #await client.send_message(message.author, "10")
            #await client.send_message(message.channel, "WOW!", tts=True) # tts will read the message
            #await client.change_presence(status=discord.Status.dnd) #fix -> changes status

            #await client.add_roles(message.author, *roles)
            #server = message.author.server
            #member = discord.utils.find(lambda r: r.name == "colour1", server.roles)
            #print(member.id)
            #message.channel.id
            #await client.add_roles(message.author, "colour1")
            #print(member)

        #elif message.content.startswith("//suggest"):

        elif message.content.startswith("//invite"):
            msg = await client.send_message(message.channel, "https://discord.gg/M9hBtqn")
            tempMessage = 15

        elif message.content.startswith("//suggest emoji"):

            adminChannel = client.get_channel("256589191444430848")
            await client.send_message(adminChannel, ":upside_down: Emoji suggestion created by: " + message.author.mention + " - Emoji:" + message.content[15:])
            msg = await client.send_message(message.channel, ":upside_down:" + message.author.mention + "Sent to an admin as an emoji suggestion. Inappropriate suggestions may lead to consequences.")
            tempMessage = 10

        elif message.content.startswith("//suggest splash"):
            adminChannel = client.get_channel("256589191444430848")
            await client.send_message(adminChannel, ":sweat_drops: Splash suggestion created by: " + message.author.mention + " - **Playing**" + message.content[16:])
            msg = await client.send_message(message.channel, ":sweat_drops: " + message.author.mention + ", Sent to an admin as a splash suggestion. Inappropriate suggestions may lead to consequences. Preview: **Playing**" + message.content[16:])
            tempMessage = 10

        elif message.content.startswith("//suggest"):
            adminChannel = client.get_channel("256589191444430848")
            await client.send_message(adminChannel, ":clipboard:  Suggestion created by: " + message.author.mention + " - " + message.content[10:])
            msg = await client.send_message(message.channel, ":clipboard: " + message.author.mention + ", Sent to an admin as an overall suggestion. Inappropriate suggestions may lead to consequences.")
            tempMessage = 10

        elif message.content.startswith("//prime"):
            s = int(message.content[8:])
            if s <= 19999999999997:
                p = int(message.content[8:]) - 1
                l = []
                if p == 1:
                    p -= 1
                if p % 2 == 0.0:
                    p -= 1
                c = 0
                while len(l) <= 1:
                    p += 2
                    d = 0
                    c = 0
                    while d < p ** (1/2) and c <= 1:
                        d += 1
                        if (p / d) % 1 == 0.0:
                            c += 1
                    if c == 1:
                        l.extend([p])
                if l[0] == 1:
                    l[0] = 2
                orig = ""
                final = ""
                s = str(s)
                f = str(l[0])
                for i in range(len(s)):
                    if len(orig) % 4 == 0:
                        orig += "\'"
                    orig += s[-i - 1]
                for i in range(len(f)):
                    if len(final) % 4 == 0:
                        final += "\'"
                    final += f[-i - 1]
                msg = await client.send_message(message.channel, "```" + orig[-1:0:-1] + " -> " + final[-1:0:-1] + "```" + message.author.mention)
            else:
                error = "Your number is too high!"
                tempMessage = 5

        elif message.content.startswith("//rules"):#############################
                error = "Sorry this command is in the works! Type //help instead!"
                tempMessage = 10

        elif message.content.startswith("//remind"):
            if message.author.top_role.name == "Admin":
                remall = message.content[9:]
                remtr = ""
                rem = ""
                spc = False
                for i in range(len(remall)):
                    if remall[i] == " " and spc == False:
                        spc = True
                    if spc == False:
                        remtr = remtr + remall[i]
                    if spc == True:
                        rem = rem + remall[i]
                remtr = int(remtr) - 1
                await asyncio.sleep(remtr)
                await client.send_typing(message.channel)
                msg = await client.send_message(message.channel, "```http\nReminder:" + rem + "```@everyone")
            else:
                error = "You do not have permission to use this command."
                tempMessage = 5
            
        elif message.content.startswith("//timer"):
            tr = int(message.content[8:])
            timermsg = await client.send_message(message.channel, ":alarm_clock: Timer:" + str(tr) + " seconds.")
            count = 5
            while tr >= 1:
                if count == 5:
                    await client.edit_message(timermsg, ":alarm_clock: Timer: " + str(tr) + " seconds.")
                    count = 0
                await asyncio.sleep(1)
                tr -= 1
                count += 1
            await client.delete_message(timermsg)
            await client.send_typing(message.channel)
            msg = await client.send_message(message.channel, "```Time is up!```" + message.author.mention)
            tempMessage = 5

        elif message.content.startswith("//delete"):
            try:
                if int(message.content[9:]) > 10:
                    msg = await client.send_message(message.channel, ":wastebasket: Slow down there!")
                    await asyncio.sleep(5)
                    await client.delete_message(msg)
                elif message.author.top_role.name == "Admin":
                    await client.purge_from(message.channel, limit=int(message.content[9:]))
                    msg = await client.send_message(message.channel, ":wastebasket: Deleted " + message.content[9:] + " message(s).")
                    await asyncio.sleep(5)
                    await client.delete_message(msg)
                else:
                    error = "You do not have permission to use this command."
                    tempMessage = 5
            except:
                error = "Not a valid number."
                tempMessage = 5
                
        elif message.content.startswith("//room"):
            if message.content.startswith("//room create"):
                pchname = "Private " + str(message.author)
                pch = discord.utils.get(message.server.channels, name = pchname, type = discord.ChannelType.voice)
                if pch not in message.server.channels:
                    pcheveryoneperms = discord.PermissionOverwrite(connect=False)
                    pchroleperms = discord.PermissionOverwrite(connect=True)
                    pchrole = await client.create_role(server=message.server,name=pchname,mentionable=True,hoist=False)
                    await client.add_roles(message.author, pchrole)
                    await client.create_channel(message.server, pchname, (message.server.default_role, pcheveryoneperms), (pchrole, pchroleperms), type=discord.ChannelType.voice)
                    msg = "Private channel created!\n" + str(message.author.mention)
                    tempMessage = 3
                else:
                    error = "You already have a private channel!\n" + str(message.author.mention)
                    tempMessage = 3
            elif message.content.startswith("//room delete"):
                pchname = "Private " + str(message.author)
                pch = discord.utils.get(message.server.channels, name = pchname, type = discord.ChannelType.voice)
                pchrole = discord.utils.get(message.server.roles, name = pchname)
                if pch in message.server.channels:
                    await client.delete_channel(pch)
                    await client.delete_role(message.server, pchrole)
                    msg = "Private channel deleted!\n" + str(message.author.mention)
                    tempMessage = 3
                else:
                    error = "No private channel exists to be deleted!\n" + str(message.author.mention)
                    tempMessage = 3
            elif message.content.startswith("//room invite all"):
                pchname = "Private " + str(message.author)
                pchrole = discord.utils.get(message.server.roles, name = pchname)
                msg = "Inviting all members to " + pchname + "..."
                for mem in message.server.members:
                    if (pchrole not in mem.roles) and (mem != message.author):
                        await client.add_roles(mem, pchrole)
                tempMessage = 0
                msg = "Invited all members to " + pchname + "!"
                tempMessage = 5
            elif message.content.startswith("//room uninvite all"):
                pchname = "Private " + str(message.author)
                pchrole = discord.utils.get(message.server.roles, name = pchname)
                msg = "Uninviting all members to " + pchname + "..."
                for mem in message.server.members:
                    if (pchrole in mem.roles) and (mem != message.author):
                        await client.remove_roles(mem, pchrole)
                tempMessage = 0
                msg = "Unnvited all members to " + pchname + "!"
                tempMessage = 5
            elif message.content.startswith("//room invite"):
                await client.send_typing(message.channel)
                pchname = "Private " + str(message.author)
                pchrole = discord.utils.get(message.server.roles, name = pchname)
                if len(message.mentions) == 0:
                    error = "Cannot invite 0 people!\n" + message.author.mention
                    tempMessage = 3
                for newmember in message.mentions:
                    if (newmember in message.server.members) and (pchrole not in newmember.roles):
                        await client.add_roles(newmember, pchrole)
                        msg = "You have been invited to " + pchname + "!\n" + newmember.mention
                        tempMessage = 7
                    elif (newmember in message.server.members) and (pchrole in newmember.roles):
                        error = str(newmember) + " is already invited to " + pchname + "!"
                        tempMessage = 5
                    else:
                        error = "Member not found!\n" + message.author.mention
                        tempMessage = 3
            elif message.content.startswith("//room uninvite"):
                pchname = "Private " + str(message.author)
                pch = discord.utils.get(message.server.channels, name = pchname, type = discord.ChannelType.voice)
                pchrole = discord.utils.get(message.server.roles, name = pchname)
                if len(message.mentions) == 0:
                    error = "Cannot uninvite 0 people!\n" + message.author.mention
                    tempMessage = 3
                for newmember in message.mentions:
                    if (newmember in message.server.members) and (pchrole in newmember.roles):
                        if newmember == message.author:
                            await client.send_typing(message.channel)
                            error = "Cannot uninvite yourself!\n" + message.author.mention
                            tempMessage = 3
                        else:
                            await client.remove_roles(newmember, pchrole)
                            msg = "You have been uninvited to " + pchname + "!\n" + newmember.mention
                            tempMessage = 7
                            if newmember.voice_channel.id == pch.id:
                                await client.move_member(newmember, message.server.afk_channel)
            else:
                error = "Invalid subcommand!\n" + message.author.mention
                tempMessage = 3

        elif message.content.startswith("//numbergame"):
            global number
            number = -1
            beforetr = 10
            tr = 5
            timermsg = await client.send_message(message.channel, ":1234: @here Number game starting in " + str(beforetr) + " seconds.")
            await asyncio.sleep(beforetr - tr)
            while tr >= 1:
                await client.edit_message(timermsg, ":1234: @here Number game starting in " + str(tr) + " seconds.")
                await asyncio.sleep(1)
                tr -= 1
            await client.delete_message(timermsg)
            number = random.randint(1, 100)
            ingame = message.author
            msg = await client.send_message(message.channel, ":1234: Guess the number! (between 1 and 100)")
            count = 60
            while count >= 0 and number != -1:
                count -= 1
                await asyncio.sleep(1)
                #print(count >= 0 and number != -1, count, number)
            if number != -1:
                await client.delete_message(msg)
                msg = await client.send_message(message.channel, ":1234: Times up!")
                number = -1
                await asyncio.sleep(5)
                await client.delete_message(msg)            
                
        elif message.content.startswith("//"):
            error = "Sorry the \"" + message.content + "\" command does not exist! Use //help for more information."
            tempMessage = 5
            #roles = message.author.roles[1]
            #print(roles.name)
            


#-----------------------------------------------------------------------------------------------------------------------------------------

    if error != "":
        msg = await client.send_message(message.channel, ":no_entry_sign: " + message.author.mention + ", " + error)
        
    if tempMessage != 0:
        await asyncio.sleep(tempMessage)
        await client.delete_message(msg)

#-----------------------------------------------------------------------------------------------------------------------------------------

    try: #number game cont
        if number >= 1:
            if int(message.content) < number:
                await client.send_typing(message.channel)
                await client.delete_message(message)
                msg = await client.send_message(message.channel, "The number is larger than " + message.content)
                await asyncio.sleep(5)
                await client.delete_message(msg)
            elif int(message.content) > number:
                await client.send_typing(message.channel)
                await client.delete_message(message)
                msg = await client.send_message(message.channel, "The number is smaller than " + message.content)
                await asyncio.sleep(5)
                await client.delete_message(msg)
            elif int(message.content) == number:
                await client.send_typing(message.channel)
                await client.delete_message(message)
                await client.send_message(message.channel, "Congrats " + str(number) + " was the number " + message.author.mention)
                number = -1

    except:
        return

        
print("Done! Connecting...")
client.run("DISCORD KEY")
print("Error!")
print("Something happened :( \n Python will now close. \n Check Internet connection and try again.")
os.system("pause")
