public class Problem003 {
	public static void main(String args[]){

		primeFactors(600851475143L);

	}

	public static void primeFactors(Long n){

		while(n % 2 == 0 ){
			System.out.println(2);
			n /= 2;
		}

		for(long i = 3; i <= Math.sqrt(n); i += 2){
			while(n % i == 0){
				System.out.println(i);
				n /= i;
			}
		}

		if(n > 2) System.out.println(n);
	}

}
