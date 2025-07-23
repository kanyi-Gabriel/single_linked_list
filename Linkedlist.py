# To delete a Node in singly linked list
class Node:
    def __init__(self,data, next =None):
        self.data = data
        self.next = next
    
# To traverse throuhh the linked list
def traverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data)
        currentNode = currentNode.next

# To delete any node
def deleteNode(head, keyNode):
    # To delete the first Node if it;s the argument passed as the key Node specified
    if keyNode == head:
        return head.next
    
    # Set the next node as the head after deleting the first node
    currentNode = head

    # To loop through all nodes and check for the specific node to delete
    while currentNode.next and currentNode.next != keyNode:
        currentNode = currentNode.next

        # To link current nod with the head node
    if currentNode.next is None:
        return head
        
    currentNode.next = currentNode.next.next

    return head
    
def main(): 
    # To create a linked list
    node1 = Node(4)
    node2 = Node(18)
    node3 = Node(45)
    node4 = Node(11)
    node5 = Node(16)
    node6 = Node(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
 
# Print Original list before deletion
    print("Linked list Before deletion")
    traverse(node1)

    # To delete node 5
    print("After Deleting specified node")
    node1 = deleteNode(node1, node4)

    # Linked list After Deletion
    traverse(node1)

if __name__ == "__main__":
    main()
