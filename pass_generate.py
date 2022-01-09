# # import random
# # passlen = int(input("enter the length of password"))
# # s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# # p = "".join(random.sample(s,passlen ))
# # print(p)
# import random
# import string
# upper=list(string.ascii_uppercase)
# lower=list(string.ascii_lowercase)
# randome_lower=random.choice(lower)
# randome_upper=random.choice(upper)
# passlen = int(input("enter the length of password"))
# upplen = int(input("enter the length of upper letter"))
# lowlen = int(input("enter the length of lower letter"))
# for i in upplen:

# print(f"{randome_upper} {randome_lower}")

import random
import array
import string
 
# maximum length of password needed
# this can be changed to suit your password length
passlen = int(input("enter the length of password"))
 
# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = list(string.digits)
LOCASE_CHARACTERS = list(string.ascii_lowercase)
UPCASE_CHARACTERS = list(string.ascii_uppercase)
SYMBOLS = list(string.punctuation)
 
# combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
 
# randomly select at least one character from each character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(passlen - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
# # combine the character randomly selected above
# # at this stage, the password contains only 4 characters but
# # we want a 12-character password
# temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
 
# # now that we are sure we have at least one character from each
# # set of characters, we fill the rest of
# # the password length by selecting randomly from the combined
# # list of character above.
# for x in range(MAX_LEN - 4):
#     temp_pass = temp_pass + random.choice(COMBINED_LIST)
 
#     # convert temporary password into array and shuffle to
#     # prevent it from having a consistent pattern
#     # where the beginning of the password is predictable
#     temp_pass_list = array.array('u', temp_pass)
#     random.shuffle(temp_pass_list)
 
# # traverse the temporary password array and append the chars
# # to form the password
# password = ""
# for x in temp_pass_list:
#         password = password + x
password = ""
for x in temp_pass_list:
        password = password + x
# # print out password
print(password)