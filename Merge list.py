
#
#                     NOT SOLVED
#


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class llist:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = ListNode(data, None)

    def printlist(self):
        if self.head is None:
            print("The list is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def merge(self, p, q):

        p_curr = p.val
        q_curr = q.val
        print(p_curr.val, q_curr.val)
        # while p_curr != None:


list1 = llist()
list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(4)
list1.printlist()
