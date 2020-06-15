# Anthony Guzman            8.10            CIS2348
string=input()

str = string.replace(" ", "").lower()

i = 0

ispalindrome = True

while i < len(str)/2:

  if str[i] != str[-1-i]:

    ispalindrome = False

    break

  i+=1

if ispalindrome:

 print (string+ " is a palindrome")

else:

 print (string+ " is not a palindrome")