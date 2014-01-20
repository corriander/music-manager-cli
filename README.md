Music Manager (CLI)
===================

This is a command-line-interface implementation of an apathetic music
management system. It has been designed with extensibility in mind so
the underlying media representation framework can be applied to other
types of media such as images or video.

The representation of music metadata within this (Python)
implementation is based on (currently informal) ontological
principles.

Overview
--------

Currently this is just placeholder code containing a loose
approximation of the framework for internal representation of media
(and audio).

Rationale
---------

Digital music collections are often managed in software-specific
libraries. This is intended to introduce a more generic method of
collection management to bring this data outside of these silos and
provide added functionality:

  - Some of us still actively maintain physical collections of media
    which is only approximately represented by digital collections.
    Music player software, for obvious reasons, does not tend to
	facilitate management of these physical collections. Whilst
	various "collection manager" software solutions exist (TODO:
	examples), they are laborious and time-consuming to populate.
  - In the case of music, digital files are generally capable of
    storing most if not all important metadata. A heirarchical
	directory structure (i.e. Music folder) is a form of management
	but it's limited by the capabilities of the file system and
	therefore, outside of specialist filesystems (TODO: examples), is
	incapable of providing intelligent search/filtering functionality
	natively.
  - When changing software, the easiest option is to rebuild a
    database from file metadata. Such metadata tends to be full of
	errors and changes are often localised to a software database and
	lost on this rebuild action.
