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

import util

class SearchProblem:
	"""
	This class outlines the structure of a search problem, but doesn't implement
	any of the methods (in object-oriented terminology: an abstract class).

	You do not need to change anything in this class, ever.
	"""

	def getStartState(self):
		"""
		Returns the start state for the search problem.
		"""
		util.raiseNotDefined()

	def isGoalState(self, state):
		"""
		  state: Search state

		Returns True if and only if the state is a valid goal state.
		"""
		util.raiseNotDefined()

	def getSuccessors(self, state):
		"""
		  state: Search state

		For a given state, this should return a list of triples, (successor,
		action, stepCost), where 'successor' is a successor to the current
		state, 'action' is the action required to get there, and 'stepCost' is
		the incremental cost of expanding to that successor.
		"""
		util.raiseNotDefined()

	def getCostOfActions(self, actions):
		"""
		 actions: A list of actions to take

		This method returns the total cost of a particular sequence of actions.
		The sequence must be composed of legal moves.
		"""
		util.raiseNotDefined()


def tinyMazeSearch(problem):
	"""
	Returns a sequence of moves that solves tinyMaze.  For any other maze, the
	sequence of moves will be incorrect, so only use this for tinyMaze.
	"""
	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())
	return  [s, s, w, s, w, w, s, w];

def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:

	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())
	"""
	"*** YOUR CODE HERE ***"
	#   Initialize Stack, format like getSuccessors: state, action list, cost
	frontier = util.Stack()
	explored = []
	#   Push StartState in Stack
	frontier.push((problem.getStartState(),[]))	

	#   Start Seaching below
	while not frontier.isEmpty():
		#	Pop the next node to search
		PacmanState, PacmanAction = frontier.pop()
		#	Skip the node that visited
		if PacmanState in explored:
			continue
		#	Stop searching if goal path is reached
		if problem.isGoalState(PacmanState):
			#	Return list of pacman move direction to goal
			return PacmanAction
		#	Renew the visited node by adding node process searching
		explored.append(PacmanState)
		#	Push all possible node in next search into stack
		for state, direction, cost in problem.getSuccessors(PacmanState):
			frontier.push((state, PacmanAction+[direction]))
	print "Search Fail"

def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	"*** YOUR CODE HERE ***"
	#   Initialize Queue, format like getSuccessors: state, action list, cost
	frontier = util.Queue()
	explored = []
	#   Push StartState in Queue
	frontier.push((problem.getStartState(),[]))
	
	#   Start Seaching below
	while not frontier.isEmpty():
		#	Pop the next node to search
		PacmanState, PacmanAction  = frontier.pop()
		#	Skip the node that visited
		if PacmanState in explored:
			continue
		#	Stop searching if goal path is reached
		if problem.isGoalState(PacmanState):
			#	Return pacman's direction of move to goal in list
			return PacmanAction
		#	Renew the visited node by adding node process searching
		explored.append(PacmanState)
		#	Push all possible node in next search into stack
		for state, direction, cost in problem.getSuccessors(PacmanState):
			frontier.push((state, PacmanAction+[direction]))
	print "Search Fail"

def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	"*** YOUR CODE HERE ***"	
	frontier = util.PriorityQueue()
	explored = []
	#	(PacmanState, PacmanAction, PacmanCost)
	frontier.push((problem.getStartState(), []), 0)

	while not frontier.isEmpty():
		#	Pop the lowest-code node to search
		PacmanState, PacmanAction = frontier.pop()
		#	Skip the node that visited
		if PacmanState in explored:
			continue
		#	Stop searching is goal is found
		if problem.isGoalState(PacmanState):
			#	Return pacman's direction of move to goal in list
			return PacmanAction
		#	Renew the visited node by adding node process searching
		explored.append(PacmanState)

		for state, direction, cost in problem.getSuccessors(PacmanState):
			#	Push successors in step cost in priority, lower search first
			frontier.push((state, PacmanAction+[direction]), problem.getCostOfActions(PacmanAction+[direction]))
	print "Search Fail"

def nullHeuristic(state, problem=None):
	"""
	A heuristic function estimates the cost from the current state to the nearest
	goal in the provided SearchProblem.  This heuristic is trivial.
	"""
	return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""
	frontier = util.PriorityQueue()
	explored = []
	#	(PacmanState, PacmanAction, f(x) = h(x))
	frontier.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))

	while not frontier.isEmpty():
		#	Pop the lowest-code node to search
		PacmanState, PacmanAction = frontier.pop()
		#	Skip the node that visited
		if PacmanState in explored:
			continue
		#	Stop searching is goal is found
		if problem.isGoalState(PacmanState):
			#	Return pacman's direction of move to goal in list
			return PacmanAction
		#	Renew the visited node by adding node process searching
		explored.append(PacmanState)

		for state, direction, cost in problem.getSuccessors(PacmanState):
			#	Push successors in step cost in priority, lower search first
			#	((node position, action list), f(x) = g(x) + h(x))
			frontier.push((state, PacmanAction+[direction]), problem.getCostOfActions(PacmanAction+[direction])+heuristic(state, problem))
	print "Search Fail"

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

from game import Directions
s = Directions.SOUTH
w = Directions.WEST
e = Directions.EAST
n = Directions.NORTH