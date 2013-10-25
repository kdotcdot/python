# my_int is set to 7 below. What do you think
my_int = 7

print my_int

#span function
def spam():
    eggs = 10**2 #Exponentiate
    return eggs
print spam()

""" This is some commented shit I'm writing
This is some more shit """

# Calculate a tip

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal*tip

print("%.2f" % total)

# Use of escape backslash
'Help! Help! I\'m being repressed!'

#Use of the string character reference
fifth_letter = "MONTY"[4]
print fifth_letter


#Dot notation works on string literals ("The Ministry of Silly Walks".upper()) and 
#variables assigned to strings (ministry.upper()) because these methods are specific to 
#strings—that is, they don't work on anything else. By contrast, len() and str() can work 
#on a whole bunch of different objects (which we'll get to later), so they aren't tied to 
#strings with dot notation.

ministry = "Poop"
print len(ministry)
print ministry.upper()