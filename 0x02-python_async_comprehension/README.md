# Alx Backend Python - Python Async Comprehension

## Description

This project focuses on creating asynchronous generators and comprehensions using Python's `asyncio` module. The goal is to develop a series of coroutines that yield random numbers asynchronously, collect those numbers, and measure runtime. 
It demonstrates the use of asynchronous programming in Python, enabling efficient handling of tasks that involve waiting—such as fetching random numbers—while maintaining responsive and concurrent execution.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. Async Generator | Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. | [0-async_generator.py](0-async_generator.py) |
| 1. Async Comprehensions | Import `async_generator` and write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers. | [1-async_comprehension.py](1-async_comprehension.py) |
| 2. Run time for four parallel comprehensions | Import `async_comprehension` and write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. Measure the total runtime and return it. | [2-measure_runtime.py](2-measure_runtime.py) |

## Environment
- Python 3.7
- Asyncio module (included with Python)

## Requirements
- Allowed editors: vi, vim, emacs.
- All files must be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the folder is mandatory.
- Code must adhere to the `pycodestyle` style (version 2.5.x).
- The length of your files will be tested using `wc`.
- All modules should have documentation.
- All functions should have documentation.
- Documentation must be meaningful and not a simple word.
- All functions and coroutines must be type-annotated.

## Learning Objectives
At the end of this project, you should be able to:
- Write an asynchronous generator.
- Use async comprehensions effectively.
- Type-annotate generators properly.

## Prototype Table

| Function Name        | Parameters   | Return Type        | Description                                                   |
|----------------------|--------------|---------------------|---------------------------------------------------------------|
| `async_generator`    | None         | `AsyncGenerator`    | Yields 10 random numbers between 0 and 10 with a 1-second delay. |
| `async_comprehension`| None         | `List[float]`       | Collects 10 random numbers using an async comprehension.     |
| `measure_runtime`    | None         | `float`             | Measures the runtime of executing `async_comprehension` four times in parallel. |

## How to Use
1. Clone the repository.
2. Navigate to the project directory.
3. Run the main scripts for each task to see the output.

## Usage
Run the script with the command:
```bash
python3 async_gen.py
```
```
## Running the Code
- Each task can be tested using the provided main scripts:
  - `0-main.py` for Task 0.
  - `1-main.py` for Task 1.
  - `2-main.py` for Task 2.
  ```
- Make sure to run these scripts in an environment where Python 3.7 is installed and the `asyncio` module is available.
- The total runtime for `measure_runtime` should be approximately 10 seconds due to concurrent execution of the async comprehensions.

## Additional Notes
#### Asynchronous Generators
An asynchronous generator allows you to define a generator that can yield values asynchronously. 

#### Using Async Comprehensions
You can use async comprehensions to consume asynchronous generators efficiently. 

#### Type Annotations
Type annotations help in clarifying what type of values your functions will return and what parameters they accept. For asynchronous generators, use `AsyncGenerator`.

#### Explanation of Total Runtime
When running `measure_runtime`, the total runtime is approximately 10 seconds. This is expected because each call to `async_comprehension` involves waiting for 10 seconds in total (1 second per number) while running four calls concurrently. Thus, while each `async_comprehension` runs for about 10 seconds, they overlap, leading to a total execution time close to 10 seconds instead of 40.

## Tasks

### 0. Async Generator

**File:** `0-async_generator.py`

**mandatory**  
Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

```python
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

### 1. Async Comprehensions

**File:** `1-async_comprehension.py`

**mandatory**  
Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

```python
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

### 2. Run time for four parallel comprehensions

**File:** `2-measure_runtime.py`

**mandatory**  
Import `async_comprehension` from the previous file and write a coroutine called `measure_runtime` that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

```python
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135
```
