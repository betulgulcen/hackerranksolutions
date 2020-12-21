if __name__ == '__main__':
    students= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key = lambda x: x[1])
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    desired_students = []
    
    for i in students:
        if i[1] == second_lowest_score:
            desired_students.append(i[0])
    print("\n".join(sorted(desired_students)))
