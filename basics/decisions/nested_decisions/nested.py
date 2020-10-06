cover = input("What type of cover does the book have? (soft/hard) ")

if cover == "soft":
  perfect_bound = input("Is the book perfect bound? (y/n) ")
  if perfect_bound == "y":
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books!")
elif cover == "hard":
  print("Books with hard covers can be more expensive!")
else:
  print("Please enter a valid answer!")
