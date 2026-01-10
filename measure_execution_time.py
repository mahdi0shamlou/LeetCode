import time
from functools import wraps

def timing_decorator(func):
    """
    Decorator that prints the execution time of the decorated function/method
    
    Example:
        @timing_decorator
        def my_function():
            ...
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()      # most precise timer
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        # Print with different formatting styles - pick your favorite:
        
        # Style 1 - Clean & readable
        print(f"{func.__name__}() → {execution_time:.4f} seconds")
        
        # Style 2 - More detailed
        # print(f"→ {func.__qualname__} finished in {execution_time:.5f}s")
        
        # Style 3 - Very compact
        # print(f"{func.__name__}: {execution_time:.3f}s")
        
        return result
    
    return wrapper