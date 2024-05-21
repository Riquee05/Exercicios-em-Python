import java.util.Scanner;

public class ifelse{
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);

        int idade = 0;

        System.out.println("Insira sua Idade:  ");
        idade = scanner.nextInt();

        if (idade <= 18){
            System.out.println("Menor de Idade");
        }
        else {
            System.err.println("Maior de idade");
        }

    }
}