class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def append(self, node):
        temp = self.tail
        node.previous = temp
        self.tail.next = node
        self.tail = node


class Node:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value


odd_list = LinkedList(Node('a'))
for c in 'bcde':
    odd_list.append(Node(c))

even_list = LinkedList(Node('a'))
for c in 'bcd':
    even_list.append(Node(c))


def print_linked_list(list: LinkedList):
    curr = list.head
    while True:
        print(curr.value)
        if not curr.next:
            break
        curr = curr.next


def linked_list_mid(list: LinkedList) -> Node:
    # odd length has middle of len//2
    fast = list.head
    slow = list.head

    while fast.next:
        if not fast.next.next:
            break

        fast = fast.next.next
        slow = slow.next

    return slow


"""
abc

fast = 
even = 
"""


def is_list_palindrome(list: LinkedList) -> bool:
    fast = list.head
    slow = list.head

    while fast.next:
        if not fast.next.next:
            break

        fast = fast.next.next
        slow = slow.next

    return slow


mid_even = linked_list_mid(even_list).value
mid_odd = linked_list_mid(odd_list).value

assert mid_even == 'b', mid_even
assert mid_odd == 'c', mid_odd
