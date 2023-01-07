#Justin Stevens CIS261 Lab 2

enter_date = input("Please enter date as Month Day, Year:  ")
while enter_date != '-1': 
    tokens= enter_date.split()   
    month= tokens[0]
    if month == 'January':
        month_int = 1
    