rent=int(input("enter the rent:"))
electricity_unit_spend=int(input("enter the unit spend:"))
electricity_unit_charge=int(input("enter the unit charge:"))
no_of_person=int(input("enter no of person:"))

electricity_amount=(electricity_unit_spend * electricity_unit_charge)
total_amount=electricity_amount + rent

payable_amount = (total_amount/no_of_person)

print(f"amount to pay per person: {payable_amount}")
