x = int(input("Digite o priemiro número "))
y = int(input("Digite o segundo número "))
z = int(input("Digite o terceiro número "))

if x > y and x > z:
    result = "x é  maior número"
elif y > x and y > z:
    result = "y é o maior número"
elif z > x and z > y:
 result = "z é o maior número"
else:
    result = "há número iguais"
    
print (result)

    