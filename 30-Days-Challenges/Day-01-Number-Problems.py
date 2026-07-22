# 1. Reverse a Number
def reverse_number(num:int) ->int:
    rev = 0
    while num>0:
        rem = num % 10
        num = num // 10
        rev = rev * 10 + rem
    return rev

# 2. Palindrome Number
def palindrome_number(number:int) ->bool:
    num = number
    rev = 0
    while num>0:
        rem = num % 10
        num = num // 10
        rev = rev * 10 + rem
    return number == rev

# 3. Prime Number
def prime_number(number:int) ->int:
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True

# 4. Greatest Common Divisor
def gcd(num1:int,num2:int) ->int:
    i = 1
    divisor = 1
    while True:
        if num1 % i == 0 and num2 % i == 0:
            divisor = i
        elif i == num1 or i == num2:
            return divisor
        i += 1
    return divisor

# 5. Armstrong_number
def armstrong_number(number:int) ->bool:
    num = number
    res = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        res += rem ** 3
    return res == number