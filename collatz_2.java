import com.sun.org.apache.xerces.internal.impl.xpath.regex.ParseException;

public class collatz_2 {

    public static void main(String[] args) {
        long startTime = System.nanoTime();
        double y = Math.pow(10,20);
        long x = (long)y;
        int steps = 0;
        System.out.println("this is x: " + x);

        while (x != 1){
            if (x % 2 == 0){
                x = x/2;
                steps ++;
                System.out.println(x);
        }
            else{
                x = 3 * x + 1;
                System.out.println(x);
                steps++;
            }
        }
    System.out.println("steps: " + steps);
    long endTime = System.nanoTime();
    long durationInNano = (endTime - startTime);
    System.out.println("time: " + durationInNano);
    }
    
}