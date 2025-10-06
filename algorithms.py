def factrial(n): #Time complexity for this line is O(n)
    if n<0:#Time complexity O(1)
        return "Input should be a non-negative integer"#O(1)
    if n==0 or n==1:#O(1)
        return 1 #O(!)
    if n>1:#O(1)
       result=1
       for i in range(2,n+1):#Loop runs (n-1) times so time complexity is O(n) where n is the input number
           result*=i    # O(1) per iteration so O(n)
        
    return result #O(1)
# Overall time complexity is O(n)
input_num=int(input("Enter a positive integer:"))
print("The factorial of",input_num,"is",factrial(input_num))

def find_max(numbers):#O(1)
    max_num = numbers[0]#O(1)
    for num in numbers:# loop runs n times where n is the length of the list so O(n)
        if num > max_num:#   # O(1) per iteration → total O(n)
            max_num = num #  # O(1) per iteration → total O(n)

    return max_num
# Overall time complexity is O(n)
input_list = list(map(int, input("Enter numbers separated by spaces: ").split())) #O(1)
print("The maximum number is :",find_max(input_list))

def linear_search(numbers, target): #O(1)
    for num in numbers: #  loop runs n times where n is the length of the list so O(n)
        if num == target: # O(1) per iteration → total O(n)
            print("Found") # O(1)
            return "True" # O(1)
    print("Not Found") # O(1)
    return "False" # O(1)
    
input_numbers = list(map(int,input("Enter numbers separated by spaces: ").split()))
input_target = int(input("Enter the target number to search for:"))
linear_search(input_numbers, input_target) # O(n)

        

       