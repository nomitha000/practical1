temp=int(input("""Enter your choice in which degree u want to enter the temperature 1.Farhenheit
2.Celsius : """))
fh=open('output1.txt','w')

if temp == 1 :
    ce=int(input("Enter the temp in Fahrenheit:"))
    C=(ce-32)*5/9
    print(C, "Degrees in celsius")
    fh.write(f'{ce} degree fahrenheit in degree {str(C)} ') 
elif temp == 2 :
    fa=int(input("Enter the temp in Celsius : "))
    F=(9/5)*fa+32
    print(F," DEGREES IN FARENHEIT")
    fh.write(f'{fa} degree celsius in farenheit{str(F)}')
else :
    print( )

fh.close()