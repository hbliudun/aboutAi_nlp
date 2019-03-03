

s = 'audacity'

s = print(s[0].upper()+s[1:])



print(s)


x = 3.14159
y = 27.777

def func(num):
    strNum = str(x)
    pointPos = strNum.find('.')
    if pointPos != -1:
        if int(strNum[pointPos+1]) >= 5:
            return int(num)+1
        else :
            return int(num)
    else:
        return num
print (func(x))   
print (func(y)) 

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    biggestNum = biggest(a,b,c)
    if biggestNum == a:
        return bigger(b,c)
    elif biggestNum == b:
        return bigger(a,c)
    else:
        return bigger(a,b)

def find_last(srcStr,key):
    retPos = 0;
    while True:
        tmpNum = srcStr.find(key,retPos)
        if tmpNum == -1:
            break;
        else:
            retPos = tmpNum + 1
    return retPos -1



print (find_last('aaaa', 'a'))
print (find_last('aaaa', 'b'))