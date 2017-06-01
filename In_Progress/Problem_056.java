import java.math.BigInteger;


public class Problem056 {
	public static void main(String args[]){
		float first = System.nanoTime();
		BigInteger prod = new BigInteger("1");
		
		int current = 0;
		int greatest = 0;
		
		for(int a = 80; a < 100; a++){
			BigInteger aBig = new BigInteger(Integer.toString(a)); 
			for(int b = 80; b < 100; b++){
				prod = aBig.pow(b);
				
				if(findSum(prod.toString()) > greatest){
					greatest = findSum(prod.toString());
				}
			}
		}
		System.out.println("The greatest number is: " + greatest);
		
		float second = System.nanoTime();
		float seconds = (second - first)/1000000000;
		System.out.println("It took " + seconds + " seconds to complete.");

		
	}
	public static int findSum(String s){
		int sum = 0;
		for(int i = 0; i < s.length();i++)
			sum += Character.getNumericValue(s.charAt(i));
		return sum;
	}

}
