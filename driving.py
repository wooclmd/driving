country = input('請問你是哪國人?: ')
age = input('你的年齡是: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以開車')
	else:
		print('你還不能開車')