import random


def read_file(file):
    with open(file, "r") as f:
        return f.read().splitlines()


def write_file(file, data):
    with open(file, "w") as f:
        f.write("\n".join(data))

def main():
    records=[]
    for p in range(1, 6):
        num = 10**p
        output_file = "records_1e{0}.txt".format(p)
        print("Generating {0} records into {1}...".format(num, output_file))
        for i in range(num):
            records.append(str(random.randint(1, 10**p)) + '\t' + str(random.randint(1, 10**p)))
        write_file(output_file, records)
    print("Done")

if __name__ == "__main__":
    main()

