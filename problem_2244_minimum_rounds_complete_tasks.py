from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_count = {}

        for i in tasks:
            if i in task_count:
                task_count[i] += 1
            else:
                task_count[i] = 1
        steps = 0

        for _, task_num in task_count.items():
            while task_num > 0:
                # if a task only has 1 then it cant be done in 2 or 3
                if task_num == 1:
                    return -1
                # Greedy algos will always take the 3 over 2
                # However 4 is a special case where 2 needs to be taken twice
                if task_num == 4:
                    steps += 2
                    task_num = 0

                elif task_num >= 3:
                    steps += 1
                    task_num -= 3
                # This is essentially task_num == 2
                else:
                    steps += 1
                    task_num -= 2

        return steps


"""
Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in 
each round, you can only complete either 2 or 3 tasks of the same difficulty level. 
Hence, you cannot complete all the tasks, and the answer is -1.
"""

if __name__ == "__main__":
    solution = Solution()
    result = solution.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4])

    print(result)

    # print(result)
