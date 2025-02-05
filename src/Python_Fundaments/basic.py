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
# INCREASED ALLOCATION OPERATOR
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
#operator procedence pmmdss :D ###################### 
########COMPARISON OPERATORS #########################
x = 3 > 2
print(x)
#LOGICAL OPERATORS and, or, not
age_cat = 4
print(age_cat > 0 and age_cat <=4)
age_cat = 4
print(age_cat > 10 or age_cat <=4)
age_cat = 4
#operator not "invert the False for the True"
print( not age_cat < 0 )

# IF STAMENTS ########3333333333333333333333333333333333
temperature = 22
if temperature > 21:
    print("It's hot")
    print("miau")
elif temperature >= 22: #(22,30]
    print("It's cool")
elif temperature > 10:
    print("It's cold")
elif temperature < 10:
    print("It'extremaly cold")
print("done")
####FIRST EXERCISEEEEEEEEEEEEEEEEEEE
#CALCULATOR WEIGHT
weight = float(input("Enter you weight: "))
answer = input("Your weight is in k(kg) or l(lbs)? ")
if answer.lower() == "k":
    print("Your weight is in Kilograms: " + str(weight))
elif answer.lower() == "l":
    print("Your weight is in Pounds: "  + str(weight*2.20462))


#While Loops ################################
i = 1_000#more readable code
while i >= 1:
    print( i * '*')
    i = i - 100
lilist=[1,2,3]
print(lilist[1,3])
        
#Lists 
names = ["liliana", "claudia", "madia"]
print(names)
print(names[0])
print[-3]
names[0] = "lilicat"
print(names[0:3])
