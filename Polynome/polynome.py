from dataclasses import dataclass
from abc import ABC , abstractmethod

class MaClasse(ABC):
    
    @abstractmethod
    def fonction(self):
        pass
    
@dataclass
class polynome(MaClasse):
    x: int
    
    @classmethod
    def fonction(cls, x):
        var = (x ** 2 - 2 * x + 1)
        return var
    
vv = polynome.fonction(6)
print(vv)
    