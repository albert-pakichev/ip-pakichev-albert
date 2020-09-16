class ListTransaction:
    def __init__(selfself,thrlist):
        self.thelist = thelist

    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy

    def __exit__(selfself,type,value,tb):
        if type is None:
            self.thelist[:] = self.workingcopy
        return False

items = [1,2,3]
with ListTransaction(items) as working:
    working.append(4)
    working.append(5)
    print(items)

try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("Немного смошенничаем")
except: RuntimeError
pass

    print(items)