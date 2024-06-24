from abc import ABC, abstractmethod

class Hittable(ABC):
    @abstractmethod
    def hit(self, ray, t_min, t_max, rec):
        pass