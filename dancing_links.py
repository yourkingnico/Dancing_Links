#!/usr/bin/python3
import sys
import unittest

class Node:
	""" TODO: Eric implement""" 
class Head:
	""" TODO: Eric implement"""
class Matrix:
	"""TODO: Mason implement """ 
	
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
		"""
		TODO: instantiate node with init function, check values
		""" 
		
	def test_head(self):
		"""
		TODO: instantiate head with init function, check values
		v
		""" 
	def test_matrix(self):
		"""
		TODO: instantiate matrix with init function, check values
		v
		""" 	
		
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

		