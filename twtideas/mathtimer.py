import random
import time

# constantes

OPERATORS = ["+", "-", "*"]
MIN_VALUE = 1
MAX_VALUE = 10
TOTAL_OP = 10

def gen_expr():
    left = random.randint(MIN_VALUE, MAX_VALUE)
    right = random.randint(MIN_VALUE, MAX_VALUE)
    center = random.choice(OPERATORS)

    expr = str(left) + " " + center + " " + str(right)
    ans = eval(expr)
    return expr, ans

mistake = 0
input("Press enter when ready!!")
start_time = time.time()
print("--------------------------")

for i in range(TOTAL_OP):
    expr, ans = gen_expr()

    while True:
        userAns = input(f"{expr} = ")
        if str(ans) == userAns:
            break
    
        mistake += 1

end_time = time.time()
print("--------------------------")

total_time = end_time - start_time
if mistake != 0:
    print(f"Congratss! You finished in {total_time} seconds and you did {mistake} mistakes!")
else:
    print(f"Congratss! You finished in {total_time} seconds and got nothing wrong!!!")