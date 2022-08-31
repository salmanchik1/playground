class Singleton:
    """
    An example of singleton design pattern using.
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

singleton = Singleton()
new_singleton = Singleton()

print(singleton is new_singleton)
singleton.single_variable = "Singleton variable"
print(new_singleton.single_variable)
