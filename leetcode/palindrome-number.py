import random

def gen_num():
    num = random.randint(1, 10000)
    return num

tries = 0
while True:
    num = gen_num()
    array = [None] * len(str(num))
    arrayinv = [None] * len(str(num))
    print(num)
 
    for i, digito in enumerate((str(num))):
        array[i] = int(digito)
        arrayinv[(len(str(num))-1-i)] = int(digito)
        
    tries += 1
    
    if array == arrayinv:
        print(f"{num} is a palindrome!")
        print(f"It takes {tries} tries to get it!")
        break