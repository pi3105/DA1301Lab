# ==============================================
# Lab Assignment 4 - Time Complexity (Q7–Q9)
# ==============================================
from time import perf_counter as pc
from math import log
# Hint:
# Try plotting the time complexity data with matplotlib to visualize growth trends
# Will help in identifying the expected time complexity class

# ---------- Q7 ----------
def func1(n):
    s = 0
    for _ in range(n):
        j = 1
        while j * j <= n:
            s += 1
            j += 1
    return s

def analyze_func1():
    """
    TODO:
    - Pick at least 3 n values
    - Measure runtime for each n and store in a dict {n: time}
    - Return (dict, "Estimated Complexity: O(?)")
    """
    # Example skeleton (replace with your own n's):
    # times = {}
    # for n in [ ... ]:
    #     Evalute func1(n) and measure time taken
    # return times, "Estimated Complexity: O(?)"
    times={}
    for n in [10,10**2,10**3]:
        s_time=pc()
        z=func1(n)
        e_time=pc()
        times[n]=e_time-s_time
    return times, "Estimated Complexity: O(n^1.5)"
# ---------- Q8 ----------
def func2(n):
    for _ in range(n):
        for _ in range(n):
            k = 1
            while k < n:
                k *= 2

def analyze_func2():
    """
    TODO: same pattern as analyze_func1
    """
    times={}
    for n in [10,10**2,10**3]:
        s_time=pc()
        z=func2(n)
        e_time=pc()
        times[n]=e_time-s_time
    return times, "Estimated Complexity: O(n^2*log(n))"


# ---------- Q9 ----------
def func3(n):
    if n <= 1:
        return 1
    return func3(n-1) + func3(n-1)

def analyze_func3():
    """
    TODO: same pattern as analyze_func1
    """
    times={}
    for n in [5,8,10]:
        s_time=pc()
        z=func3(n)
        e_time=pc()
        times[n]=e_time-s_time
    return times, "Estimated Complexity: O(2^n)"