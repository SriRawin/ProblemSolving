def restoreString(s, indices):
    shuffled = [0]*len(indices)
    for index, i in enumerate(indices):
        shuffled[i] = s[index]
    print("".join(shuffled))


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
restoreString(s, indices)
