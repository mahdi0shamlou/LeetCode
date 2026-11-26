package main

import "fmt"

func isValid(s string) bool {

    stack := []rune{}

    for _, char := range s {

        
        if char == '(' || char == '{' || char == '[' {
            stack = append(stack, char)
            continue
        } else {
			// Closing parentheses
			if len(stack) == 0 {
				return false
			}

			// Get the last opened parenthesis
			top := stack[len(stack)-1]

			// Remove the top element
			stack = stack[:len(stack)-1]

			// Check matching parentheses
			if char == ')' && top != '(' {
				return false
			}

			if char == '}' && top != '{' {
				return false
			}

			if char == ']' && top != '[' {
				return false
			}
		}

 
    }

    // Stack must be empty
    return len(stack) == 0
}

func main() {

    testCases := []string{
        "()",
        "()[]{}",
        "(]",
        "([])",
        "([)]",
        "(((",
        "{[()]}",
    }

    for _, test := range testCases {
        fmt.Printf("Input: %-10s Output: %t\n", test, isValid(test))
    }
}