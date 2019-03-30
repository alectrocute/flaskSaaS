'''
This might not be the exact code used since it is pure python and we are inplementing this in Flask, but the logic will stay the same.

This will go over an input string and weight the relevance of it based on JSON values.
'''

import json

with open('wordlist.json') as f:
  data = json.load(f)
# print (data) 
# {'words': {'cat': 'meow', 'dog': 'bark'}}
# TO get BARK we would call data['words']['dog']
# follow this logic when grabbing stuff 

# DATA -> WORD -> ROLES
# data["website"]["roles"]
words = [x for x in data]
# user input is being POST'd so the Flask routing thing will run a function on it
def bestMatch(postData):
  for i in postData.split(" "):
    if i in words:
      #tooltip prompt pops up for data[i]["roles"]
      #iterates over the roles to add them
      pass
      
#That's actually it for the JSON logic. Of course it will be different with Flask + we have to actually style it.
