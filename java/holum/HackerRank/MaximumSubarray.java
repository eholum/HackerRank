package holum.HackerRank;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

/**
 * https://www.hackerrank.com/challenges/maxsubarray
 *
 */
public class MaximumSubarray {
    
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numLines = Integer.parseInt(br.readLine());
        for (int i=0; i<numLines; i++) {
            br.readLine();
            System.out.println(computeMaxSubarray(br.readLine()));
        }
    }
    
    private static String computeMaxSubarray(String arrayString) {
        List<Long> results = new LinkedList<>();
        long currentMax = Long.MIN_VALUE;
        long overallMax = Long.MIN_VALUE;
        long nonContigMax = 0;
        
        // Keeping track of indicies is not required for this problem
        Scanner arrayScanner = new Scanner(arrayString);
        while (arrayScanner.hasNext()) {
            long value = arrayScanner.nextLong();
            
            if (currentMax < 0) {
                currentMax = value;
            }
            else {
                currentMax = currentMax + value;
            }
            
            if (currentMax > overallMax) {
                overallMax = currentMax;
            }
            results.add(overallMax);
            
            if (value >= 0) {
                nonContigMax += value;
            }
        }
        arrayScanner.close();
        
        // No positive values in array
        if (overallMax < 0) {
            nonContigMax = overallMax;
        }
        
        return overallMax + " " + nonContigMax;
    }
}
