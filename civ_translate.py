import json
file1 = json.loads(open('civgraph.json').read())
file2 = open('makefile1', 'w')
for i in file1:
	str = i + ': '
	str += ' '.join(file1[i])
	file2.write(str + "\n")
	str = '\t@echo ' + i
	file2.write(str + "n")
	str = '\t@echo ' + i + " > " + i
	file2.write(str + '\n\n')
str = 'clean:\n'
for i in file1:
	str += '\t@del ' + i + '\n'
file2.write(str)
