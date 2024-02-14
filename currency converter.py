from currency_converter import CurrencyConverter          # it's one of the python in-built module

c=CurrencyConverter ()

while True:

 amount = input("enter the amount : ")                

 from_amount = input("From Currency : ").upper()

 to_amount = input("To currency : ").upper()

 final = c.convert(amount,from_amount,to_amount)          # codition for convert amount, from amount to to amount


 if from_amount == to_amount:
    print("It's same , Please enter correct currency name.")      # from_amount to_amount same it's will work

 else:
    print(final)                                                  # all details currect currency value will print & break
    break