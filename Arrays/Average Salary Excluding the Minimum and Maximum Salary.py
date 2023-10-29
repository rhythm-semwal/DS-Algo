class Solution:
    def average(self, salary: List[int]) -> float:
        min, max = float('inf'), float('-inf')
        sum_salary = 0

        for i in salary:
            sum_salary += i
            if i < min:
                min = i
            if i > max:
                max = i
        
        return (sum_salary - min - max) / (len(salary)-2)

    def average1(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        answer = 0
        count = 0
        for i in salary:
            if i != min_salary and i != max_salary:
                answer += i
                count += 1
        
        return answer /count
