my_list=[0,1,2,0,1,0,2,1,5]


# 冒泡排序
N=len(my_list)
# print(N)
K=N-1
while(K>=0):
    for i in range(K):
        a=my_list[i]
        b=my_list[i+1]
        if (a>b):
            my_list[i]=b
            my_list[i+1]=a
    K=K-1

print(my_list)

