"""
  bucket_sort.py

  Bucket sort is a non-comparative sort that has a linear asympotic time
  complexity on average
"""

import time

def insertion_sort(array):
  for i in range(1, len(array)):
    value = array[i]
    j = i - 1
    while j >= 0 and array[j] > value:
        array[j+1] = array[j]
        j -= 1
    array[j + 1] = value

def toIndex(n):
  return (n - 1) // 10
    
def bucket_sort(array, n):
  buckets = [[] for _ in range(n)]
  
  for a in array:
      buckets[toIndex(a)].append(a)
    
  for bucket in buckets:
      insertion_sort(bucket)
  
  return [element for bucket in buckets for element in bucket]

### TESTING

COMPARE_COUNTER = 0
EXCHANGE_COUNTER = 0

def insertion_sort_count(array):
  global COMPARE_COUNTER, EXCHANGE_COUNTER
  for i in range(1, len(array)):
    value = array[i]
    j = i - 1
    while j >= 0 and array[j] > value:
        COMPARE_COUNTER += 2
        array[j+1] = array[j]
        EXCHANGE_COUNTER += 1
        j -= 1
    array[j + 1] = value
    EXCHANGE_COUNTER += 1

def bucket_sort_count(array, n):
  buckets = [[] for _ in range(n)]
  
  for a in array:
      buckets[toIndex(a)].append(a)
  
  for bucket in buckets:
      insertion_sort_count(bucket)
  
  return [element for bucket in buckets for element in bucket]

### 

def main():
  with open("data10000.", "r") as file:
      
    numbers = file.readlines()
    numbers = [int(n) for n in numbers]

    start = time.time() 
    sorted = bucket_sort(numbers, 10)
    end = time.time() 

    print("Elapsed time", end - start)

    bucket_sort_count(numbers, 10)
    print("Compares:", COMPARE_COUNTER)
    print("Exchanges:", EXCHANGE_COUNTER)

main()
