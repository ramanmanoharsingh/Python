"""Q19. ATM Program"""

account_balance = 50000
wrong_pin_count = 0
account_status = "Active"

while True:
    if wrong_pin_count < 3:
        pin = int(input("Enter PIN: "))

        if pin == 123456:
            print("Access granted")
            choice = int(input("Enter transaction choice:\n1. Withdraw\n2. Deposit\n3. Balance Check\nEnter choice: "))

            if choice == 1:
                amount = int(input("Enter withdrawal amount: "))

                if amount > account_balance:
                    print("Transaction Status: Unsuccessful")
                    print("Reason: Insufficient balance")
                    print("Remaining Balance:", account_balance)
                    print("Account Status:", account_status)

                else:
                    if amount > 20000:
                        print("OTP verification required")
                        otp = input("Enter OTP: ")

                        if otp == "000000":
                            account_balance = account_balance - amount
                            print("OTP verified")
                            print("Transaction Status: Successful")
                            print("Remaining Balance:", account_balance)
                            print("Account Status:", account_status)
                        else:
                            print("Transaction Status: Unsuccessful")
                            print("Reason: Wrong OTP")
                            print("Remaining Balance:", account_balance)
                            print("Account Status:", account_status)
                    else:
                        account_balance = account_balance - amount
                        print("Transaction Status: Successful")
                        print("Remaining Balance:", account_balance)
                        print("Account Status:", account_status)

            elif choice == 2:
                amount = int(input("Enter deposit amount: "))
                account_balance = account_balance + amount
                print("Transaction Status: Successful")
                print("Remaining Balance:", account_balance)
                print("Account Status:", account_status)

            elif choice == 3:
                print("Transaction Status: Successful")
                print("Remaining Balance:", account_balance)
                print("Account Status:", account_status)

            else:
                print("Transaction Status: Unsuccessful")
                print("Reason: Invalid choice")
                print("Remaining Balance:", account_balance)
                print("Account Status:", account_status)

            break

        else:
            wrong_pin_count = wrong_pin_count + 1
            print("Wrong PIN")
            print("Transaction Status: Unsuccessful")

    else:
        account_status = "Blocked"
        print("Account Status:", account_status)
        break
