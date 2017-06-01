
public class Problem005 {


	public static void main(String args[]){
		//Create value to find multiples of to, or k
		//& create value to add onto during iterations
		int k = 20;
		int N = 1;
		int a = 1;
		//Set limit of sqrt of k, b/c if p[i]^2 > k then it needs to stop
		double limit = Math.sqrt(k);

		boolean keepRunning = true;
		int[] p = primes(k);

		for(int i = 0; i < p.length; i++){
				a = 1;
				if(p[i] <= limit){
					a = (int) Math.floor(Math.log(k)/Math.log(p[i]));
					System.out.println(a);
				}
				N *= Math.pow(p[i], a);
		}
		
		System.out.println(N);


	}

	public static int[] primes(int k){

		int size = 0;
		for(int i = 0; i < PrimeNumber.returnPrimes(k).length; i++){
			if(PrimeNumber.returnPrimes(k)[i])
				size++;
		}

		int p[] = new int[size];
		size = 0;

		for(int i = 0; i < PrimeNumber.returnPrimes(k).length; i++){
			if(PrimeNumber.returnPrimes(k)[i]){
				p[size] = i;
				size++;
			}
		}
		return p;
	}
}
