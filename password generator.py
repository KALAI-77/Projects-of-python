import random                                      # python in-built function (random)

capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"           

small = "abcdefghijklmnopqrstuvwxyz"            

numbers = "0123456789"                           

symbols = "@#$%&*?"                              

string = ( capital + small + numbers + symbols )   # this string variable has elements of capital , samll , numbers , symbols 

password = " ".join( random.sample( string,10 ))    #  join function work with sample function & adds the space between each number of passwords

print( "Your 10 Digit Password is : ",password )    #  in print statement print the 10 digit password
