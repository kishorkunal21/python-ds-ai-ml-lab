# Pythonic things vs Java — quick examples

This file shows concise Java → Python comparisons for common concepts you should know when moving from Java to Python.

- Java snippets are illustrative and use Java-style syntax; Python snippets are runnable Python.

---

## 1. Dynamic typing
Short: Variables hold values, not types; types are checked at runtime.
Java:
```java
int x = 1;
// types checked at compile time
```
Python:
```python
x = 1  # no declared type; runtime-typed
x = 'now a string'
```

## 2. Indentation-significant blocks
Short: Python uses indentation for blocks instead of braces.
Java:
```java
if (cond) {
    doThing();
}
```
Python:
```python
if cond:
    do_thing()
```

## 3. Duck typing (no interfaces required)
Short: Behavior matters more than declared types — if it implements the method, it works.
Java:
```java
interface Quacker { void quack(); }
class Duck implements Quacker { public void quack() { ... } }
```
Python:
```python
class Duck:
    def quack(self):
        print('quack')

def make_it_quack(q):
    q.quack()
```

## 4. Immutability vs mutability (ints/str immutable)
Short: Some built-ins are immutable (ints, str, tuple), others are mutable (list, dict).
Java:
```java
Integer a = 1; // boxed immutable-like
```
Python:
```python
s = 'hi'
# s.replace returns new string; original unchanged
s2 = s.replace('h','H')
```

## 5. Rebinding semantics (x += 1 creates new int)
Short: Operations on immutables rebind names to new objects instead of mutating them.
Java:
```java
Integer x = 0;
x = x + 1; // new object for boxed Integer semantics
```
Python:
```python
x = 0
x += 1  # rebinds name x to new int object
```

## 6. Varargs / kwargs
Short: Python supports arbitrary positional and keyword arguments via *args/**kwargs.
Java:
```java
void foo(int... vals) { }
```
Python:
```python
def foo(*args, **kwargs):
    print(args, kwargs)

foo(1,2, a=3)
```

## 7. Multiple return values (tuples)
Short: Functions can return multiple values via tuples — no small DTO needed.
Java:
```java
// return a small DTO or array
```
Python:
```python
def coords():
    return 1, 2
x, y = coords()
```

## 8. First-class functions / lambdas
Short: Functions are objects — you can pass them around and return them.
Java:
```java
Runnable r = () -> System.out.println("hi");
```
Python:
```python
def f():
    print('hi')
map(lambda x: x*2, [1,2,3])
```

## 9. List comprehensions
Short: Comprehensions give concise, readable collection construction.
Java:
```java
// verbose loop to build list
```
Python:
```python
squares = [x*x for x in range(10)]
```

## 10. Generators & yield (lazy)
Short: Generators produce values lazily using `yield`, saving memory.
Java:
```java
// use Iterator implementations or Streams
```
Python:
```python
def nums():
    for i in range(10):
        yield i
for n in nums():
    print(n)
```

## 11. Iteration helpers (enumerate / zip)
Short: Built-in helpers simplify common iteration patterns (indexing, parallel loops).
Java:
```java
// indexed loop with for(int i=0; i<list.size(); i++)
```
Python:
```python
for i, v in enumerate(['a','b']):
    print(i, v)
for a, b in zip([1,2], ['x','y']):
    print(a,b)
```

## 12. Context managers (try-with-resources equivalent)
Short: `with` ensures deterministic setup/teardown (like Java's try-with-resources).
Java:
```java
try (BufferedReader r = ...) { /* auto-close */ }
```
Python:
```python
with open('f.txt') as f:
    data = f.read()
```

## 13. Exceptions (no checked exceptions)
Short: Python has only unchecked exceptions; callers aren't forced to declare them.
Java:
```java
void foo() throws IOException { }
```
Python:
```python
try:
    open('nope')
except FileNotFoundError as e:
    print('handled')
```

## 14. Decorators (like Java annotations + AOP)
Short: Decorators wrap functions or classes to add behavior declaratively.
Java:
```java
// annotations + proxies for behavior
```
Python:
```python
def timed(fn):
    def wrapper(*a, **k):
        import time
        t = time.time()
        res = fn(*a, **k)
        print('took', time.time()-t)
        return res
    return wrapper

@timed
def work():
    pass
```

## 15. Dataclasses (boilerplate reduction)
Short: `@dataclass` generates constructor, repr, eq and more automatically.
Java:
```java
class Point { int x,y; Point(int x,int y){...} }
```
Python:
```python
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
```

## 16. Properties (getters/setters without boilerplate)
Short: `@property` exposes attribute access with optional getter/setter logic.
Java:
```java
class Foo { private int x; public int getX(){return x;} }
```
Python:
```python
class Foo:
    def __init__(self):
        self._x = 0
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, v):
        self._x = v
```

## 17. Dunder methods (operator overloading)
Short: Special methods like `__repr__` and `__eq__` customize object behavior.
Java:
```java
// override equals, toString
```
Python:
```python
class V:
    def __init__(self,x):
        self.x = x
    def __repr__(self):
        return f'V({self.x})'
    def __eq__(self, other):
        return isinstance(other, V) and self.x==other.x
```

## 18. Mutable default arg pitfall
Short: Default argument values are evaluated once — avoid mutable defaults.
Java:
```java
// method-scoped defaults don't exist
```
Python:
```python
def f(a=None):
    if a is None:
        a = []
    a.append(1)
    return a
```

## 19. Identity vs equality
Short: `is` checks identity (same object), `==` checks value equality.
Java:
```java
String a = new String("x"); // == compares refs
```
Python:
```python
a = [1]; b = [1]
print(a == b)  # True (value)
print(a is b)  # False (identity)
```

## 20. Slicing & negative indices
Short: Python supports concise slicing and negative indexing for convenience.
Java:
```java
// use subList or Arrays.copyOfRange
```
Python:
```python
arr = [0,1,2,3]
print(arr[1:3])  # [1,2]
print(arr[-1])   # 3
```

## 21. f-strings (interpolation)
Short: f-strings provide compact, readable string interpolation.
Java:
```java
System.out.printf("%s %d", s, n);
```
Python:
```python
name='you'; n=3
print(f"hi {name} {n}")
```

## 22. Modules / packages
Short: Files are modules; directories organize packages — imports are simple.
Java:
```java
package com.example;
```
Python:
```python
# file structure: pkg/__init__.py, pkg/mod.py
from pkg.mod import fn
```

## 23. Virtualenvs & packaging (concept)
Short: Virtual environments isolate project dependencies, similar to per-project build tools.
Java:
```java
// use maven/gradle per-project
```
Python:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 24. Concurrency (GIL note) — threads vs multiprocessing
Short: Python threads are limited by the GIL for CPU-bound work; use multiprocessing or async.
Java:
```java
// true parallel threads for CPU-bound work
```
Python:
```python
import threading
# threads are fine for I/O; use multiprocessing for CPU-bound
```

## 25. Useful stdlib modules
Short: The standard library provides many utilities (collections, itertools, functools).
Java:
```java
// use Guava, Apache Commons
```
Python:
```python
from collections import defaultdict, Counter
from itertools import chain
```

## 26. Testing (pytest)
Short: `pytest` is a compact, popular testing framework for Python.
Java:
```java
// use JUnit
```
Python:
```python
# test_sample.py
def test_add():
    assert 1+1 == 2
```

---

If you want, I can: add runnable examples, run quick snippets, or shorten this to a printable cheat-sheet.
