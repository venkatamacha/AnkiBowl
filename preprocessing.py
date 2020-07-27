import csv
import json
import simplejson

FILENAME = '/Users/venkatamacha/Downloads/All Decks.csv'
TAG = "United States Medical Licensing Examination / Step 1"
OUT = '/Users/venkatamacha/Documents/GitHub/AnkiBowl/data/all_decks.json'

texts = []
answers = []

def find_n_max(str):
	if "{{c15" in str: 
		return 15;
	if "{{c14" in str: 
		return 14;	
	if "{{c13" in str: 
		return 13;	
	if "{{c12" in str: 
		return 14;	
	if "{{c11" in str: 
		return 11;	
	if "{{c10" in str: 
		return 10;	
	if "{{c9" in str: 
		return 9;	
	if "{{c8" in str: 
		return 8;	
	if "{{c7" in str: 
		return 7;	
	if "{{c6" in str: 
		return 6;	
	if "{{c5" in str: 
		return 5;	
	if "{{c4" in str: 
		return 4;					
	if "{{c3" in str: 
		return 3;	
	if "{{c2" in str: 
		return 2;	
	if "{{c1" in str: 
		return 1;	
	if True:
		return 0;

with open(FILENAME) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		n_max = find_n_max(row[0])
		if n_max > 0:
			for i in range(0, n_max):
				# modify input Anki text
				pretext = (row[0] + '.')[:-1]
				text = pretext + " "

				# isolate the correct answer
				loc = text.find("{{c" + str(i+1))
				subtext = text[loc:]
				subloc = subtext.find("}}")
				preanswer = subtext[6:subloc] ## skip the first 6 characters of {{c#::
				answer = (preanswer + '.')[:-1]
				if "::" in preanswer:
					hintloc = preanswer.find("::")
					answer = preanswer[:hintloc]

				# take the rest of the question
				prequestion = text[:loc] + " BLANK " + subtext[subloc+2:] ##skip the end braces after subloc

				# remove all the other c-answers from the prequestion
				while("{{c" in prequestion):
					extra_loc = prequestion.find("{{c")
					extra_subtext = prequestion[extra_loc:]
					extra_subloc = extra_subtext.find("}}")
					pre_c_answer = extra_subtext[6:extra_subloc] ## skip the first 6 characters of {{c#::
					c_answer = (pre_c_answer + '.')[:-1]
					if "::" in pre_c_answer:
						extra_hintloc = pre_c_answer.find("::")
						c_answer = pre_c_answer[:extra_hintloc]
					mod_prequestion = prequestion[:extra_loc] + c_answer + extra_subtext[extra_subloc+2:] ##skip the end braces after subloc
					prequestion = mod_prequestion
				question = prequestion

				# append to appropriate lists
				texts.append(question)
				answers.append(answer)

with open('/Users/venkatamacha/Documents/GitHub/AnkiBowl/data/nats_prep.json') as f:
  data = json.load(f)

# data = {}
# data["num_tossups_found"] = 0
# data["num_tossups_shown"] = 0
# data["tossups"] = []

data["data"]["tossups"] = []
tossups = []

for i in range(len(texts)):
	sample = {
        "id": 0,
        "text":  texts[i],
        "answer": answers[i],
        "number": 0,
        "tournament_id": 0,
        "category_id": 0,
        "subcategory_id": 0,
        "round": "10",
        "created_at": "",
        "updated_at": "",
        "quinterest_id": 0,
        "formatted_text": texts[i],
        "formatted_answer": answers[i],
        "wikipedia_url": 0,
        "url": "",
        "type": "tossup",
        "tournament": {
          "id": 0,
          "year": 0,
          "name": "",
          "address": "",
          "quality": "",
          "type": 0,
          "link": "",
          "created_at": "",
          "updated_at": "",
          "difficulty": TAG,
          "difficulty_num": 0,
          "url": ""
        },
        "category": {
          "id": 0,
          "name": "",
          "created_at": "",
          "updated_at": "",
          "url": ""
        },
        "subcategory": {
          "id": 0,
          "name": "",
          "created_at": "",
          "updated_at": "",
          "url": ""
        }
       }
	tossups.append(sample)

data["data"]["tossups"] = tossups

file = open(OUT, "w")
file.write(json.dumps(data, indent=4, sort_keys=True))
file.close()





