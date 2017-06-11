from generate import read_file, write_file

def insertion_sort( array ):
    array = [p.split(' ') for p in array]
    for i in range(len( array )):
        tmp = array[i]
        k = i
        while k > 0 and tmp[0] <= array[k - 1][0]:
            if tmp[0]==array[k-1][0]:
                if int(tmp[2])<int(array[k-1][2]):
                    array[k]=array[k-1]
            else:
                array[k] = array[k - 1]
            k -= 1
        array[k] = tmp
    check = list()
    for x in array:
        x = ' '.join(x)
        check.append(x)
    return check

def bucket_sort(lst):
    bucket, bucket1, bucket2 = [], [], []  # The three empty buckets
    # Populating the buckets with the list elements
    lst = [p.split(' ') for p in lst]
    for i in range(len(lst)):
        if lst[i][0][0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            bucket.append(lst[i])
        elif lst[i][0][0] in ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']:
            bucket1.append(lst[i])
        elif lst[i][0][0] in ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            bucket2.append(lst[i])
    bucket.sort(key=lambda k: k[0])
    bucket1.sort(key=lambda k: k[0])
    bucket2.sort(key=lambda k: k[0])
    final_lst = bucket+bucket1+bucket2
    check = list()
    for x in final_lst:
        x=' '.join(x)
        check.append(x)
    return check

if __name__ == "__main__":
    peoples=read_file("records_1e1.txt")
    write_file("result.txt", insertion_sort(peoples))