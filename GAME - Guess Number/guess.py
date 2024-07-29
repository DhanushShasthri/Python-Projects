import random
def compare(a,b):
    if a == b:

        print("Correct!")
        return 1
    elif a < b:
        print("Too high")
    else:
        print("Too low")


a=random.randint(1,30)
print(a)
guess=False
c=0
num=0

for num in range (0,100):
    b = int(input("Enter your guess(1-30)"))
    c=c+1
    d=compare(a,b)
    if d==1:
        guess=True
        break
print(f"Attempts- {c}")
