class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i :[] for i in range(numCourses)}
        for course, preReqs in prerequisites:
            preMap[course].append(preReqs)

        # 1: 0
        # 0: 1
        visiting = set()
        def dfs(course):
            if preMap[course] == []:
                return True

            if course in visiting:
                return False
            
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

