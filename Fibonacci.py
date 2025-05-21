# Fibonacci Sequence (for loop): Input N. 
# Print the first N terms of the Fibonacci sequence
first_term=0
second_term=1
num=5

while num>0:
    print(first_term)
    next_term=first_term+second_term
    first_term=second_term
    second_term=next_term
    num-=1

print("the series is=",first_term,second_term,next_term)