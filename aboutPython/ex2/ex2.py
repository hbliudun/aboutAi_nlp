#�������� �ǿ� ������������ʾ�����Ǹ������������У����Ǹ��Ե�λ���ǰ��� ���� �ķ�ʽ�洢�ģ��������ǵ�ÿ���ڵ�ֻ�ܴ洢 һλ ���֡�

#��������ǽ��������������������᷵��һ���µ���������ʾ���ǵĺ͡�

#�����Լ���������� 0 ֮�⣬���������������� 0 ��ͷ��

#ʾ����

#���룺(2 -> 4 -> 3) + (5 -> 6 -> 4)
#�����7 -> 0 -> 8
#ԭ��342 + 465 = 807

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodeRet = ListNode(0)
        tmp = nodeRet
        while( l1 or l2 ):
            ret = l1.val+l2.val + tmp.val
            if ret > 10:
                tmp.val = ret%10
                a = ListNode(0)
                a.val = int(ret/10)
                tmp.next = a
            else:
                a = ListNode(0)
                a.val = ret
                a.next = None
                tmp = a
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
            
        return nodeRet