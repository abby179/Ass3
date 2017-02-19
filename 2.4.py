class LevinshteinTable:
	def __init__(self, s1, s2):
		self.s1 = s1
		self.s2 = s2
		self.table = [[(0,'') for _ in range(len(self.s1) + 1)] for _ in range(len(self.s2) + 1)]
	
	def __str__(self):
		printStr = '\n  ' + ''.join(map(lambda x: x.center(5), ' ' + self.s1)) + '\n' + ' '  # for the first string
		for y in range(len(self.s2) + 1):
			for x in range(len(self.s1) + 1):
				printStr += '{}{}'.format(self.table[y][x][0], self.table[y][x][1]).center(5)
			if y != len(self.s2):
				printStr += '\n{}'.format(self.s2[y])  # for the second string
		return printStr
	
	def iterative_levenshtein(self):
		rows = len(self.s1)+1
		cols = len(self.s2)+1
		# source prefixes can be transformed into empty strings 
		# by deletions:
		for i in range(1, rows):
			self.table[0][i] = (i, 'd')
		# target prefixes can be created from an empty source string
		# by inserting the characters
		for i in range(1, cols):
			self.table[i][0] = (i, 'i')
			
		for col in range(1, cols):
			for row in range(1, rows):
				if self.s1[row-1] == self.s2[col-1]:
					cost = 0
				else:
					cost = 1
				minNum = min(self.table[col][row-1][0] + 1,      # deletion
					     self.table[col-1][row][0] + 1,      # insertion
					     self.table[col-1][row-1][0] + cost) # substitution
							 
				if minNum == self.table[col-1][row-1][0] + cost:
					if cost == 0:
						self.table[col][row] = (minNum, 'm')
					else:
						self.table[col][row] = (minNum, 's')
				elif minNum == self.table[col-1][row][0] + 1:
					self.table[col][row] = (minNum, 'i')
				else:
					self.table[col][row] = (minNum, 'd')
						

		
lt = LevinshteinTable('saturday', 'sunday')
lt.iterative_levenshtein()
print(lt)
