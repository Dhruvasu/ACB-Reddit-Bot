import praw
import re
import os
import time
import pdb

from praw.exceptions import APIException

def modify(id):
	posts_replied_to.append(id)
	with open("posts_replied_to.txt", "w") as f:
		for post_id in posts_replied_to:
			f.write(post_id + "\n")

reddit = praw.Reddit(client_id='',	#add client_id here
	             client_secret='',	#add client_secret here
		     user_agent='',	#add user_agent here
		     username='',	#add account username here
		     password='')	#add account password here

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

#add name of subreddit where bot will function
subreddit = reddit.subreddit('')
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


for submission in subreddit.hot(limit = 20):
	if submission.id not in posts_replied_to:
		for vowel in vowels:
			phrase1 = ' a ' + vowel
			if phrase1 in submission.title:
				submission.reply("The article 'a' must be followed by a consonant")
				print("Bot replied to ", submission.id)
				modify(submission.id)
				time.sleep(5)
		for consonant in consonants:
			phrase2 = ' an ' + consonant
			if phrase2 in submission.title:
				submission.reply("The article 'an' must be followed by a vowel")
				print("Bot replied to ", submission.id)
				modify(submission.id)
				time.sleep(5)