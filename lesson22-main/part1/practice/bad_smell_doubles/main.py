class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted_func(self):
        return sorted(self.lst, reverse=False)


if __name__ == "__main__":
    some_instance = SomeClass()
    print(some_instance.sorted_func())
