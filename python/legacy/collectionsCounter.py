#!/bin/python3

import collections

shoeCount = int(input())

shoes = collections.Counter(map(int, input().split()))
if sum(shoes.values()) != shoeCount:
    print(sum(shoes.values()))
    print("The shoe count does not equal shoes entered. Please restart and try again.")

customerCount = int(input())

income = 0

for i in range(customerCount):
    size, price = map(int, input().split())
    if(shoes[size]):
        income += price
        shoes[size] -= 1
print(income)
