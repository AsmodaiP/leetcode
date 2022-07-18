func addBinary(a string, b string) string {
	var result string
	var carry int
	var a_len int = len(a)
	var b_len int = len(b)
	var max_len int
	if a_len > b_len {
		max_len = a_len
	} else {
		max_len = b_len
	}
	for i := 0; i < max_len; i++ {
		var a_digit int
		var b_digit int
		if i < a_len {
			a_digit = int(a[a_len-i-1] - '0')
		} else {
			a_digit = 0
		}
		if i < b_len {
			b_digit = int(b[b_len-i-1] - '0')
		} else {
			b_digit = 0
		}
		var sum int = a_digit + b_digit + carry
		if sum > 1 {
			carry = 1
			sum = sum - 2
		} else {
			carry = 0
		}
		result = strconv.Itoa(sum) + result
	}
	if carry == 1 {
		result = "1" + result
	}
	return result
}