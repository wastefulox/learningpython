#print(dir(5))

def this_function_is_an_object():
  x = 0
  while x < 10:
    x += 1
  return x

print(dir(this_function_is_an_object))