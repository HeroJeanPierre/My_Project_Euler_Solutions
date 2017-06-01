import java.io.*;


public class Problem018 {
	public static void main(String args[]){
	int numberz[][] = {
			               {75},
			             {95,64},
			            {17,47,82},
	                   {18,35,87,10},
			          {20,04,82,47,65},
			         {19,01,23,75,03,34},
			        {88,02,77,73,07,63,67},
			       {99,65,04,28,06,16,70,92},
			      {41,41,26,56,83,40,80,70,33},
			     {41,48,72,33,47,32,37,16,94,29},
			    {53,71,44,65,25,43,91,52,97,51,14},
			   {70,11,33,28,77,73,17,78,39,68,17,57},
			  {91,71,52,38,17,14,91,43,58,50,27,29,48},
			 {63,66,04,68,89,53,67,30,73,16,69,87,40,31},
			{04,62,98,27,23,9,70,98,73,93,38,53,60,04,23},		
	};
	
	int iMin = 0, jPlus = 0;
	
	for(int i = (numberz.length-1); i > 0; i--){
		iMin = i-1;
		for(int j = 0; j < numberz[iMin].length; j++){
			jPlus = j+1;
			if(numberz[i][j] >= numberz[i][jPlus]){
				System.out.println(numberz[i][j]+ " Greater Than " + numberz[i][jPlus]);
				numberz[iMin][j] += numberz[i][j];
			}else{
				System.out.println(numberz[i][j]+ " Less Than " + numberz[i][jPlus]);
				numberz[iMin][j] += numberz[i][jPlus];
			}

		}
		System.out.println("New Line-----------");
		for(int k[]: numberz){
			for(int kk: k){
				System.out.print(kk + " ");
			}
			System.out.println();
		}
		}
	System.out.println();
	System.out.println(numberz[0][0] + " is the max sum!");
	
	
	}
	public static void read(){
		int numbers[][]= {{3,2}};
		try{
			FileReader fr  = new FileReader("C:/Users/Julien/Desktop/Tri.txt");
			BufferedReader br  = new BufferedReader(fr);
			
			String str;
			while ((str = br.readLine()) != null){
				
			}
			
		}catch(Exception e){
			System.out.println("File not Found.");
		}
		
		
	}
	
	
	
}
