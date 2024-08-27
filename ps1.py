def generate_parenthesis(n):
  """Generates all possible combinations of balanced parentheses for n pairs.

  Args:
      n: The number of pairs of parentheses.

  Returns:
      A list containing all valid combinations of parentheses.
  """
  result = []

  def backtrack(s="", opening=0, closing=0):
    """Recursive helper function to generate balanced parentheses combinations.

    Args:
        s: The current string being built.
        opening: The number of opening parentheses used so far.
        closing: The number of closing parentheses used so far.
    """
    if opening == n and closing == n:
      result.append(s)
      return

    if opening < n:
      backtrack(s + "(", opening + 1, closing)

    if closing < opening:
      backtrack(s + ")", opening, closing + 1)

  backtrack()
  return result

# Get the number of pairs of parentheses from the user
num_pairs = int(input("Enter the number of parentheses pairs: "))

# Generate and print all combinations
all_combinations = generate_parenthesis(num_pairs)
print("All possible combinations of balanced parentheses:")
for combination in all_combinations:
  print(combination)
