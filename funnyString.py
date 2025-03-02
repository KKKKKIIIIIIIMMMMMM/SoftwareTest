def funnyString(s):
    sr = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(sr[i])-ord(sr[i-1])):
            return 'Not Funny'
    return 'Funny'

print(funnyString('acxz'))
print(funnyString('bcxz'))  