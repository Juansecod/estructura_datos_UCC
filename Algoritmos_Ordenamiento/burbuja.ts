function bubbleSortTypescript(lista: number[]): number[] {
    const n: number = lista.length;
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n - i - 1; j++) {
        if (lista[j] > lista[j + 1]) {
          [lista[j], lista[j + 1]] = [lista[j + 1], lista[j]];
        }
      }
    }
    return lista;
}