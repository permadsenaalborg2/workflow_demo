from LinkedList import LinkedList

ll = LinkedList()

ll.add_first(34)
ll.add_first(12)

print(ll)
ll.print()
print()

ll.add_first(56)
ll.add_first(43)

print(ll)
ll.print()
print()

for t in range(4):
    print("t: " + str(t))
    ll.remove_first()
    print(ll)
    ll.print()
    print()
