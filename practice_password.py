# 
#password = 'a123456'
#time = 3
#pw = input('Enter your password: ')
#while pw != password:
#	if time > 0:
#		print('Try again')
#		time = time - 1
#		print('You have', time, 'time left')
#		pw = input('Enter your password: ')
#	elif time == 0:
#		print('No more chance!')
#		break
#print('Good job!')

password = 'a123456'
time = 3
while time > 0:
	pwd = input('Enter your password: ')
	if pwd == password:
		print('Login Successfully!')
		break
	else:
		time = time - 1
		print('You have', time, 'time left.')
print('No more chance!')
