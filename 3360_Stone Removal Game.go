package main 

import (
    "fmt"
)

func canAliceWin(n int) bool {

	for i := 10; i > 0; i-- {
		n = n - i

		if n < 0 {
			if i % 2 == 0 {
				return false
			} else {
				return true
			}
		}
	}
}