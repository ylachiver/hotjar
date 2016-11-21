#!/usr/bin/env python

seq = [2, 3, 4]

def check_seq_in_array(a):
   # Convert int array and seq to str
   # Check if seq str is in int array str
   int_array_str = ','.join([str(x) for x in a])
   seq_str = ','.join([str(x) for x in seq])
   return seq_str in int_array_str

def main():
  int_array = [1, 2, 3, 4, 6]
  print check_seq_in_array(int_array)

if __name__ == '__main__':
    main()
