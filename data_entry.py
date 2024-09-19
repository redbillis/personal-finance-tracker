from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

# prompt: is what we're going to ask the user to input,
# before they give us the date
# __________
# allow_default: tells us if we should have a default value of today's date
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY format.")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter category ('I' for Inocome, 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    

    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")