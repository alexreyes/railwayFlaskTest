class Book: 
	def __init__(self, title, link, author=None, desc=None, rating=None): 
		self.title = title
		self.author = author
		self.desc = desc
		self.link = link 
		self.rating = rating