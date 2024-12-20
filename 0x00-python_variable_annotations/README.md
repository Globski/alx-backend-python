# Alx Backend Python - Python Variable Annotations

## Description
This project focuses on implementing type annotation in Python 3 to improve code readability, maintainability, and type safety. You will create various functions with specific type annotations, exploring concepts such as duck typing and type checking using MyPy. Using Python's dynamic typing features, you'll gain practical experience in writing clearer, more robust code through the effective use of type annotation.

## Project Structure

| Task                                     | Description                                                                                                                                                      | Source Code                          |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| **0. Basic annotations - add**           | Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.                                  | [0-add.py](0-add.py)                |
| **1. Basic annotations - concat**        | Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.                       | [1-concat.py](1-concat.py)          |
| **2. Basic annotations - floor**         | Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.                                               | [2-floor.py](2-floor.py)            |
| **3. Basic annotations - to string**     | Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.                                 | [3-to_str.py](3-to_str.py)          |
| **4. Basic annotations - define variables** | Define and annotate variables: an integer `a`, a float `pi`, a boolean `i_understand_annotations`, and a string `school`.                                    | [4-define_variables.py](4-define_variables.py) |
| **5. Complex types - list of floats**    | Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.                           | [5-sum_list.py](5-sum_list.py)      |
| **6. Complex types - mixed list**        | Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.                       | [6-sum_mixed_list.py](6-sum_mixed_list.py) |
| **7. Complex types - string and int/float to tuple** | Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple.                                     | [7-to_kv.py](7-to_kv.py)            |
| **8. Complex types - functions**         | Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`. | [8-make_multiplier.py](8-make_multiplier.py) |
| **9. Let's duck type an iterable object**| Annotate the below function’s parameters and return values with the appropriate types.                                                                           | [9-element_length.py](9-element_length.py) |
| **10. Duck typing - first element of a sequence** | Augment the code with the correct duck-typed annotations.                                                                                                     | [100-safe_first_element.py](100-safe_first_element.py) |
| **11. More involved type annotations**   | Add type annotations to the function provided in the task.                                                                                                     | [101-safely_get_value.py](101-safely_get_value.py) |
| **12. Type Checking**                    | Use MyPy to validate the provided piece of code and apply necessary changes.                                                                                    | [102-type_checking.py](102-type_checking.py) |
### Environment
- Ubuntu 18.04 LTS
- python3 (version 3.7)
- MyPy for static type checking

## Requirements

- Code must run on **Ubuntu 18.04 LTS** with **Python 3.7**.
- Ensure files:
  - End with a new line.
  - Start with the shebang: `#!/usr/bin/env python3`.
  - Are executable.
  - Follow `pycodestyle` guidelines (version 2.5). PEP 8 style compliance
  - Use `mypy` to validate your type annotations.
  - The length of your files will be tested using the `wc` command.
  - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
  - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c     'print(__import__("my_module").MyClass.my_function.__doc__)')
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Learning Objectives
By the end of this project, you will be able to:
- Understand and implement type annotations in Python.
- Use type hints to specify function signatures and variable types.
- Explain duck typing and its significance in Python.
- Validate your code using MyPy.
- How to specify variable types and function signatures.


## Prototypes Used in the Project

| Prototype Name                                                             | Description                                                                                          |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `def add(a: float, b: float) -> float`                                     | Adds two floats and returns their sum.                                                             |
| `def concat(str1: str, str2: str) -> str`                                 | Concatenates two strings and returns the result.                                                   |
| `def floor(n: float) -> int`                                               | Returns the floor of a given float.                                                                 |
| `def to_str(n: float) -> str`                                              | Converts a float to its string representation.                                                     |
| `def sum_list(input_list: List[float]) -> float`                          | Sums a list of floats and returns the total.                                                       |
| `def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`           | Sums a mixed list of integers and floats and returns the total.                                    |
| `def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`           | Returns a tuple containing a string and the square of a number.                                    |
| `def make_multiplier(multiplier: float) -> Callable[[float], float]`     | Returns a function that multiplies a float by a given multiplier.                                  |
| `def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]` | Returns a list of tuples containing elements and their lengths.                                     |
| `def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]`         | Returns the first element of a sequence, or None if the sequence is empty.                         |
| `def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]` | Returns a value from a dictionary or a default value if the key is not present.                    |
| `def zoom_array(lst: Tuple, factor: int = 2) -> List`                    | Returns a zoomed-in version of the input array based on the specified factor.                      |

