import java.util.*;

public class elephant{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int target = sc.nextInt();
        int count = 0;
        // ArrayList arr() = new ArrayList<>();
        // List<Integer> lmao = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        if (target > 5){
            count = (target / 5);
            if (target % 5 != 0){
                count += 1;
            } 
        }
        else{
            count = 1;
        }
        System.out.println(count);
        sc.close();
    }
}