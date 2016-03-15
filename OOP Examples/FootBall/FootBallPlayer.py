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
		print "My name is %s and I'm %d years old." % (self.name, self.age)
		print "I'm %s and play for %s as number %d" % (self.nationality, self.club, self.number)

	@abstractmethod
	def playerAction(self):
		pass


