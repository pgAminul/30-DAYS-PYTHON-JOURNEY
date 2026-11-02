# Task 1 — Smart Name Formatter

# name = input("Enter Your Name").strip()
# case= name.upper()
# count = len(name)
# firstCha= name[0]
# lastCha= name[-1]
# reverse= name[::-1]
# print(f"Hello {case}, your Name length is {count}, your first char of name {firstCha}, your last char of name {lastCha}, if Reverse your name the name will be {reverse}")

# Task 2 — Username Validator

# msg =''
# userName = input("Write Your User Name").strip()
# if len(userName) < 5 or len(userName) > 15:
#     msg = "user Name too short or too big"
#     print(msg)

# elif userName.isalnum() and len(userName) >=5 and len(userName) <=15:
#     msg = "Valid User Name"
#     print(msg)
# else:
#     error = "Someting Error"
#     print(error)


# Task 3 — Email Domain Extractor

# email = input("Enter Your Email").strip()
# ckAtvalid = email.find("@")
# ckUserDomain = email.split("@")
# ckDotValid = email.count(".")

# if ckAtvalid == -1 :
#     print("missing (@)")
# elif ckDotValid == 0:
#     print("missing (.)")
# elif ckUserDomain[0] == "" or  ckUserDomain[-1] == "" :
#     print('missing domain')
# else:
#     print('ok')

# print(f"user Name is {ckUserDomain[0]} Domain is {ckUserDomain[-1]}")

# User-এর কাছ থেকে একটি Sentence Input নেবে।

# Requirements:
# - Sentence-এর Word Count দেখাবে।
# - "python" শব্দটি কতবার আছে, Case-insensitive ভাবে গণনা করবে।
# - সবচেয়ে বড় Word দেখাবে।
# - সব Word Uppercase করে Print করবে।
# Hint: split(), lower(), len(), for Loop।

Sentence = input("Enter Your Sentence").strip()
lowerCase = Sentence.lower()
countt = lowerCase.count("python")
upperCase = Sentence.upper()
spiltWord = upperCase.split(" ")

maximum = 0
largestWord = ""

for length in spiltWord:
    ckLength = len(length)

    if ckLength > maximum:
        maximum = ckLength
        largestWord = length

print(largestWord)