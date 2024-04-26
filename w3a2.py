# ATM 







# define concept
# balance = 10000


# def withdraw(amount):
#     global balance
#     if amount > balance:
#         ("Insuffucient funds!")
#     else:
#         balance -= amount
#     print("withdraw succesful")
#     print(f"your new acouint balance is {balance}")

# def deposite(amount):
#     global balance
#     balance += amount
#     print("deposite succesful")
#     print(f"your new acouint balance is {balance}")

# def check_balance():
#     global balance
#     print(f"your new acouint balance is {balance}")



# # welcome text

# pin1 = 7788
# pin = int(input("please enter your pin: "))
# # main programme
# trial = 3

# while pin1 == pin:
#     trial -= 1
#     if pin1 == pin:
#         print("Welcome Kelvin Smith")
#         print("please enter one of the options: ")
#         print("1. Withdraw")
#         print("2. Deposit")
#         print("3. Check Balance")
#         print("4. Cancel")
#         print()

#         choice = input("Enter your choice: ")
#         # pin = int(input("Enter pin: "))

#         if pin == pin1:
#             if "1" == choice:
#                 amount = float(input("Enter amount to withdraw: "))
#                 withdraw(amount)

#             elif "2" == choice:
#                 amount = float(input("Enter amount to Deposit: "))
#                 deposite(amount)

#             elif "3" == choice:
#                 check_balance()

#             elif  choice == "4":
#                 print("Goodbye")
#                 break
            
#         else:
#             print("Invalid entry")
#             print("please try again.")
#     continue            




# print("welcome to ATM")
# trial = 3
# userpin = 1234

# while trial != 0:
#     pin = int(input("please enter your 4 digit pin number: "))
#     if pin != userpin:
#         trial -=1
#         print("wrong pin number ", trial, "trials left")
#     else:
#         userchoice = input("d: Deposit or w: Withdraw: ")
#         if userchoice == "d":
#             userdeposit = input("Enter the amount you would like to deposit: ")
#             print(userdeposit, "$ have been deposited into your account.")
#         elif userchoice == "w":
#             userwithdraw = input("Enter the amount you would like to withdraw: ")
#             print(userwithdraw, "$ have been withdrawn from your account.")
#     userexit = input("would you like to continue? Y/N")
#     if userexit == "N":
#         print("thank you for using ATM")
#         break




# # Define the initial balance and PIN
# balance = 1000.0
# correct_pin = "1234"
# pin_attempts = 3  # Number of allowed PIN attempts

# # Function to display the ATM menu
# def display_menu():
#     print("\nATM Menu:")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")

# # Function to handle the ATM operations
# def atm():
#     global balance

#     while pin_attempts > 0:
#         # Prompt the user to enter the PIN
#         pin = input("Enter your PIN: ")

#         # Check if the entered PIN is correct
#         if pin == correct_pin:
#             print("PIN accepted!")
#             while True:
#                 display_menu()
#                 choice = input("Please select an option: ")

#                 if choice == "1":
#                     # Check balance
#                     print(f"Your current balance is: ${balance:.2f}")
#                 elif choice == "2":
#                     # Deposit
#                     deposit_amount = float(input("Enter the amount to deposit: $"))
#                     if deposit_amount > 0:
#                         balance += deposit_amount
#                         print(f"${deposit_amount:.2f} deposited successfully!")
#                     else:
#                         print("Invalid amount. Please try again.")
#                 elif choice == "3":
#                     # Withdraw
#                     withdraw_amount = float(input("Enter the amount to withdraw: $"))
#                     if withdraw_amount > 0:
#                         if withdraw_amount <= balance:
#                             balance -= withdraw_amount
#                             print(f"${withdraw_amount:.2f} withdrawn successfully!")
#                         else:
#                             print("Insufficient balance.")
#                     else:
#                         print("Invalid amount. Please try again.")
#                 elif choice == "4":
#                     # Exit
#                     print("Thank you for using the ATM. Have a great day!")
#                     break
#                 else:
#                     print("Invalid option. Please try again.")

