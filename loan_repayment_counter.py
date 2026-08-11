import math

MENU_CONTENT = """
===========================
- Type [pay] to pay this month's loan repayment
- Type [quit] to quit
===========================
"""

total_loan_amount = int(input("ENTER TOTAL LOAN AMOUNT: "))
monthly_repayment_amount = int(input("ENTER PARTIAL AMOUNT FOR MONTHLY REPAYMENTS: "))

safe_monthly_repayment_amount = math.ceil(monthly_repayment_amount)

remaining_loan_amount = total_loan_amount

while remaining_loan_amount > 0:
    print(MENU_CONTENT)
    menu_input = input("Type your option: ")
    if menu_input == 'pay':
         remaining_loan_amount = remaining_loan_amount - safe_monthly_repayment_amount
         print(f"From your Total Amount [{total_loan_amount} USD.]")
         print(f"You have now paid another fixed amount for this month [i.e. {safe_monthly_repayment_amount} USD.]")
         print("*****************")
         print(f"Your remaining loan amount to be repaid is [{remaining_loan_amount} USD.]")
