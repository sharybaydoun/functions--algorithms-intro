def Fibonacci_sequence(n): # iterative approach 
   
    if n < 0:
        return "Input must be a non-negative integer"
    if n ==0 :
        return [0]
    elif n==1:
        return[0,1]
    sequence=[0,1]
    for i in range(2, n): # loop runs n-2 times so O(n)
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    
    return sequence
      # Overall time complexity is O(n)

def fibonacci_sequence_recursive(n):
    if n < 0:
        return "Input must be a non-negative integer"
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1] 
    
    seq = fibonacci_sequence_recursive(n-1)
    
    if len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    
    return seq   # Overall time complexity is O(n)

num=int(input("Enter a positive integer:"))
print("Fibonacci sequence iterative approach up to",num,":",Fibonacci_sequence(num))
print("Fibonacci sequence recursive approach up to",num,":",fibonacci_sequence_recursive(num))

    
