import math
"""
#############################################
# Index:                                    #
#############################################
# Assignments:                              #
Q1. Count Factors - 2                       #
Q2. IsPrime                                 #
Q3. Square root of a number                 #
Q4. Sum of evens                            #
Q5. Power function                          #
Q6. Sum of N natural numbers                #
Q7. Find Iterations                         #
Q8. Divide by 2                             #
#############################################
# Homework                                  #
Q1. Find Perfect Numbers                    #
Q2. Count of primes                         #
Q3. Is Perfect Square ?                     #
Q4. Make it                                 #
Q5. Number of elements in a range           #
Q6. Number of elements in a range - II      #
Q7. Find Armstrong Numbers                  #
#############################################
"""

# Assignments
"""
Q1. Count Factors - 2
Problem Description
Given an integer A, you need to find the count of it's factors.
Factor of a number is the number which divides it perfectly leaving no remainder.

Example : 1, 2, 3, 6 are factors of 6

Problem Constraints
1 <= A <= 109

Input Format
First and only argument is an integer A.

Output Format
Return the count of factors of A.

Example Input
Input 1:5
Input 2:10

Example Output
Output 1:2
Output 2:4

Example Explanation
Explanation 1:
Factors of 5 are 1 and 5.
Explanation 2:
Factors of 10 are 1, 2, 5 and 10.
"""


def count_factors(arg):
    factor_count = 0
    sqrt_arg = math.sqrt(arg)
    i = 1
    while i <= sqrt_arg:
        if arg % i == 0:
            if i != (arg/i):
                factor_count = factor_count + 2
            else:
                factor_count = factor_count + 1
        i = i + 1
    return factor_count


"""
Q2. IsPrime
Problem Description
Given an Integer A. Return 1 if A is prime and return 0 if not.

Problem Constraints
1 <= A <= 1012

Input Format
The first argument is a single integer A.

Output Format
Return 1 if A is prime else return 0.

Example Input
Input 1:A = 5
Input 2:A = 10

Example Output
Output 1:1
Output 2:0

Example Explanation
Explanation 1:5 is a prime number.
Explanation 2:10 is not a prime number.
"""


def is_prime(arg):
    factor_count = 0
    sqrt_arg = math.sqrt(arg)
    i = 1
    return_value = 0
    while i <= sqrt_arg:
        if factor_count > 2:
            return_value = 0
        if arg % i == 0:
            if i != (arg/i):
                factor_count = factor_count + 2
            else:
                factor_count = factor_count + 1
        i = i + 1
    if factor_count == 2:
        return_value = 1
    return return_value


"""
Q3. Square root of a number
Problem Description: Given a number A. Return square root of the number if it is perfect square otherwise return -1.

Problem Constraints: 1 <= A <= 108

Input Format: First and the only argument is an integer A.

Output Format: Return an integer which is the square root of A if A is perfect square otherwise return -1.

Example Input
Input 1:A = 4
Input 2:A = 1001

Example Output
Output 1:2
Output 2:-1

Example Explanation
Explanation 1:sqrt(4) = 2
Explanation 2:1001 is not a perfect square.
"""


def square_root(arg):
    return_value = -1
    root_arg = math.sqrt(arg)
    i = 1
    while i <= root_arg:
        if i * i == arg:
            return_value = i
            break
        i = i + 1
    return return_value


"""Q5. Power function
Q4. Sum of evens
Problem Descriptionimport math
You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A.
Even numbers are those numbers that are divisible by 2.

Problem Constraints: 1 <= N <= 500
Input Format: First and only argument is an integer A.
Output Format: Return an integer denoting the sum of even numbers between [1, A] (both inclusive).

Example Input
Input 1: 5
Input 2: 2Q7. Find Iterations

Example Output
Output 1: 6
Output 2: 2

Example Explanation
Explanation 1: Even numbers between [1, 5] are (2, 4).
Explanation 2: Even numbers between [1, 2] are (2)
"""


def sum_evens(arg):
    count = 0
    i = 1
    while i <= arg:
        if i % 2 == 0:
            count = count + i
        i = i + 1
    return count


"""
Q5. Power function
Problem DescriptionQ7. Find Iterations
You are given two integers A and B.
You have to find the value of AB.import math
NOTE: The value of answer is always less than or equal to 109.

Problem Constraints: 1 <= A, B <= 1000

Input Format: First parameter is an integer A.
              Second parameter is an integer B.

Output Format
Return an integer.

Example Input
Input 1:
 A = 2
 B = 3 
Input 2:
 A = 1
 B = 10 
Q7. Find Iterations
Example Output
Output 1: 8 
Output 2: 1 

Example Explanation
Explanation 1: For A = 2 and B = 3, the value of 23 = 2 * 2 * 2 = 8. 
Explanation 2: For A = 1 and B = 10, the value of 110 = 1.
"""


def power(arg1, arg2):
    final_sum = 1
    i = 0
    while i < arg2:
        final_sum = final_sum * arg1
        i = i + 1
    return final_sum


"""
Q6. Sum of N natural numbers
The sum of n natural numbers is : (n*(n+1))/2
"""

"""
Q7. Find Iterations
Find the number of times below code runs where N is a perfect square

for i -> 1 to N
if(i * i == N)
return i

Ans: sqrt(N)
"""

"""
Q8. Divide by 2
What is the number of times we need to divide N by 2 till it reaches 1 ?
Ans: floor(logN)
"""

# Home_Work
"""
Q1. Find Perfect Numbers
Problem Description
You are given an integer A. You have to tell whether it is a perfect number or not.
Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
A proper divisor of a natural number is the divisor that is strictly less than the number.

Problem Constraints: 1 <= A <= 106

Input Format: First and only argument contains a single positive integer A.

Output Format: Return 1 if A is a perfect number and 0 otherwise.

Example Input
Input 1:

A = 4

Input 2:

A = 6



Example Output

Output 1:

0 

Output 2:

1 



Example Explanation

Explanation 1:

For A = 4, the sum of its proper divisors = 1 + 2 = 3, is not equal to 4.

Explanation 2:

For A = 6, the sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6. 

"""