# Dosya: models.py
from typing import Dict, Any, Callable, List
from pydantic import BaseModel, Field

# Type Alias
WorldState = Dict[str, Any]

class GoapAction(BaseModel):
    name: str
    cost: int
    preconditions: WorldState
    effects: WorldState
    handler: Callable[[Any], Any] = Field(exclude=True) # Pydantic serileştirmesin diye

    def is_valid(self, state: WorldState) -> bool:
        """State, preconditionları karşılıyor mu?"""
        for key, value in self.preconditions.items():
            if state.get(key) != value:
                return False
        return True

    def apply(self, state: WorldState) -> WorldState:
        """Sanal state oluşturur"""
        new_state = state.copy()
        new_state.update(self.effects)
        return new_state
