def countJewelsInStones(J, S):
    return sum(s in J for s in S)

J = "abcd"
S = "aabbccd"
result = countJewelsInStones(J, S)
print(result)
