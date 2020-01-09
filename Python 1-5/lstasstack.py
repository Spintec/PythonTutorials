#Using lists as stacks
stack=[1,2,3,4]

stack.append(5)
stack.append("last")
print(stack)

stack.pop()
print(stack)

stack.pop(0)
print(stack)

#Using lists as queue

from collections import deque

queue=deque(["Eric","John","Michael"])
queue.append("Scarry")
queue.append("Terry")

queue.popleft()
queue.pop()
print(queue)
