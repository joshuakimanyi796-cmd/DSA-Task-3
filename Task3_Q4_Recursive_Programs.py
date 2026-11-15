# (a) Sum of first N natural numbers ------------------------------------------
#     sum(N) = N + sum(N-1)        sum(0) = 0
def sum_natural(n):
    if n == 0:                       # base case
        return 0
    return n + sum_natural(n - 1)    # recursive case


# (b) Factorial -----------------------------------------------------------------
#     N! = N * (N-1)!              0! = 1! = 1
def factorial(n):
    if n == 0 or n == 1:             # base case
        return 1
    return n * factorial(n - 1)      # recursive case


# (c) Nth Fibonacci term (series: 0, 1, 1, 2, 3, 5, 8, ...) ---------------------
#     F(1) = 0, F(2) = 1           F(N) = F(N-1) + F(N-2)
def fibonacci_term(n):
    if n == 1:                       # base cases
        return 0
    if n == 2:
        return 1
    return fibonacci_term(n - 1) + fibonacci_term(n - 2)   # recursive case


# (d) Generate N terms of the Fibonacci series ----------------------------------
#     Carry the current pair (a, b) along; each call produces one term and
#     recurses on (b, a + b) with one term fewer to go.
def fibonacci_series(n, a=0, b=1):
    if n == 0:                       # base case: nothing left to generate
        return []
    return [a] + fibonacci_series(n - 1, b, a + b)         # recursive case


def read_int(prompt, minimum, maximum, reason=""):
    """Keep asking until the user enters a whole number in [minimum, maximum]."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if minimum <= value <= maximum:
            return value
        extra = f" ({reason})" if reason else ""
        print(f"  Enter a number between {minimum} and {maximum}{extra}.")


def main():
    print("=" * 60)
    print(" Recursive programs")
    print("=" * 60)

    # (a)
    n = read_int("\n(a) Enter N for the sum of the first N natural numbers: ", 0, 900,
                 "Python's recursion depth limit")
    if n == 0:
        print("    Sum of the first 0 natural numbers = 0")
    else:
        terms = " + ".join(str(i) for i in range(1, n + 1)) if n <= 10 else "1 + 2 + ... + " + str(n)
        print(f"    Sum of the first {n} natural numbers = {terms} = {sum_natural(n)}")

    # (b)
    n = read_int("\n(b) Enter a number to find its factorial: ", 0, 900,
                 "Python's recursion depth limit")
    print(f"    {n}! = {factorial(n)}")

    # (c)
    n = read_int("\n(c) Enter N to find the Nth Fibonacci term: ", 1, 30,
                 "plain recursion becomes very slow for larger values")
    print(f"    Fibonacci term number {n} = {fibonacci_term(n)}")

    # (d)
    n = read_int("\n(d) Enter N to generate N Fibonacci terms: ", 1, 500,
                 "Python's recursion depth limit")
    print(f"    First {n} Fibonacci terms: {', '.join(map(str, fibonacci_series(n)))}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ended.")
