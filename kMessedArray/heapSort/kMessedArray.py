"""
  From Pramp interview #1

  Inputs: numbers, k
  Outputs: sorted(numbers)

Straightforward solution: sorted(numbers) - but this doesn't take into account input is mostly sorted
Actual solution: use incremental heap sort over the last k elements

  build k-sized min heap
    heap_pushpop()
        returns min element after pushing a new element on
        returns None if heap has < k elements
"""

import heapq

class K_heap:
  def __init__(self, k):
    self.heap = []
    self.k = k

  def push_pop(self, new_el):
    if len(self.heap) < self.k:
      heapq.heappush(self.heap, new_el)
      return None
    else:
      return heapq.heappushpop(self.heap, new_el)
    
  def pop(self):
    return heapq.heappop(self.heap)

def sort_k_messed_array(arr, k):
  k_heap = K_heap(k)
  for index, number in enumerate(arr):
    arr[max(0, index - k)] = k_heap.push_pop(number)
  for index in range(len(arr) - k, len(arr)):
    arr[index] = k_heap.pop()
  return arr

