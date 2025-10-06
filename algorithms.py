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
       

def find_max(numbers):#O(1)
    max_num = numbers[0]#O(1)
    for num in numbers:# loop runs n times where n is the length of the list so O(n)
        if num > max_num:#   # O(1) per iteration → total O(n)
            max_num = num #  # O(1) per iteration → total O(n)

    return max_num
# Overall time complexity is O(n)
        
input_List = [3,5,7,8,9,10] #O(1)
print("The maximum number is:",find_max(input_List)) #O(1)

def linear_search(numbers, target): #O(1)
    for num in numbers: #  loop runs n times where n is the length of the list so O(n)
        if num == target: # O(1) per iteration → total O(n)
            print("Found") # O(1)
            return "True" # O(1)
    print("Not Found") # O(1)
    return "False" # O(1)
    
linear_search(input_List, 9) # O(n)
        
def login_system(username, password):
    return username == "admin" and password == "pass123"
# Overall time complexity is O(1)

# Initial state
logged_in = False # O(1)

while True: # Loop is potentially infinite → controlled by user input 
    choice = input(
        "\nChoose an option:\n"
        "1. Factorial\n"
        "2. Find Max\n"
        "3. Linear Search\n"
        "4. Login\n"
        "5. Exit\n"
        "Enter your choice: "
    ) # depending on how many times the user interacts this will be O(k) where k is the number of interactions

    if choice == '5': # O(1) 
        print("Exiting program.")
        break

    if choice == '4': # O(1) 
         if logged_in:
              print("You are already logged in.") 
              break
         else:
             username = input("Enter username: ")
             password = input("Enter password: ")
             logged_in = login_system(username, password)
         if logged_in:
            print("Login successful.")
         else:
            print("Login failed.")

    elif not logged_in  and choice in ['1','2','3']: # O(1)
        print("You must log in first to use this functionality please choose option 4 to login.")

    elif choice == '1': # O(1)
        num = int(input("Enter a positive integer: ")) # O(1)
        print("Factorial:", factrial(num)) #O(n) where n is the input number

    elif choice == '2': # O(1)
        input_list = list(map(int, input("Enter numbers separated by space: ").split())) # O(1)
        print("Maximum number:", find_max(input_list)) # O(n) where n is the length of input_list

    elif choice == '3': # O(1)
        input_list = list(map(int, input("Enter numbers separated by space: ").split())) # O(1)
        target = int(input("Enter number to search for: ")) # O(1)
        linear_search(input_list, target) # O(n) where n is the length of input_list

    else:
        print("Invalid choice.") # O(1)

# overall time complexity is O(k*n) because the operations are nested inside a loop that runs k times based on user interaction and n is the size of the input for the chosen operation