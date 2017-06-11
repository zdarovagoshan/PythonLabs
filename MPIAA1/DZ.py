def read_file(file):
    with open(file, "r") as f:
        return f.read().splitlines()

def write_file(file, data):
    with open(file, "w") as f:
        f.write("\n".join(data))

def sravn(data):
    if (data[0] == data[data.index(' ') + 1]):
        return True
    return False


def find(peoples):
    odinakovki = []
    for people in peoples:
        if (sravn(people)==True):
            odinakovki.append(people)
    return odinakovki

if __name__ == "__main__":
    peoples = read_file("records_1e{0}.txt".format(2))
    output_file = "result.txt"
    write_file(output_file, find(peoples))