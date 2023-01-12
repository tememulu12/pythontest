import heapq
import  functools

heap = []
# heapq.heappush()
# heapq.heappush()
# heapq.heappush()
# heapq.heappush()
# heapq.heappush()

push = functools.partial(heapq.heappush, heap)
smallest = functools.partial(heapq.nsmallest, iterable=heap)

push(1)
push(3)
push(5)
push(2)
push(4)
print(smallest(3))
print(heap)
