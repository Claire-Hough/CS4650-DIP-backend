#Here are your imports. Declare at the top
import math
import sys


#This is how you define a function/method. You don't have to define
#variables or define the passing, python will assume type based on ititialization.
def function(parameter):
	print(parameter)



#Everything down here is "main". You can define it however
#Just putting stuff on the far left indent is fine for it. Python
#uses indentation to differentiate 
parameter = input(sys.argv[1])
function(parameter)

#To run this, download python 3 and go to your file location in a terminal
#Type python3 hello.py and it should run