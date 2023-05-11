"""
x^3 + 5x = 20
x{sub}n+1 = (20-5x{sub}n)^1/3
"""
x_0 = round((20-5*2)**(1/3), 3)
x_n = x_0
counter = 0
while True:
    counter += 1
    x_n_plus_1 = round((20 - 5 * x_n) ** (1 / 3), 3)
    if x_n == x_n_plus_1:
        break
    else:
        x_n = x_n_plus_1

print(f'{x_n_plus_1} which is the {counter}th term')