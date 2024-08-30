'''
Growing up I noticed my parents sitting down with notebooks and going through 
bank papers, upon asking them, I was told that they were balancing their chequebooks. 
Balancing your chequebook is nothing more than going over your record of 
transactions and seeing if they align with the bank records. Doing this manually is 
a tedious task, so I thought to create a calculator that helps do the calculating. 
Upon asking for your statement balance and your chequebook balance, 
this calculator will read in transactions and also manually ask you to enter in 
transactions not accounted for already in your bank statement.These not 
accounted-for transactions will either be added or subtracted from the statement 
balance in accordance to thier nature (draft or deposit). At the end of the program, 
it will let you know if your chequebook is balanced or not 
(statement balance = chequebook balance).
'''

def get_transactions_draft():
    transactions = []
    draft = []
    
    with open('transactionfile.txt', 'r') as transactionfile:
        for i in transactionfile:
            amount,type_of_transaction = i.strip().split(',')
#splits the read in line at the comma and removes any unnecessary spaces
#assigns variables that represent the amount and type of transaction of the modified read in line
            amount = float(amount)
            #changes the string value of the amount into a float
            txttran = [amount,type_of_transaction]
            #assigns a list containing the read in values to a variable 
            transactions.append(txttran)
            #appends newly assigned list to a list containing all read in transactions
    
        for i in transactions:
            #iterates over the list of read in transactions
            if i[1] == " draft":
            #if the value at index 1 is equal to draft append the index 0 (amount)
                draft.append(i[0])
                
        return draft
        #returns the draft list

def get_transactions_deposit():
    #same flow of logic as the get_transactions_draft function
    transactions = []
    deposit = []
    
    with open('transactionfile.txt', 'r') as transactionfile:
        for i in transactionfile:
            amount, type_of_transaction = i.strip().split(',')
            amount = float(amount)
            txttran = [amount, type_of_transaction]
            transactions.append(txttran)
    
        for i in transactions:
            if i[1] == " deposit":
                deposit.append(i[0])
                
        return deposit
    
def manual_draft_list():
    #this function allows the user to add drafts not accounted for in manually
    
    draft_total = []
    
    while(True):
        #while loop that infinitly prompts user for # of drafts untill a valid integer or float is inputted
        try:
            num_drafts = float(input("enter the number of drafts you had: "))
            break
        except ValueError:
            print("enter a decimal or integer value please")
    
    while num_drafts > 0:
        #while loop that asks user for the value of each draft 
        try:
            draft = float(input("enter the amount of your draft(Must be a integer or decimal value): "))
        except ValueError:
            print ("enter a decimal or integer value please")
            # if the value inputted is not an float value it catches the ValueError and prompts for a valid input
        else:
            draft_total.append(draft)
            # This adds the value of the draft to a list which will be summed with the read in drafts later
            num_drafts -= 1
            #ensures user is only promted to enter in as many drafts as they has inputted earlier
    
    return draft_total
    
def manual_deposit_list():    
    #same format of logic as for the manual_draft_list function
    deposit_total = []
    
    while(True):
        try:
            num_deposits = float(input("enter the number of deposits you had: "))
            break
        except ValueError:
            print('enter a decimal or integer value please')
        
    while num_deposits > 0:
        try:
            deposit = float(input("enter the amount of your deposit(Must be a decimal or integer value): "))
        except ValueError:
            print('enter a decimal or integer value please')
        else:
            deposit_total.append(deposit)
            num_deposits -= 1
            
    return deposit_total 

def deposits_sum():
    #This functions calculates the total sum of the deposits of user
    list_of_manual_deposits = manual_deposit_list()
    #assign variable to the function that has a list of manually entered deposits
    list_of_read_in_deposits = get_transactions_deposit()
    #assign variable to the function that has a list of read in deposits
    return sum(list_of_manual_deposits + list_of_read_in_deposits)
    # add the two lists together and use the sum function to calculate the total of deposits 
    
def drafts_sum():
    #same flow of logic as the deposits_sum function
    listc = get_transactions_draft()
    listd = manual_draft_list()
    return sum(listc+listd)
  
def checkbook_balance_calculator():
    while(True):
        #asks user for their current statement balance and only accepts a valid integer or decimal value
        try:
            statement_balance = float(input("what is your current statement balance?: "))
            break
        except ValueError:
            print("enter a valid integer or decimal value")
            
    while(True):
        #asks user for their checkbook balance and only accepts a valid integer or decimal value
        try:
            checkbook_balance = float(input("what is your current checkbook balance?: "))
            break
        except ValueError:
            print("enter a valid integer or decimal value")
            
    final_statement_balance = statement_balance + deposits_sum() - drafts_sum()
    # subtracts drafts from the inputted statement balance and add deposits too it
    
    with open('cps109_a1_output.txt','w') as f:
        f.write(str(final_statement_balance))
        # writes out statement balance to a file
    
    if checkbook_balance != final_statement_balance:
        return print("\n------------------------------------------------------------------------","\nYour Checkbook Balance is", checkbook_balance, "and your calculated Statement Balance is", final_statement_balance,"\nYour checkbook and statements are not balanced!, check for missed deposits and or drafts!")
    else:
        return print("\n------------------------------------------------------------------------","\nYour Checkbook Balance is", checkbook_balance, "and your calculated Statement Balance is", final_statement_balance,"\nYour checkbook and statements balanced!, All Done!")

checkbook_balance_calculator()