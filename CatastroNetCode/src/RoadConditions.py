from enum import Enum

class RoadConditions(Enum):
    NORMAL = 0
    STORM = 1
    FLOOD= 2
    FOG = 3
    DESTROYED = 4

    def __str__(self):
        # Return a user-friendly string representation of the enum
        return self.name

    def __repr__(self):
        # Return a more developer-friendly representation of the enum
        return f"RoadConditions.{self.name}"