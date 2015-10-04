import time #Keep track of bottlenecks in code stages
import collections
import sys
import os #To check if database is prebuilt
import sqlite3 #Create and query database

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
BO = '\033[1m'   # bold
NO = '\033[0m'   # normal

#Initialization stuffs
answers = open('answers.txt', 'w') #Answers save loc.

#Database generation
print " [*] checking if database exists already"
stage1start = time.time()
if os.path.isfile('adb1000.db'):
    conn = sqlite3.connect('adb1000.db') #DB initialize
    c = conn.cursor() #SQLite req
    print " [*] yes, database is here!"
else:
    print " [*] nope, we will have to generate one now"
    conn = sqlite3.connect('adb1000.db') #DB initialize
    c = conn.cursor() #SQLite req
    print " [*] generating database, please be patient"
    #Create sqlite table
    c.execute('''CREATE TABLE adb
		(passwd TEXT, hint TEXT, email TEXT)''')
    print " [*] reading list of encrypted passwords file"
    cred = open('cred1000')
    #Formatting data for table
    for line in cred:
	pipe_removal = line.split('|-')
	if len(pipe_removal) == 6: 
		passwd = pipe_removal[3][:-3]
		hint = pipe_removal[4]
		email = pipe_removal[2][:-1]
		if len(hint) > 0:
                        #Inserting data into table
			c.execute("INSERT INTO adb (passwd, hint, email) VALUES (?, ?, ?)",
				(passwd, hint, email))
    print " [*] finished generating database, that only had to be done once"
#Close out database for now
    conn.commit()
    conn.close()
#Calculate stage time estimation
stage1end = time.time()
print "~" + str(int((stage1end - stage1start)/60)) + " minutes"


"""
#Stage 2: Create list of only passwords:
print "Stage 2: Creating list of only passwords..."
stage2start = time.time()
passwds = []
for line in pass_and_hint:
	passwds.append(line[0])
stage2end = time.time()
print "~" + str(int(stage2end - stage2start)/60) + " minutes"

#Stage 3: Counting replication amount:
print "Stage 3: Counting replication amount..."
stage3start = time.time()
sorted_rep_count = collections.Counter(passwds).most_common()
stage3end = time.time()
print "~" + str(int(stage3end - stage3start)/60) + " minutes"

#Stage 4: Gather all hints applicable to current puzzle
#current_pass_loc = current line number of source pass in sorted_rep_count[]
#hints = number of allowed hints.
loc_on_list = 0 #Current scan location in pass_and_hint[] for applicable hints
def gather_hints(current_pass_loc, hints):
	print current_pass_loc
	global loc_on_list
	print "Gathering hints..."
	stage4start = time.time()
	applicable_hints = []
	while loc_on_list < len(pass_and_hint) and len(applicable_hints) <= hints:
		if sorted_rep_count[current_pass_loc][0] == pass_and_hint[loc_on_list][0]:
			hint_str = pass_and_hint[loc_on_list][2] + W + NO +": " + O + BO + pass_and_hint[loc_on_list][1] + W + NO
			applicable_hints.append(hint_str)
		loc_on_list+=1	
	if loc_on_list >= len(pass_and_hint):
		print "Out of hints!"
	stage4end = time.time()
	print "~" + str(int(stage4end - stage4start)/60) + " minutes"
	return applicable_hints

def fragment(passwd):
	return "x"*len(passwd)


answer_list = []
count = 0
def display_puzzle(hints):
	global loc_on_list
	global count
	print count
	for current_pass_loc in range(count, len(sorted_rep_count)):
		current_hints = gather_hints(current_pass_loc, hints)
		sys.stderr.write("\x1b[2J\x1b[H") #Clear terminal when done loading hints
		print "\n" + " "*38 + BO + G + sorted_rep_count[current_pass_loc][0] + NO + W
		print " "*38 + BO + R + fragment(sorted_rep_count[current_pass_loc][0]) + NO + W + '\n'
		centered = []
		for i in range(len(current_hints)): #Calculating center text display
			center = 55
			current = current_hints[i]
			colon_pos = current.index(':')
			calc = center - colon_pos
			centered.append(" "*calc + current)
		for hint in centered:
			print hint 
		selection = raw_input("\n" + " "*23 + BO + C + "[A]" + W + NO + "nswer, " + P + BO + "[M]" + W + NO + "ore hints, " + P + BO +"[S]" + W + NO + "kip " + P + BO + "[Q]" + W + NO + "uit: ")
		if selection.upper() == "M":
			display_puzzle(hints)
		elif selection.upper() == "A" or selection == '':	
			answer = raw_input("What is the answer?: ")
			print "\n"
		elif selection.upper() == "Q":
			answers.close()
			exit()
		elif selection.upper() == "S":
			continue
		else:
			answer = raw_input("What is the answer?: ")
			print "\n"
		count += 1
		if len(answer) > 0:
			answer_list.append([answer, sorted_rep_count[current_pass_loc][0]])
			answers.write(str(sorted_rep_count[current_pass_loc][0]) + " = " + str(answer + "\n"))
			loc_on_list = 0
	
display_puzzle(25)
answers.close()
print answer_list
"""
