def decodeHuff(root, s):
    #Enter Your Code Here
    temp = root
    st = ""
    for i in range(len(s)):
        if temp.right == None and temp.left == None:
            st += temp.data
            temp = root
        
        if s[i] == '0':
            temp = temp.left
        elif s[i] == '1':
            temp = temp.right
    st += temp.data
    print(st)