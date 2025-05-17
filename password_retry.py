password = 'a123456'
inpass = input('Please input passwaord:')
chance = 2

while chance >= 0:
	if inpass == password:
		print('success !')
		break
	else:
		print('error ! you only have', chance, 'chance.')
		inpass = input('Please input passwaord:')
		chance = chance - 1
		if chance == 0 and inpass != password:
			print('error ! you have no chance.')
			break