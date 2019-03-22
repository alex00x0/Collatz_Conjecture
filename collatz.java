public class collatz {

    public static void main(String[] args) {
        
        double num = Math.pow(10, 2);
        int run = (int)num;

        int y = 0;
    
        for (int i=2; i <= run; i++){
            int x = i;
            while (x != 1){
                if (x % 2 == 0)
                    x = x/2;
                else
                    x = 3 * x + 1;
            }
            y = y + 1;
            }
        System.out.println(y);
    }
    
}
