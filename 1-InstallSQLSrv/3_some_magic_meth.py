###

class MyClass:
    def __init__(self, name) -> None:
        self.name = name
        print('__init__')
    def __enter__(self):
        print('__enter__')
        return self
    def __exit__(self, ex_type, ex_value, ex_tb):
        print("__exit__")
    def __del__(self):
        print("__del__")
    def __str__(self):
        return self.name
    def __repr__(self) -> str:
        return f'''{__class__.__name__}('{self.name}')'''

o1 = MyClass('o1')   
print(o1)
print(o1.__class__.__name__)
print(str(o1))
print(repr(o1))
print()

with MyClass('obj1') as o:
    print(f'''I'm {str(o)}, an instance {repr(o)}''')

var = input('Waiting till press enter...')