## How to Use
To run this project, ensure you have Python 3.7 and MyPy installed on your system. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/alx-backend-python.git
cd alx-backend-python/0x00-python_variable_annotations
```

### Running the Tests
You can run the provided main files to test each function:

```bash
chmod +x <main_file.py>
./<main_file.py>
```

### Validation
To validate type annotations, run:

```bash
mypy <file_name.py>
```

### Additional Notes
- Type annotations help convey the expected data types of function parameters and return values.
- Using MyPy allows for static type checking, which can help catch errors before runtime.
- For more detailed information on type annotations in Python, refer to the [official documentation](https://docs.python.org/3/library/typing.html).

## Tasks

0. **Basic annotations - add**
   - Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.
     ```python
     bob@dylan:~$ cat 0-main.py
      #!/usr/bin/env python3
      add = __import__('0-add').add

      print(add(1.11, 2.22) == 1.11 + 2.22)
      print(add.__annotations__)

      bob@dylan:~$ ./0-main.py
      True
      {'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
     ```

1. **Basic annotations - concat**
   - Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.
     ```python
     bob@dylan:~$ cat 1-main.py
      #!/usr/bin/env python3
      concat = __import__('1-concat').concat

      str1 = "egg"
      str2 = "shell"

      print(concat(str1, str2) == "{}{}".format(str1, str2))
      print(concat.__annotations__)

      bob@dylan:~$ ./1-main.py
      True
      {'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
     ```

2. **Basic annotations - floor**
   - Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.
     ```python
     bob@dylan:~$ cat 2-main.py
      #!/usr/bin/env python3

      import math

      floor = __import__('2-floor').floor

      ans = floor(3.14)

      print(ans == math.floor(3.14))
      print(floor.__annotations__)
      print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

      bob@dylan:~$ ./2-main.py
      True
      {'n': <class 'float'>, 'return': <class 'int'>}
      floor(3.14) returns 3, which is a <class 'int'>
     ```

3. **Define variables**
   - Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.
     ```python
     bob@dylan:~$ cat 3-main.py
      #!/usr/bin/env python3
      to_str = __import__('3-to_str').to_str

      pi_str = to_str(3.14)
      print(pi_str == str(3.14))
      print(to_str.__annotations__)
      print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))

      bob@dylan:~$ ./3-main.py
      True
      {'n': <class 'float'>, 'return': <class 'str'>}
      to_str(3.14) returns 3.14, which is a <class 'str'>
     ```
4. **Basic annotations - to string**
   - Define and annotate the following variables with the specified values:
   - a, an integer with a value of 1
   - pi, a float with a value of 3.14
   - i_understand_annotations, a boolean with a value of True
   - school, a string with a value of “Holberton”
     ```python
     bob@dylan:~$ cat 4-main.py
      #!/usr/bin/env python3

      a = __import__('4-define_variables').a
      pi = __import__('4-define_variables').pi
      i_understand_annotations = __import__('4-define_variables').i_understand_annotations
      school = __import__('4-define_variables').school

      print("a is a {} with a value of {}".format(type(a), a))
      print("pi is a {} with a value of {}".format(type(pi), pi))
      print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
      print("school is a {} with a value of {}".format(type(school), school))

      bob@dylan:~$ ./4-main.py
      a is a <class 'int'> with a value of 1
      pi is a <class 'float'> with a value of 3.14
      i_understand_annotations is a <class 'bool'> with a value of True
      school is a <class 'str'> with a value of Holberton
     ```

5. **Complex types - list of floats**
   - Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.
     ```python
     bob@dylan:~$ cat 5-main.py
      #!/usr/bin/env python3

      sum_list = __import__('5-sum_list').sum_list

      floats = [3.14, 1.11, 2.22]
      floats_sum = sum_list(floats)
      print(floats_sum == sum(floats))
      print(sum_list.__annotations__)
      print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))

      bob@dylan:~$ ./5-main.py
      True
      {'input_list': typing.List[float], 'return': <class 'float'>}
      sum_list(floats) returns 6.470000000000001 which is a <class 'float'>
     ```

6. **Complex types - mixed list**
   - Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.
     ```python
     bob@dylan:~$ cat 6-main.py
      #!/usr/bin/env python3

      sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

      print(sum_mixed_list.__annotations__)
      mixed = [5, 4, 3.14, 666, 0.99]
      ans = sum_mixed_list(mixed)
      print(ans == sum(mixed))
      print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))

      bob@dylan:~$ ./6-main.py
      {'mxd_lst': typing.List[typing.Union[int, float]], 'return': <class 'float'>}
      True
      sum_mixed_list(mixed) returns 679.13 which is a <class 'float'>
     ```

7. **Complex types - string and int/float to tuple**
   - Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.
     ```python
     bob@dylan:~$ cat 7-main.py
      #!/usr/bin/env python3

      to_kv = __import__('7-to_kv').to_kv

      print(to_kv.__annotations__)
      print(to_kv("eggs", 3))
      print(to_kv("school", 0.02))

      bob@dylan:~$ ./7-main.py
      {'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
      ('eggs', 9)
      ('school', 0.0004)
     ```

8. **Complex types - functions**
   - Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.
     ```python
     bob@dylan:~$ cat 8-main.py
      #!/usr/bin/env python3

      make_multiplier = __import__('8-make_multiplier').make_multiplier
      print(make_multiplier.__annotations__)
      fun = make_multiplier(2.22)
      print("{}".format(fun(2.22)))

      bob@dylan:~$ ./8-main.py
      {'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}
      4.928400000000001
     ```

9. **Let's duck type an iterable object**
   - Annotate the below function’s parameters and return values with the appropriate types:
     ```python
     def element_length(lst):
         return [(i, len(i)) for i in lst]
     ```
      ```python
      bob@dylan:~$ cat 9-main.py 
      #!/usr/bin/env python3

      element_length =  __import__('9-element_length').element_length

      print(element_length.__annotations__)

      bob@dylan:~$ ./9-main.py 
      {'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
      ```

10. **Duck typing - first element of a sequence**
    - Augment the following code with the correct duck-typed annotations:
      ```python
      # The types of the elements of the input are not know
      def safe_first_element(lst):
          if lst:
              return lst[0]
          else:
              return None
      ```
      ```python
      bob@dylan:~$ cat 100-main.py 
      #!/usr/bin/env python3

      safe_first_element =  __import__('100-safe_first_element').safe_first_element

      print(safe_first_element.__annotations__)

      bob@dylan:~$ ./100-main.py 
      {'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}
      ```
11. **More involved type annotations**
    - Given the parameters and the return values, add type annotations to the function:
      ```python
      def safely_get_value(dct, key, default = None):
          if key in dct:
              return dct[key]
          else:
              return default
      ```
      ```python
      bob@dylan:~$ cat 101-main.py 
      #!/usr/bin/env python3

      safely_get_value = __import__('101-safely_get_value').safely_get_value
      annotations = safely_get_value.__annotations__

      print("Here's what the mappings should look like")
      for k, v in annotations.items():
      print( ("{}: {}".format(k, v)))

      bob@dylan:~$ ./101-main.py 
      Here's what the mappings should look like
      dct: typing.Mapping
      key: typing.Any
      default: typing.Union[~T, NoneType]
      return: typing.Union[typing.Any, ~T]
      ```

12. **Type Checking**
    - Use MyPy to validate the following piece of code and apply any necessary changes:
      ```python
      def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
          zoomed_in: Tuple = [
              item for item in lst
              for i in range(factor)
          ]
          return zoomed_in

      array = [12, 72, 91]

      zoom_2x = zoom_array(array)

      zoom_3x = zoom_array(array, 3.0)
      ```
      ```python
      bob@dylan:~$ mypy 102-type_checking.py
      Success: no issues found in 1 source file
      bob@dylan:~$ cat 102-main.py 
      #!/usr/bin/env python3

      zoom_array =  __import__('102-type_checking').zoom_array

      print(zoom_array.__annotations__)

      bob@dylan:~$ ./102-main.py 
      {'lst': typing.Tuple, 'factor': <class 'int'>, 'return': typing.List}
      ```
