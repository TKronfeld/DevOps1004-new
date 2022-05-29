import fibonacci # import all content of fibonacci.py

fibonacci.fib(100)

# OR take only specific function or variable

from fibonacci import fib as fib_av
from day2-fibo import fib as fib_my

fib_av(100)
fib_my(100)

