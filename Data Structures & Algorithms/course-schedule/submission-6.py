class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses #number of edges pointing to that item
        q = deque()
        adj = [[] for i in range(numCourses)]
        for crs,pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre]+=1
        
        for item in range(len(indegree)):
            if indegree[item] == 0:
                q.append(item)
        finished = 0
        while q:
            node = q.popleft()
            finished+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return finished == numCourses