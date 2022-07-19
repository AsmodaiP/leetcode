func mySqrt(x int) int {
	if x < 2 {
		return x
	}
	start, end := 1, x>>1
	for start < end {
		mid := int((start + end + 1) >> 1)
		if mid <= x/mid {
			start = mid
		} else {
			end = mid - 1
		}
	}
	return end
}