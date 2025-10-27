import java.util.Locale;
import java.util.Scanner;

public class Ex5344 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int countPares = 0;

        int n = sc.nextInt(); // botas entregues
        for (int i = 0; i < n; i++) {
            String input = sc.nextLine().replace(" ", "");

            String[] pes = new String[61];

            pes[i] = input;


        }

        System.out.println(countPares);
    }
}
