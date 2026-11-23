#include <stdio.h>
int main() {
    float n1, n2, n3, moyenne;
    printf("Entrez la premiere note : ");
    scanf("%f", &n1);
    printf("Entrez la deuxieme note : ");
    scanf("%f", &n2);
    printf("Entrez la troisieme note : ");
    scanf("%f", &n3);
    moyenne = (n1 + n2 + n3) / 3;
    printf("La moyenne est : %.2f\n", moyenne);
    if (moyenne >= 10) {
        printf("Resultat : Admis\n");
    } else {
        printf("Resultat : Non admis\n");
    }
    return 0;
}