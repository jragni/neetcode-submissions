class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        has_looped = False

        loop_count = 0
        # looping through each student
        while students:
            # if the student at the front wants the sandwhich,
            if students[0] == sandwiches[0]:
                # remove him and the sandwich
                students.pop(0)
                sandwiches.pop(0)
                loop_count = 0
            # otherwise:
            else:
                # move the person to the back of the line
                student = students.pop(0)
                students.append(student)
                loop_count += 1
            if loop_count >= len(students):
                break
        
        return len(students)

        