class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_q = deque(students)
        sandwich_q = deque(sandwiches)

        loop_counter = 0

        while len(students_q):
            if sandwich_q[0] == students_q[0]:
                students_q.popleft()
                sandwich_q.popleft()
                loop_counter = 0
            else:
                students_q.append(students_q.popleft())
                loop_counter += 1

                if loop_counter >= len(students_q):
                    return len(students_q)
        
        return 0
