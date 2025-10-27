import java.util.Locale;
import java.util.Scanner;

public class Ex3048 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int anterior = -1;
        int contador = 0;

        for (int i = 0; i < n; i++) {
            int atual = sc.nextInt();

            if (atual != anterior) {
                contador++;
            }

            anterior = atual;

        }
        System.out.println(contador);
    }
}
