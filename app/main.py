from fastapi import FastAPI
import math
from typing import Union

app = FastAPI()

@app.get("/isFibonacci/{fib_num}")
def read_item(fib_num: int, q: Union[str, None] = None):
    return fib_num if isFibonacci(fib_num) else "not a Fibonacci number."

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)