# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def solve(student_marks, query_name):
    lista = student_marks[query_name]
    tamanho = len(lista)
    return sum(lista)/tamanho
    

def prints(student_marks, query_name):
    print(student_marks)
    print(query_name)

def entrance():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    return (student_marks, query_name)
    

def main():
    student_marks, query_name = entrance()
    res = solve(student_marks, query_name)
    print("{:.2f}".format(res))
    


if __name__ == '__main__':
    main()
    