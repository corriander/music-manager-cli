# Module for media interfaces and low-level management.

class Set(list):
	"""
	Represent a set of media objects.

	Interfacing with the music-manager database is performed on sets
	of media rather than individual items. Media item metadata is
	encapsulated in a media object (see MediaObject class) and this
	class represents such a set.

	"""
	def __init__(self):
		pass

class Collection(Set):
	"""
	Represent a collection of media.

	A collection may belong to a person, or may exist on a particular
	device. Essentially it's an arbitrary grouping of Media items or
	sets of Media items.

	"""
	def __init__(self):
		pass

class Media(object):
	"""
	Represent the metadata of a media item.

	Media items might be audio, image and video files or they may be
	physical instances of media (CDs, DVDs, etc.)

	"""

	def __init__(self):
		pass

class Digital(Media):
	"""
	Represent a Media item contained within a file.

	"""
	def __init__(self):
		pass

class Physical(Media):
	"""
	Represent a Media item contained within a physical medium.

	This might be a CD, or DVD.

	"""
	def __init__(self):
		pass
