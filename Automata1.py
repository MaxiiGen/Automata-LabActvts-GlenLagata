def dfa1(word):
    s = "a"
    for c in word:
        if s == "a":
            if c == "0":
                s = "a"
            if c == "1":
                s = "b"
        elif s == "b":
            if c == "0":
                s = "b"
            if c == "1":
                s = "a"
    if s == "b":
        return True
    else:
        return False


tests = ["1","10","101","11","100","00"]

for t in tests:
    if dfa1(t):
        print(t,"ACCEPTED")
    else:
        print(t,"REJECTED")
