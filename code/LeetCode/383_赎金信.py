def canConstruct(ransomNote: str, magazine: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = {}
    for i in range(26):
        d[alphabet[i]] = [0, 0]
    if len(ransomNote) <= len(magazine):
        for i in range(len(ransomNote)):
            d[ransomNote[i]][0] += 1
        for i in range(len(magazine)):
            d[magazine[i]][1] += 1
        for i in d:
            if d[i][0] > d[i][1]:
                return False
        return True
    else:
        return False


def canConstruct2(ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, '', 1) # 因为只能用一次，那用完就删
            else:
                return False
        return True

if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aaa"
    result = canConstruct(ransomNote,magazine)
    print(result)