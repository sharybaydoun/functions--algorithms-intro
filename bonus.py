def Fibonacci_sequence(n):
   
    if n < 0:
        return "Input must be a non-negative integer"
    if n ==0 :
        return [0]
    elif n==1:
        return[0,1]
    sequence=[0,1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    
    return sequence
    
num=int(input("Enter a positive integer:"))
print("Fibonacci sequence up to",num,":",Fibonacci_sequence(num))

    
   

    