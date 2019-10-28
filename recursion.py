def recursion(f, x):
    f = f + x
    return f

# yield

if __name__ == '__main__':
    s = 0
    for i in range(1, 10):
        s = recursion(s, i)
    print(s)