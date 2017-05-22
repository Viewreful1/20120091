# BFS DFS # https://www.acmicpc.net/problem/1260

def initializeEdgeMap(n):
	edgeMap = []
	for i in range(0,n):
		edgeMap.append([0]*n)
	return edgeMap

def makeEdge(edgeMap, fromNode, toNode):
	edgeMap[fromNode-1][toNode-1] = 1
	edgeMap[toNode-1][fromNode-1] = 1


def dfs(edgeMap, v):
	visited = [0] * len(edgeMap)
	stack = [v-1]
	path = []
	while len(stack) > 0:
		fromNode = stack[-1]
		if visited[fromNode] == 0:
			visited[fromNode] = 1
			path.append(fromNode+1)
		noMore = True
		for toNode in range(len(edgeMap[fromNode])):
			if (not fromNode == toNode) and (edgeMap[fromNode][toNode] == 1) and visited[toNode] == 0:
				stack.append(toNode)
				noMore = False
				break
		if noMore == True:
			stack.pop()
	return " ".join(str(x) for x in path)


def bfs(edgeMap, v):
	visited = [0] * len(edgeMap)
	queue = [v-1]
	visited[v-1] = 1
	path = []
	while len(queue) > 0:
		fromNode = queue.pop(0)
		path.append(fromNode+1)
		for toNode in range(len(edgeMap[fromNode])):
			if (not fromNode == toNode) and (edgeMap[fromNode][toNode] == 1) and visited[toNode] == 0:
				visited[toNode] = 1
				queue.append(toNode)
	return " ".join(str(x) for x in path)


def run():
	n,m,v = map(int,input().split())
	edgeMap = initializeEdgeMap(n)
	for _ in range(m):
		fromNode, toNode = map(int,input().split())
		makeEdge(edgeMap, fromNode, toNode)
	print(dfs(edgeMap, v))
	print(bfs(edgeMap, v))

def testRun(testSource):
	lines = testSource.split("\n")
	firstLine = lines.pop(0)	
	otherLines = lines
	test(firstLine, otherLines)

def test(firstLine, otherLines):
	n,m,v = map(int,firstLine.split())
	edgeMap = initializeEdgeMap(n)
	for eachLine in otherLines:
		fromNode, toNode = map(int, eachLine.split())
		makeEdge(edgeMap, fromNode, toNode)
	print(dfs(edgeMap, v))
	print(bfs(edgeMap, v))

testSource = \
"""\
4 5 1
1 2
1 3
1 4
2 4
3 4"""
# testRun(testSource)
 
run()