class My_Int_Error(Exception):
    def __init__(self, if_obj, element):
        self.IF_object = if_obj
        self.element = element
    def __str__ (self):
        return self.element + ' is not an integer'
class IList(list):
    def append(self, element):
        if not isinstance(element, (int)):
            raise My_Int_Error (self, element)
        return super(IList, self).append(element)

MyList = IList()
MyList.append(44)
MyList.append(200)
# MyList.append("Hello World")
print(MyList)