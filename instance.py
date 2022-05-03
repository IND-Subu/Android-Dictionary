import json
import os
import random



filename = 'data.json'
if os.path.exists(filename):
	with open(filename,'r') as f:
		dictionary = json.load(f)
		f.close()
else:
	dictionary = {}
	
	
# Add to Dictionary
choice = input('Options: d/t/q => ')
if choice =='exit':
	print('Thanks for Using our App')
elif choice == 'd':
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
elif choice == 't':
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
elif choice == 'q':
	correct = 0
	for sl in range(1,1000):
		quiz = list(dictionary.keys())
		rankey = random.choice(quiz)
		print(f'{sl} The Question is {rankey}')
		answer = input('Your answer?  \n')
		if answer == 'q':
			break
		elif answer != dictionary[rankey]:
			print(f'Wrong! correct answer is "{dictionary[rankey]}"')
			answer = input('Your answer?  \n')
		
		else:
			correct = correct+1
	sl = sl-1
	try:
		print(f"				 Score: {int((correct/sl)*100)}%")
	except Exception as e:
		pass
else:
	print('choose correct option. d for add to Dictionary, t for Translation, q for Quiz.')