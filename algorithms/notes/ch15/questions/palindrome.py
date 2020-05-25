
def palindrome(s):
    longest_pal = ''
    best_lcs_m = None
    if s is '':
        return '', []
    for k in range(len(s)):
        #lcs_m = [[None] * len(s) for _ in range(len(s))]
        #pal = lcs_mirrors(s, 0, len(s)-1, k, lcs_m)
        lcs_m = lcs_bu(s, k)
        pal = lcs_m[0][len(s)-1]
        print(k, pal, s[k], s)
        for row in lcs_m:
            print(row)
        if len(pal) > len(longest_pal):
            longest_pal = pal
            best_lcs_m = lcs_m
    return longest_pal, best_lcs_m

def lcs_bu(s, k):
    lcs_m = [[None] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        lcs_m[i][k] = s[k]
        lcs_m[k][i] = s[k]
    for i in range(k -1 , -1, -1):
        for j in range(k + 1, len(s), 1):
            if s[i] == s[j]:
                lcs_m[i][j] = s[i] + lcs_m[i+1][j-1] + s[j]
            else:
                if len(lcs_m[i][j-1]) > len(lcs_m[i+1][j]):
                    lcs_m[i][j] = lcs_m[i][j-1]
                else:
                    lcs_m[i][j] = lcs_m[i+1][j]
    return lcs_m

def lcs_mirrors(s, i, j, k, lcs_m):
    if lcs_m[i][j] is not None:
        return lcs_m[i][j]
    elif i == k or j == k:
        lcs = s[k]
    elif s[i] == s[j]:
        lcs = s[i] + lcs_mirrors(s, i +1, j-1, k, lcs_m) + s[j]
    else:
        # the longer one of the left or the right
        lcs_l = lcs_mirrors(s, i+1, j, k, lcs_m)
        lcs_r = lcs_mirrors(s, i, j-1, k, lcs_m)
        if len(lcs_l) > len(lcs_r):
            lcs = lcs_l
        else:
            lcs = lcs_r
    lcs_m[i][j] = lcs
    #print("check {} {} {} => {}".format(i, j, k, lcs))

    return lcs

strs = ['abcba', 'a', 'chactactha', '']

for str_i in strs:
    pal, lcs_m = palindrome(str_i)
    print("{} => {}".format(str_i, pal))
    for row in lcs_m:
        print(row)
