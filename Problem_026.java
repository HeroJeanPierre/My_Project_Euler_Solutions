import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;

public class Problem026 {
	static HashMap<String, Boolean> map = new HashMap<>();

	public static void main(String args[]) {
		ArrayList<Integer> i = new ArrayList<Integer>();
		
		
		for (int k = 0; k < 100; k++) {
			i.add(k);
		}
		int size = i.size();
		for(int k = 0; k < size;k++){
			if(k == i.size()-1)break;
			
			if(i.get(k) % 3 == 0){
				i.remove(k);
			}
			System.out.println(i.size());
		}
	}
}
