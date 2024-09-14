import java.io.*;
import java.util.*;
public class Main228A{
	public static void main(String[] args)throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n =4;
		Set<String> set = new HashSet<>();
		StringTokenizer st = new StringTokenizer(bf.readLine());
		bf.close();
		while(n-->0){
			set.add(st.nextToken());
		}
		System.out.print(4-set.size());
	}
}