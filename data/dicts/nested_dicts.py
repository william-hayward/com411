def run():
  def short_pattern():
    pattern_short = {"sequence":"101", "occurrences":5}
    return pattern_short
  
  def medium_pattern():
    pattern_medium = {"sequence":"111000", "occurrences":25}
    return pattern_medium
  
  def long_pattern():
    pattern_long = {"sequence":"1100110011001100", "occurrences":50}
    return pattern_long

  print("Analysing Patterns...\n")
  full_pattern = {
    "Short Pattern:":short_pattern(),
    "Medium Pattern:":medium_pattern(),
    "Long Pattern:":long_pattern()
  }

  print(full_pattern)
  