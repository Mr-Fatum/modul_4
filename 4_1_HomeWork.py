s = input()
h = len(s)
print(s[:h] == s[:len(s) - h - 1:-1])