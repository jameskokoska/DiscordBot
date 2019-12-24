def help():
    helpDetail = """```Markdown
*Detailed help:*
//rules: Display the rules of this server
//help: Displays a simple help listing commands
//help detail: displays help in detail, this page
//morse <message...>: Puts messages in morse code
//demorse <message...>: Decodes a message from morse code
//spam <amount> <message...>: Repeats messages
//roll <max amount>: Chooses a random number like rolling dice
//prime <number>: Find the closest prime number above the value passed in
//choose <option 1, 2, 3,...>: Picks a random option out of the ones listed (options separated by comma then space)
//numbergame: Starts a number game
//salt or //salty: Displays the common "salt" emoticon
//deleteme: ...
//anon <message...>: Display a message anonymously
//reverse <message...>: Display a message in reverse
//flip <message...>: Flips a message
//flipr <message...>: Flips and reverses a message
//colour <colour>: Changes the users colour, blank for no colour
//colour list: Lists the colours
//notify off <channel>: Adds the user to certain announcement text channels
//notify on <channel>: Removes the user from certain announcement text channels
//invite: shows the invitation for people to join this server
//suggest <message...>: suggests a feature/special text channel/voice channel etc an admin
//suggest splash <message...>: suggests a message to be displayed under the Bots profile as <Playing + message>
//suggest emoji <message...>: suggests an emoji that could be added to this server
//timer <number>: sets a timer for a given number of seconds

//remind <time> <message...>: sets a reminder off a timer, only admins may use this
//delete <number>: deletes a number of past messages in bulk, only admins may use this

Private Channels:
//room create
//room delete
//room invite <user>
//room uninvite <user>

//vote
//hexcolour
//repeat
//petition

//remind <time> <message...>
//delete <number>

//ask <question>

//define <word>
//synonym <word>
//antonym <word>
//french <word>
```
"""
    return helpDetail
def helpSimple():
    helpSimple = """```Markdown
*Help:*
//rules
//help
//help detail
//morse <message...>
//demorse <message...>
//spam <amount> <message...>
//roll <max amount>
//prime <number>
//choose <option 1, 2, 3,...>
//numbergame
//salt or //salty
//deleteme
//anon <message...>
//reverse <message...>
//flip <message...>
//flipr <message...>
//colour <colour>
//colour list
//notify off <channel>
//notify on <channel>
//invite
//suggest <message...>
//suggest splash <message...>
//suggest emoji <message...>
//timer <number>

Private Channels:
//room create
//room delete
//room invite <user>
//room uninvite <user>

//vote
//hexcolour
//repeat
//petition

//remind <time> <message...>
//delete <number>

//ask <question>

//define <word>
//synonym <word>
//antonym <word>
//french <word>
```
"""
    return helpSimple
