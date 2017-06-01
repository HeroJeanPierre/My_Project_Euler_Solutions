public class Problem002 {
	public static void main(String args[]){
		int first = 1, second = 1, third = 0;

		int sum = 0;

		while(third <= 4000000){
			third = first + second;
			first = second;
			second = third;

			sum += (third % 2 ==0) ? third:0;
		}

		System.out.println("The sum is: " + sum);
	}
}
