#!/usr/bin/python3
import sys
import unittest

class Node:
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def deattach(self):
		self.up.down = self.down
		self.down.up = self.up

	def attach(self):
		self.down.up = self.up.down = self
		
class Head:
	def __init__(self, col):
		self.col = col

	def deattach(self):
		self.left.right = self.right
		self.right.left = self.left

	def attach(self):
		self.right.left = self.left.right = self
		
class Matrix:
	def linkLeftRight(self, srows):
		for srow in srows:
			n = len(srow)
			j = 1 
			while j < n:
				srow[j].right = srow[(j + 1) % n]
				srow[j].left = srow[(j - 1 + n) % n]
				j +=1

	def linkUpDown(self, scols):
		for scol in scols:
			n = len(scol)
			i = 1
			while i < n:
				scol[i].down = scol[(i + 1) % n]
				scol[i].up = scol[(i - 1 + n) % n]
				scol[i].head = scol[0]
				i += 1

	def __init__(self, matrix):
		numberOfRows = len(matrix)
		numberOfColumns = len(matrix[0])
		srow = [[ ] for _ in range(numberOfRows)]
		heads = [Head(j) for j in range(numberOfColumns)]
		scol = [[head] for head in heads]

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
					scol[j].append(node)
					srow[i].append(node)
				j += 1
			i += 1

		self.linkLeftRight(srow)
		self.linkUpDown(scol)
	
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

class AlgorithmXTest( unittest.TestCase):

	def test_node(self):
		my_node = Node(0,0)
		self.assertEqual(my_node.row, 0)
		self.assertEqual(my_node.col, 0)
		
	def test_node_attach(self):
		""""create up down links first? 
		#test_node = Node(0,0)
		#test_node.attach()
		#self.assertEqual(test_node.down.up, self)"""
		
	def test_head(self):
		test_head = Head(0)
		self.assertEqual(test_head.col, 0)
		
	def test_matrix_head(self):
		test_matrix = Matrix([ [1, 0], [0, 1] ])
		self.assertEqual(test_matrix.head.col, -1)
		
	def test_generic_x_4(self):
		"""
		TODO: pass in 4x4 matrix, and expect result to be empty matrix
		""" 
		self.assertEqual( generic_x(), [ [], [], [], [] ])
		
	def test_generic_x_6(self):
		"""
		TODO: pass in 6x6 matrix, and expect result to be empty matrix
		"""
		self.assertEqual( generic_x(),  [ [], [], [],  [], [], [] ])
		
	def test_generic_x_8(self):
		"""
		TODO: pass in 8x8 matrix, and expect result to be empty matrix
		"""
		self.assertEqual( generic_x(), [ [], [], [], [], [],  [], [], [] ])
		
	"""
		TODO: Create additional test for unsolvable constraints. 
	""" 
	
def main():
	unittest.main()	
		
if __name__ == '__main__':
	unittest.main()

		