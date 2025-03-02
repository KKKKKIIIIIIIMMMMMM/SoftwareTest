def alternate(s):
    chars = list(set(s)) 
    max_len = 0
    
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            c1, c2 = chars[i], chars[j]
            last = None
            valid = True
            current_len = 0

            for c in s:
                if c == c1 or c == c2:
                    if c == last:
                        valid = False
                        break
                    last = c
                    current_len += 1
            if valid:
                max_len = max(max_len, current_len)
    
    return max_len

print(alternate("beabeefeab"))