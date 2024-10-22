print("Hello World!!!!")
age = 19
age = 18 + 2
price = 23.44
first_name = "Maritza"
me_before = False
print(age)
#myfirstexercise
patient = "John Smith"
age = 20
state = "New"
print(patient," ",age," ",state)
#funcion input se usa para leer un valor desde la ventana del terminal
#input function is used to read a value from the terminal window
name = input("What is your name? ")
print("Hola " + name)
#tipos de datos
#date types
birth_year = input("Enter your birth year: ")
#FUNCTIONS
#---int()---float()---bool()--str()---
#La funcion int convierte en entero mi cadena de texto ingresaada
#The  int function converts my entered text string to an integer
age = 2024 - int(birth_year)
print(age)
#Second Exercise
num1 = float(input("Enter the number of years your michirelationship :3 "))
num2 = float(input("Enter the exact number of years your michirelationship :3 "))
print("The number years is : " + str(num1 + num2))
#num1 = 1
#num2 = 1.162536
#print(float(num1) + num2)
#int_num = num1 + int(num2)
#print(int_num)
##################STRINGS#################
course = 'Phyton for beginners'
#find() The method shows if my string contains a character or a sequence of characteres/ shows the index of the string
print(course.upper()) 
print(course.find('r')) 
#replace(arg,arg) The method replaces a string with another string
#Strings in python are inmutable
print(course.replace('for','For'))
#operator in returns a boolean value  if the string is found int the string
print('Phyton' in course)
########### ARITHMETHIC OPERATORS ##########
#if one slash is used, a float is returned, but if two slashes are used, ant int is returned
print(10/4)
print(10//4)
# Operartor ** represents an exponent
print(10**2)
#Operator de ASIGNACION AUMENTADA
age_cat = 4
age_cat += 5
print(age_cat)
age_cat *= 2
print(age_cat)
age_cat **= 2
print(age_cat)
age_cat %= 5
print(age_cat)
age_cat /=3
print(age_cat)
age_cat //=3
print(age_cat)
