class Element:
    def __init__(self, d):
        self.data = d
        self.next = None

    # is self less that el
    def is_greater(self, el):
        if type(self.data) == type(el.data):
            return self.data > el.data
        else:
            return str(self.data) > str(el.data)


class LinkedList:

    def __init__(self):
        self.__first = None

    def __str__(self):
        return "LinkedList with " + str(self.count()) + " elements"

    def count(self):
        counter = 0
        ref = self.__first
        while ref is not None:
            counter += 1
            ref = ref.next
        return counter

    def add_first(self, data):
        el = Element(data)
        if self.__first is None:
            self.__first = el
        else:
            el.next = self.__first
            self.__first = el

    def remove_first(self):
        if self.__first is not None:
            self.__first = self.__first.next

    def __str__(self):
        ref = self.__first
        output = ""
        while ref is not None:
            output = output + str(ref.data) + ", "
            ref = ref.next
        return output

    def print(self):
        print(self)

    def sort(self):
        if self.__first is not None:
            swapped = False
            ref = self.__first
            while ref.next is not None:
                if ref.is_greater(ref.next):
                    tmp = ref.data
                    ref.data = ref.next.data
                    ref.next.data = tmp
                    swapped = True
                ref = ref.next
            if swapped:
                self.sort()

    def get_first(self):
        if self.__first is None:
            return None
        else:
            return self.__first.data
