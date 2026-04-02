# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Convert to an array
#        class ListNodeObj:
#            def __init__(self, val=0, next=None):
#                self.val = val
#                self.next = next

        def nodes_to_array(head):
            result = []
            current = head

            while current:
                result.append(current.val)
                current = current.next

            return result
            
        def array_to_nodes(array):
            if not array:
                return None

            head = ListNode(array[0])
            current = head

            for i in range(1, len(array)):
                current.next = ListNode(array[i])
                current = current.next
            
            return head        

        array1 = nodes_to_array(list1)
        array2 = nodes_to_array(list2)

        for num in array2:
            array1.append(num)

        array1.sort()

        result = array_to_nodes(array1)
        return result
