import java.io.*;
import java.math.BigInteger;

public class Problem099 {
	private int expo[][] = new int[1000][2];

	public static void main(String args[]) {
		float first = System.nanoTime();

		Problem099 p = new Problem099();
		p.readAndSet();
		System.out.println();
		p.run();
		float second = System.nanoTime();
		float time = (second - first) / 1000000000;
		System.out.println(time + " seconds elapsed.");
	}

	public void run() {
		double current =0, biggest=0, number, pow;
		int index =0;
		
		for(int i = 0; i <= 999; i++){
			number = expo[i][0];
			pow = expo[i][1];
			
			current = 1 + pow * Math.log(number);

			if(current > biggest){
				biggest = current;
				index = i;
			}
		}
		
		System.out.println("List number = " + (index + 1) + ". Number is " + Math.floor(biggest) + " digits long.");
	}

	public void readAndSet() {
		FileReader fw;
		String temp = "";
		String split[] = new String[2];

		try {
			fw = new FileReader("C:/Users/Julien/Desktop/Exponents.txt");
			BufferedReader bf = new BufferedReader(fw);

			temp = bf.readLine();
			int i = 0;
			while (temp != null) {
				split = temp.split(",");
				// System.out.println(split[0] + ", " + split[1]);
				expo[i][0] = Integer.parseInt(split[0]);
				expo[i][1] = Integer.parseInt(split[1]);

				temp = bf.readLine();
				i++;
			}

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
