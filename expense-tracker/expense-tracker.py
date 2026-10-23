expenses = []

user_input = {
    "product" : input ("What did you buy? "),
}

while user_input["product"].strip().lower() != "done":
    try:
        user_input["amount"] = float(input("How much was spent? "))
        expenses.append(user_input)
        for expense in expenses:
            print(f"{expense["product"]} - ¥{expense["amount"]:.2f}")
        user_input = {
        "product" : input ("What did you buy? ")
        }

    except ValueError:
        print("Please enter a valid number")
        user_input = {
        "product" : input ("What did you buy? ")
        }
