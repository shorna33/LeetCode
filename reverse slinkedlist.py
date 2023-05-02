
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

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
            return
        temp = ListNode(data, self.head)
        self.head = temp

    def printlist(self):
        if self.head is None:
            print("The list is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next

    def reverse(self):
        temp = self.head
        while temp is not None:
            rlist.insert_at_beginning(temp.val)
            temp = temp.next


head = ListNode(1, ListNode(2, None))
list1 = llist()
rlist = llist()
while head is not None:
    list1.insert_at_end(head.val)
    head = head.next
list1.printlist()
list1.reverse()
print()
rlist.printlist()
