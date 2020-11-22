

import pyodbc

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
import string
from nltk.corpus import wordnet
from itertools import product



conn = pyodbc.connect( 'DRIVER={ODBC Driver 17 for SQL Server};'
                       'SERVER=prj.database.windows.net,1433;'
                       'DATABASE=temp1;UID=ijaffer;'
                       'PWD=$Parrow1')
cursor = conn.cursor()

def read_password(username):
	global cursor

	query = 'SELECT Password FROM dbo.Users2 WHERE Name = ?'
	print(query)
	cursor.execute(query, (username,))
	data = cursor.fetchone()

	return data

def read_data(cursor):
	data = cursor.execute('SELECT * FROM dbo.Users1')
	print(data)
	for row in data:
		print(row)


def pre_process(corpus):
    # convert input corpus to lower case.
    corpus = corpus.lower()
    # collecting a list of stop words from nltk and punctuation form
    # string class and create single array.
    stopset = stopwords.words('english') + list(string.punctuation)
    # remove stop words and punctuations from string.
    # word_tokenize is used to tokenize the input corpus in word tokens.
    corpus = " ".join([i for i in word_tokenize(corpus) if i not in stopset])
    # remove non-ascii characters
    corpus = unidecode(corpus)
    #print(corpus)
    return corpus
#pre_process("Sample of non ASCII: Ceñía. How to remove stopwords and punctuations?")



def match_ranking(desription, interests):
	#interests = interests.split(",")
	score = 0
	desription = pre_process(desription)
	interests = pre_process(interests)
	print(desription, interests)
	allsyns1 = set(ss for word in desription for ss in wordnet.synsets(word))
	allsyns2 = set(ss for word in interests for ss in wordnet.synsets(word))

	count = 0
	total = 0 
	for w1 in allsyns1:
		for w2 in allsyns2:
			val = wordnet.wup_similarity(w1, w2)
			if val != None:
				total += val
				count+=1 
			#print(val)
	avg = total/count 
	print(avg)
	return avg 
	


def find_events(cursor, user):
	data = cursor.execute('SELECT * FROM dbo.Events')
	events = []
	for row in data:
		#if row[1]==user['location']:
		row = list(row)
		row.append(match_ranking(row[5], user['interests']))
		events.append(row)

	## get all possible events sorted by time 
	events = sorted(events, key = lambda x:x[2], reverse=True)
	print(events)
	for event in events:
		match_ranking(event[5], user['interests'])

	## get users interests 



	## create a match ranking using Location and NLP


	events = sorted(events, key = lambda x:x[6], reverse=True)
	#print(events)
    




	
	## return sorted events 

	return events

def get_events(event_name):
	global cursor

	query = 'SELECT * FROM dbo.Events WHERE Name = ?'
	print(query)
	cursor.execute(query, (event_name,))
	data = cursor.fetchall()

	return data

user = {"name":'ishaan', 'location':'Pittsburgh', 
'interests':'religion, swim, gym, coffee, food'}


#find_events(cursor, user)

def add_user(user_info_packet):
	## user info packet like: ( 'Ishaan', N'Australia', 'sh@gmail.com', 'Male','20','Hockey, swim, code, gym, food')
	global cursor
	# query = "INSERT INTO dbo.Users2 ([Name],[Password],[Location],[Email], [Gender], [Age], [Interests]) VALUES" +  " (" + user_info_packet + ")"
	query = "INSERT INTO dbo.Users2 ([Name],[Password],[Location],[Email], [Gender], [Age], [Interests]) VALUES (?)"

	print(query)
	cursor.execute(query, (user_info_packet,))
	cursor.commit()
	print("ADDED User")
	return

def add_interests(username, interests):
	global cursor
	
	# query = "UPDATE dbo.Users2 SET Interests = " +  "'" + interests + "'" + " WHERE Name = " + "'" + username + "'"
	query = "UPDATE dbo.Users2 SET Interests = ? WHERE Name = ?"

	print(query)
	cursor.execute(query, (interests, username))
	cursor.commit()
	print("Updated User")






def add_event(cursor):
	## name, location, date-time, number of attendees, online/inperson, description

	return 42








