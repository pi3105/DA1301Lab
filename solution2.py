# ==============================================
# Lab Assignment 4 - String Manipulation (Q10â€“Q11)
# ==============================================

# Q10: Palindrome Rearrangement Checker
def palindrome_checker(s):
    # TODO:
    # - Return "Yes" if string can be rearranged into a palindrome
    # - Return "No" otherwise
    # - Return "input invalid" for empty or non-string
    try:
        s=s.replace(" ","").lower()
        if len(s)==0:
            return "input invalid"
        counter={*list(s)}
        if len(s)%2==0:
            for letter in counter:
                if s.count(letter)%2!=0:
                    return "No"
            return "Yes"
        else:
            count=0
            for letter in counter:
                if s.count(letter)%2!=0:
                    if count<1:
                        count+=1
                    else:
                        return "No"
            return "Yes"
    except:
        return "input invalid"

# Q11: String Rotation Validator
def rotation_checker(s1, s2):
    # TODO:
    # - Return True if s2 is a rotation of s1
    # - Return False otherwise
    # - Return "input invalid" if inputs are not strings or lengths differ
    try:
        if len(s1)!=len(s2):
            return "input invalid"
        for i in range(len(s1)):
            if s2==s1[i:]+s1[:i]:
                return True
        return False
    except:
        return "input invalid"