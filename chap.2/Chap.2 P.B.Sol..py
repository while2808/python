#!/usr/bin/env python
# coding: utf-8

# # Chap.2 P.B. Sol.

# ### 152. Write a program to determine a given number is ‘odd’ or ‘even’ and print the following message “Number is ODD” or “Number is Even”. 

# In[ ]:


a = int(input("enter no.: "))
if(a%2==0):
    print("Number is Even")
else:
    print("Number is ODD")


# ### 153. Write a program to check if the input number is positive, negative or zero.

# In[ ]:


a = int(input("enter no.: "))
if(a > 0):
    print("+ve")
elif(a<0):
    print("-ve")
else:
    print("Zero!!")


# ### 154. Write a program to find the maximum number among the three input numbers.

# In[ ]:


a = int(input("Enter Value : "))
b = int(input("Enter Value : "))
c = int(input("Enter Value : "))
if(a < b):
    if(c < b):
        print("b is greater")
    else:
        print("c is greater")
elif(b < c):
    if(c < a):
        print("a is greater")
    else:
        print("c is greater")
else:
    print("a is greater")


# ### 155. Write a program to check if year is a leap year or not (Nested If).

# In[ ]:


year = int(input("Enter Year.: "))
if(year % 4 == 0) or (year%400 == 0 and y%100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# ### 156. Write a program to find sum of first N natural numbers given by user.

# In[ ]:


a = int(input("enter no.: "))
sum = 0
i = 0
while(i <= a):
    sum = sum + i
    i+=1
print("Sum is :",sum)


# ### 157. Write a program to find average of first N natural numbers given by user.

# In[ ]:


a = int(input("enter no.: "))
sum = 0
i = 0
while(i <= a):
    sum = sum + i
    i+=1
print("Sum is :",sum)
print("Avg.is :", sum/a)


# ### 158. Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’

# In[ ]:


a = int(input("Enter No.(starting point): "))
b = int(input("Enter No.(endind point): "))
c = int(input("Enter No.(divisible value): "))
for i in range(a+1, b+1):
    if(i%c==0):
        print(i,"is divisible by",c)


# ### 159. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

# In[ ]:


for number in range(7):  # Loop through numbers from 0 to 6
    if number != 3 and number != 6:  # Check if the number is not 3 or 6
        print(number)  # Print the number if it's not 3 or 6        
# i = 0
# while i<=10:
#     if((i == 3) or (i == 6)):
#         break
#     else:
#         continue
#         print(i)
#         i += 1


# ### 160. Write a Python program to print the multiplication table of given number by user.

# In[ ]:


n = int(input("Enter No.: "))
for i in range(1,11):
    print(n,'*',i,'=',n*i)


# ### 161. Write a program to find the factorial of a number provided by the user.

# In[ ]:


n = int(input("Enter No.: "))
f = 1
for i in range(2,n+1):
    f *= i
print("fact is",f)


# ### 162. Write a python program to display the Fibonacci sequence up to n-th term.

# In[ ]:


n = int(input("Enter No.: "))
a,b = 0,1
c = 0
while(c<n):
    print(a,end=" ")
    nth = a + b
    a = b
    b = nth
    c += 1
# end -> don't print in new line


# ### 163. Write a program to take 10 values from keyboard using loop and print their average on the screen

# In[ ]:


sum = 0
a = 0
for i in range(10):
    a = int(input("enter no."))
    sum += a
print("Sum is :", sum)
print("Avg. is :", sum/10)


# ### 164. Write a program to reverse a number.

# In[ ]:


n = int(input("Enter No.: "))
rev = 0
while n>0:
    r = n % 10
    rev = (rev*10) + r
    n = n // 10
print("Reverse :", rev)


# ### 165. Write a program to check whether a number is Armstrong number or not

# In[ ]:


num = int(input("Enter a number: "))
l = len(str(num))
sum = 0
temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** l
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# ### 166. Write a program to check if a number is prime or not.

# In[ ]:


# num = int(input("Enter the desired number: "))

# flag = False

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break

# if flag:
#     print("The number entered is not a prime number")
# else:
#     print("The number entered is a prime number")

# one more option take count var.
num = int(input("Enter the desired number: "))
count = 0
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            count += 1

if(count == 0):
    print("The number entered is a prime number")
else:
    print("The number entered is not a prime number")


# ### 167. Write a program to print prime numbers between given interval from user.

# In[ ]:





# ### 168. Draw a pattern using a python program: 
# ### *
# ### * *
# ### * * *
# ### * * * *

# In[ ]:


i = 1
while i<=4:
    print("* "*i)
    i += 1
# *
# * *
# * * *
# * * * *


# ### 169. Draw a pattern:

# In[ ]:


for i in range(5,0,-1):
    print(" "*(5-i),'*'*i)


#  *****
#   ****
#    ***
#     **
#      *


# ### 170.

# In[ ]:


for i in range(1,5):
    print(" "*(5-i),('*'+' ')*i)

#      * 
#     * * 
#    * * * 
#   * * * * 

# for i in range(5,0,-1):
#     print(" "*(5-i),('*'+' ')*i)
    
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 


# ### 171.

# In[ ]:


for i in range(5,0,-1):
    print('*'*i)
# *****
# ****
# ***
# **
# *


# ### 172.

# In[ ]:


for i in range(5,0,-1):
    for j in range(1, i+1):
        print(j,end=" ")
    print()
    
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 


# ### 173.

# In[ ]:


for i in range(1,5,1):
    for j in range(1, i+1):
        print(j,end=" ")
    print()
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 


# ### 174.

# In[ ]:


for i in range(0,5):
    print(i*str(i))

# 1
# 22
# 333
# 4444


# ### 175.

# In[ ]:


for i in range(1,5):
    if(i%2==0):
        print('#'*i)
    else:
        print('*'*i)

# *
# ##
# ***
# ####


# ### 176.

# In[ ]:





# ### 177.

# In[ ]:


for i in range(1,5):
    print(" "*(4-i),end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4


# ### 181. Write a python program to print all numbers between 1 and 100 (including 1 and 100) that are both, Disarium and Harshad numbers.
# ### A number is said to be a Disarium number when the sum of its digit raised to the power of their respective positions 
# ### becomes equal to the number itself.
# ### For example, 175 is a Disarium number as follows:
# ### 11+ 72 + 53 = 1+ 49 + 125 = 175
# ### A harshad number is a number that is divisible by the sum of its digits. E.g., the number 18 is a harshad number, because 
# ### the sum of the digits 1 and 8 is 9 (1 + 8 = 9), and 18 is divisible by 9. 
# ### Grading scheme:
# ### 2 marks for writing correct code for checking Disarium number
# ### 2 marks for writing correct code for checking Harshad number
# ### 1 mark for writing correct code for only printing those numbers that are both, Disarium and Harshad numbers.

# In[ ]:


# num = int(input("Enter No.: "))
# l = len(str(num))
# sum = 0
# temp = num
# r = l

# while temp > 0:
#    digit = temp % 10
#    sum = sum + digit ** r
#    temp //= 10
#    r -= 1
# print(sum)

for num in range(1,1001):
    hrsd = 0
    l = len(str(num))
    sum = 0
    temp = num
    r = l
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** r
        hrsd = hrsd + digit
        temp //= 10
        r -= 1
    if(sum==num)and(num%hrsd==0):
        print(num) 
'''Ans. is:
1
2
3
4
5
6
7
8
9
135
518
'''
# Diasarium No.
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 89
# 135
# 175
# 518
# 598


# ### 182. Ask the user to enter 10 test scores. Write a program to do the following:
# ### a)	If user enters score greater than 100, then give warning to user that entered score is more than 100 and take that 
# ### input again from user. b)	Print out the highest and lowest scores.
# ### c)	Print out the average of the scores. d)	Print out the second largest score.
# ### e)	Drop the two lowest scores and print out the average of the rest of them.
# ### Note: Use of Python Data structures like string, list, tuple etc. and their inbuilt function is not allowed.
# ### For Ex.
# ### If Input is like following:
# ### Enter Test Score: 80
# ### Enter Test Score: 65
# ### Enter Test Score: 98
# ### Enter Test Score: 70
# ### Enter Test Score: 93
# ### Enter Test Score: 130
# ### Entered score is more than hundred, so enter again
# ### Enter Test Score: 95
# ### Enter Test Score: 50
# ### Enter Test Score: 40
# ### Enter Test Score: 75
# ### Enter Test Score: 72
# ### Output should be:
# ### Highest Score is: 98
# ### Lowest Score is: 40
# ### Average Test Score is: 73.8
# ### Second Largest Score is: 95
# ### Average after dropping the two lowest scores: 81.0

# In[3]:


s = 0
f_max = 0
f_min = 100
c = 1
while(c <= 10):
    num = int(input(f"Enter {c} Score : "))
    if(num>100):
        print("Entered score is more than hundred, so enter again")
        continue
    c += 1
    s += num
    if(num>f_max):
        s_max = f_max
        f_max = num
    elif(num>s_max):
        s_max = num
    
    if(num<f_min):
        s_min = f_min
        f_min = num
    elif(num<s_min):
        s_min = num
    drop = s - f_min - s_min

print("Highest Score is:", f_max)
print("Lowest Score is:", f_min)
print("Second Largest Score is:", s_max)
print("Average Test Score is:", s/10)
print("Average after dropping the two lowest scores:", drop/8)


# ### 183. Write a program to encode a number by changing the digits in the given positive integer by user. The rule for changing the 
# ### digits in number will be:
# ### If the digit in number is between 0 to 8 than replace the number with 1 to 9 respectively. (incrementing each digit by +1).
# ### If the digit is 9, then replace it with 0.
# ### To encode a number, replace digits in following manner:
# ### For example:
# ### Input: 31590218
# ### Output: The number after encoding is: 42601329
# ### For example:
# ### Input: 9259
# ### Output: The number after encoding is: 360
# ### For example:
# ### Input: 65217001
# ### Output: The number after encoding is: 76328112
# ### Original Digit in Number 	 New Digit after Encoding
# ### 0	 1
# ### 1	 2
# ### 2	 3
# ### 3	 4
# ### 4	 5
# ### 5	 6
# ### 6	 7
# ### 7	 8
# ### 8	 9
# ### 9	 0
# ### Note: Use of Python Data structures like string, list, tuple etc. and their inbuilt function is not allowed.

# In[ ]:


input_number = int(input("Enter a positive integer: "))

encoded_number = 0
place = 1  # To keep track of the current place (units, tens, etc.)

while input_number > 0:
    digit = input_number % 10  # Get the last digit
    input_number = input_number // 10  # Remove the last digit

    # Apply encoding rules
    if digit == 9:
        new_digit = 0
    else:
        new_digit = digit + 1

    # Build the encoded number
    encoded_number += new_digit * place
    place *= 10  # Move to the next place

# Output the result
print("The number after encoding is:", encoded_number)


# ### 184. Write a python program to swap first and last digits of a number using loop.
# ### (for example: input = 123456 then output=623451) 

# In[5]:


n = int(input("Enter a No.: "))
l = len(str(n))
# temp = n
# l = 0
# while temp>0:
#     temp//=10
#     l += 1
last = n%10
first = n //(10**(l-1))
mid = (n%(10**(l-1)))//10
new = last * (10 **(l-1))+ (mid*10)+ first
print(new)


# In[ ]:




