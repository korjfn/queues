q = []
# Enqueue
q.append("a")
q.append("b")
q.append("c")

print("queue: ", q)

# dequeue

element = q.pop(0)
print("dequeue", element)

# peak
frontelement = q[0]
print("peak", frontelement)

#IsEmpty
isEmpty = not bool(q)
print("isEmpty", isEmpty)

# Size
print("size", len(q))