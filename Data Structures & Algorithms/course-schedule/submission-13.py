class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        #[1] -> 0
        #[0] -> 1
        seen = set()
        def dfs(course):
            if course in seen:
                return False
            seen.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



        