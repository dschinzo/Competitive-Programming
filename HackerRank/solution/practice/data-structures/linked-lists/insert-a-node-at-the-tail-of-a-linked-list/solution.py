

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if not head:
        head = SinglyLinkedListNode(data)
        return head
    else:
        ptr = head
        while ptr.next:
            tail = ptr.next
            ptr = tail
        ptr.next = SinglyLinkedListNode(data)
        return head
