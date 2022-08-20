# Author: Feiyue
# Date: 2022-08-20

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def dev(x, y):
  try:
    return x / y
  except Exception as e:
    print(e)
    return None
