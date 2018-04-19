#Make the factorial function
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

#Print the answer
print("5! is equal to", factorial(5))

#5! is 5 x 4 x 3 x 2 x 1
#More infomation on how to do this at https://en.wikipedia.org/wiki/Factorial
