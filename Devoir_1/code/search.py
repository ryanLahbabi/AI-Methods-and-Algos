# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from custom_types import Direction
from pacman import GameState
from typing import Any, Tuple,List
import util

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self)->Any:
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state:Any)->bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state:Any)->List[Tuple[Any,Direction,int]]:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions:List[Direction])->int:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem:SearchProblem)->List[Direction]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem:SearchProblem)->List[Direction]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    LIFO --> stack
    """

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 1 ICI
    '''

    stack = util.Stack()
    stack.push((problem.getStartState(), [], 0))
    visited = set()

    while not stack.isEmpty():
        state, actions, cost = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for nextState, nextAction, nextCost in problem.getSuccessors(state):
                newActions = list(actions)
                newActions.append(nextAction)
                stack.push((nextState, newActions, cost + nextCost))


def breadthFirstSearch(problem:SearchProblem)->List[Direction]:
    """Search the shallowest nodes in the search tree first."""

    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 2 ICI
            FIFO --> queue
    '''
    queue = util.Queue()
    queue.push((problem.getStartState(), [], 0))
    visited = set()

    while not queue.isEmpty():
        state, actions, cost = queue.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)
            for nextState, nextAction, nextCost in problem.getSuccessors(state):
                newActions = list(actions)
                newActions.append(nextAction)
                queue.push((nextState, newActions, cost + nextCost))



    util.raiseNotDefined()

def uniformCostSearch(problem:SearchProblem)->List[Direction]:
    """Search the node of least total cost first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 3 ICI
    '''

    current_state = problem.getStartState()

    # initializing a stack for the successors
    successor_FIFO = util.PriorityQueue()
    successor_FIFO.push((current_state, [], 0), 0)
    visited = []

    while successor_FIFO.isEmpty() == False:  # as long as the stack is not empty
        current_state = successor_FIFO.pop()  # pop the last state of the stack
        if current_state[0] not in visited:
            if problem.isGoalState(current_state[0]):  # verify if this state is the goal state
                return current_state[1]  # if yes, return the action to this state

            else:  # if not,
                successors_list = problem.getSuccessors(current_state[0])  # get the list of successors
                for successor in successors_list:  # for each element in the successors list fetched

                    if successor[0] not in visited:
                        action = list(current_state[1])
                        action.append(successor[1])
                        cost = float(current_state[2] + successor[2])
                        successor_FIFO.push((successor[0], action, cost), cost)
                visited.append(current_state[0])

    util.raiseNotDefined()

def nullHeuristic(state:GameState, problem:SearchProblem=None)->List[Direction]:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem:SearchProblem, heuristic=nullHeuristic)->List[Direction]:
    """Search the node that has the lowest combined cost and heuristic first."""
    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 4 ICI
    '''

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
