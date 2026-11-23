#include <stdio.h>
int calculerSomme(int T[], int n) {
    int somme = 0;
    for (int i = 0; i < n; i++) {
        somme = somme + T[i];
    }
    return somme;
}
int main() {
    int T[5] = {10, 20, 30, 40, 50};
    int somme = calculerSomme(T, 5);
    printf("La somme des elements est : %d\n", somme);
    return 0;
}