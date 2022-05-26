#Ruppees To Dollarconverter
dollar=int(input("Dollar price as today: "))
ruppes = int(input('Price(in Ruppees): '))

rtod=ruppes/dollar

def ruptodol():
	rtod=ruppes / dollar
	print(f"Pkr {ruppes} in dollar = {rtod}")
ruptodol()
	
again=input('Again: ')
while again=='y' or again=='Y':
	ruppes=int(input('price (in ruppees): '))
	ruptodol()
	again=input('Again: ')
while again=='n' or 'N':
	print("done")
	break
	

	
	
	
	
