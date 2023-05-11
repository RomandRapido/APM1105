import time


def ite_fibo(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibo = [0, 1]
    for i in range(n - 2):
        fibo.append(fibo[-2] + fibo[-1])
    return fibo[-1]


def rec_fibo(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # calls rec_fibo until there's a definite value
        return rec_fibo(n - 2) + rec_fibo(n - 1)


def run_time_fibs(function, n):
    start_time = time.perf_counter()
    result = function(n)
    end_time = time.perf_counter()
    final_time = end_time - start_time
    if function == ite_fibo:
        return f'Iterative approach result: {result}\nTime taken (iterative approach): {final_time}'
    elif function == rec_fibo:
        return f'Recursive approach result: {result}\nTime taken (recursive approach): {final_time}'



def main():
# n == nth term that starts with 0
    n = 20
    iterative = run_time_fibs(ite_fibo, n)
    recursive = run_time_fibs(rec_fibo, n)
    print(f'n = {n}\n{iterative}\n{recursive}')


if __name__ == '__main__':
    main()
