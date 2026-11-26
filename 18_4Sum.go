package main 

import (
    "fmt"
)

func fourSum(nums []int, target int) [][]int {
	
	sort_bob(nums)

	return [][]int{}
}

func sort_bob(nums []int) {

	var len_nums int = len(nums)
	fmt.Println("Input sort_bob:", nums)
	for i := 0; i < len_nums - 1; i = i + 1 {
		for j := 0; j < len_nums - i - 1; j++ {
			if nums[j] > nums[j+1] {
                nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}
	fmt.Println("Input sort_bob:", nums)

}

func main() {
    nums := []int{1, 0, -1, 0, -2, 2}
    target := 0

    result := fourSum(nums, target)

    fmt.Println("Input:", nums)
    fmt.Println("Target:", target)
    fmt.Println("Result:", result)

}
