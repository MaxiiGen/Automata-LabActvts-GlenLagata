def dfa2(word):
    st = "q0"
    finals = ["q0","q1"]
    
    for ch in word:
        if st == "q0":
            if ch == "a":
                st = "q1"
            if ch == "b":
                st = "q2"
        elif st == "q1":
            if ch == "a":
                st = "q1"
            if ch == "b":
                st = "q3"
        elif st == "q2":
            if ch == "a":
                st = "q1"
            if ch == "b":
                st = "q2"
        elif st == "q3":
            if ch == "a":
                st = "q3"
            if ch == "b":
                st = "q3"
    
    if st in finals:
        return True
    else:
        return False


tests = ["", "a", "b", "aa", "bb", "ab"]

for t in tests:
    if dfa2(t):
        print(t, "ACCEPTED")
    else:
        print(t, "REJECTED")
