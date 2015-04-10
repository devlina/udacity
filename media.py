class Movie:
	"""class to store movie information: title, poster image ad youtube trailer link
	"""

	def __init__(self, title, poster_url=None, trailer_url=None):
		self.title = title
		self.poster_image_url = poster_url
		self.trailer_youtube_url = trailer_url