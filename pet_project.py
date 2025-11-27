
alphabet = {
  "A": "ALFA",
  "B": "BRAVO",
  "C": "CHARLIE",
  "D": "DELTA",
  "E": "ECHO",
  "F": "FOXTROT",
  "G": "GOLF",
  "H": "HOTEL",
  "I": "INDIA",
  "J": "JULIETT",
  "K": "KILO",
  "L": "LIMA",
  "M": "MIKE",
  "N": "NOVEMBER",
  "O": "OSCAR",
  "P": "PAPA",
  "Q": "QUEBEC",
  "R": "ROMEO",
  "S": "SIERRA",
  "T": "TANGO",
  "U": "UNIFORM",
  "V": "VICTOR",
  "W": "WHISKEY",
  "X": "X-RAY",
  "Y": "YANKEE",
  "Z": "ZULU"
}

word = input("Input word: ")

for char in word:
    char = char.upper()
    for i in alphabet:
        if char == i:
            print(alphabet[char] + "\n")




