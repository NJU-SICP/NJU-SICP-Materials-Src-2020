```python
def count_factors(n):
    i, count = 1, 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def count_primes(n):
    i, count = 1, 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

# 使用刚才定义的函数
count_factors(10)
count_factors(20)
count_factors(30)
count_primes(10)
```

当你看到这段代码的时候，你会发现`count_factors`和`count_primes`除了`if`语句后面的表达式，其它代码都一模一样。
你想到了课堂上的抽象，所以打算把`if`后的表达式抽象出来。

做抽象，首选是函数。然后你发现，这两个`if`后面的布尔表达式用到了变量`i`和`n`，那你可以抽出两个参数一致的函数代替它们，得到代码

```python
# 新抽象出来的函数
def condition_for_factors(n, i):
    return n % i == 0

# 新抽象出来的函数
def condition_for_primes(n, i):
    return is_prime(i)

def count_factors(n):
    i, count = 1, 0
    while i <= n:
        if condition_for_factors(n, i): # 替换表达式
            count += 1
        i += 1
    return count

def count_primes(n):
    i, count = 1, 0
    while i <= n:
        if condition_for_primes(n, i): # 替换表达式
            count += 1
        i += 1
    return count
```

现在代码看起来基本一样了，但是就只有`if`后调用的函数名不一样，所以你把函数名抽象成了一个参数，得到：

```python
def condition_for_factors(n, i):
    return n % i == 0

def condition_for_primes(n, i):
    return is_prime(i)

def count_factors(n, condition): # condition应该是个指向函数的参数
    i, count = 1, 0
    while i <= n:
        if condition(n, i):
            count += 1
        i += 1
    return count

def count_primes(n, condition):
    i, count = 1, 0
    while i <= n:
        if condition(n, i):
            count += 1
        i += 1
    return count

count_factors(10, condition_for_factors)
count_factors(20, condition_for_factors)
count_factors(30, condition_for_factors)
count_primes(10, count_primes)
```

只不过，现在你想像原来一样达到`count_factor(10)`的效果，就需要调用`count_factor(10, condition_for_factors)`。

接下来你发现`count_factors`和`count_primes`两个函数定义一模一样，不如合并成同一个函数吧，名字就叫`count_cond`。
于是你得到一个新的很简洁的代码：

```python
def condition_for_factors(n, i):
    return n % i == 0

def condition_for_primes(n, i):
    return is_prime(i)

def count_cond(n, condition):
    i, count = 1, 0
    while i <= n:
        if condition(n, i):
            count += 1
        i += 1
    return count

count_cond(10, condition_for_factors)
count_cond(20, condition_for_factors)
count_cond(30, condition_for_factors)
count_cond(10, count_primes)
```

虽说现在的代码很简单了，但是使用`count_cond`很麻烦。因为每次调用后面都要跟一坨`condition_for_factors`。
你想，能不能再抽象一个函数`make_count_cond`，达到下面这个效果：

```python
def condition_for_factors(n, i):
    return n % i == 0

def condition_for_primes(n, i):
    return is_prime(i)

def count_cond(n, condition):
    i, count = 1, 0
    while i <= n:
        if condition(n, i):
            count += 1
        i += 1
    return count

def make_count_cond(condition):
    def f(n):
        return ______ # 该写什么?
    return f

count_factors = make_count_cond(condition_for_factors)
count_factors(10) # 等价于 count_cond(30, condition_for_factors)
count_factors(20) # 等价于 count_cond(30, condition_for_factors)
count_factors(30) # 等价于 count_cond(30, condition_for_factors)
make_count_cond(condition_for_primes)(10)  # 等价于 count_cond(10, count_primes)
```

最后你发现，`condition_for_factors`和`condition_for_primes`定义后只使用了一次，不如用lambda表达式代替，于是你就写了：

```python
def count_cond(n, condition):
    i, count = 1, 0
    while i <= n:
        if condition(n, i):
            count += 1
        i += 1
    return count

def make_count_cond(condition):
    def f(n):
        return ______ # 该写什么?
    return f

count_factors = make_count_cond(lambda n, i: n % i == 0) # lambda表达式代替了condition_for_factors
count_factors(10)
count_factors(20)
count_factors(30)
make_count_cond(lambda n, i: is_prime(i))(10)  # lambda表达式代替了 condition_for_primes
```

最后看着这个简单而又骚气的代码，你不由得感慨，高阶函数真牛逼！