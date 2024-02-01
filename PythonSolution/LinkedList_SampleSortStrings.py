from LinkedList import LinkedList

ll = LinkedList()

ll.add_first("Per")
ll.add_first(123)
ll.add_first(37.3)
ll.add_first(37.7)
ll.add_first(".")
ll.add_first('2')
ll.add_first(739)
ll.add_first("Ib")

print("Original list:")
ll.print()
print()

ll.sort()
print("Sorted list:")
ll.print()
print()

