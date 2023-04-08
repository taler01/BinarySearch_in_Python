package main

func main() {
	arr := []int{1, 2, 3, 4, 5, 6}
	result := binarysearch(arr, 4)
	println("**********", result)
}

func binarysearch(a []int, target int) int {
	low := 0
	arr_len := len(a)
	high := arr_len - 1
	mid := (low + high) / 2
	if arr_len == 0 {
		println("数组为空！")
	} else {
		for {
			if a[mid] == target {
				println("位置为：", mid)
				return mid
			} else {
				if a[mid] > target {
					high = mid - 1

				} else if a[mid] < target {
					low = mid + 1
				}
				mid = (low + high) / 2
				println("-----------", mid)
			}
		}

	}
	return -1
}
