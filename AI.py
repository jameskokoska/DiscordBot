import random
import wikipedia
#from PyDictionary import PyDictionary
#from google import search

def answer(message, admin):
    
    sleep = ["Programmer asleep... come back later", "Ask me again... I'm tired!", "Random stuff is not actually random... ask again!", "Loading please wait... ask later.",
    "Closed. Come back soon!", "I'm rude, so ask later.", "Python died. Ask later.", "Hold on. Let me Google it. Ask me later", "Go away. I do not wish to answer at this time.",
    ]
    noQ = ["That is no question...", "I could write an actual question when I was 3 years old.", "You no grammar? < an actual question", "How dumb are you? question = ?",
    "Come back after you learn what a question consists of!"]
    noSmart = ["That's an odd question.", "I'm sorry, I don't understand.", "Such a random question.",
    "Why do you ask that?", "Please consider whether you can answer your own question.", "Perhaps the answer lies within yourself?", "Why don't you tell me?",
    "Wow! What a weird question.","Can you elaborate on that?","Very interesting. I'll leave that up to you!", "Did you try Googling it?", "Wow... Just wow.", "Elaborate please",
    "Why am I here? ...", "...okay... try again please.", "I'm giving up. Is this really a question???", "What does this really mean?"]

    #["kw birthday", "I was first functioning as a basic answer bot in early 2017."]
    #simpler questions below, eg can you and can i before can
    #key words (kw) ususally comes first
    #"kwhello" -> hello must be first word in question
    #"kw hello" -> must not be first word
    # can have up to 2 key words in first 2 options of list
    questions = [
    ["kw source", "kw your", "I have a personal built in database but I also look up my facts on Wikipedia and reference definitions of words using a dictionary."],
    ["kw you", "kwwho", "I am an AI that answers your questions to the best of my ability developed by James."],
    ["kw your", "kw name", "I don't have a name, " + random.choice(["I guess", "If you want"]) + " you can call me Test Dummy as that is my originated Discord bot name."],
    ["kw your", "kw creator", "My creator is James. He programmed me from scratch. I try my best to help you answer your question."],
    ["kw coin", "kwflip", "I choose " + random.choice(["heads.", "tails."]), "Okay... " + random.choice(["heads!", "tails!"]),
     "I'll flip a " + random.choice(["penny", "dime", "quarter", "loonie", "nickel", "toonie", "one-hundred dollar bill"]) + ". I got " + random.choice(["heads!", "tails!"])],
    ["kw time", "kwwhat", random.choice(["It's", "It's about", "I think it's"]) + " time to get a watch."],
    ["kw dice", "kwroll", "I rolled a " + str(random.randint(1,6)) + ".", "Rolling... I got " + str(random.randint(1,6)) + "."],
    ["kwhello", "Hello... I'm glad you could drop by today.", "Hi there... how are you today?", "Hello, how are you feeling today?", "Hello there!", 
    "Not really a question... but hi!",
    "Hello, it's me, I was wondering if after all these years you'd like to meet, To go over everything, They say that time's supposed to heal ya, But I ain't done much healing."],
    ["kw or ", "Why don't you choose?", "Choose using your best judgement!", "Always choose the first option!", 
    "It depends on conditions to make the best decision.", "Make an educated guess.", "Why not use //choose?"],
    ["kwmark", str(random.randint(80,100)) + "%... that's a" + random.choice(["n excellent", " great", " good"]) + " mark.",
    str(random.randint(70,80)) + "%... that's a" + random.choice([" decent", " alright", "n okay"]) + " mark.", 
    str(random.randint(0,70)) + "%..." + random.choice([" let's not talk about it.", " I think you can do better.", " there is always next time.", " you tried your best right?"]),
    "It's " + random.choice(["around ", "something like ", "about "]) + str(random.randint(70,100)) + "%"],
    ["kwprime number", "A prime number is a whole number greater than 1, whose only two whole-number factors are 1 and itself."],
    ["kwwill", "It could be very so.", "That's hard to answer.", "I cannot predict the future!", "Probably.", "It depends if you like bad or good news."],
    ["can you", "What makes you think I can't %s?", "If I could %s, then what?", "Why do you ask if I can %s?"],
    ["can i", "Perhaps you don't want to %s.", "Do you want to be able to %s?", "If you could %s, would you?", "Yes you can %s.", "Sorry, I don't think you can %s.",
    "I wouldn't count on it.", "Not with that math mark!"],
    ["can", "Yes.", "No.", "Maybe.", "It can be quite possible.", "Not with that math mark!", "I don't understand you!", 
    "How immature!", "Hmmm... that's tough!"],
    ["do i need", "Why do you need %s?", "Would it really help you to get %s?", "Are you sure you need %s?"],
    ["do you think it is", "Perhaps it's %s -- what do you think?", "If it were %s, what would you do?", "It could well be that it is %s."],
    ["are you", "Why does it matter whether I am %s?", "Would you prefer it if I were not %s?", "Perhaps you believe I am %s.", "I may be %s -- what do you think?"],
    ["what do you think", "What do *you* think about %s?", "My opinion is hard to create.", "Opinions are hard...", "To further create an opinion, I will need resources."],
    ["what", "Why do you ask?", "How would an answer to that help you?", "What do you think?", "If you think about it, you will know."],
    ["how many", str(random.randint(0,100)) + " to be exact."],
    ["how much", str(random.randint(0,100)) + " to be exact."],
    ["how are", "Very well.", "It's okay.", "Very fine.", "Fine.", "Good.", "Great.", "Excellent.", "Okay.", "So-so."],
    ["how come", "That's hard to say.", "Why do you think?"],
    ["how", "How do you suppose?", "Perhaps you can answer your own question.", "What is it you're really asking?"],
    ["why dont you", "Do you really think I don't %s?", "Perhaps eventually I will %s.", "Do you really want me to %s?"],
    ['why cant i', "Do you think you should be able to %s?", "If you could %s, what would you do?", "I don't know - why can't you %s?", "Have you really tried?"],
    ["why is", "Why do *you* think?", "That requires a lot of observations to support that... to the Google!", "Proof must be provided to create a conclusion!"],
    ["why do you think", "Why do *you* think %s?", "That requires a lot of observations to support that... to the Google!", "Proof must be provided to create a conclusion!"],
    ["why do", "Why don't you tell me the reason why %s?", "Why do you think %s?"],
    ["why does", "Why don't you tell me the reason why %s?", "Why do you think %s?"],
    ["why", "Why don't you tell me the reason why %s?", "Why do you think %s?"],
    ["i dont", "Don't you really %s?", "Why don't you %s?","Do you want to %s?"],
    ["is there", "Do you think there is %s?", "It's likely that there is %s.", "Would you like there to be %s?"],
    ["where", "Use some logic to find out where.", "To the google maps!", "You should reference a map!"],
    ["did", "I don't know much history.", "Google all the history, it's easier!"],
    ["who is", "Is %s rich?", "Do you know %s?", "I think %s is a" + random.choice([" nice", " great", " good", "n okay", " not that nice of a"]) + " person."],
    ["who", "Are they rich?", "I'm not a people person.", "I don't know much about anyone... I'm all alone."],
    ["is", "Yes.", "No.", "Maybe.", "It can be quite possible.", "I don't understand you!", "Hmmm... that's tough!"],
    ["does", "Yes.", "No.", "Maybe.", "It can be quite possible.", "I don't understand you!", "Hmmm... that's tough!"],
    ["when", "Soon.", "Can you estimate?", "In about " + str(random.randint(5,60)) + " minutes.", "It's going to be a while."],
    ["am i", "If you think so!", "Yes.", "No.", "Maybe.", "It can be quite possible.", "I don't understand you!", "Hmmm... that's tough!"],
    ["do you think", "Do you think %s?", "My opinion is hard to create.", "Opinions are hard..."],
    ["should", "Yes.", "No.", "Maybe.", "Do you think %s?", "My opinion is hard to create.", "Opinions are hard...", 
    "That requires a lot of observations to support that... to the Google!", "Proof must be provided to create a conclusion!"],
    ["on a scale of ", "How many significant digits should I assume for the scale?", "Well, I would say around " + str(random.randint(0,10)) + ".",
     "Maybe about " + str(random.randint(0,10)) + ".", "Exactly " + str(random.randint(0,10)) + ".", "Go low... " + str(random.randint(0,3)) + "."]
    ]
    
    numbers = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "ten" : 10,
    "eleven" : 11,
    "twelve" : 12,
    "thirteen" : 13,
    "fourteen" : 14,
    "fifteen" : 15,
    "sixteen" : 16,
    "seventeen" : 17,
    "eighteen" : 18,
    "nineteen" : 19,
    "twenty" : 20,
    "thirty" : 30,
    "forty" : 40,
    "fifty" : 50,
    "sixty" : 60,
    "seventy" : 70,
    "eighty" : 80,
    "ninety" : 90,
    "plus" : ")+(",
    "and" : "+",
    "point" : ".",
    "divided" : ")/(",
    "minus" : ")-(",
    "times" : ")*(",
    "squared" : ")**2",
    "cubed" : ")**3",
    "exponent" : ")**",
    "^" : "**",
    "raised" : ")**",
    "power" : ")**",
    "hundred" : "*100",
    "thousand" : "*1000",
    "million" : "*1000000",
    "billion" : "*1000000000",
    "trillion" : "*1000000000000"
    }
    
    numbersOnly = ["1","2","3","4","5","6","7","8","9","0","one","two","three","four","five","six","seven","eight","nine","zero",
                        "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty",
                        "forty","fifty","sixty","seventy","eighty","ninety", "hundred", "thousand", "million", "billion", "trillion"]
    largeNumbersOnly = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety", "hundred", "thousand", "million", "billion", "trillion"]
    operationsOnly = ["power", "raised", "exponent", "cubed", "squared", "times", "minus", "divided", "point", "+", "*", "-", "/"]
    exponentialOnly = ["power", "raised", "exponent", "cubed", "squared"]
    
    accomplish = False
    message = message.replace("'", "")
    seed = 0
    #for letter in message:
    #    seed += ord(letter)
    calculateConfidence = 0
    exponentCount = 0
    for number in numbersOnly:
        if number in message:
            calculateConfidence += 1
    for operation in operationsOnly:
        if operation in message:
            calculateConfidence += 1
    for word in message.split():
        if word in exponentialOnly:
            exponentCount += 1
    if calculateConfidence >= 2:
        message = message.replace("?", " ?")
        solve = "("+ "("*exponentCount
        previous = False
        for word in message.split():
            if previous == True and word in numbersOnly and word not in largeNumbersOnly:
                solve+=("+")
            if word in numbersOnly:
                previous = True
            else:
                previous = False
            #print(solve)
            for operation in ["+","-","*","**","/"]:
                if operation in word:
                    solve+=str(word)
                    continue
            try:
                solve+=str(int(word))
            except:
                try:
                    solve+=str(float(word))
                except:
                    try:
                        solve+=str(numbers[word])
                    except:
                        continue
    try:
        solveDisplay = solve.replace("**", "^")
        solveDisplay = solveDisplay.replace("/", "\u00F7")
        solveDisplay = solveDisplay.replace("*", "\u00D7")
        solveDisplay = solveDisplay + str(")")
        return(solveDisplay + "=" + str(eval(solve+")")))
    except:
        if " or " in message:
            message = message.replace("?", "")
            message = message.replace(",", "")
            splitQuestion = message.split()
            searchIndex = -1
            for word in splitQuestion:
                searchIndex += 1
                if word == "or":
                    break
            return(random.choice(["I choose the first: " + splitQuestion[searchIndex-1], "I choose the second: " + splitQuestion[searchIndex+1],
                                  "I choose " + splitQuestion[searchIndex-1], "I choose " + splitQuestion[searchIndex+1]])+ ".")
        #if "?" not in message:
            #return random.choice(noQ)
        elif random.randint(0,20) == 1:
            return random.choice(sleep)
        #elif "james" in message.lower() or "greenslime" in message.lower():
            #return "We do not talk about my creator!"
        else:
            #random.seed(seed)
            wiki = True
            define = False
            noWiki = ["you", "my", "your", "me", "am", "i", "I", "mark", "time"]
            message = message.replace("?", "")
            messageWords = message.split()
            for word in messageWords:
                if word == "mean":
                    define = True
                if word in noWiki:
                    wiki = False
                #print(word)
            if define == True:   
                dictionary=PyDictionary()
                if dictionary.meaning(messageWords[2]) == None:
                    return "Sorry I can't seem to find a definition for that."
                else:
                    return str(dictionary.meaning(messageWords[2]))
            if (message.lower().startswith("what") or message.lower().startswith("who")) and wiki == True:              
                try:
                    wikiResult = (str(wikipedia.summary(message[7:])).split())
                    sentenceIndex = 0
                    randomEnd = []
                    randomEndIndex = 0
                    for word in wikiResult:
                        sentenceIndex+=1
                        if sentenceIndex >= 100:
                            break
                        elif word[-1] == ".":
                            randomEnd.append(sentenceIndex)
                    randomEndIndex = int(random.choice(randomEnd))
                    #print(randomEndIndex)
                    sentenceIndex = 0
                    wikiResultReturn = []
                    for word in wikiResult:
                        sentenceIndex += 1
                        wikiResultReturn.append(word)
                        if sentenceIndex == randomEndIndex:
                            break
                    return ' '.join(wikiResultReturn)
                except wikipedia.exceptions.DisambiguationError as exception:
                    multipleResults = "What are you talking about? " + ", ".join(exception.options)
                    return multipleResults
                except wikipedia.exceptions.PageError:
                    x = 1
            for row in range(len(questions)):
                if questions[row][1][0:2] == "kw":
                    if (questions[row][1][2:] in message.lower()) and (questions[row][0][2:] in message.lower()):
                        return random.choice(questions[row][2:])
                elif questions[row][0][0:2] == "kw":
                    if questions[row][0][2:] in message.lower():
                        return random.choice(questions[row][1:])
                elif message.lower().startswith(questions[row][0]):
                    oldsubject = message[(len(questions[row][0])+1):]
                    subject = oldsubject.replace("?", "")
                    subject = subject.replace(" my ", " your ")
                    subject = subject.replace(" me ", " you ")
                    subject = subject.replace(" i ", " you ")
                    subject = subject.replace(" ill ", " you'll ")
                    choice = random.choice(questions[row][1:])
                    if "%" in choice:
                        return choice % (subject)
                    else:
                        return choice
                    #print("%" in choice)
                    accomplish = True
            if accomplish == False:
                #if admin == True:
                #    urls = []
                #    for url in search(message, tld='ca', lang='en', stop=1):
                #        urls.append(url)
                #    urlResult = "This may help: " + urls[0]
                #    return(urlResult)
                #else:
                return random.choice(noSmart)

#while True:
#    message = input("Question? ")
#    print(answer(message, False))

