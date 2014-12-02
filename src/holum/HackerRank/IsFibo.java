package holum.HackerRank;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * https://www.hackerrank.com/challenges/is-fibo
 *
 */
public class IsFibo {

    private static final String IS_FIBO = "IsFibo";
    private static final String IS_NOT_FIBO = "IsNotFibo";
    
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numLines = Integer.parseInt(br.readLine());
        for (int i=0; i<numLines; i++) {
            System.out.println(isFibo(Double.parseDouble(br.readLine())));
        }
    }
    
    // A number n is a fibonacci number iff 5x^2 ± 4 is a perfect square.
    // http://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
    private static String isFibo(double n) {
        double check = n * n * 5;
        
        boolean isFibonacciNumber = (isSquare(check + 4) || isSquare(check - 4));
        
        return isFibonacciNumber ? IS_FIBO : IS_NOT_FIBO;
    }
    
    private static boolean isSquare(double check) {
        double root = Math.sqrt(check);
        return root % 1 == 0;
    }
}
