package Java.Chapter1.If;
import java.util.Scanner;

public class Mid3 {
    static int med3(int a, int b, int c){
        if(a > b){
            if(b > c) return b;
            else{
                if(a > c) return c;
                else return a;
            }
        } else {
            if(c > b) return b;
            else{
                if(a > c) return a;
                else return c;
            }
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("세 정수의 중앙값을 구합니다.");
        System.out.print("a의 값 : "); int a = stdIn.nextInt();
        System.out.print("b의 값 : "); int b = stdIn.nextInt();
        System.out.print("c의 값 : "); int c = stdIn.nextInt();
        
        int max = med3(a, b, c);
        System.out.println("중앙값은 " + max + "입니다.");

    }
}
