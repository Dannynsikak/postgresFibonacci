from django.shortcuts import render
from .models import Fibonacci

# Generate Fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    yield a
    yield b
    for _ in range(2, min(n, 100)):
        a, b = b, a + b
        yield a

# Store Fibonacci numbers in the database
def store_fibonacci(n=100):
    for fib_num in fibonacci(n):
        Fibonacci.objects.create(fibonacci_value=fib_num)

# View to display Fibonacci sequence
def fibonacci_sequence(request):
    # Store the first 1000 Fibonacci numbers in the database
    store_fibonacci(1000)  # Only call once to store 1000 numbers

    # Retrieve Fibonacci numbers from the database
    fibonacci_numbers = Fibonacci.objects.all()

    # Render the template with the Fibonacci numbers
    return render(request, 'fibonacci_app/fibonacci_list.html', {'fibonacci_numbers': fibonacci_numbers})

# Optionally, you can define a home view if needed
# def home(request):
#     return render(request, 'home.html')
