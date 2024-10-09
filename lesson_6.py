# creating a function that can convert all data type to an integer
import json

def int_converter(value):
  try: 
     if type(value) is int:
        print(value)
     elif type(value) is float:
        print(int(value))
     elif type(value) is str:
        number = json.loads(value)
        print(int(number))
     elif value is True:
        print(1)
     elif value is False:
        print(0)
  except(TypeError, ValueError):
        print("can't convert")
     
int_converter(False)
