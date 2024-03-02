from tax_brackets import federal_tax_brackets, state_tax_brackets

def input_income_details():
    income_type = input("Enter your income type (Monthly/Annual/Hourly): ").lower().strip()
    if income_type == 'hourly':
        hourly_rate = float(input("Enter your hourly wage: $"))
        return ((hourly_rate * 40) * 4) * 12
    elif income_type == 'monthly':
        monthly_income = float(input("Enter your monthly income: $"))
        return monthly_income * 12
    elif income_type == 'annual':
        return float(input("Enter your annual income: $"))
    else:
        print("Invalid input. Please enter Monthly, Annual, or Hourly.")
        return input_income_details()

def calculate_social_security_tax(income):
    SOCIAL_SECURITY_TAX_RATE = 0.062
    SOCIAL_SECURITY_TAX_CAP = 147000
    return min(income, SOCIAL_SECURITY_TAX_CAP) * SOCIAL_SECURITY_TAX_RATE

def calculate_medicare_tax(income, filing_status):
    MEDICARE_TAX_RATE = 0.0145
    ADDITIONAL_MEDICARE_TAX_RATE = 0.009
    ADDITIONAL_MEDICARE_TAX_THRESHOLD = {
        'SINGLE': 200000,
        'MARRIED FILING JOINTLY': 250000,
        'MARRIED FILING SEPARATELY': 125000,
        'HEAD OF HOUSEHOLD': 200000,
    }
    tax = income * MEDICARE_TAX_RATE
    if income > ADDITIONAL_MEDICARE_TAX_THRESHOLD[filing_status]:
        tax += (income - ADDITIONAL_MEDICARE_TAX_THRESHOLD[filing_status]) * ADDITIONAL_MEDICARE_TAX_RATE
    return tax

def calculate_state_tax(state_name, income):
    tax_info = state_tax_brackets.get(state_name)
    if tax_info is None:
        return 0  # No state income tax
    elif 'flat_rate' in tax_info:
        return income * tax_info['flat_rate']  # Apply flat tax rate directly
    else:
        tax_amount = 0
        # Variable to keep track of income that has already been taxed
        previously_taxed_income = 0
        for bracket in tax_info:
            if income > bracket[0]:  # Check if income exceeds the lower bound of the bracket
                # Calculate income applicable to the current bracket
                applicable_income = min(income, bracket[1]) - previously_taxed_income
                # Apply tax rate to the applicable income
                tax_amount += applicable_income * bracket[2]
                # Update the amount of income that has been taxed
                previously_taxed_income += applicable_income
            else:
                break  # Exit loop if income does not exceed the lower bound of the bracket
        return tax_amount

def calculate_federal_tax(filing_status, income):
    # Access the correct set of brackets based on filing status
    # Convert the filing_status to uppercase to match the keys in your dictionary
    tax_brackets = federal_tax_brackets[filing_status.upper()]
    
    tax_due = 0
    for start, end, rate in tax_brackets:
        if income > start:
            taxable_income = min(income, end) - start
            tax_due += taxable_income * rate
        if income <= end:
            break

    return tax_due


def input_expenses():
    expenses = {}
    print("Please enter your monthly expenses in USD below")
    expenses_categories = ['401k/ira_contribution', 'student_loan_payment', 'home_mortgage_payment', 'other_loans',
                           'health_insurance', 'car_insurance', 'phone_bill', 'subscriptions', 'groceries', 'utilities', 
                           'miscellaneous_expenses']
    for category in expenses_categories:
        while True:
            try:
                user_input = input(f"{category.replace('_', ' ').title()}: $")
                # Check if the input is empty or not a number
                if not user_input.strip() or not user_input.replace('.', '', 1).isdigit() or float(user_input) < 0:
                    raise ValueError
                expenses[category] = float(user_input)
                break  # Break the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    total_monthly_expenses = sum(expenses.values())
    return total_monthly_expenses


def main():
    filing_status = input("Please enter your filing status (Single, Married Filing Jointly, Married Filing Separately, Head of Household): ").upper().strip()
    state_name = input("Please enter your state: ").title().strip()
    annual_income = input_income_details()

    federal_tax = calculate_federal_tax(filing_status, annual_income)
    state_tax = calculate_state_tax(state_name, annual_income)
    social_security_tax = calculate_social_security_tax(annual_income)
    medicare_tax = calculate_medicare_tax(annual_income, filing_status)

    remaining_annual_income = annual_income - (federal_tax + state_tax + social_security_tax + medicare_tax)
    monthly_income_remaining = remaining_annual_income / 12

    total_monthly_expenses = input_expenses()
    monthly_income_after_expenses = monthly_income_remaining - total_monthly_expenses

    print(f"\nAnnual Income: ${annual_income:.2f}")
    print(f"Federal Tax Deducted: ${federal_tax:.2f}")
    print(f"State Tax Deducted: ${state_tax:.2f}")
    print(f"Total Social Security Tax Deducted: ${social_security_tax:.2f}")
    print(f"Total Medicare Tax Deducted: ${medicare_tax:.2f}")
    print(f"Remaining Annual Income after Taxes: ${remaining_annual_income:.2f}")
    print(f"Remaining Monthly Income before Expenses: ${monthly_income_remaining:.2f}")
    print(f"Monthly Income after Expenses: ${monthly_income_after_expenses:.2f}")

if __name__ == "__main__":
    main()