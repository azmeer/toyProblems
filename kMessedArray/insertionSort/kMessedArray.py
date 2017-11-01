"""
  From Pramp Interview #1

  Inputs: numbers, k
  Outputs: sorted(numbers)

Straightforward solution: sorted(numbers) - but this doesn't take into account input is mostly sorted
Actual solution: use incremental insertion sort over the last k elements

"""

def swap(numbers, a, b):
  temp = numbers[a]
  numbers[a] = numbers[b]
  numbers[b] = temp

def insertion_sort(numbers, min = 0, max = None):
  max = len(numbers) if max == None else max
  for idx_up in range(min, max):
    insert_me = idx_up
    for idx_down in range(idx_up - 1, min - 1, -1):
      print idx_up, idx_down, insert_me
      if (numbers[idx_down] > numbers[insert_me]):
        swap(numbers, idx_down, insert_me)
        insert_me = idx_down
      else:
        print "Inserting ", numbers[insert_me], " into numbers[", insert_me, "]"
        break
  return numbers

def sort_k_messed_array(arr, k):
  for index, number in enumerate(arr):
    insertion_sort(arr, index, min(index + k + 1, len(arr)))
  return arr  

#arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
#k = 2
#print(arr)
#arr = insertion_sort(arr, 2, 5)
#print(arr)
#print(sort_k_messed_array(arr, k))
