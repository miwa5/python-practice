while True:
    try:
        amount_spent = float(input("How much was spent? "))
        print(f"You've spent ¥{amount_spent:.2f}")
        break
    except ValueError:
        print("Please enter a valid number")
