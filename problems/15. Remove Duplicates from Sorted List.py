class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return head

    init = head

    while init.next:
        if init.val == init.next.val:
            init.next = init.next.next
        else:
            init = init.next

    return head

x = ListNode(1)
y = ListNode(1)
z = ListNode(2)

x.next = y
y.next = z


print(deleteDuplicates(x))

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
