class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        cnt = 0

        while sandwiches and students:

            if cnt > len(sandwiches): break

            if students[0] == sandwiches[0]:
                cnt = 0
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students[0])
                students.pop(0)
                cnt += 1

        return len(students)
            
