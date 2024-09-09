import java.io.*;
import java.util.*;
public class Main467A{
	public static void main(String[] args)throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(bf.readLine());
		int count = 0;
		while(t-->0){
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int fill = Integer.parseInt(st.nextToken());
			int total = Integer.parseInt(st.nextToken());
			count = (total-fill)>=2? ++count:count;
		}
		System.out.print(count+"\n");

	}
}