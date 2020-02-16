import abc
from codecs import register

class Double(metaclass=abc.ABCMeta):
    pass

## This actually registers float as a virtual subclass. 
Double.register(float)

print(issubclass(float, Double))
print(isinstance(1.33333, Double))

@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass

print(issubclass(Double64, Double))  # True