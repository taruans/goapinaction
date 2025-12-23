# Dosya: planner.py
import heapq
from typing import List, Optional
from models import WorldState, GoapAction # <--- models.py'ı çağırır

def calculate_plan(start_state: WorldState, goal_state: WorldState, actions: List[GoapAction]) -> Optional[List[GoapAction]]:
    # (cost, current_state_dict, plan_list)
    # State'i hash'lenebilir yapmak için frozenset'e çeviriyoruz veya string yapıyoruz
    queue = [(0, start_state, [])]
    visited = set()

    while queue:
        current_cost, current_state, plan = heapq.heappop(queue)

        # Hedef kontrolü
        matches_goal = True
        for k, v in goal_state.items():
            if current_state.get(k) != v:
                matches_goal = False
                break
        
        if matches_goal:
            return plan

        state_key = str(sorted(current_state.items()))
        if state_key in visited:
            continue
        visited.add(state_key)

        for action in actions:
            if action.is_valid(current_state):
                new_state = action.apply(current_state)
                new_plan = plan + [action]
                heapq.heappush(queue, (current_cost + action.cost, new_state, new_plan))
                
    return None
