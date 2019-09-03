import webbrowser
import random
import csv
file_dir = '/Users/xuzinan/PycharmProjects/crawl_cf/problem.csv'
csv_file = open(file_dir, "r")
reader = csv.reader(csv_file)
score = '0'
with open('in', 'r') as f:
	score = f.readline().strip()
question_url = []
for item in reader:
	if item[3] == '1' or item[1] != score:
		continue
	question_url.append(item[4])

length = len(question_url)
ind = int(random.random()*length)
webbrowser.open(question_url[ind])
