class ChatMembers(list):
    pass

    def append(self, name):
        list.append(self, name)
        print(f"Hello, {name}!")

    def pop(self, __index: int = ...):
        print(f"Goodbye, {list.pop(self, __index)}!")

    def remove(self, name):
        list.remove(self, name)
        print(f"Goodbye, {name}!")
