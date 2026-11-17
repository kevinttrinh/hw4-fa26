---
title: Python Decorators
date: 2024-11-03
tags: [python]
author: Alex
---

A hunch I've been developing: decorators are underused for cross-cutting concerns.

## The basic pattern

A decorator is just a function that takes a function and returns a function.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper
```

## When are they actually useful?

- Timing and profiling
- Caching (`functools.lru_cache`)
- Authentication checks in web frameworks
- Retry logic for flaky network calls

## Open questions

- Are class-based decorators ever cleaner than function-based ones?
- How do decorators interact with type checkers?
