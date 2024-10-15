# Alx Backend Python - Python Async

## Description

The project focuses on mastering asynchronous programming in Python using the asyncio library. By the end, you will understand the `async` and `await` syntax, how to create and run concurrent coroutines, create and manage asyncio tasks, and measure execution time. Each task builds on the previous one, leading to a comprehensive understanding of how to effectively manage concurrent operations.

## Project Structure

| Task Number | Description                                                                                              | Source Code                          |
|-------------|----------------------------------------------------------------------------------------------------------|--------------------------------------|
| 0           | Write an asynchronous coroutine called `wait_random` that waits for a random delay.                     | [0-basic_async_syntax.py](0-basic_async_syntax.py) |
| 1           | Create a coroutine `wait_n` that calls `wait_random` multiple times and returns the delays in order.    | [1-concurrent_coroutines.py](1-concurrent_coroutines.py) |
| 2           | Implement `measure_time` to measure the execution time of `wait_n` and return the average delay.       | [2-measure_runtime.py](2-measure_runtime.py) |
| 3           | Write a function `task_wait_random` that returns an asyncio Task for `wait_random`.                     | [3-tasks.py](3-tasks.py)           |
| 4           | Implement `task_wait_n` that calls `task_wait_random` instead of `wait_random`.                        | [4-tasks.py](4-tasks.py)           |

## Environment

- Python 3.7
- Ubuntu 18.04 LTS

## Learning Objectives

- Understand the `async` and `await` syntax in Python.
- Execute an async program using `asyncio`.
- Run concurrent coroutines efficiently.
- Create and manage asyncio tasks.
- Utilize the `random` module for generating random values.
- Measure execution time for asynchronous tasks.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using wc
- The first line of all your files should be exactly #!/usr/bin/env python3
- Your code should use the pycodestyle style (version 2.5.x)All your functions and coroutines must be type-annotated.
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
  
## Prototype Table

| Function Name      | Parameters                | Return Type         |
|--------------------|---------------------------|----------------------|
| `wait_random`      | `max_delay: int = 10`    | `float`              |
| `wait_n`           | `n: int, max_delay: int`  | `List[float]`       |
| `measure_time`     | `n: int, max_delay: int`  | `float`              |
| `task_wait_random` | `max_delay: int`          | `asyncio.Task`      |
| `task_wait_n`      | `n: int, max_delay: int`  | `List[float]`       |

## How to Use

## Usage

To run the example scripts and test the implementations, use the following commands:

```bash
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
```

- Make sure all your files are executable with `chmod +x filename`.

## Additional Notes

1. **Async and Await Syntax**: 
   - `async` defines a coroutine, which is a special type of function that can pause its execution.
   - `await` is used to pause the coroutine until the awaited task is complete.

2. **Executing an Async Program with asyncio**:
   - Use `asyncio.run(main())` to run the main coroutine.

3. **Running Concurrent Coroutines**:
   - You can use `asyncio.gather()` to run multiple coroutines concurrently.

4. **Creating Asyncio Tasks**:
   - Use `asyncio.create_task(coroutine())` to schedule a coroutine to run concurrently.Sure! Here’s a detailed README for your project, covering each task and providing context for the code you'll be implementing.


## Tasks

### 0. The basics of async

**File**: `0-basic_async_syntax.py`

**mandatory**   
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.  
Use the random module.

```python
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```

### 1. Let's execute multiple coroutines at the same time with async

**File**: `1-concurrent_coroutines.py`

**mandatory**  
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.  
wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.

```python
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

### 2. Measure the runtime

**File**: `2-measure_runtime.py`

**mandatory**   
From the previous file, import wait_n into 2-measure_runtime.py.  
Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.  
Use the time module to measure an approximate elapsed time.

```python
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
```

### 3. Tasks

**File**: `3-tasks.py`

**mandatory**  
Import wait_random from 0-basic_async_syntax.  
Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.

```python
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
<class '_asyncio.Task'>
```

### 4. Tasks

**File**: `4-tasks.py`

**mandatory**   
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.

```python
bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
```
