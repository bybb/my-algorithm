package Java.Chapter1.For;
import java.util.Scanner;

public class SumOf {
    static int sumOf(int a, int b){
        int sum = 0;
        while(a != b){
            if(a > b){
                sum += a;
                a--;
            } else {
                sum += a;
                a++;
            }
        }
        return sum+b;
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("정수 a를 입력하세요 : ");
        int a = stdIn.nextInt();
        System.out.print("정수 b를 입력하세요 : ");
        int b = stdIn.nextInt();

        System.out.println("a에서 b까지의 합은 " + sumOf(a, b) + "입니다.");
    }
}
