import java.io.*;
public class Main705A{
	public static void main(String[] args)throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		bf.close();
		String luv = "I love that ";
		String het = "I hate that ";
		String str = "";
		for(int i=0; i<n; i++){
			if(i%2==0) str=str+het;
			else str=str+luv;
		}
		int k = str.lastIndexOf("that");
		str=str.substring(0,k);
		System.out.print(str+"it");
	}
}