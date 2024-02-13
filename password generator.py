import random       # python in-built function (random)

capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"     # capital variable's string elements include in password

small = "abcdefghijklmnopqrstuvwxyz"      # small variable's string elements include in password

numbers = "0123456789"        # numbers variable's string elements include in password

symbols = "@#$%&*?"       # symbols variable's string elements include in password

string = ( capital + small + numbers + symbols )   # this string variable has elements of capital , samll , numbers , symbols 

word = random.sample( string,10 )    #  one of the random keywords is 'sample' it's giving number of password in string variable

password = " ".join(word)       #  join function adds the space between each number of passwords

print( "Your 10 Digit Password is : ",password )    #  in print statement print the 10 digit password