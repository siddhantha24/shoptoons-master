import sqlite3

#Open database
conn = sqlite3.connect('final.db')

#Create table
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone INTEGER
		)''')

conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		mainId INTEGER,
		sizeId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId),
		FOREIGN KEY(mainID) REFERENCES main(mainId),
		FOREIGN KEY(sizeID) REFERENCES sizes(sizesId)
		)''')

conn.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')

conn.execute('''CREATE TABLE sizes
		(sizeId INTEGER PRIMARY KEY,
		name TEXT
		)''')

conn.execute('''CREATE TABLE main
		(mainId INTEGER PRIMARY KEY,
		main TEXT
		)''')

conn.execute('''CREATE TABLE Order
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.close()

