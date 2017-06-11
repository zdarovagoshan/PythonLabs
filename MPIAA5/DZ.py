
import time

from item import Item
from Backpack import Backpack

def standart(W, P, backpack, items):
    K=backpack.avalible_weight
    n=len(W)
    Ans=[]
    p=[[0]*(K+1)for i in range(n)]
    F = [0] * (K+1)
    for i in range(n):
        for k in range(W[i], K+1):
            if F[k]<F[k-W[i]]+P[i]:
                F[k] = F[k - W[i]] + P[i]
                p[i][k]+=1
    i=n-1
    k=0
    for v in range (1, K+1):
        if F[k]<F[v]:
            k=v
    while i>=0:
        if p[i][k]==1:
            while p[i][k] == 1:
                k=k-W[i]
                backpack.insert(items[i])
        i=i-1
    return backpack.current_weight, backpack.full_price

def greedy(l, backpack):
    items = l
    items.sort(key=lambda x: x.price_cooficient)
    for i in items:
        while True:
            if not backpack.insert(i):
                break
    return backpack.current_weight, backpack.full_price

if __name__ == "__main__":
    list_of_items = [Item('1', 2, 1), Item('2', 2, 3), Item('3', 3, 2), Item('4', 1, 1)]
    W=[list_of_items[i].weight for i in range(len(list_of_items))]
    P=[list_of_items[i].price for i in range(len(list_of_items))]
    #list_of_items = [Item("item " + str(i), random.random() * 100, random.random() * 1000, i) for i in range(1000)]
    static_list = list_of_items[:]
    bp = Backpack(7)
    t1 = time.time()
    print(standart(W, P, bp, list_of_items))
    t2 = time.time()
    print("sta algorythm time: " + str(t2 - t1))
    bp.clear()
    #greedy
    t1 = time.time()
    print(greedy(list_of_items, bp))
    t2 = time.time()
    print("greedy algorythm time: " + str(t2 - t1))