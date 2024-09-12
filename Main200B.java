import java.io.*;
import java.util.*;
public class Main200B{
	public static void main(String[] args)throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		double n = Double.parseDouble(bf.readLine());
		double k = n;
		StringTokenizer st = new StringTokenizer(bf.readLine());
		double org = 0;
		while(k-->0){
			double i = Double.parseDouble(st.nextToken());
			org = org + (i/100);
		}
		System.out.printf("%.12f\n",(org/n)*100);

	}
}