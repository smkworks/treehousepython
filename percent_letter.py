__author__ = 'seanknowles'

user_string = input("whats your word?: ")
user_num = input("whats your number?: ")

try:
    our_num = int(user_num)
except:
    our_num = float(user_num)

if not'.'in user_num:
    print(user_string[our_num])
else:
    ratio = round(len(user_string)*our_num)
    print(user_string[ratio])