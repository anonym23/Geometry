import sqlite3

def save(name, dist):
	connection = sqlite3.connect('results.db')
	cursor = connection.cursor()
	
	query = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, dist REAL)'
	cursor.execute(query)
	
	query = "INSERT INTO items (name, dist) VALUES ('%s', %d)" % (name, dist)
	cursor.execute(query)
	
	connection.commit()
	
	connection.close()
	
	print('done')
	
	
def calcDistance():
	
	bigFingerSize = 6
	print('Размер большого пальца = ' + str(bigFingerSize) + ' см')
	objectSizeProj = float(input('Размер проекции объекта на плоскость большого пальцааа = '))
	fromEyeToFinger = 60
	objectRealSize = int(input('Рельная высота объекта = '))

	fromEyeToObject = objectRealSize * fromEyeToFinger / objectSizeProj

	print('Дальность до объекта = %.2f см' % fromEyeToObject)
	print('Дальность до объекта = %.2f м' % (fromEyeToObject/100))
	
	answer = input('Сохранить результат(y/n)?\n')

	if answer == 'y':
		name = input('Название предмета ')
		save(name, fromEyeToObject)
		
def outputDb():
	print ('\n')
	connection = sqlite3.connect('results.db')
	cursor = connection.cursor()
	
	query = 'SELECT * FROM items'
	cursor.execute(query)
	
	for row in cursor.fetchall():
		print ('%d. %s %.2fм' % (row[0], row[1], row[2] / 100))
	
	connection.close()
	
	print ('\n')
	
def deleteRecord():
	connection = sqlite3.connect('results.db')

	cursor = connection.cursor()
	
	id = int(input('Номер строки '))
	query = 'DELETE FROM items WHERE id=%d' % (id)

	cursor.execute(query)
	
	connection.commit()
	connection.close()
	
	print('done')

action = 0

while action != 4:
	print('''
1. Посчитать расстояние до предмета
2. Вывести данные
3. Удалить запись
4. Выход
	''');
	action = int(input('Действие: '))
	
	if action == 1:
		calcDistance()
	elif action == 2:
		outputDb()
	elif action == 3:
		deleteRecord()