import random
import numpy as np
import queue

from gridutil import next_direction, next_loc, DIRECTIONS, generate_locations


class Agent:
    # 📝 Stan Agenta i Akcje (Notatki do Zadania 5)

    # 1. Jakie są teraz możliwe stany agenta? Jak je zapisać?
    # Stan jest rozszerzony: lokalizacja i kierunek są kluczowe.
    # Zapis: Stan = ((x, y), dir)
    # - (x, y): krotka (tuple) z lokalizacją agenta (np. (5, 7)).
    # - dir: kierunek (np. 'N', 'E', 'S', 'W').

    # 2. Jak poszczególne akcje zmieniają stan agenta?
    # Akcje mają różne koszty (czas) i zmieniają stan:
    # - 'turnleft' (Koszt: 5): Zmienia kierunek w lewo. Lokalizacja się NIE ZMIENIA.
    # - 'turnright' (Koszt: 2): Zmienia kierunek w prawo. Lokalizacja się NIE ZMIENIA.
    # - 'forward' (Koszt: 1): Zmienia lokalizację o 1 pole w dir. Jeśli trafia na ścianę, lokalizacja zostaje ta sama (ale koszt i tak jest ponoszony!). Kierunek się NIE ZMIENIA.

    def __init__(self, size, walls, loc, dir, goal):
        self.size = size
        self.walls = walls
        self.locations = list({*generate_locations(self.size)}.difference(self.walls))
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.goal = goal

        self.t = 0
        self.path, self.actions = self.find_path()

    def __call__(self):
        if not self.actions:
            return 'N'

        action = self.actions.pop(0)

        return action

    def find_path(self):
        action_costs = {'turnleft': 5, 'turnright': 2, 'forward': 1}
        actions_list = ['turnleft', 'turnright', 'forward']

        start_state = (self.loc, self.dir)
        goal_loc = self.goal

        min_costs = {start_state: 0}
        predecessors = {start_state: None}

        pq = queue.PriorityQueue()
        pq.put((0, start_state))

        final_goal_state = None

        while not pq.empty():
            current_cost, current_state = pq.get()
            current_loc, current_dir = current_state

            if current_loc == goal_loc:
                final_goal_state = current_state
                break

            if current_cost > min_costs.get(current_state, float('inf')):
                continue

            for action in actions_list:
                cost = action_costs[action]
                new_dir = current_dir
                new_loc = current_loc

                if action == 'turnleft':
                    new_dir = next_direction(current_dir, -1)
                elif action == 'turnright':
                    new_dir = next_direction(current_dir, 1)
                elif action == 'forward':
                    temp_loc = next_loc(current_loc, current_dir)
                    if temp_loc in self.locations:
                        new_loc = temp_loc

                new_state = (new_loc, new_dir)
                new_cost = current_cost + cost

                if new_cost < min_costs.get(new_state, float('inf')):
                    min_costs[new_state] = new_cost
                    predecessors[new_state] = (current_state, action)
                    pq.put((new_cost, new_state))

        path_states = []
        actions = []
        current = final_goal_state

        if current is not None:
            while current != start_state:
                prev, action = predecessors[current]
                path_states.append(current)
                actions.append(action)
                current = prev

            path_states.append(start_state)
            path_states.reverse()
            actions.reverse()

            path = [state[0] for state in path_states]

        return path, actions

    def get_path(self):
        return self.path