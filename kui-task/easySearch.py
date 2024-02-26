import random
from kuimaze2 import SearchProblem, Map, State


class Agent:
    def __init__(self, environment: SearchProblem):
        self.environment = environment
    def find_path(self) -> list[State]:
        state = self.environment.get_start()
        pathQueue = [] # State(0,4), ..),( .., ..) 

        print(self.getCellFromState(state))

        pathQueue.append(state)
        while True:
            actions = self.environment.get_actions(state)
            
            new_state, cost = self.environment.get_transition_result(state, next_action)
            #costs[new_state] = costs[state] + cost
            if self.environment.is_goal(state):
                break
            self.environment.render(current_state=state, wait=True)
            state = new_state


        self.environment.render(path=path, wait=True)
        return path
    
    def getAllpossibleMoves(self, path):

        row = self.environment.map.height
        col = self.environment.map.width


        print(row, col)

    def getCellFromState(self,state):
        for cell in self.environment.map:
            if (cell.position == state):
                return cell
       

if __name__ == "__main__":
    # Create a Map instance
    MAP = """
    .S...
    .###.
    ...#G
    """
    map = Map.from_string(MAP)
    # Create an environment as a SearchProblem initialized with the map
    env = SearchProblem(map, graphics=True)
    # Create the agent and find the path
    agent = Agent(env)
    agent.find_path()
