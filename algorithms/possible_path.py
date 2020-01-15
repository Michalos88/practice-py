
"""Determine weather there is a possible path"""
# Technical Interview with Applied Intuition

# You are given a 2D grid with r rows and c cols, and a number of static obstacles each
# with an (x, y) position. You are then given one actor (a vehicle - designated R),
# with a start point and a destination. Determine whether it is possible for
# the vehicle to reach its destination without colliding with the wall or any obstacles (x).

# This is an example of the start state and the intended end state:

#---#---#---#           #---#---#---#
#   |   | R |           #   |   |   |
#---#---#---#           #---#---#---#
#   | x | x |    ->     #   | x | x |
#---#---#---#           #---#---#---#
#   |   |   |           #   |   | R |
#---#---#---#           #---#---#---#


class Enviorment(object):

    def __init__(self,
                 height,
                 width,
                 obstacles):
        self.height = height
        self.width = width
        self.obstacles = obstacles

        self.map = list()

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacles


class Agent(object):
    def __init__(self,
                 start,
                 stop,
                 enviorment):
        self.start = start
        self.stop = stop
        self.enviorment = enviorment
        self.prev_steps = set()
        self.path_feasability = False

    def is_possible_path(self):

        # input check
        self.dfs(self.start[0], self.start[1])
        result = self.path_feasability
        self.reset()
        return result

    def dfs(self, x, y):
        if (x, y) == self.stop:
            self.path_feasability = True

        self.prev_steps.add((x, y))

        # move up
        if y - 1 >= 0 and not self.enviorment.is_obstacle(x, y-1) and\
                (x, y-1) not in self.prev_steps:
            self.dfs(x, y-1)

        # move down
        if y + 1 < self.enviorment.height and\
                not self.enviorment.is_obstacle(x, y+1) and\
                (x, y+1) not in self.prev_steps:
            self.dfs(x, y+1)

        # move left
        if x - 1 >= 0 and not self.enviorment.is_obstacle(x-1, y) and\
                (x-1, y) not in self.prev_steps:
            self.dfs(x-1, y)

        # move right
        if x + 1 < self.enviorment.width and\
                not self.enviorment.is_obstacle(x+1, y) and\
                (x+1, y) not in self.prev_steps:
            self.dfs(x+1, y)

    def reset(self):
        self.path_feasability = False
        self.prev_steps = set()


class Tests:
    def run_all(self):
        self.is_obstacle()
        self.is_possible_path()

    def is_obstacle(self):
        env = Enviorment(3, 3, [(1, 1), (1, 2)])
        assert env.is_obstacle(1, 1)
        assert env.is_obstacle(1, 2)
        print('is_obstacle_test: passed')

    def is_possible_path(self):
        # Case 1: There is a possible path
        env = Enviorment(3, 3, [(1, 1), (2, 1)])
        agent = Agent((2, 0), (2, 2), env)
        assert agent.is_possible_path()

        env = Enviorment(3, 3, [(1, 1), (2, 1)])
        agent = Agent((2, 0), (2, 2), env)
        assert agent.is_possible_path()

        # Case 2: There is no possible path
        env = Enviorment(3, 3, [(0, 1), (1, 1), (2, 1)])
        agent.enviorment = env
        assert not agent.is_possible_path()
        print('is_possible_path_test: passed')


if __name__ == "__main__":
    tests = Tests()
    tests.run_all()
