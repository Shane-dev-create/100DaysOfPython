#Write your code below this line 👇
import math

#Solution number 1

# def prime_checker(number):
#     if number % number == 0 and number % 2 == 1:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number.")

#Solution number 2

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number.")

#Solution number 3

def prime_checker(number):
    prime_num = True
    # Thonny v3.7 does not support isqrt() function
    number2 = math.trunc(math.sqrt(number))
    print(f'{number2}')
    # Add fuction that checks and calculates all prime numbers of the input according to the math algo
    for i in range(2, number):
        if number % i == 0:
            prime_num = False
    if prime_num == True:        
        print("It's a prime number.")
    else:
        print("It's not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



