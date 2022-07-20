/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil{
        return head
    }
	prev, node := head, head.Next
	for node != nil {
		if prev.Val == node.Val {
			prev.Next = node.Next
		} else {
			prev = node
		}
		node = node.Next
	}
	return head
}