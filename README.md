# -Piscine-Python-for-datascience

*--- CORE CONCEPTS *--------------------*					|

1st: Data Structure Manipulation (ex00) |
					|
2nd: Date/Time Formatting (ex01)        |
					|
3th: Type Checking (ex02/ex03)		|	
					|
4th: Argument Parsing (ex04/ex05)	|
					|	
5th: text Analysis (ex05)		|
					|
6th: Error Handling (all exercises)	|
					|
----------------------------------------*	

/**********************/			
/* LEARNING RESOURCES */
/*********************/

/*----Python Fundamentals----*/

I first of all went to look for basics of python and one of the good documentation srcs I found:

---->  https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html:w
---->  DeepSeek AI for concept clarification

/*----Time Formatting Tutorials----*/

About time formatting I watched some Youtube videos about time function 

----link1: https://www.youtube.com/watch?v=eirjjyP2qcQ&t=804s
----link2: https://www.youtube.com/watch?v=s2nM8__2-8s



///////WHAT I LEARNED///////////
--------->Through these exercises, I've gained some Python skills:
***
*1* Working with Data Structures:
***
 - modifyin lists:
Lists (ft_list = ["Hello", "tata!"])
What it is:
	Ordered, mutable (can be changed), and allows duplicates.
	Created with square brackets [].
	Supports operations like append(), remove(), and slicing.


- Modifing sets:
Sets (ft_set = {"Hello", "tutu!"})
What it is:
	Unordered, mutable, and no duplicates.
	Created with curly braces {}.
	Cannot access elements by index (no order).


- Modifying dictionaries:
What it is:
	Unordered, mutable, and stores key-value pairs.
	Created with curly braces and colons {"key": "value"}.
	Keys must be unique (e.g., "Hello" maps to one value).
	Values accessed via keys (e.g., ft_dict["Hello"] → "titi!").
	
- Modifing tuples:
What it is:
	Ordered, immutable (cannot be changed after creation), and allows duplicates.
	Created with parentheses ().
	Faster than lists for fixed data (due to immutability).


----------> I've Learned when to use each type and their key differences.
***
*2*
*** Handling Dates and Times - Figured out how to convert timestamps and format dates properly using strftime patterns.

Format Specifier :,.4f
This is composed of 3 parts:

Component: Meaning	       	       Input → Output
,	Thousand separator	  1696222200 → 1,696,222,200
.4	4 decimal places precision 123.45678 → 123.4568
f	Fixed-point notation	      123456 → 123456.0000

--------string formatting--------------------------*
*/*formatted string				   |
						   |
f"{variable:format_specifier}"			   |
						   |
f indicates an f-string (formatted string literal) |
						   |
{} contains the value to be formatted		  |
						  |
: separates the variable from the format specifie |	|
						  |
--------------------------------------------------*

!!!looking for tutorials {check links above :)}
***									
*3*
*** Type Checking - Discovered different ways to check variable types and handle special cases like NULL values {The type() and isinstance()}

- type()
What it does:
	Returns the exact class/type of an object.
	Strictly checks if an object is of a specific type (no inheritance considered).
	type(object)  --> Returns the type object (ex: <class 'list'>)
- instance()
What it does:
	Checks if an object is an instance of a class or a subclass of it.
	isinstance(object, Class)  --> Returns True/False

*/*/*/*/*/*/the NULL types:

Nothing = None → NoneType

Garlic = float("NaN") → float

Zero = 0 → int

Empty = '' → str

Fake = False → bool


***
*4*
***Command Line Input - Learned to make scripts that accept arguments and validate them properly + AssertionError.

- Command Line Input in Python (with sys) :

import sys
	sys.argv is a list of command-line arguments.
	sys.argv[0] is the script name.
	sys.argv[1:] are the actual arguments passed.
	sys.exit(1) -->for failure exiting
	len() function ---> it was useful
	Syntax: len(object) --> Parameters: object: The object whose length you want to find.This can be a string, list, tuple, dictionary, etc.
	Return Value ---> Returns the number of items in the object.
- AssertionError :

An AssertionError in Python is an error that occurs when an assertion fails. Assertions are used to test if a condition is true, and if it’s not, Python raises an AssertionError to signal that something has gone wrong in the program.

***
*5*
***Text Analysis - Built a text analyzer that counts characters, words, and punctuation. String methods like isupper() and isdigit() turned out to be super useful.
    
- Used function --> isupper:  Checks if the character is an uppercase letter.
	            islower:  Checks if the character is an lowercase letter.
		    isdigit:  Checks if the character is a digit (0-9).
		    isspace:  Checks if the character is a whitespace character
		    string.punctuation:  Checks if the character is in the string of punctuation characters defined by string.punctuation.

--------------->Return values: all returns True/False
