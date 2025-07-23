###### Write a program that takes a string, string should be of even length. Divide 

###### the string into two equals parts, check the number of vowels in both the parts 

###### of the string. If both parts of string have same number of vowels then return 

###### true otherwise return false. 



s = "rebels"

vowels = "AEIOUaeiou"

length = len(s)

mid = length // 2



if length % 2 == 0:

&nbsp;   first\_half = s\[:mid]

&nbsp;   second\_half = s\[mid:]

else:

&nbsp;   first\_half = s\[:mid]

&nbsp;   second\_half = s\[mid+1:]

count1 = 0

count2= 0

for i in first\_half :

&nbsp;   if i in vowels :

&nbsp;       count1 += 1

for j in second\_half :

&nbsp;   if j in vowels :

&nbsp;       count2 += 1

if count1 == count2 :

&nbsp;   print("True")

else :

&nbsp;   print("False")

&nbsp;       

&nbsp;       

&nbsp;       

&nbsp;       

