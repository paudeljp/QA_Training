def function1(age):
    if age <=10:
        print("Your are is",age,"so you are child.")
    elif 10<age<40:
        print("your age is",age,"so you are young.")
    else:
        print("You are old",age,"so you are old.")

if __name__ == "__main__":
    age = int(input('Please enter your age: '))
    function1(age)