# TODO

Do it! Remember, keep it simple, effective, eyes on the goal!

### 0.1. Enhanced Server Selection

- [ ] Switch to v2/servers API for better efficiency:
  ```python
  def get_servers_cache() -> dict:
      """Fetch and cache full server list from v2/servers:
      1. Single API call to get all servers
      2. Cache for hour
      3. Local filtering by country/load/features
      """
  ```
- [ ] Implement fast server selection:
  ```python
  def select_fastest_server(country_code: str, servers: dict) -> str:
      """Select fastest server:
      1. Filter cached servers by country
      2. Take top 5 by load
      3. Parallel ping test
      4. Return fastest responding server
      """
  ```

### 0.2. Simplified Setup
- [ ] Create one-command initialization:
  ```bash
  nyord init  # Sets up everything needed
  ```
  - Validate OpenVPN installation
  - Create config directories
  - Set up credential storage
  - Test API connectivity
  - Generate initial config

### 0.3. API Usage Optimization
- [ ] Switch to https://api.nordvpn.com/v2/servers for server data fetching (the local "cached" file should be made compatible with the v2 format)
- [ ] Retire both https://api.nordvpn.com/v1/servers/countries and https://api.nordvpn.com/v1/servers/recommendations — the v2 API is better because we don't want a list of all countries in the world, just the ones that have servers :) 
  - Single API call instead of multiple v1 endpoints
  - Local filtering instead of multiple API requests
  - Simpler error handling (only one endpoint)

Keep it focused on these core improvements that directly enhance user experience.

### 0.4. Retry, switch gears

- [ ] Make sure that if the country is not specified, we choose the country randomly
- [ ] Implement a bool parameter "random" that chooses a random server (rather than "the fasterst") from the country 
- [ ] When we're connecting, we should retry connection once and if that's not successful, we should try another random server from the same country. See below for some ideas. 



### 0.5. ANALYSIS FOR "RETRY, SWITCH GEARS"

Out‐of‐the‐box, both re‑engage and tenacity are designed to re‑invoke your function with the same arguments on each attempt. They don’t automatically “step through” a list of alternative parameter values. 

That said, with tenacity you can customize the retry behavior by using callback hooks (such as the “after” hook) to modify the function’s keyword arguments between attempts. For example, you can write a small helper like this:

```python
from tenacity import retry, stop_after_attempt, RetryCallState

def update_B(new_value):
    def after_callback(retry_state: RetryCallState):
        # Update the value for the parameter "B" for the next attempt
        retry_state.kwargs['B'] = new_value
    return after_callback

# First, try with B=5 (the default).
# After two failures, update B to 7.
@retry(stop=stop_after_attempt(2), after=update_B(7))
def func(A, B=5):
    print(f"Attempt with B={B}")
    # Example failure condition
    if B < 11:
        raise Exception("Not high enough!")
    return f"Success with B={B}"

try:
    result = func("some_value")
except Exception as e:
    # You might even chain another retry that sets B to 11 after another round
    print("Initial retry block failed:", e)
    # You can re‑decorate or call a wrapper that uses the next parameter value.
    # For example, you could write a loop that tries B from a list [5,7,11]
    for new_B in [7, 11]:
        try:
            result = func("some_value", B=new_B)
            break
        except Exception:
            continue
    else:
        result = None

print("Result:", result)
```

In this example, the tenacity decorator’s “after” hook is used to modify the value of B for the next attempt. (A similar idea was discussed on Stack Overflow, where an answer demonstrated using an after‑callback to change a parameter dynamically.) citeturn0search0

If you need a more complex sequence (like “try with B=5, if that fails twice then use B=7, then 11”), you might either chain multiple decorators or, more simply, write a custom wrapper that iterates over your list of values and calls your function accordingly.

In summary, while neither library provides a one‑line decorator that automatically “steps” through alternative argument values, tenacity’s flexible callback hooks let you implement that behavior with a bit of extra code.

Both the **Re-Engage** and **Tenacity** libraries provide decorators for retrying functions until success or failure, but they do not natively support the specific use case of trying different arguments upon failure. However, you can implement this functionality using a combination of decorators and custom logic.

## 1. Overview of Libraries

### 1.1. Re-Engage
- **Re-Engage** is a fork of the original backoff library, designed for retrying function calls with decorators like `@backoff.on_exception` and `@backoff.on_predicate`. These decorators allow you to specify conditions under which to retry a function based on exceptions or return values[1].

