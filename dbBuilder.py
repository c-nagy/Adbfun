import sqlite3

conn = sqlite3.connect('adb.db')
c = conn.cursor()

c.execute('''CREATE TABLE adb
		(passwd TEXT, hint TEXT, email TEXT)''')

#Stage 1: Creating and pickling [password, hint] reference list:
print " [+] Reading list of encrypted passwords file..."
cred = open('cred')
print " [+] Building database. Go take a walk, this will take a long time."
for line in cred:
	pipe_removal = line.split('|-')
	if len(pipe_removal) == 6: 
		passwd = pipe_removal[3][:-3]
		hint = pipe_removal[4]
		email = pipe_removal[2][:-1]
		if len(hint) > 0:
			c.execute("INSERT INTO adb (passwd, hint, email) VALUES (?, ?, ?)",
				(passwd, hint, email))

conn.commit()
conn.close()
