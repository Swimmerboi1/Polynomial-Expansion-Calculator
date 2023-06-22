import os
from sympy import symbols, simplify, expand


print("Welcome to the polynomial expansion calculator! This calculator can expand any polynomial in the form of (a + b + c +....)^n. to add a coefficient to a variable separate the two by an * \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
num_terms = input("How many terms are in the polynomial you want to expand?\n")

while num_terms.isdigit() is False or len(num_terms) == 0: #finds the number of terms that are getting expanded
  print("the number of terms must be an integer")
  num_terms = input()
num_terms = int(num_terms)

polynomial = []
for i in range(num_terms): #takes all of the terms and puts them into a list
  number = str(i+1)
  term = input("Input term number "+number+":\n")
  while len(term) == 0:
    print("you must input a term")
    term = input()
  polynomial.append(term)

#creates a variable for the exponent and makes sure it is a number
exponent = input("What is the exponent that you want to raise the polynomial to?\n")
while exponent.isnumeric() is False or len(exponent) == 0:
  print("The exponent must be numeric")
  exponent = input()
exponent = int(exponent)

for i in range(len(polynomial)):
  #Extracts variable symbols from the polynomial
  variables = set([char for char in polynomial[i] if char.isalpha()])
  
  #Defines the variables dynamically
  symbols_dict = {}
  for variable in variables:
      symbols_dict[variable] = symbols(variable)
  
  #Parses the equation and replaces ^ with ** and recognizes sqrt
  polynomial[i] = polynomial[i].replace('^', '**')
  parsed_polynomial = eval(polynomial[i], symbols_dict)
  
  #Simplifies the equation
  simplified_polynomial = simplify(parsed_polynomial)
  polynomial[i] = simplified_polynomial

def list_to_equation(lst): 
    equation = sum(term for term in lst)
    simplified_equation = simplify(equation)
    return simplified_equation

os.system('clear')
final_polynomial = (list_to_equation(polynomial))**exponent
print("the expanded version of the polynomial:",final_polynomial,"is:")
print(expand(final_polynomial))

