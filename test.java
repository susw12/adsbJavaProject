import java.util.Scanner;
import java.io.IOException;

public class test{ 
    public static void main(String[] args) throws IOException{
        Scanner userInput = new Scanner(System.in);
        System.out.print("Please enter the twitter handle of the company: ");
        String company = userInput.nextLine();
        System.out.print("\nPlease enter the twitter handle of the conference: ");
        String conference = userInput.nextLine();
        try {
            Process p = Runtime.getRuntime().exec("python interface.py company conference");
            System.out.println(p);
        } catch (IOException e1) {
            System.out.println("Shoot!");
        }
    }
}