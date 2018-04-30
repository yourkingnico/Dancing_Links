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
		rows = [[ ] for _ in range(numberOfRows)]
		heads = [Head(j) for j in range(numberOfColumns)]
		columns = [[head] for head in heads]

		# Master Head 
		self.head = Head(-1)
		heads = [self.head] + heads
		self.linkLeftRight([heads])
		i = 0
		while i < numberOfRows:
			j = 0
			while j < numberOfColumns:
				if matrix[i][j] == 1:
					node = Node(i, j)
					columns[j].append(node)
					rows[i].append(node)
				j += 1
			i += 1

		self.linkLeftRight(rows)
		self.linkUpDown(columns)
		self.rows = rows
		self.columns = columns
		
		
	def linkLeftRight(self, rows):
		""" link the rows on the left and right

		:param rows: the rows being linked
		:type rows: list
		"""
		for row in rows:
			n = len(row)
			j = 0
			while j < n:
				row[j].right = row[(j + 1) % n]
				row[j].left = row[(j - 1 + n) % n]
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
		
	def test_head_without_nodes(self):
		"""Test that a matrix with no 1's does not make Node instances attached to the heads"""
		test_matrix = Matrix([ [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0] ])
		col = test_matrix.columns
		first_head = col[0][0].left
		next_head = first_head.right
		while(next_head.column is not -1):
			self.assertEqual(next_head, next_head.down)
			next_head = next_head.right
		
	def test_matrix_head_links_left(self):
		"""Test the left directional links between heads"""
		test_matrix = Matrix([ [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 0], [1, 0, 0,1] ])
		col = test_matrix.columns
		test_head = col[0][0].left
		next_head = test_head.left
		num = 0
		while(next_head.column is not -1):
			num = num +1
			next_head = next_head.left
		self.assertEqual(num, 4)
		
	def test_matrix_head_links_right(self):
		"""Test the right directional links between heads"""
		test_matrix = Matrix([ [1, 0, 1, 1], [0, 0, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0] ])
		col = test_matrix.columns
		test_head = col[0][0].left
		next_head = test_head.right
		num = 0
		while(next_head.column is not -1):
			num = num +1
			next_head = next_head.right
		self.assertEqual(num, 4)
	
	def test_node_links(self):
		"""Test that the nodes are linked"""
		test_matrix = Matrix([ [1, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0], [1, 0, 0,1] ])
		col = test_matrix.columns
		right = col[0][0]
		right = right.right
		right = right.down
		self.assertEqual(type(right), Node)
	
	def test_node_down_link(self):
		""" Test down circular links for the nodes"""
		test_matrix = Matrix([ [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0,1] ])
		col = test_matrix.columns
		right = col[0][0]
		right = right.down
		self.assertEqual(right, col[0][0])
		right = right.down
		self.assertEqual(right, col[0][0])
	
	def test_node_up_link(self):
		"""Test up links for the nodes"""
		test_matrix = Matrix([ [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0,1] ])
		col = test_matrix.columns
		right = col[0][0]
		right = right.up
		self.assertEqual(right, col[0][0])
		right = right.up
		self.assertEqual(right, col[0][0])
		
	def test_linkLeftRight(self):
		"""Test linkLeftRight function"""
		test_matrix = Matrix([ [1, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0], [1, 0, 0,1] ])
		row = test_matrix.rows
		test_rows = row[1][1]
		test_rows = test_rows.right
		test_rows = test_rows.right
		self.assertFalse(test_rows == row[1][1])
		test_rows = test_rows.left
		test_rows = test_rows.left
		self.assertEqual(test_rows, row[1][1])
		

def main():
	unittest.main()	
		
if __name__ == '__main__':
	unittest.main()

		