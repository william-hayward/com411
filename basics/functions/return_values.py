def sum_weights(bop_weight, beep_weight):
  total_weight = bop_weight + beep_weight
  return total_weight

def calc_avg_weight(bop_weight, beep_weight):
  total_weight = bop_weight + beep_weight
  avg_weight = total_weight / 2
  return avg_weight

def run():
  bop_weight = float(input("What is the weight of Bop? \n"))
  beep_weight = float(input("\nWhat is the wight of Beep? \n"))
  calculation = input("\nWhat would you like to calculate? (sum/average) \n")

  if calculation.lower() == "sum":
    answer = sum_weights(bop_weight, beep_weight)
    print("\nThe sum of Beep and Bop's weight is: {:0.2f}".format(answer))
  elif calculation.lower() == "average":
    answer = calc_avg_weight(bop_weight, beep_weight)
    print("\nThe average weight of Beep and Bop is: {:0.2f}".format(answer))