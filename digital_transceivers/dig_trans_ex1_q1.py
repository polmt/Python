import numpy as np

N = int(input("N = "))
def sym_rand(N):
    if N % 2 != 0:
        raise ValueError("N should be an even number for equal probability of -1 and 1.")

    # normal distribution (mean=0, std_dev=1)
    values_random = np.random.randn(N // 2)

    # map positive values to 1 and negative to -1
    sym = np.where(values_random > 0, 1, -1)

    # final array
    array = np.tile(sym, 2)

    return array

array = sym_rand(N)
print(array)

x = 0
y = 0

for sym in array:
    if sym == 1:
        x = x + 1
    elif sym == -1:
        y = y + 1
print('"1" appears', x, 'times or', '%.2f' % (x/N*100), '% of the time.')
print('"-1" appears', y, 'times or' , '%.2f' % (y/N*100), '% of the time.')