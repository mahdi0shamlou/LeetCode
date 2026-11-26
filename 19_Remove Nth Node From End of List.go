package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {

	length := 0
	current := head
	for current != nil {
		length++
		current = current.Next
	}

	position := length - n

	// Edge case: Remove head
	if position == 0 {
		return head.Next
	}

	current = head
	for i := 0; i < position-1; i++ {
		current = current.Next
	}

	
	current.Next = current.Next.Next

	return head
}

func createLinkedList(values []int) *ListNode {
	if len(values) == 0 {
		return nil
	}

	head := &ListNode{Val: values[0]}
	current := head

	for i := 1; i < len(values); i++ {
		current.Next = &ListNode{Val: values[i]}
		current = current.Next
	}

	return head
}

func printLinkedList(head *ListNode) {
	for head != nil {
		fmt.Printf("%d", head.Val)

		if head.Next != nil {
			fmt.Print(" -> ")
		}

		head = head.Next
	}

	fmt.Println(" -> nil")
}

func main() {
	head := createLinkedList([]int{1, 2, 3, 4, 5})

	fmt.Println("Original Linked List:")
	printLinkedList(head)

	head = removeNthFromEnd(head, 2)

	fmt.Println("After Removing 2nd Node From End:")
	printLinkedList(head)
}