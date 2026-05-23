
name = input("Enter your name: ")
Os = input("Enter your Operating system: ")

if name == "Sardor":
    print(name, "you are Gay!") 
elif Os == "Windows":
    print(name, "you are a kid") 
elif Os == "Linux":
    print(name, "you are in your prime")
else:
    print(name, "welcome!")

print("====================") 



# I dont knwo what i am doing but behind me i have a mom who i looking at me , i guess she is cheking what i am doing , eather this or she is just chiling 
def calculator():
    print("--- Simple Python Calculator ---")
    print("Type 'exit' to close the program.")
    
    while True:
        try:
            # Capture the full expression from the user
            user_input = input("\nEnter expression (e.g., 10 + 5): ")
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            # Using eval() to process the math expression directly
            # Note: eval() is powerful but should only be used with trusted input
            result = eval(user_input)
            print(f"Output: {result}")
            
        except ZeroDivisionError:
            print("Error: You cannot divide by zero.")
        except Exception as e:
            print(f"Error: Invalid input. Please try again.")

# Run the calculator
if __name__ == "__main__":
    calculator()
