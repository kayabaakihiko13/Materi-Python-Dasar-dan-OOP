def fibonacci(n):
    if n<0:
        raise Exception('Angka masukan harus bernilai positif')
    if n<2:
        return 1
    
    return n*fibonacci(n-1)
def division(number1,number2):
    try:
        return number1/number2
    except Exception as err:
        print(err)
def square(n):
    if n<0:
        return ValueError('Angka harus positive')
    return n**.5
        

print(fibonacci(5)) 
print(square(10)) 
print(square(-5))

