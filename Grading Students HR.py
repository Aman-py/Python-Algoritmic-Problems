def solve(grades):
    i = 0
    while i != n:
        if grades[i] >= 38:
            if grades[i]%5 >= 3:
                print(((grades[i]//5)+1)*5)
                i = i+1
            else:
                print(grades[i])
                i = i+1
        else:
            print(grades[i])
            i = i+1

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
