# Module for audio-specific ontology representation.
# Inherits from, and therefore dependent on, media.py

import media

# --------------------------------------------------------------------
#                       List sub-classes
# --------------------------------------------------------------------

class Set(media.Set):
	"""
	Represent a set of audio items.

	An audio item can be anything representable by the Audio class.

	"""
	def __init__(self):
		pass

class Release(Set):
	"""
	Represent a real-world audio/music release.

	A Release is an LP, EP, single, etc. In terms of implementation
	this is a special type of audio set.

	"""
	def __init__(self):
		pass

class Medium(Set):
	"""
	Represent a Release component.

	In the case of a single disc Release (for example), Medium is
	synonymous with Release. Where a Release contains multiple discs,
	this is where Medium becomes important.

	"""
	def __init__(self):
		pass

# --------------------------------------------------------------------
#                            Objects
# --------------------------------------------------------------------

class Audio(object):
	"""
	Represent an audio item.

	An audio item is any kind of unit "recording" instance (basically,
	an audio track/song).

	"""
	def __init__(self):
		pass

class Artist(object):
	"""
	Represent an artist (or recognised group of artists).

	"""
	def __init__(self):
		pass

class Label(object):
	"""
	Represent a label (as in imprint and/or the controlling company).

	"""
	def __init__(self):
		pass

