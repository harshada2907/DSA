import java.util.Scanner;

public class j1 {

    public static long factorial(int num) {
        long fact = 1;
        for (int i = 1; i <= num; i++) {
            fact *= i;
        }

        return fact;
    }




    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a number to find its factorial : ");
        int num = sc.nextInt();

        long result = factorial(num);
        System.out.println("Factorial of " + num + " is: " + result);

        sc.close();
    }
}
