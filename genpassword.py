#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
by @youngsummerlight
'''

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passlen = int(input("Enter password length: "))
p = str("".join(random.sample(s,passlen )))



if __name__ == "__main__":
    print(p)