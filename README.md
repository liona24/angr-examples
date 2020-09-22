Examples of using [angr](https://angr.io/)
==========================================

The examples are ordered by increasing complexity. Generally each example is composed of a C-source file and a python script to *solve* it.

If not stated otherwise the examples can be compiled with *gcc* simply by using the following command:
```bash
$ gcc -o test0 test0.c
```

To run the examples you will need to install [angr](https://angr.io/):
```bash
$ pip3 install angr
```

Most of the scripts assume that they find a binary with the same name in the current directory. You should be able to run them by simply typing:
```bash
$ python3 test0.py
```

## Overview

I would suggest playing around with the examples if you are interested in learning.
For the sake of completeness, here is a quick overview of them:

- [test0](test0/test0.c), a simple binary which requires you to enter a password.
- [test1](test1/test1.c), basically the same binary as *test0*, though it performs an additional simple XOR obfuscation step

