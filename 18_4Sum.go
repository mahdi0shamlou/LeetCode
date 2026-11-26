package main 

import (
    "fmt"
)

func fourSum(nums []int, target int) [][]int {

	var n int = len(nums)
	sort_bob(nums)
	result := [][]int{}

    for i := 0; i < n-3; i++ {

        // Skip duplicate first numbers
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }

        // Step 3: Select the second number
        for j := i + 1; j < n-2; j++ {

            // Skip duplicate second numbers
            if j > i+1 && nums[j] == nums[j-1] {
                continue
            }

            // Step 4: Initialize two pointers
            left := j + 1
            right := n - 1

            for left < right {

                // Calculate the sum
                sum := int64(nums[i]) + int64(nums[j]) + int64(nums[left]) + int64(nums[right])

                if sum == int64(target) {

                    // Found a valid quadruplet
                    quadruplet_finded := []int{
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right],
                    }

                    result = append(result, quadruplet_finded)

                    left++
                    right--

                    // Skip duplicate values on the left
                    for left < right && nums[left] == nums[left-1] {
                        left++
                    }

                    // Skip duplicate values on the right
                    for left < right && nums[right] == nums[right+1] {
                        right--
                    }

                } else if sum < int64(target) {

                    left++

                } else {

                    right--
                }
            }
        }
    }

    return result
}


func sort_bob(nums []int) {
	// this fun sort the input 
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
