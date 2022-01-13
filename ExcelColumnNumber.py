def columnNumber(tile):
    col_num = 0
    alpha_dict = {"A": 1, "B": 2, "C": 3, 'D': 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
                  "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    for idx, i in enumerate(range(len(tile)-1, -1, -1)):
        col_num += (alpha_dict[tile[i]]*(26**idx))
    print(col_num)

    return


tc = "NTP"
columnNumber(tc)
