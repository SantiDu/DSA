# Newton's method

def sqrt(n, init_guess, epoch=100):
    x = init_guess
    for _ in range(epoch):
        # the tangent line of y = x^2 - n at x0
        slope = 2 * x
        y = x**2 - n
        # solve x from equation y = y0 + slope * (x - x0) where y=0
        x = -y / slope + x
    return x
    
if __name__ == "__main__":
    from random import randint
    guess = randint(0, 10)
    print(sqrt(4, guess))
