def is_prime(n):
    """Pove ali je stevilo prastevilo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Vrne fakulteto stevila"""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def fibonacci(n):
    """Vrne n-to fibonaccijevo stevilo."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def gcd(a, b):
    """Vrne najveji skupni delitelj."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Vrne najvecji skupni veckratnik."""
    return a * b // gcd(a, b)

import random

_question_pool = [
    ("prime", lambda: random.randint(2, 50)),
    ("factorial", lambda: random.randint(2, 6)),
    ("fibonacci", lambda: random.randint(1, 10)),
    ("gcd", lambda: (random.randint(2, 20), random.randint(2, 20))),
    ("lcm", lambda: (random.randint(2, 15), random.randint(2, 15)))
]

def next_question():
    """
    Returns a tuple: (q_type, value, question_text)
    """
    q_type, generator = random.choice(_question_pool)
    value = generator()

    if q_type == "prime":
        question_text = f"Ali je število {value} praštevilo? (da/ne)"
    elif q_type == "factorial":
        question_text = f"Kaj je {value}! (faktorial {value})?"
    elif q_type == "fibonacci":
        question_text = f"Katero je {value}-to število Fibonaccijeve vrste?"
    elif q_type == "gcd":
        a, b = value
        question_text = f"Kateri je največji skupni delitelj števili {a} in {b}?"
    elif q_type == "lcm":
        a, b = value
        question_text = f"Kateri je najmanjši skupni večkratnik števili {a} in {b}?"

    return q_type, value, question_text

