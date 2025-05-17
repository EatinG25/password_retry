password = 'a123456'
chance = 3
while chance > 0:
	chance = chance - 1
	inpass = input('Please input passwaord:')
	if inpass == password:
		print('success !')
		break
	else:
		if chance == 0:
			print('error ! you have no chance.')
			break
		else:
			print('error ! you only have', chance, 'chance.')
