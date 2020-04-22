''' Letter values '''
letter_values = {
    "a":1,
    "b":4,
    "c":4,
    "d":2,
    "e":1,
    "f":4,
    "g":3,
    "h":3,
    "i":1,
    "j":1,
    "k":5,
    "l":2,
    "m":4,
    "n":2,
    "o":1,
    "p":4,
    "q":1,
    "r":1,
    "s":1,
    "t":1,
    "u":2,
    "v":5,
    "w":4,
    "x":8,
    "y":3,
    "z":1 
}

''' Word orientations '''
UP    = 0
DOWN  = 1
LEFT  = 2
RIGHT = 3

''' Special tile values '''
EM = 0
DL = 1
TL = 2
DW = 3
TW = 4
CE = 5

''' Special tile locations '''
special_chars = [
    [EM, EM, EM, TW, EM, EM, TL, EM, TL, EM, EM, TW, EM, EM, EM],
    [EM, EM, DL, EM, EM, DW, EM, EM, EM, DW, EM, EM, DL, EM, EM],
    [EM, DL, EM, EM, DL, EM, EM, EM, EM, EM, DL, EM, EM, DL, EM],
    [TW, EM, EM, TL, EM, EM, EM, DW, EM, EM, EM, TL, EM, EM, TW],
    [EM, EM, DL, EM, EM, EM, DL, EM, DL, EM, EM, EM, DL, EM, EM],
    [EM, DW, EM, EM, EM, TL, EM, EM, EM, TL, EM, EM, EM, DW, EM],
    [TL, EM, EM, EM, DL, EM, EM, EM, EM, EM, DL, EM, EM, EM, TL],
    [EM, EM, EM, DW, EM, EM, EM, CE, EM, EM, EM, DW, EM, EM, EM],
    [TL, EM, EM, EM, DL, EM, EM, EM, EM, EM, DL, EM, EM, EM, TL],
    [EM, DW, EM, EM, EM, TL, EM, EM, EM, TL, EM, EM, EM, DW, EM],
    [EM, EM, DL, EM, EM, EM, DL, EM, DL, EM, EM, EM, DL, EM, EM],
    [TW, EM, EM, TL, EM, EM, EM, DW, EM, EM, EM, TL, EM, EM, TW],
    [EM, DL, EM, EM, DL, EM, EM, EM, EM, EM, DL, EM, EM, DL, EM],
    [EM, EM, DL, EM, EM, DW, EM, EM, EM, DW, EM, EM, DL, EM, EM],
    [EM, EM, EM, TW, EM, EM, TL, EM, TL, EM, EM, TW, EM, EM, EM]
]