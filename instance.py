import json
import os
import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('d', help='to Add word meaning to the Dictionary')
#parser.add_argument('t', help='Translate English word to Hindi meaning.')
#parser.add_argument('q', help='Play Quiz game!')


args = parser.parse_args()


filename = 'instance.json'
if os.path.exists(filename):
	with open(filename,'r') as f:
		dictionary = json.load(f)
		f.close()
else:
	dictionary = {}
	
	
	
	
# Add to Dictionary
#choice = input('Add new data? y/n ')
if args.d == 'd':
	while True:
		word = input('Word: ')
		if word == 'q':
			break
		meaning = input('meaning: ')
		if meaning == 'q':
			break
		dictionary[word] = meaning
	with open(filename,'w') as f:
		json.dump(dictionary,f)
		f.close()







#Getting meaning from Dictionary
elif args.d == 't':
	while True:
		word = input('Translate: ')
		if word == 'q':
			break
		if word not in dictionary:
			err = 'Not Exist in the Dictionary. You can add this to the Dictionary.'
		try:
			print(dictionary[word])
		except Exception as e:
			print("'"+word+"'", err)
			if e is not None:
				new_Word = input('Do you want to add to Dictionary? y/n ')
				if new_Word == 'y':
					if new_Word == 'q':
						break
					its_meaning = input('Meaning: ')
					dictionary[word] = its_meaning
				with open(filename,'w') as f:
					json.dump(dictionary,f)
					f.close()








# Quiz section
elif args.d == 'q':
	score = 0
	while True:
		quiz = list(dictionary.keys())
		rankey = random.choice(quiz)
		print(f'The Question is {rankey}')
		answer = input('Your answer?  \n')
		if answer == dictionary[rankey]:
			score = score+10
		elif answer == 'q':
			break
		else:
			print(f'Wrong! correct answer is "{dictionary[rankey]}"')
	try:
		print("				 Score: ",score)
	except Exception as e:
		pass
else:
	print('choose correct option. d for add to Dictionary, t for Translation, q for Quiz.')