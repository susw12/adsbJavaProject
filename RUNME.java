import java.util.Scanner;
import java.io.*;

public class RUNME{ 
    
    public static void main(String args[]) throws IOException{
        String s = null;        
        Scanner userInput = new Scanner(System.in);
        System.out.print("Please enter the twitter handle of the company: ");
        String company = userInput.nextLine();
        System.out.print("\nPlease enter the twitter handle of the conference: ");
        String conferenceHandle = userInput.nextLine();
        System.out.print("\nPlease enter the twitter hastag of the conference: ");
        String conferenceHashtag = userInput.nextLine();
        try {
            Process p = Runtime.getRuntime().exec("python3 interface.py " + company + " " + conferenceHashtag + " " + conferenceHandle);
            BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));

            while ((s = stdInput.readLine()) != null) {
                System.out.println(s);
            }

            //Testing code that printed out errors
            /* BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            System.out.println("The following errors were printed:\n");
            while ((s = stdError.readLine()) != null) {
                System.out.println(s);
            }
            */
        } catch (IOException e1) {
            System.out.println("Shoot!");
        }
        userInput.close();
    }
}