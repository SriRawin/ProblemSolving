def commonString(str_ls):
    common = ""
    for i in range(len(str_ls[0])):
        for j in range(1, len(str_ls)):
            if str_ls[0][i] != str_ls[j][i]:
                return common
        common += str_ls[0][i]
    return common


strs = ["dog", "flow", "flight"]
resutl = commonString(strs)
print(resutl)



