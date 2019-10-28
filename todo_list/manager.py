# -*- coding: utf-8 -*-
import sys
import os

# 下面是一些 common 变量 和 common 函数
### 所有事项的位置
todo_dir_path = '/Users/xuzinan/just-for-fun/todo_list/todo_info/'
### 按行读取一个文件中的所有内容，并返回一行的最大长度
def get_todo_from_file(file_path):
	max_len = 0 
	msg = []
	with open(file_path, 'r') as f:
		for line in f.readlines():
			line_strip = line.strip()
			if len(line_strip) <= 0:
				continue
			max_len = max(max_len, len(line_strip.encode('gbk')))
			msg.append(line_strip)
	return max_len, msg
### 输出一个text，并用空格前后补齐到total_len
def print_with_space(text, total_len):
	text_len = len(text.encode('gbk'))
	all_space = total_len - text_len
	left_space = int(all_space / 2)
	righ_space = all_space - left_space
	for i in range(left_space):
		print(' ', end='')
	print(text, end='')
	for j in range(righ_space):
		print(' ', end='')
### 输出行分隔
def print_row_split(max_len):
	for i in range(len(max_len)):
		if i == 0:
			print('  ', end='')
		print('|', end='')
		for j in range(max_len[i]):
			print('-', end='')
		if i == len(max_len)-1: 
			print('|')
### 删除指定内容对应的行
def del_from_file(file_path, content):
	with open(file_path,'r') as r:
		lines=r.readlines()
	with open(file_path,'w') as w:
		for l in lines:
			if content not in l:
				w.write(l)
### 将某一行内容写入文件
def save_to_file(file_path, content):
	with open(file_path, 'a') as f:
		f.write(content + '\n')

# 添加一个todo
def add_todo():
	if len(sys.argv) < 3:
		print('tell me what we need to do')
		return
	print('add some thing todo:', sys.argv[2])
	todo_file_dir = todo_dir_path + 'todo'
	with open(todo_file_dir, 'a+') as f:
		f.write(sys.argv[2] + '\n')


# 删除一个事项
def del_todo():
	if len(sys.argv) == 2:
		print('tell me what to del')
		return 
	elif len(sys.argv) == 3:
		print('tell me del which index')
		return 
	file_path = todo_dir_path + sys.argv[2]
	row_ind = int(sys.argv[3])
	with open(file_path, 'r') as f:
		lines=f.readlines()
		content = lines[row_ind-1]
		print('move this content:', content)
	del_from_file(file_path, content)


# 将一个事项添加到别的列表中
def move():
	if len(sys.argv) == 2:
		print('tell me to move what')
		return 
	elif len(sys.argv) == 3:
		print('tell me which tag to move')
		return 
	elif len(sys.argv) == 4:
		print('tell me where to go')
		return 
	from_file_path = todo_dir_path + sys.argv[2]
	row_ind = int(sys.argv[3])
	to_file_path = todo_dir_path + sys.argv[4]
	with open(from_file_path, 'r') as f:
		lines=f.readlines()
		content = lines[row_ind-1]
		print('move this content:', content)
	del_from_file(from_file_path, content)
	save_to_file(to_file_path, content)


# 展示当前有的所有列表，或者指定某个特定的列表
def show():
	show_list = []
	if len(sys.argv) == 2:
		print('don\'t tell me which to show, so I only show todo, doing and done')
		show_list = ['todo', 'doing', 'done']
# show_list = os.listdir(todo_dir_path)
	else:
		length = len(sys.argv) - 2
		for i in range(length):
			show_list.append(sys.argv[i + 2].strip())

	row_num = 0
	sum_len = 1
	max_len = []  # 每一列中的字串最大长度
	msg = []
	for i in show_list:
		buf_max_len, buf_msg = get_todo_from_file(todo_dir_path + i)
		row_num = max(row_num, len(buf_msg))
		buf_max_len = max(buf_max_len, len(i.encode('gbk')))
		max_len.append(buf_max_len)
		msg.append(buf_msg)
		sum_len = sum_len + buf_max_len + 1
	print_row_split(max_len)
	for i in range(len(show_list)):
		if i == 0:
			print('  ', end='')
		print('|', end='')
		print_with_space(show_list[i], max_len[i])
		if i == len(show_list) - 1:
			print('|')
	print_row_split(max_len)
	for i in range(row_num):
		print(' '+str(i+1), end='')
		for j in range(len(show_list)):
			print('|', end='')
			if len(msg[j]) <= i:
				print_with_space('', max_len[j])
				continue
			print_with_space(msg[j][i], max_len[j])
		print('|')
	print_row_split(max_len)


##########
# 对应的func : 示例					: 示例解释
# add_todo(): add 'text'			: 将'text'作为一个新的todo加入到todolist中
# move()	: move listName1 int1 listName2	: 将列名为 listName1编号为 int1 的todo加入到名为 listName2 的列表中
# show()	: show					: 展示当前已有的列表
##########
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('tell me some instructure, such as \'add\' or \'move\'')
		exit(0)
	if sys.argv[1] == 'add':
		add_todo()
	elif sys.argv[1] == 'mv':
		move()
	elif sys.argv[1] == 'show':
		show()
	elif sys.argv[1] == 'del':
		del_todo()
	else:
		print('I don\'t know what you ask me to do')

