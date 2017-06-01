public class Problem004 {
	public static void main(String args[]){


		int current = 0;
		int largest = 0;

		for(int i = 100; i < 1000; i++){
			for(int j = 100;j<1000; j++){
				current = j*i;

				if(isPalindromic(Integer.toString(current))){
					//if the current product is larger than the largest then reevaluate the largest
					if(current > largest)
						largest = current;
				}

			}
		}
		System.out.println("The largest product is: " + largest);


	}

	public static boolean isPalindromic(String s){
		int endChar = s.length() - 1;

		for(int i = 0; i < s.length(); i++){
			if(s.charAt(i) != s.charAt(endChar - i)){
				return false;
			}
		}
		return true;


	}
}
