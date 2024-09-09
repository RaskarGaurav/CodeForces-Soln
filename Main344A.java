import java.io.*;
public class Main344A{
	public static void main(String[] args)throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		int[] a = new int[n];
		for(int i=0; i<n; i++){
			a[i] = Integer.parseInt(bf.readLine());
		}
		int count = 1;
		for(int i=0; i<n-1; i++){
			if(a[i]!=a[i+1]) count++;
		}
		System.out.print(count);
	}
}