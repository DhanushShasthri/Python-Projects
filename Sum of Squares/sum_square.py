print("Enter the value of n")
n=int(input())
i=1
sum=0
tot_sum=0
while i<n+1:
    sum=i*i
    tot_sum+=sum
    i+=1
print(f"the sum of squares of numbers till {n} is {tot_sum}")

