def serialise_csv(path: str):
    return open(path, mode = 'rb').read()
def process_csv(serialised_csv: str):
    data = serialised_csv.decode('utf-8').splitlines()
    return [line.split(",") for line in data]
def task(serialised_csv: str):
    matrix = process_csv(serialised_csv)
    answer=[]
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
    answer.append(r1)
    answer.append(r2)
    answer.append(r3)
    answer.append(r4)
    answer.append(r5)
    return answer
def main():
    try:
        path = 'csv_sample.csv'
        csv = serialise_csv(path)
        print(task(csv))
    except Exception as error:
        print(error)
        
main()