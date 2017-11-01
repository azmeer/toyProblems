"""
  From Pramp Interview 3
  Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.
"""

def array_of_products(arr, step):
  start, end = (0, len(arr)) if step > 0 else (len(arr) - 1, 0 - 1)
  product = None
  products = []
  for index in range(start, end, step):
    product = product * arr[index - step] if product != None else 1
    if step > 0:
      products.append(product) 
    else:
      products.insert(0, product)
  return products

def array_of_array_products(arr):
  return [x*y for x, y in zip(array_of_products(arr, 1), array_of_products(arr, -1))] if len(arr) > 1 else []

