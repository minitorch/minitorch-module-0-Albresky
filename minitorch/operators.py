"""Collection of the core mathematical operators used throughout the code base."""

import math
import builtins

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - addLists
# - neg
# - negList
# - lt
# - eq
# - max
# - is_close
# - prod
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x, y):
    return x*y

def id(x):
    return x

def add(x, y):
    return x+y

# def addLists(x, y):
#     return [a+b for a, b in zip(x, y)]

def neg(x):
    return -x

# def negList(x):
#     return [-a for a in x]

def lt(x, y):
    return x < y

def eq(x, y):
    return x == y

def max(x, y):
    return x if x > y else y

def prod(x):
    return math.prod(x)

def is_close(x, y):
    return abs(x-y) < 1e-2

def sigmoid(x):
    # 稳定性实现
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))

def relu(x):
    return max(0, x)

def log(x):
    return math.log(x)

def exp(x):
    return math.exp(x)

def log_back(x):
    return 1/x

def inv(x):
    return 1/x

def inv_back(x):
    return -1/(x**2)

def relu_back(x, y):
    return y if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(fn: Callable[[float], float], arr: Iterable[float]) -> Iterable[float]:
    return [fn(a) for a in arr]

def zipWith(fn: Callable[[float, float], float], arr1: Iterable[float], arr2: Iterable[float]) -> Iterable[float]:
    return [fn(a, b) for a, b in zip(arr1, arr2)]

def reduce(fn: Callable[[float, float], float], arr: Iterable[float], init: float) -> float:
    return builtins.sum([fn(init, a) for a in arr]) # 使用内置 sum() 函数求和

def negList(x):
    return map(neg, x)

def addLists(x, y):
    return zipWith(add, x, y)

def sum(x):
    return reduce(add, x, 0)
