def fib(n):
    neg = False
    if n < 0:
      n = n * -1
      neg = True
    f_n, f_n_plus_1 = 0, 1
    for i in range(n.bit_length() - 1, -1, -1):
        f_n_squared = f_n * f_n
        f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
        f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
        f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
        if n >> i & 1:
            f_n, f_n_plus_1 = f_2n_plus_1, f_2n + f_2n_plus_1
        else:
            f_n, f_n_plus_1 = f_2n, f_2n_plus_1
    if neg and n % 2 == 0:
      return -1 * f_n
    else:
      return f_n
