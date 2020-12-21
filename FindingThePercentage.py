if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    l = list(student_marks[query_name])
    i = len(l)
    s = sum(l)
    k = s/i
    print('%.2f'%k)
