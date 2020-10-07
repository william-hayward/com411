sequence = input("Please enter a sequence using these characters: '-'s and two 'x's ")
marker = "x"

marker1_pos = -1
marker2_pos = -1

for i in range(0, len(sequence), 1):
  letter = sequence[i]

  if letter == marker:
    if marker1_pos == -1:
      marker1_pos = i
    else:
      marker2_pos = i

print("The distance between the markers is", marker2_pos - marker1_pos -1)