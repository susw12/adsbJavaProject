import java.util.Scanner;
import java.io.*;

public class test{ 
    
    public static void main(String args[]) throws IOException{
        String s = null;        
        Scanner userInput = new Scanner(System.in);
        System.out.print("Please enter the twitter handle of the company: ");
        String company = userInput.nextLine();
        System.out.print("\nPlease enter the twitter handle of the conference: ");
        String conference = userInput.nextLine();
        try {
            Process p = Runtime.getRuntime().exec("python3 interface.py " + company + " " + conference);
            BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));

            BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            while ((s = stdInput.readLine()) != null) {
                System.out.println(s);
            }
            
        } catch (IOException e1) {
            System.out.println("Shoot!");
        }
    }
}