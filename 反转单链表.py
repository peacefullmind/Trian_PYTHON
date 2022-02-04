# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 19:55
# @Author  : taoji
# @Email   : tao13131265081@163.com
# @File    : 反转单链表.py
# @Software: PyCharm
# 反转单链表。例如链表为：1->2->3->4。反转后为 4->3->2->1

class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    # def print_from_start_node(self):
    #     start_node=self
    #     print(start_node.data,end='\t')
    #     while(start_node.next):
    #         start_node=start_node.next
    #         print(start_node.data,end='\t')
class ListNode(object):
    def __init__(self,head):
        self.head=head
    def print_list(self):
        my_node=self.head
        print(my_node.data,end='\t')
        while(my_node.next):
            my_node=my_node.next
            print(my_node.data,end='\t')
    def reverseList(self,head):
        if head==None or head.next==None:
            return head
        else:
            pre=head
            n=head.next
            ll=self.reverseList(n)
            n.next=pre
            pre.next=None
            return ll


n4=Node(4)
n3=Node(3,n4)
n2=Node(2,n3)
n1=Node(1,n2)

ln=ListNode(n1)
ln.print_list()
print('')

LK=ln.reverseList(ln.head)
ln2=ListNode(LK)
ln2.print_list()