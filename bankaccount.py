accounts = {}
# Created a bank account program that creates new bank accounts, finds accounts, receives the balance of an account, makes deposits and withdrawals. I tested the program using the main function.

def create_acct(number, name, balance):
	global accounts
	if not accounts.get(number):
		acct = {'num':number, 'name':name, 'bal':balance}
		accounts[number] = acct
		result = ('success', acct)
	else:
		result = ('error', 'account exists', number)
	return result
def main():
	global accounts
	print(create_acct(123, 'Jeff', 10))
	print(create_acct(987, 'Donald T.', 1000000))

	print('\nthe account dictionary is:')
	print(accounts)

	print('\ntesting find_account:')
	print(find_account(123))
	print(find_account(987))
	print(find_account(555))

	print('\ntesting get_balance:')
	print(get_balance(123))
	print(get_balance(987))
	print(get_balance(555))

	print('\ntesting deposit:')
	print(deposit(123, 100))
	print(deposit(987, 50))
	print(deposit(555, 10))

	print('\ntesting withdraw:')
	print(withdraw(123, 100))
	print(withdraw(987, 50))
	print(withdraw(555, 10))

def find_account(number):
	global accounts
	for x in accounts:
		if accounts.get(number):
			x =("account", accounts[number])
	
		else:
			x =("error","no such account",number)
	return x
def get_balance(number):
	global accounts
	findres = find_account(number)
	if findres[0] == 'account':
		print("success!")
		x1 = ("balance",accounts[number]['bal'])
		return x1
	else:
		print("Error! the account does not exist")
		return findres
 
def deposit(number,deposit):
	global accounts
	findres = find_account(number)
	if findres[0] == 'account':
		print("success!")
		x1 = ("balance",number,deposit,
accounts[number]['bal']+deposit)
		accounts[number]['bal'] = accounts[number]['bal']
		return x1
	else:
		x =("error","no such account",number)
		return x
def withdraw(number,withdraw):
	global accouunts
	findres = find_account(number)
	if findres[0] == 'account':
		print("success!")
		x1 = ("withdraw",number,withdraw,
accounts[number]['bal'])
		accounts[number]['bal'] = accounts[number]['bal']
		return x1
	else:
		x =("error","no such account",number)
	return x

if __name__ == '__main__':
        main()