### 1.2. Tenacity
- **Tenacity** is a general-purpose retrying library that simplifies adding retry behavior to functions. It allows for extensive customization through decorators like `@retry`, which can be configured with various parameters such as maximum attempts, delay between retries, and conditions for retrying[2].

## 2. Implementing Dynamic Argument Retrying

To achieve the desired behavior of trying different arguments after failures, you can create a custom decorator that wraps your function and manages the argument variations. Here’s an example implementation:

```python
from tenacity import retry, stop_after_attempt

def dynamic_retry(args_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for args in args_list:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed with args {args}: {e}")
            raise Exception("All attempts failed.")
        return wrapper
    return decorator

@dynamic_retry([(5,), (7,), (11,)])  # List of argument tuples
def my_function(b):
    # Simulate a function that may fail
    if b != 11:  # Let's say it fails unless b is 11
        raise ValueError("Failed!")
    return "Success!"

# Usage
result = my_function(5)  # This will try 5, then 7, then 11.
print(result)  # Outputs: Success!
```

### 2.1. Explanation:
- The `dynamic_retry` decorator takes a list of argument tuples.
- The `wrapper` function iterates over these arguments, attempting to call the target function.
- If an exception occurs, it catches the error, logs it, and moves on to the next set of arguments.
- If all attempts fail, it raises an exception.

## 3. Conclusion

While neither Re-Engage nor Tenacity directly supports dynamically changing function arguments upon failure out-of-the-box, you can implement this functionality using custom decorators. This approach allows you to maintain flexibility in your retry logic while leveraging the robust features provided by existing libraries.

Based on the search results and your specific question about retrying with different arguments, I'll provide a comprehensive answer about implementing such functionality.

Let me break this down step by step:

### 3.1. Current State of Retry Libraries

The common retry libraries like `tenacity` and `re-engage` focus primarily on retrying with the same arguments. While they're powerful for basic retry scenarios, they don't directly support changing arguments between retries [0].

### 3.2. Custom Solution Implementation

Here's a custom decorator implementation that allows retrying with different arguments:

```python
from functools import wraps
from typing import List, Any, Callable
import time

def retry_with_different_args(arg_sequences: List[Any], delay: int = 1):
    """
    Retry decorator that attempts the function with different argument values.
    
    Args:
        arg_sequences: List of values to try for the decorated function's first argument
        delay: Delay between retries in seconds
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            # Replace the first argument with each value in the sequence
            for arg_value in arg_sequences:
                try:
                    new_args = (arg_value,) + args[1:]
                    return func(*new_args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt with value {arg_value} failed: {str(e)}")
                    time.sleep(delay)
            
            # If we get here, all attempts failed
            raise last_exception or Exception("All retry attempts failed")
            
        return wrapper
    return decorator
```

Example usage:

```python
# Example using the decorator
@retry_with_different_args([5, 7, 11])
def divide_number(divisor: int, number: int = 100):
    if divisor == 7:
        raise ValueError("Don't like 7")
    return number / divisor

# This will try with divisor=5, then 7, then 11
try:
    result = divide_number(5, number=100)
    print(f"Success: {result}")
except Exception as e:
    print(f"Final failure: {e}")
```

### 3.3. Key Points to Consider

1. **Flexibility**: This implementation allows you to specify a sequence of values to try for a specific argument [0].

2. **Error Handling**: Each attempt is wrapped in a try-except block, allowing you to catch and handle specific exceptions [0].

3. **Delay Control**: You can specify delays between attempts to prevent overwhelming systems [0].

### 3.4. Best Practices

1. **Specific Exceptions**: Always catch specific exceptions rather than using a broad Exception catch.

2. **Logging**: Include proper logging to track retry attempts and failures.

3. **Timeout Consideration**: Consider implementing an overall timeout mechanism.

4. **State Management**: Be careful with stateful operations when retrying with different arguments.

### 3.5. Alternative Approach Using Tenacity

While tenacity doesn't directly support changing arguments, you can achieve similar functionality by combining it with a custom retry strategy:

```python
from tenacity import retry, stop_after_attempt
from functools import partial

def retry_sequence(func, arg_sequences):
    for arg in arg_sequences:
        try:
            return func(arg)
        except Exception:
            continue
    raise Exception("All attempts failed")

# Usage example
@retry(stop=stop_after_attempt(1))
def wrapped_function(x):
    return retry_sequence(some_function, [5, 7, 11])
```

This solution provides a way to work with existing retry libraries while adding the functionality to try different arguments, though it's not as elegant as the custom decorator approach.