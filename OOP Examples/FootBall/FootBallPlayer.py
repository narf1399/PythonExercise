from abc import ABCMeta, abstractmethod

class FootballPlayer:

	__metaclass__ = ABCMeta

	def __init__(self, name, nationality, age, number, club):
		self.name = name
		self.nationality = nationality
		self.age = age
		self.number = number
		self.club = club

	def playerInformation(self):
		print "My name is", self.name, "and I'm", self.age, "years old."
		print "I'm", self.nationality, "and play for", self.club, "as number", self.number

	@abstractmethod
	def playerAction(self):
		pass


