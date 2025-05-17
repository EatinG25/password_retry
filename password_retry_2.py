password = 'a123456'
chance = 3
while True:
	inpass = input('Please input passwaord:')
	if inpass == password:
		print('success !')
		break
	else:
		chance = chance - 1
		if chance == 0:
			print('error ! you have no chance.')
			break
		else:
			print('error ! you only have', chance, 'chance.')
