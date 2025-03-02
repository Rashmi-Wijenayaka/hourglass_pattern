def hourglass_pattern(n):
   for i in range(n, 0, -1):
       print(" " * (n - i) + "* " * i)

   for i in range(2, n+1):
       print(" " * (n - i) + "* " * i)

number = int(input("Please provide an integer bigger than 1: "))
hourglass_pattern(number)
