# recursion.py

def fibonacci(n):
    """Returns the nth element of the Fibonacci sequence."""
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    """Returns the greatest common divisor of a and b using Euclid's algorithm."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    """Compares two strings recursively.
    Returns:
    - A negative number if s1 < s2,
    - 0 if s1 == s2,
    - A positive number if s1 > s2.
    """
    if not s1 and not s2:
        return 0
    elif not s1:
        return -ord(s2[0])
    elif not s2:
        return ord(s1[0])
    elif s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    else:
        return compareTo(s1[1:], s2[1:])

# Example usage
if __name__ == "__main__":
    print("Fibonacci sequence:")
    for i in range(1, 10):
        print(fibonacci(i), end=" ")
    print("\n")

    print("Greatest Common Divisor:")
    print("GCD of 48 and 18 is", gcd(48, 18))
    print("\n")

    print("String Comparison:")
    print("Comparing 'apple' and 'apricot':", compareTo("apple", "apricot"))
    print("Comparing 'banana' and 'banana':", compareTo("banana", "banana"))
    print("Comparing 'cherry' and 'berry':", compareTo("cherry", "berry"))
