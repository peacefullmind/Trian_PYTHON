my_list=[0,1,2,0,1,0,2,1,5]


# 快排
N=len(my_list)

def quickSort(my_list,begin,end):
    if begin>=end:
        return
    i_start=begin
    i_end=end
    privot=my_list[i_start]
    while i_start<i_end:
        while i_start<i_end and my_list[i_end]>=privot:
            i_end=i_end-1
        my_list[i_start]=my_list[i_end]
        while i_start<i_end and my_list[i_start]<=privot:
            i_start=i_start+1
        my_list[i_end]=my_list[i_start]

    my_list[i_start]=privot
    quickSort(my_list, begin, i_start-1)
    quickSort(my_list, i_start+1, end)


quickSort(my_list, 0, N-1)
print(my_list)
print('==========================================')

def quickSort2(my_list):
    if(len(my_list)<=1):
        return my_list

    p=my_list[0]
    little_nums=[l for l in my_list[1:] if l <=p]
    big_nums=[l for l in my_list[1:] if l>p]
    return quickSort2(little_nums)+[p]+quickSort2(big_nums)

my_list1=[0,1,2,0,1,0,2,1,5]
quickSort2(my_list1)
print(quickSort2(my_list1))




