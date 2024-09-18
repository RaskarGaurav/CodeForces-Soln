import java.io.*;
import java.util.*;
public class Main469A{
	public static void main(String[] args)throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int siz = Integer.parseInt(st.nextToken());
		Set<Integer> set1 = new HashSet<>();
		Set<Integer> set2 = new HashSet<>();
		int k =siz;
		while(k-->0){
			int j=Integer.parseInt(st.nextToken());
			set1.add(j);
		}
		StringTokenizer st1 = new StringTokenizer(bf.readLine());
		k=siz;
		while(siz-->0){
			int j=Integer.parseInt(st1.nextToken());
			set1.add(j);
		}
		for(int i=1;i<=n;i++){
			set2.add(i);
		}
		System.out.print(set1.equals(set2)? "I become the guy.":"Oh, my keyboard!");
	}
}