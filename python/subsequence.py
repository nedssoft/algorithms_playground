
def isSubsequence(str1, str2):
    for index, char in enumerate(str2):
        if char not in str1:
            return  False
        elif index > 0 and str1.index(char) < str1.index(str2[index-1]):
            return False
    return True

print(isSubsequence('coding', 'iod')) # False


