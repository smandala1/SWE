
def Vowels(str):
  v = 0
  c = 0
  for i in str:
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
      v = v + 1
    else: 
      c = c + 1
  if v > c: 
    return(True) 
  elif c > v:
      return (False)
  else: return None 
  

print(Vowels("Shubhada"))

import math
def volume (r,h):
 volume = math.pi*pow(r,2)*h
 return volume 


 
def combine(str):
 things = ','.join(str)
 return (things)


import os
def combined(v):
 a = ''
 for t in v:
  a = a + combine(t)
  a = a + ','
 a = a[:-1]
 f = open("Question4.txt", "w")
 f.write(a)
 f.close()
 path = os.path.abspath('Question4.txt')
 return path 



from csv import reader
def reread(file):
 with open(file, 'r') as read_obj:
  csv_reader = reader(read_obj)
  list_of_rows = list(csv_reader)
  return(list_of_rows)


def two_num(x,y):
 try:
  return (x/y)
 except ZeroDivisionError:
  print("Warning the second number is 0")


def remove_duplicate(list_of_intergers):
   return list(set(list_of_intergers))


import os
def create_new_file():
 current_directory = os.getcwd()
 final_directory = os.path.join(current_directory, 'hw3-folder')
 if not os.path.exists(final_directory):
  os.makedirs(final_directory)

