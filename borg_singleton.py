class BorgSingleton:
    """
    Design pattern example. Allows state sharing for different instances.
    """
    _shared_borg_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_borg_state
        return obj


borg = BorgSingleton()
borg.shared_variable = "Shared_variable"


class ChildBorg(BorgSingleton):
    pass


childBorg = ChildBorg()
print(childBorg is borg)
print(childBorg.shared_variable)
