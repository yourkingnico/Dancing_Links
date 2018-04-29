#!/usr/bin/python3
import sys
import unittest

class Node:
	def __init__(self, row, column):
		""" Initialize a Node

		:param row: the row of the node
		:param column: the column of the node
		:type row: list
		:type column: list
		"""
		self.row = row
		self.column = column

	def deattach(self):
		""" Deattach the Node """
		self.up.down = self.down
		self.down.up = self.up

	def attach(self):
		""" Attach the Node """
		self.down.up = self.up.down = self
		
class Head:
	def __init__(self, column):
		""" Initialize a Head

		:param column: the column that will be the head
		:type column: int
		"""
		self.column = column

	def deattach(self):
		""" Deattach the Head """
		self.left.right = self.right
		self.right.left = self.left

	def attach(self):
		""" Attach the Head """
		self.right.left = self.left.right = self
		
class Matrix:
	def __init__(self, matrix):
		""" Initialize a Matrix

		:param matrix: the matrix being initialized
		:type matrix: list
		"""
		numberOfRows = len(matrix)
		numberOfColumns = len(matrix[0])
		row = [[ ] for _ in range(numberOfRows)]
		heads = [Head(j) for j in range(numberOfColumns)]
		column = [[head] for head in heads]

		# Master Head 
		self.head = Head(-1)
		heads = [self.head] + heads
		self.linkLeftRight([heads])
		i = 1
		while i < numberOfRows:
			j = 1
			while j < numberOfColumns:
				if matrix[i][j] == 1:
					node = Node(i, j)
					column[j].append(node)
					row[i].append(node)
				j += 1
			i += 1

		self.linkLeftRight(row)
		self.linkUpDown(column)
		self.rows = row
		self.columns = column
		
		
	def linkLeftRight(self, srows):
		""" link the rows on the left and right

		:param srows: the rows being linked
		:type srows: list
		"""
		for srow in srows:
			n = len(srow)
			j = 0
			while j < n:
				srow[j].right = srow[(j + 1) % n]
				srow[j].left = srow[(j - 1 + n) % n]
				j +=1

	def linkUpDown(self, columns):
		""" link the columns up and down

		:param columns: the columns being linked
		:type columns: list
		"""
		for column in columns:
			n = len(column)
			i = 0
			while i < n:
				column[i].down = column[(i + 1) % n]
				column[i].up = column[(i - 1 + n) % n]
				column[i].head = column[0]
				i += 1

	
class AlgorithmX:
	"""TODO: implement """ 
def generic_x(matrix):
	""" 
		TODO: implement this and additional data structures
		.. generic_x: Construct an internal, working version of the matrix as a grid of linked lists. Backtrack recursively on the matrix, removing 
		and restoring columns and rows, until an empty matrix is obtained

		:param matrix: 2-dimensional array to be passes as input
		:type matrix: array<array<boolean>>?
		:return: 2-dimensional array
		:rtype: array
	""" 

	return None 


class AlgorithmXTest(unittest.TestCase):

	def test_node(self):
		""" Make a Node  """
		my_node = Node(0,0)
		self.assertEqual(my_node.row, 0)
		self.assertEqual(my_node.column, 0)
		
	def test_head(self):
		""" Set the Head """
		test_head = Head(0)
		self.assertEqual(test_head.column, 0)
		
	def test_matrix_head(self):
		""" Make sure head is right for a 2x2 matrix """
		test_matrix = Matrix([ [1, 0], [0, 1] ])
		self.assertEqual(test_matrix.head.column, -1)
		
	def test_matrix_head_links(self):
		test_matrix = Matrix([ [1, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0], [1, 0, 0,1] ])
		col = test_matrix.columns
		right = col[0][0]
		print(right.left.left.column)
		
		

def main():
	unittest.main()	
		
if __name__ == '__main__':
	unittest.main()

		