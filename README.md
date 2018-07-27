# funky-collections

A set of collections implamented in pure python.  Nessesary?  No, probably not; most of the built in collections are writtten in C so they will be faster, but I was challenged to build a lower level c style collection the other day in python and my interest has been piqued! All collections are currently implamented using a doubly linked array approach with some optimizations of the special methods that most sequence types contain.

Currently Available:

* Immutable Lists
* Immutable Fixed Length Lists
* Mutable Lists sort of
* Mutable Fixed Lenth Lists sort of

Todo:
* Sets
* Tuples
* FIFO Stack
* FILO Stack
* Optimize collections by introducing new tree search methods
* Test all of the things!
* Benchmark all of the things!
