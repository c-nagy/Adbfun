import time
import dataset

db = dataset.connect('sqlite:///adobepws.db')
table = db['adobepws']

#Stage 1: Creating and pickling [password, hint] reference list:
print " [+] Reading list of encrypted passwords file..."
stage1start = time.time()
with open('cred') as openfileobject:
	pass_and_hint = []
	print " [+] Building database. Go take a walk, this will take a long time."
	for line in openfileobject:
       		pipe_removal = line.split('|-')
		if len(pipe_removal) == 6:
			email = pipe_removal[2][:-1] #[:-1] removes last '-' char from email str
			passwd = pipe_removal[3][:-3] #[:-3] removes last three "==-" chars from passwd str
			hint = pipe_removal[4]
			if len(hint) > 0: #If hint is empty, ignore line
				#pass_and_hint.append([passwd, hint, email])
				table.insert(dict(passwd=passwd, hint=hint, email=email))
stage1end = time.time()
print "~" + str(int((stage1end - stage1start)/60)) + " minutes"



