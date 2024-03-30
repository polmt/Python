import numpy as np
def s(N):
    R = np.random.randn(N)
    R [R > 0] = 1
    R [R <= 0] = -1
    return R
n = input("What is the length of the array? ")
N = int(n)
R = s(N)
list = ['R']
x = 0
y = 0
for element in R:
    if element == 1:
        x = x + 1
    elif element == -1:
        y = y + 1
print('"1" appears', x, 'times or', '%.2f' % (x/N*100), '% of the time.')
print('"-1" appears', y, 'times or' , '%.2f' % (y/N*100), '% of the time.')
