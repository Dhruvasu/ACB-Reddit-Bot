# ACB-Reddit-Bot

ACB (Article Checking Bot) is a Reddit bot that analyzes every post in a particular subreddit and checks for grammatical errors, particularly involving the use of indefinite articles "a" and "an". The bot replies with "The article 'a' must be followed by a consonant" or "The article 'an' must be followed by a vowel" when correcting mistakes. 
To run the ACB.py file, first fill in the parameters to praw.Reddit(). Following are the parameters required:
  1) client_id and client_secret: found after creating a new script app is registered with a Reddit account
  2) user_agent: can be anything! Usually of the form "\<OS used>:\<bot name>:\<bot version> (by /u/\<Reddit username>)"
  3) username: Reddit username of account associated with bot
  4) password: Reddit password of account
Also ensure that praw and Python are installed (preferrably the latest version). Crontab can also be used to automate the bot. 
