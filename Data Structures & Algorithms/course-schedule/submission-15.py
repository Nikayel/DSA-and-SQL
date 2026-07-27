class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for _ in range(numCourses)]
        for crs,pre in prerequisites:
            prereqs[crs].append(pre)
        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if prereqs[course] == []:
                return True
            seen.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            prereqs[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
