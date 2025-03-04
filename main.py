import textwrap

language = "Base64"
debug = False
values = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I",
    9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R",
    18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z", 26: "a",
    27: "b", 28: "c", 29: "d", 30: "e", 31: "f", 32: "g", 33: "h", 34: "i", 35: "j",
    36: "k", 37: "l", 38: "m", 39: "n", 40: "o", 41: "p", 42: "q", 43: "r", 44: "s",
    45: "t", 46: "u", 47: "v", 48: "w", 49: "x", 50: "y", 51: "z", 52: "0", 53: "1",
    54: "2", 55: "3", 56: "4", 57: "5", 58: "6", 59: "7", 60: "8", 61: "9", 62: "+", 63: "/"
}

def convertToBinary(input) -> int:
    return ' '.join([f"{ord(char):08b}" for char in input])

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

while True:
    action = input("Encode, Decode, or Settings?\n")
    if action == "Settings":
        action = input(f"[Language: {language}] [Debug mode: {debug}]\n")
        if "Language:" in action:
            if action.split(" ")[1] == "Base64":
                if language == "Base64":
                    print("Language is already set to Base64\n")
                else:
                    language = "Base64"
                    print("Language set to Binary\n")
            elif action.split(" ")[1] == "Binary":
                if language == "Binary":
                    print("Language is already set to Binary\n")
                else:
                    language = "Binary"
                    print("Language set to Binary")
            else:
                print("Unrecognized language")
        elif "Debug mode:" in action:
            if action.split(" ")[2] == "True":
                if debug == True:
                    print("Debug mode is already on\n")
                else:
                    debug = True
                    print("Debug mode turned on\n")
            elif action.split(" ")[2] == "False":
                if debug == False:
                    print("Debug mode is already off\n")
                else:
                    debug = False
                    print("Debug mode turned off\n")
    elif (language == "Base64" and any(srchstr in action for srchstr in ('Encode', 'Decode'))):
        if action == "Encode":
            action = input("Type or paste the phrase to be encoded below:\n")
            given = action
            output = ""
            for i in given:
                output += convertToBinary(i)
            if debug:
                print("Output = " + str(output))
            output = textwrap.wrap(str(output), 6)
            if debug:
                print("Output = " + str(output))
            if len(output[len(output)-1]) < 6:
                output[len(output)-1] = str(output[len(output)-1])
                while len(output[len(output)-1]) < 6:
                    output[len(output)-1] += "0"
            if debug:
                print("Output = " + str(output))
            for i in output:
                output[output.index(i)] = int(i, 2)
            if debug:
                print("Output = " + str(output))
            for i in output:
                output[output.index(i)] = values[i]
            if debug:
                print("Output = " + str(output))
            if len(output)%3 != 0:
                while len(output)%3 != 0:
                    output.append("=")
            if debug:
                print("Output = " + str(output))
            output = ''.join(output)
            print(output + "\n")
        elif action == "Decode":
            action = input("Type or paste the string to be decoded below:\n")
            given = action
            output = []
            if "=" in given:
                given = list(given)
                while "=" in given:
                    given.remove("=")
            for i in given:
                output.append(i)
            if debug:
                print("Output = " + str(output))
            for i in range(len(output)):
                for x in range(len(values)):
                    if output[i] == values[x]:
                        output[i] = x
            if debug:
                print("Output = " + str(output))
            for i in range(len(output)):
                output[i] = '{:06b}'.format(output[i])
            if debug:
                print("Output = " + str(output))
            output = textwrap.wrap(''.join(output), 8)
            if debug:
                print("Output = " + str(output))
            output = bits2string(output)
            print(output + "\n")
    elif (language == "Binary" and any(srchstr in action for srchstr in ('Decode', 'Encode'))):
        if action == "Encode":
            action = input("Type or paste the phrase you would like to encode below:\n")
            print(convertToBinary(action) + "\n")
        else:
            action = input("Type or paste the string you would like to decode below:\n")
            output = action.split(" ")
            if debug:
                print("Output = " + str(output))
            print(bits2string(output) + "\n")
    else:
        print("Unrecognized command")
