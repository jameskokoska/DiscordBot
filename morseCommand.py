def encode(decoded):
    encoded = ""
    for char in range(len(decoded)):
        if decoded[char] == "a":
            encoded = encoded + ".- "
        elif decoded[char] == "b":
            encoded = encoded + "-... "
        elif decoded[char] == "c":
            encoded = encoded + "-.-. "
        elif decoded[char] == "d":
            encoded = encoded + "-.. "
        elif decoded[char] == "e":
            encoded = encoded + ". "
        elif decoded[char] == "f":
            encoded = encoded + "..-. "
        elif decoded[char] == "g":
            encoded = encoded + "--. "
        elif decoded[char] == "h":
            encoded = encoded + ".... "
        elif decoded[char] == "i":
            encoded = encoded + ".. "
        elif decoded[char] == "j":
            encoded = encoded + ".--- "
        elif decoded[char] == "k":
            encoded = encoded + "-.- "
        elif decoded[char] == "l":
            encoded = encoded + ".-.. "
        elif decoded[char] == "m":
            encoded = encoded + "-- "
        elif decoded[char] == "n":
            encoded = encoded + "-. "
        elif decoded[char] == "o":
            encoded = encoded + "--- "
        elif decoded[char] == "p":
            encoded = encoded + ".--. "
        elif decoded[char] == "q":
            encoded = encoded + "--.- "
        elif decoded[char] == "r":
            encoded = encoded + ".-. "
        elif decoded[char] == "s":
            encoded = encoded + "... "
        elif decoded[char] == "t":
            encoded = encoded + "- "
        elif decoded[char] == "u":
            encoded = encoded + "..- "
        elif decoded[char] == "v":
            encoded = encoded + "...- "
        elif decoded[char] == "w":
            encoded = encoded + ".-- "
        elif decoded[char] == "x":
            encoded = encoded + "-..- "
        elif decoded[char] == "y":
            encoded = encoded + "-.-- "
        elif decoded[char] == "z":
            encoded = encoded + "--.. "
        elif decoded[char] == "0":
            encoded = encoded + "----- "
        elif decoded[char] == "1":
            encoded = encoded + ".---- "
        elif decoded[char] == "2":
            encoded = encoded + "..--- "
        elif decoded[char] == "3":
            encoded = encoded + "...-- "
        elif decoded[char] == "4":
            encoded = encoded + "....- "
        elif decoded[char] == "5":
            encoded = encoded + "..... "
        elif decoded[char] == "6":
            encoded = encoded + "-.... "
        elif decoded[char] == "7":
            encoded = encoded + "--... "
        elif decoded[char] == "8":
            encoded = encoded + "---.. "
        elif decoded[char] == "9":
            encoded = encoded + "----. "
        else:
            encoded = encoded + "/ "
    if len(encoded) == 0:
        encoded = " "
    return encoded

def decode(encoded):
    plain = ""
    morsechar = ""
    for i in range(len(encoded)):
        morsechar = morsechar + encoded[i]
        if morsechar[-1] == " ":
            if morsechar == ".- ":
                plain = plain + "a"
            elif morsechar == "-... ":
                plain = plain + "b"
            elif morsechar == "-.-. ":
                plain = plain + "c"
            elif morsechar == "-.. ":
                plain = plain + "d"
            elif morsechar == ". ":
                plain = plain + "e"
            elif morsechar == "..-. ":
                plain = plain + "f"
            elif morsechar == "--. ":
                plain = plain + "g"
            elif morsechar == ".... ":
                plain = plain + "h"
            elif morsechar == ".. ":
                plain = plain + "i"
            elif morsechar == ".--- ":
                plain = plain + "j"
            elif morsechar == "-.- ":
                plain = plain + "k"
            elif morsechar == ".-.. ":
                plain = plain + "l"
            elif morsechar == "-- ":
                plain = plain + "m"
            elif morsechar == "-. ":
                plain = plain + "n"
            elif morsechar == "--- ":
                plain = plain + "o"
            elif morsechar == ".--. ":
                plain = plain + "p"
            elif morsechar == "--.- ":
                plain = plain + "q"
            elif morsechar == ".-. ":
                plain = plain + "r"
            elif morsechar == "... ":
                plain = plain + "s"
            elif morsechar == "- ":
                plain = plain + "t"
            elif morsechar == "..- ":
                plain = plain + "u"
            elif morsechar == "...- ":
                plain = plain + "v"
            elif morsechar == ".-- ":
                plain = plain + "w"
            elif morsechar == "-..- ":
                plain = plain + "x"
            elif morsechar == "-.-- ":
                plain = plain + "y"
            elif morsechar == "--.. ":
                plain = plain + "z"
            elif morsechar == "----- ":
                plain = plain + "0"
            elif morsechar == ".---- ":
                plain = plain + "1"
            elif morsechar == "..--- ":
                plain = plain + "2"
            elif morsechar == "...-- ":
                plain = plain + "3"
            elif morsechar == "....- ":
                plain = plain + "4"
            elif morsechar == "..... ":
                plain = plain + "5"
            elif morsechar == "-.... ":
                plain = plain + "6"
            elif morsechar == "--... ":
                plain = plain + "7"
            elif morsechar == "---.. ":
                plain = plain + "8"
            elif morsechar == "----. ":
                plain = plain + "9"
            else:
                plain = plain + " "
            morsechar = ""
    return plain

def flip(unflip):
    flip = ""
    for char in range(len(unflip)):
        if unflip[char] == "a":
            flip = flip + "ɐ"
        elif unflip[char] == "b":
            flip = flip + "q"
        elif unflip[char] == "c":
            flip = flip + "ɔ"
        elif unflip[char] == "d":
            flip = flip + "p"
        elif unflip[char] == "e":
            flip = flip + "ǝ"
        elif unflip[char] == "f":
            flip = flip + "ɟ"
        elif unflip[char] == "g":
            flip = flip + "ƃ"
        elif unflip[char] == "h":
            flip = flip + "ɥ"
        elif unflip[char] == "i":
            flip = flip + "ᴉ"
        elif unflip[char] == "j":
            flip = flip + "ɾ"
        elif unflip[char] == "k":
            flip = flip + "ʞ"
        elif unflip[char] == "l":
            flip = flip + "l"
        elif unflip[char] == "m":
            flip = flip + "ɯ"
        elif unflip[char] == "n":
            flip = flip + "u"
        elif unflip[char] == "o":
            flip = flip + "o"
        elif unflip[char] == "p":
            flip = flip + "d"
        elif unflip[char] == "q":
            flip = flip + "b"
        elif unflip[char] == "r":
            flip = flip + "ɹ"
        elif unflip[char] == "s":
            flip = flip + "s"
        elif unflip[char] == "t":
            flip = flip + "ʇ"
        elif unflip[char] == "u":
            flip = flip + "n"
        elif unflip[char] == "v":
            flip = flip + "ʌ"
        elif unflip[char] == "w":
            flip = flip + "ʍ"
        elif unflip[char] == "x":
            flip = flip + "x"
        elif unflip[char] == "y":
            flip = flip + "ʎ"
        elif unflip[char] == "z":
            flip = flip + "z"
        elif unflip[char] == "0":
            flip = flip + "0"
        elif unflip[char] == " ":
            flip = flip + " "
        else:
            flip = flip + "¿"
    if len(flip) == 0:
        flip = " "
    return flip
