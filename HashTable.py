from typing import List


class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashArray:
    def __init__(self, size: int, c1: int = 1, c2: int = 0):
        self.tab: List[Element and None] = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.size = size

    def hash(self, key, i: int = 0) -> int:
        if isinstance(key, str):
            h_key = 0
            for char in key:
                h_key += ord(char)
            return int((h_key + self.c1*i + self.c2*(i**2)) % self.size)
        else:
            return int((key + self.c1*i + self.c2*(i**2)) % self.size)

    def insert(self, element: Element) -> None:
        num = 0
        start_index = self.hash(element.key, num)
        index = self.hash(element.key, num)
        while self.tab[index]:
            if self.tab[index].key == element.key:
                self.tab[index] = element
                return
            else:
                num += 1
                index = self.hash(element.key, num)
                if index == start_index:
                    raise ValueError("List is already full!")
        self.tab[index] = element
        return

    def search(self, key) -> [int, float, str, None]:
        num = 0
        start_index = self.hash(key, num)
        index = self.hash(key, num)
        while True:
            if self.tab[index]:
                if self.tab[index].key == key:
                    return self.tab[index].value
                else:
                    num += 1
                    index = self.hash(key, num)
                    if index == start_index:
                        return None
            else:
                num += 1
                index = self.hash(key, num)
                if index == start_index:
                    return None

    def remove(self, key) -> None:
        num = 0
        start_index = self.hash(key, num)
        index = self.hash(key, num)
        while True:
            if self.tab[index]:
                if self.tab[index].key == key:
                    self.tab[index] = None
                    return
                else:
                    num += 1
                    index = self.hash(key, num)
                    if index == start_index:
                        raise ValueError("Key was not found")
            else:
                num += 1
                index = self.hash(key, num)
                if index == start_index:
                    raise ValueError("Key was not found")

    def __str__(self):
        string = "["
        for element in self.tab:
            if element:
                string += str(element.key) + ": " + str(element.value) + ", "
        string = string[0: -2] + "]"
        return string

    def display(self) -> None:
        string = "["
        for element in self.tab:
            if element:
                string += str(element.key) + ": " + str(element.value) + ", "
            else: string += str(element) + ', '
        string = string[0: -2] + "]"
        print(string)









