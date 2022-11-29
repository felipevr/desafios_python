#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def main(records):
    gd = {}
    gs = []
    for s in records:
        key = s[1]
        if not key in gd:
            gd[key] = []
        gd[key].append(s[0])
        gs.append(key)
    gs = [*set(gs)] #remove duplicates
    gs.sort()
    second = gs[1]
    gd[second].sort()
    for s in gd[second]:
        print(s)
    


# if __name__ == '__main__':
#     records = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])
#     main(records)

# records = [["chi", 20.0], ["beta", 50.0], ['alpha', 50.0]]
# main(records)

# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# main(students)

students = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
main(students)