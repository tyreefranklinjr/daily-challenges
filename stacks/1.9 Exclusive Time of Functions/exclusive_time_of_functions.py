class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        # Declare variables
        res = [0] * n
        stack = []
        peek = 0
        prev_time = 0

        # First iteration
        ID, status, time_stamp = logs[0].split(":")
        stack.append(int(ID))
        prev_time = int(time_stamp)

        # Loop to organize and assign log structure
        for i in range(1, len(logs)):
            ID, status, time_stamp = logs[i].split(":")
            ID, time_stamp = int(ID), int(time_stamp)
            
            if status == "start":
                
                # Start time stamp
                if stack:
                    res[stack[-1]] += time_stamp - prev_time

                prev_time = time_stamp
                stack.append(ID)

            else:

                # Calculate the size of each function
                res[stack[-1]] += time_stamp - prev_time + 1
                stack.pop()
                prev_time = time_stamp + 1

        return res
