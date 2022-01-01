'''
2048 Demo
Main Script
Language: Python
Last Updated: 2021-12-31
Author: Chloris
'''

import random

hashpool = list(range(1, 17))

class Unit:
	def __init__(self, x_, y_):
		self.value = 0; self.x = x_; self.y = y_

dict_direction = {
	'W': (-1, 0),
	'S': (1, 0),
	'A': (0, -1),
	'D': (0, 1)
}

Board = []

def Move_Unit(x, y, command): # Move Each Unit
	# print("({}, {}) 到此一游".format(x + 1, y + 1))
	dx = dict_direction[command][0]; dy = dict_direction[command][1]
	xn = x + dx; yn = y + dy
	if Board[x][y].value == 0: return
	while True:
		# print("True")
		if xn < 0 or xn > 3 or yn < 0 or yn > 3:
			break
		nxt = Board[xn][yn]
		# print(nxt.value, Board[x][y].value)
		if nxt.value == 0:
			Board[xn][yn].value = Board[x][y].value
			Board[x][y].value = 0
		elif nxt.value == Board[x][y].value and type(nxt.value) == type(Board[x][y].value):
			Board[xn][yn].value *= 2.0; Board[x][y].value = 0  # The Protection Process
			break
		else:
			break
		x = xn; y = yn
		xn += dx; yn += dy
	return

def OutPut():
	for i in range(4):
		for j in range(4):
			print(Board[i][j].value, end = ' ' if j != 3 else '\n')


def Recovery():
	for i in range(4):
		for j in range(4):
			Board[i][j].value = int(Board[i][j].value)


def Move(command):
	if command == 'W' or command == 'A':
		for i in range(4):
			for j in range(4):
				Move_Unit(j, i, command) if command == 'W' else Move_Unit(i, j, command)
	elif command == 'D' or command == 'S':
		for i in range(4):
			for j in range(4):
				Move_Unit(i, j, command) if command == 'D' else Move_Unit(j, i, command)
	Recovery()


def RandGenerate(): # Generate the 2 (or 4) randomly
	if len(hashpool) == 0:
		return False
	idx = random.choice(hashpool)
	hashpool.remove(idx)
	x = (idx - 1) // 4; y = (idx - 1) % 4
	# print(x + 1, y + 1)
	Board[x][y].value = 2 if random.randint(0, 9) else 4
	return True

def UpdateHash():
	hashpool.clear()
	for i in range(4):
		for j in range(4):
			if Board[i][j].value == 0:
				hashpool.append(i * 4 + j + 1)


Board = [[Unit(i, j) for j in range(4)] for i in range(4)]

def main():
	RandGenerate()
	UpdateHash()
	while True:	
		OutPut()
		command = input()
		Move(command)
		RandGenerate()
		UpdateHash()

if __name__ == '__main__':
	main()