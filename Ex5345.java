import javax.swing.*;
import java.util.Locale;
import java.util.Scanner;
import java.util.Stack;

public class Ex5345 {
    public static int sum(Stack<Integer> s) { int resultado = 0; for (int n : s) { resultado += n; } return resultado; }
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Stack<Integer> pilhaDeNumeros = new Stack<>();
        for (int i = 0; i < n; i++) {
            int numeroAtual = sc.nextInt();
            if (numeroAtual == 0) {
                if (!pilhaDeNumeros.empty()) {
                    pilhaDeNumeros.pop();
                }
            }
            if (numeroAtual !=0){
                pilhaDeNumeros.push(numeroAtual);
            }
        }
        int sum = sum(pilhaDeNumeros);
        System.out.println(sum);

    }
}
