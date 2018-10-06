#!/usr/bin/env python3

def test_func(input_):
    return ("Hello " + input_)



if __name__ == "__main__":
    var = test_func(input("Input a name: "))
    print((var + "\n") * 3)