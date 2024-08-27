#using list comprehension to get all the prime numbers in a less time (simplest way)
n=100
primes = [num for num in range(2, n + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

print(primes)

n=int(input('enter your desired number: '))
primes=[num for num in range(2,n+1) if all(num%i!=0 for i in range(2,int(num**0.5)+1))]
print(primes)

#vy using functions to get prime numbers 
def is_prime(n):
  """
  This function checks if a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if n is prime, False otherwise.
  """
  # Handle 0 and 1 cases
  if n <= 1:
    return False
  # Check from 2 to n-1 for divisibility
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def find_primes(n):
  """
  This function finds all prime numbers less than n.

  Args:
    n: The upper limit for prime numbers.

  Returns:
    A list of all prime numbers less than n.
  """
  primes = []
  for num in range(2, n):
    if is_prime(num):
      primes.append(num)
  return primes

# Get the limit for prime number search
n = 100

# Find all prime numbers less than n
primes = find_primes(n)

# Print the list of prime numbers
print(primes)
        