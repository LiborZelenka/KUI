import random
from kuimaze2 import SearchProblem, Map, State


class Agent:
    def __init__(self, environment: SearchProblem):
        self.environment = environment

    def find_path(self) -> list[State]:
        state = self.environment.get_start()
        costs = {state: 0}
        actions = self.environment.get_actions(new_state)

        pathQueue = ()
        last_state = None

        while len(pathQueue) > 0:
            path = pathQueue.pop(0)
            new_state = path(len(path))
            if (len(path) > 1):
                last_state = path(len(path)-1)

            new_cell = self.getCellFromState(new_state)

            for move in self.getAllPossibleMoves(self, path):
                if(len(self.getAllPossibleMoves(self, path)) == 0):
                    break
                path.append(move)
                pathQueue.appenf(path)

            new_state, cost = self.environment.get_transition_result(state, next_action)
            costs[new_state] = costs[state] + cost
            if self.environment.is_goal(state):
                break
            self.environment.render(current_state=state, next_states=[new_state], texts=costs, colors=costs, wait=True)
            state = new_state

        path = [State(0,4), State(1,4)]
        self.environment.render(path=path, wait=True)
        return path

    def getCellFromState(self,state):
        for cell in self.environment.map:
            if (cell.position == state):
                return cell
    
    def getAllPossibleMoves(self, path):
        possibleMoves = () #(State(0,1), State(..),..)
        new_cell = self.getCellFromState(path(len(path)))
        last_cell = self.getCellFromState(path(len(path)-1)) if (len(path) > 1) else None



if __name__ == "__main__":
    MAP = """
    .S...
    .###.
    ...#G
    """
    map = Map.from_string(MAP)
    env = SearchProblem(map, graphics=True)
    agent = Agent(env)
    agent.find_path()
