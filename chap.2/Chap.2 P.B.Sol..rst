Chap.2 P.B. Sol.
================

152. Write a program to determine a given number is ‘odd’ or ‘even’ and print the following message “Number is ODD” or “Number is Even”.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    a = int(input("enter no.: "))
    if(a%2==0):
        print("Number is Even")
    else:
        print("Number is ODD")

153. Write a program to check if the input number is positive, negative or zero.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    a = int(input("enter no.: "))
    if(a > 0):
        print("+ve")
    elif(a<0):
        print("-ve")
    else:
        print("Zero!!")

154. Write a program to find the maximum number among the three input numbers.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

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

155. Write a program to check if year is a leap year or not (Nested If).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    year = int(input("Enter Year.: "))
    if(year % 4 == 0) or (year%400 == 0 and y%100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

156. Write a program to find sum of first N natural numbers given by user.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    a = int(input("enter no.: "))
    sum = 0
    i = 0
    while(i <= a):
        sum = sum + i
        i+=1
    print("Sum is :",sum)

157. Write a program to find average of first N natural numbers given by user.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    a = int(input("enter no.: "))
    sum = 0
    i = 0
    while(i <= a):
        sum = sum + i
        i+=1
    print("Sum is :",sum)
    print("Avg.is :", sum/a)

158. Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    a = int(input("Enter No.(starting point): "))
    b = int(input("Enter No.(endind point): "))
    c = int(input("Enter No.(divisible value): "))
    for i in range(a+1, b+1):
        if(i%c==0):
            print(i,"is divisible by",c)

159. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

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

160. Write a Python program to print the multiplication table of given number by user.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    n = int(input("Enter No.: "))
    for i in range(1,11):
        print(n,'*',i,'=',n*i)

161. Write a program to find the factorial of a number provided by the user.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    n = int(input("Enter No.: "))
    f = 1
    for i in range(2,n+1):
        f *= i
    print("fact is",f)

162. Write a python program to display the Fibonacci sequence up to n-th term.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

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

163. Write a program to take 10 values from keyboard using loop and print their average on the screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    sum = 0
    a = 0
    for i in range(10):
        a = int(input("enter no."))
        sum += a
    print("Sum is :", sum)
    print("Avg. is :", sum/10)

164. Write a program to reverse a number.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    n = int(input("Enter No.: "))
    rev = 0
    while n>0:
        r = n % 10
        rev = (rev*10) + r
        n = n // 10
    print("Reverse :", rev)

165. Write a program to check whether a number is Armstrong number or not
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

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

166. Write a program to check if a number is prime or not.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

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

167. Write a program to print prime numbers between given interval from user.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


168. Draw a pattern using a python program:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\*
~~

.. _section-1:

\* \*
~~~~~

.. _section-2:

\* \* \*
~~~~~~~~

.. _section-3:

\* \* \* \*
~~~~~~~~~~~

.. code:: ipython3

    i = 1
    while i<=4:
        print("* "*i)
        i += 1
    # *
    # * *
    # * * *
    # * * * *

169. Draw a pattern:
~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    for i in range(5,0,-1):
        print(" "*(5-i),'*'*i)
    
    
    #  *****
    #   ****
    #    ***
    #     **
    #      *


.. parsed-literal::

     *****
      ****
       ***
        **
         *
    

170.
~~~~

.. code:: ipython3

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


.. parsed-literal::

         * 
        * * 
       * * * 
      * * * * 
    

171.
~~~~

.. code:: ipython3

    for i in range(5,0,-1):
        print('*'*i)
    # *****
    # ****
    # ***
    # **
    # *


.. parsed-literal::

    *****
    ****
    ***
    **
    *
    

172.
~~~~

.. code:: ipython3

    for i in range(5,0,-1):
        for j in range(1, i+1):
            print(j,end=" ")
        print()
        
    # 1 2 3 4 5 
    # 1 2 3 4 
    # 1 2 3 
    # 1 2 
    # 1 


.. parsed-literal::

    1 2 3 4 5 
    1 2 3 4 
    1 2 3 
    1 2 
    1 
    

173.
~~~~

.. code:: ipython3

    for i in range(1,5,1):
        for j in range(1, i+1):
            print(j,end=" ")
        print()
    # 1 
    # 1 2 
    # 1 2 3 
    # 1 2 3 4 


.. parsed-literal::

    1 
    1 2 
    1 2 3 
    1 2 3 4 
    

174.
~~~~

.. code:: ipython3

    for i in range(0,5):
        print(i*str(i))
    
    # 1
    # 22
    # 333
    # 4444


.. parsed-literal::

    
    1
    22
    333
    4444
    

175.
~~~~

.. code:: ipython3

    for i in range(1,5):
        if(i%2==0):
            print('#'*i)
        else:
            print('*'*i)
    
    # *
    # ##
    # ***
    # ####


.. parsed-literal::

    *
    ##
    ***
    ####
    

176.
~~~~


177.
~~~~

.. code:: ipython3

    for i in range(1,5):
        print(" "*(4-i),end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    
    #     1 
    #    1 2 
    #   1 2 3 
    #  1 2 3 4


.. parsed-literal::

        1 
       1 2 
      1 2 3 
     1 2 3 4 
    