#             break  # Break out of the loop if the user chooses to exit
#         else:
#             # Incorrect PIN
#             pin_attempts -= 1
#             if pin_attempts > 0:
#                 print(f"Incorrect PIN. You have {pin_attempts} attempts remaining.")
#             else:
#                 print("Too many incorrect attempts. Account locked.")

# # Run the ATM function
# atm()






# # Define the initial balance and PIN
# balance = 1000.0
# correct_pin = "1234"
# pin_attempts = 3  # Number of allowed PIN attempts

# # Start the ATM session
# while pin_attempts > 0:
#     # Prompt the user to enter the PIN
#     pin = input("Enter your PIN: ")

#     # Check if the entered PIN is correct
#     if pin == correct_pin:
#         print("PIN accepted!")
#         # Main loop for ATM menu
#         while True:
#             # Display the menu
#             print("\nATM Menu:")
#             print("1. Check Balance")
#             print("2. Deposit")
#             print("3. Withdraw")
#             print("4. Exit")

#             # Get the user's choice
#             choice = input("Please select an option: ")

#             # Process the user's choice
#             if choice == "1":
#                 # Check balance
#                 print(f"Your current balance is: ${balance:.2f}")
#             elif choice == "2":
#                 # Deposit
#                 deposit_amount = float(input("Enter the amount to deposit: $"))
#                 if deposit_amount > 0:
#                     balance += deposit_amount
#                     print(f"${deposit_amount:.2f} deposited successfully!")
#                 else:
#                     print("Invalid amount. Please try again.")
#             elif choice == "3":
#                 # Withdraw
#                 withdraw_amount = float(input("Enter the amount to withdraw: $"))
#                 if withdraw_amount > 0:
#                     if withdraw_amount <= balance:
#                         balance -= withdraw_amount
#                         print(f"${withdraw_amount:.2f} withdrawn successfully!")
#                     else:
#                         print("Insufficient balance.")
#                 else:
#                     print("Invalid amount. Please try again.")
#             elif choice == "4":
#                 # Exit
#                 print("Thank you for using the ATM. Have a great day!")
#                 break
#             else:
#                 print("Invalid option. Please try again.")

#         # Break out of the PIN loop if the user chooses to exit
#         break
#     else:
#         # Incorrect PIN
#         pin_attempts -= 1
#         if pin_attempts > 0:
#             print(f"Incorrect PIN. You have {pin_attempts} attempts remaining.")
#         else:
#             print("Too many incorrect attempts. Account locked.")
































balance = 10000
correct_pin = 9988
pin_attempt = 2

while pin_attempt > 0:
    pin = int(input("Enter your pin: "))
    if pin == correct_pin:
        while True:
            print("Welcome!")
            print()
            print("1. to Withdraw")
            print("2. to Deposit")
            print("3. to Check Balance")
            print("4. to Cancel")
            print("")
            entry = int(input("Please select one option: "))

            if entry == 1:
                withdraw_amount = int(input("Enter amount: "))
                print()
                print("you entered: ", withdraw_amount)
                print(f"your current account balance is: {balance - withdraw_amount}")
                print()
                cont1 = input("to perform another transaction press Y or N to exit: \n")
                if cont1 == "Y":
                    continue
                else:
                    break
            elif entry == 2:
                deposit_amount = int(input("Enter amount to Deposit: "))
                print()
                print("you entered: ", deposit_amount)
                print(f"your current account balance is: {balance - deposit_amount}")
                cont2 = input("to perform another transaction press Y or N to exit: \n")
                if cont2 == "Y":
                    continue
                else:
                    break
            elif entry == 3:
                print(f"your current account balance is: {balance}")
                cont3 = input("to perform another transaction press Y or N to exit: \n")
                if cont3 == "Y":
                    continue
                else:
                    break
            elif entry == 4:
                print()
                print("Goodbye!")
                break
        break    

    else:
        if pin != correct_pin:
            pin_attempt -= 1
            print("wrong pin, you have: ", pin_attempt, "left")
        else:
            print("Invalid entry")
            break