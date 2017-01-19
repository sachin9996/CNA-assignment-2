INF = 10000000

class Graph:
	def __init__(self, n = 0):
		self.n = n
		self.adj_list = [{} for _ in range(n)]

	def add_edge(self, u, v, w):
		self.adj_list[u][v] = w

	def weight(self, u, v):
		try:
			return self.adj_list[u][v]
		except KeyError:
			return INF

	def BFS(self, s):
		'''
		Performs a BFS on the graph starting at the vertex s.
		Assumes unweighted edges. Returns a list of minimum distances
		from the vertex s. The distance is INF if unreachable from s.
		'''
		n = self.n
		result = [INF for _ in range(n)]
		visited = [False for _ in range(n)]
		dist = 0
		result[s] = dist
		visited[s] = True
		Q = [s]
		while len(Q) != 0:
			dist += 1
			frontier = []
			for u in Q:
				for v in self.adj_list[u]:
					if visited[v] is False:
						frontier.append(v)
						visited[v] = True
						result[v] = dist
			Q = frontier
		return result

	def dijkstra(self, s):
		import heapq
		n = self.n
		result = [INF for _ in range(n)]
		visited = [False for _ in range(n)]
		result[s] = 0
		Q = []
		for i in range(n):
			if i != s:
				Q.append((INF, i))
			else:
				Q.append((0, s))
		for i in range(n):
			least_distance, u = heapq.heappop(Q)
			visited[u] = True
			for v in self.adj_list[u]:
				if not visited[v]:
					d = result[u] + self.weight(u, v)
					if d < result[v]:
						result[v] = d
						heapq.heappush(Q, (d, v))
		return result

	
	def diameter(self):
		n = self.n
		result = 0
		for i in range(n):
			result = max(result, max(self.BFS(i)))
		return result


	def average_path_length(self):
		n = self.n
		count = 0
		total = 0.0
		for i in range(n):
			distances = self.BFS(i)
			for value in distances:
				if value != INF and value != 0:
					count += 1
					total += value
		average = total * 1.0 / count
		return average


	def density(self):
		n = self.n
		edges = 0
		for i in range(n):
			edges += len(G.adj_list[i])
		edges /= 2
		density = edges * 2.0 / (n * (n - 1))
		return density

	def degree_centrality(self):
		n = self.n
		edges = 0
		for i in range(n):
			edges += len(G.add_edge[i])
		return edges * 1.0 / n

'''
def clustering_coeff(G):
	n = len(G)
	cc = []
	for i in range(n):
		count = 0
		for u in G[i]:
			for v in G[i]:
				if v in G[u]:
					count += 1
		nbd = len(G[i])
		try:
			cc.append(count * 1.0 / (nbd * (nbd - 1)))
		except ZeroDivisionError:
			cc.append(0)
	return sum(cc) * 1.0 / len(cc)