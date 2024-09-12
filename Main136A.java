import java.io.*;
import java.util.*;

public class Main136A{
	public static void main(String[] args)throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		StringTokenizer st = new StringTokenizer(bf.readLine());
		bf.close();
		int[] a = new int[n];
		for(int i=0; i<n; i++){
			a[i] = Integer.parseInt(st.nextToken());
		}
		int k =1;
		while(k<=n){
			for(int i=0; i<n; i++){
				if(a[i]==k){
					System.out.print((i+1)+" ");
					break;
				}
			}
			k++;
		}
	}
}