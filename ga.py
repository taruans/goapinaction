from typing import List, Dict, Callable, Any
from pydantic import BaseModel

# Dünyanın durumu (Örn: 'user_authenticated': True, 'report_generated': False)
WorldState = Dict[str, Any]

class GoapAction(BaseModel):
    name: str
    cost: int  # Bu eylemin maliyeti (Süre, para veya karmaşıklık)
    preconditions: WorldState  # Bu eylemi yapabilmek için ne lazım?
    effects: WorldState        # Bu eylem yapıldıktan sonra dünya nasıl değişir?
    
    # LangChain Tool veya Agent burada çağrılacak
    handler: Callable[[Any], Any] 

    def is_valid(self, state: WorldState) -> bool:
        """Mevcut state, precondition'ları karşılıyor mu?"""
        for key, value in self.preconditions.items():
            if state.get(key) != value:
                return False
        return True

    def apply(self, state: WorldState) -> WorldState:
        """Eylemin etkilerini sanal olarak uygula (Planlama aşaması için)"""
        new_state = state.copy()
        new_state.update(self.effects)
        return new_state
