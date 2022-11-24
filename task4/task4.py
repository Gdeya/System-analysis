import math

def serialise_csv(path: str):
    return open(path, mode = 'r').read()
def process_csv(serialised_csv: str):
    data = serialised_csv.splitlines()
    return [line.split(",") for line in data]
def task(serialised_csv: str):
    matrix = process_csv(serialised_csv)
    #Прямое управление
    r1 = []
    #Прямое подчинение
    r2 = []
    #Опосредственное управление
    r3 = []
    #Опосредственное подчинение
    r4 = []
    #Соподчинение
    r5 = []
    for vec in matrix:
        if vec[0] not in r1:
            r1.append(vec[0])
    for vec in matrix:
        if vec[1] not in r2:
            r2.append(vec[1])
    for vec in matrix:
        for vec1 in matrix:
            if vec[0] not in r3 and vec1[0]==vec[1]:
                r3.append(vec[0])
    for vec in matrix:
        for vec1 in matrix:
            if vec[1] not in r4 and vec1[1]==vec[0]:
                r4.append(vec[1])
    for vec in matrix:
        for vec1 in matrix:
            if vec[1] not in r5 and vec1[0]==vec[0] and vec1!=vec:
                r5.append(vec[1])
    vertices = [] # количество вершин
    for x in matrix:
        for y in x:
            if y not in vertices:
                vertices.append(y)
    vertices.sort()
    results = []
    for v in vertices:
        results.append([])
    
    for v in vertices:
        results[int(v)-1].append(r1.count(v))
        results[int(v)-1].append(r2.count(v))
        results[int(v)-1].append(r3.count(v))
        results[int(v)-1].append(r4.count(v))
        results[int(v)-1].append(r5.count(v))

    enthropy = 0
    for j in range(len(vertices)):
        for i in range(5):
            if results[j][i] != 0:
                enthropy += (results[j][i] / (len(vertices) - 1)) * math.log(results[j][i] / (len(vertices) - 1), 2)

    return -enthropy
def main():
    try:
        path = 'csv_sample.csv'
        csv = serialise_csv(path)
        print(task(csv))
    except Exception as error:
        print(error)
        
main()