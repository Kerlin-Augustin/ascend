age = 42

age = age - 10

print(age)

input_value = input("Give me a number ")

print(input_value)

sum = int(input_value) + 25

print(sum)

if(age < 16):
    print('They can not drive')
elif(age < 18):
    print("They can't hate from outside the club, because they can't even get in.")
elif(age < 21):
    print("they can not drink")
elif(age < 25):
    print("they can not rent cars affordably")
elif(age < 30):
    print("they can not rent fancy cars affordably")
elif(age >= 30):
    print("them there is nothing left to look forward too")

def subtract_two_numbers(a, b):
    print(a - b)

subtract_two_numbers(10, 7)

def divide_three_numbers(a,b,c):
    print(int((a/b)/c))

divide_three_numbers(125,5,5)

def multiply_three_numbers(a,b,c):
    print(a * b * c)

multiply_three_numbers(5,5,5)

def remainder(a,b,c):
    print((a + b) % c)

remainder(5,10,4)

def algorithm(a,b,c,d):
    first_two = a * b
    if(first_two > 100):
        print(first_two + (c + d))
    elif(first_two < 100):
        print(first_two - (c - d))
    elif(first_two == 100):
        print((a * b * c) % d)

algorithm(10,9,10,10)