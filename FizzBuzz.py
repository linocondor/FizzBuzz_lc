# This program receives a number and then iterates with this rules: if the number(integer) is multiple of 3 print Fizz, if the number is multiple of 5 print Buzz, and if the number is multiple of 3 and 5 print FizzBuzz.
number = int(input("Please enter a number(integer): "));

for i in range(1, number + 1):
    
    if i%3 == 0 and i%5 == 0 :
        print("FizzBuzz")

    elif i%3 == 0 :
        print("Fizz")

    elif i%5 == 0 :
        print("Buzz")
    
    else: 
        print(i)
    



    




