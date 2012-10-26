from listNode import *

class hashTable:
	
	#constructor: creates an array the size of a large prime number
	def __init__(self):
		primesText = open("primes.txt")
		self.primes = primesText.read().split()
		self.data = [None] * int(self.primes[100])#you can change the number on this to vary your array size
	
	# inserts value into hashtable as a listNode object	
	def insert(self, key):
		num = hash(key) % len(self.data)
		if self.data[num] == None:
			link = listNode()
			link.data = key
			self.data[num] = link
		else:
			current = self.data[num]
			while current.next != None:
				current = current.next
			current.next = listNode()
			current.data = key
	
	# returns the linkedList of the data stored at your specific hash
	# void your key is absent
	def get(self, key):
		num = hash(key) % len(self.data)
		#no items in list
		if self.data[num] == None:
			print "Sorry, he's not there :("
		#one item in list
		elif self.data[num].next == None: 
			return self.data[num]
		#multiple items
		else:
			print "you have a collision. Here is your linked List"
			return self.data[num]
	
	#method to see if two arrays have a union
	#true for yes, false for no
	def hasUnion(self, a1, a2):
		self.inputArray(a1)
		self.inputArray(a2)
		a = a1 + a2
		for i in a:
			node = self.get(i)
			if node.next != None:
				return True
		return False

	#helper method to put items from an array into the hash table
	def inputArray(self, a):
		for i in a:
			self.insert(i)
		
		
		

	
	
