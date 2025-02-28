import textwrap

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
    action = input()
    if "encode" in action:
        given = action.split("/:/")[1]
        output = ""
        for i in given:
            output += convertToBinary(i)
        output = textwrap.wrap(str(output), 6)
        if len(output[len(output)-1]) < 6:
            output[len(output)-1] = str(output[len(output)-1])
            while len(output[len(output)-1]) < 6:
                output[len(output)-1] += "0"
        for i in output:
            output[output.index(i)] = int(i, 2)
        for i in output:
            output[output.index(i)] = values[i]
        if len(output)%3 != 0:
            while len(output)%3 != 0:
                output.append("=")
        output = ''.join(output)
        print(output)
    elif "decode" in action:
        given = action.split("/:/")[1]
        output = []
        if "=" in given:
            given = list(given)
            while "=" in given:
                given.remove("=")
        for i in given:
            output.append(i)
        for i in range(len(output)):
            for x in range(len(values)):
                if output[i] == values[x]:
                    output[i] = x
        for i in range(len(output)):
            output[i] = '{:06b}'.format(output[i])
        output = textwrap.wrap(''.join(output), 8)
        output = bits2string(output)
        print(output)
    else:
        print("Unrecognized command")
