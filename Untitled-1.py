

print("--- Welcome to the Examination System ---")


stored_email = "student@example.com"
stored_password = "123"

print("\n--- Phase 2: Login ---")
email = input("Enter Email: ")
password = input("Enter Password: ")


if email == stored_email and password == stored_password:
    print("✅ Access Granted: Welcome to Dashboard")

    print("\n--- Phase 3: Browse Exams ---")
    print("Available Exam: [ Professional Certification Exam ]")
    choice = input("Do you want to book this exam? (yes/no): ")

    if choice.lower() == "yes":
        print("\n--- Phase 4: Payment & Booking ---")
        print("Exam Fees: 1000 SAR")
        pay = input("Pay full fees now? (yes/no): ")
        
        if pay.lower() == "yes":
            print("✅ Payment Successful. Appointment Booked!")
            print("Confirmation message sent to your email.")

            print("\n--- Phase 6: Results & Fail Scenarios ---")
            result = input("Enter Exam Result (pass/fail): ")

            if result.lower() == "pass":
                print("Congratulations! You passed and got the Certificate. ✅")
            else:
                attempt = input("Is this your 1st, 2nd, or 3rd fail? (1/2/3): ")
                if attempt == "1":
                    print("❌ Result: Fail. You must pay 50% fees to re-book.")
                elif attempt == "2":
                    print("❌ Result: Fail. You must pay 25% fees to re-book.")
                elif attempt == "3":
                    print("❌ Result: Fail. Wait 1 month and pay Full Fees to re-book.")
        else:
            print("Booking cancelled. Payment required.")
    else:
        print("Returning to Main Menu.")

else:
    # مسار الـ No في الفلوشارت
    print("❌ Error: Invalid Email or Password. Please try again.")
