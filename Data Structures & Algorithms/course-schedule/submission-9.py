class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        # create a adj_list for the prereques -> [course]: [prereq1,prereq2]
        for c, p in prerequisites:
            if c in adj_list:
                adj_list[c].append(p)
            else:
                adj_list[c] = [p]
            
            if p not in adj_list:
                adj_list[p] = []

        def can_complete(course: int, visited=set(), visiting=set()) -> bool:
            if not adj_list[course]:
                return True
            
            if course in visited:
                return True

            if course in visiting:
                return False
            
            visiting.add(course)
            
            
            for c in adj_list[course]:
                if not can_complete(c, visited, visiting):
                    return False
            
            visiting.remove(course) 
            visited.add(course)

            return True
        
        for course in adj_list.keys():
            if not can_complete(course):
                return False
        
        return True