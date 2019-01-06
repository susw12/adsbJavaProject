package mr.gonzalez.xc150;

import java.io.*;
import java.util.*;

public class JSONtoTXT {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner reader = new Scanner(new File("tweets.json"));
		PrintWriter writer = new PrintWriter(new File("tweets.txt"));
		
		while(reader.hasNextLine()) {
			String line = reader.nextLine();
			writer.write(line);
		}
	
		reader.close();
		writer.close();
	}
	
}