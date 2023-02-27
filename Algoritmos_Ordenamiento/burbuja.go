func bubbleSort(lista []int) {
	n := len(lista)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if lista[j] > lista[j+1] {
				lista[j], lista[j+1] = lista[j+1], lista[j]
			}
		}
	}
}