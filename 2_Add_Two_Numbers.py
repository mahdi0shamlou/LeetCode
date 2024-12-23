class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = self.sum(l1,l2,0)
        return res

    def sum(self, l1, l2, added):
        posetive = l1.val + l2.val + added
        added = 0
        if posetive >= 10:
            posetive = posetive - 10
            added = 1
        if l1.next != None and l2.next != None:
            list_node = ListNode(val=posetive, next=self.sum(l1.next, l2.next, added))
        elif l2.next == None and l1.next != None:
            list_node = ListNode(val=posetive, next=self.sum(l1.next, ListNode(val=0, next=None), added))
        elif l2.next != None and l1.next == None:
            list_node = ListNode(val=posetive, next=self.sum(ListNode(val=0, next=None), l2.next, added))
        else:
            list_node = ListNode(val=posetive, next=None)
        return list_node

