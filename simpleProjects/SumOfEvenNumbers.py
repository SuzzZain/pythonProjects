target = int(input()) # Enter a number between 0 and 1000

total = 0
for number in range(2, target + 1, 2):
  total += number
print(total)

#total = 0
#for number in range(1, total + 1):
#   if number % 2 == 0:
#      total += number
#   print(total)