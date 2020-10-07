numbers_to_sum = int(input("How many numbers should i sum up? "))
i = 0
answer = 0

while i < numbers_to_sum:
  print("Please enter number",(i+1),"of", numbers_to_sum)
  numbers = int(input())
  answer = answer + numbers
  i = i + 1

print("The answer is:", answer)