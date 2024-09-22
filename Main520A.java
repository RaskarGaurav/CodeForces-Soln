import java.io.*;
import java.util.*;
public class Main520A{
	public static void main(String[] args)throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		String str = bf.readLine();
		Set<Character> set = new HashSet<>();
		for(int i=0; i<n; i++){
			char c=str.charAt(i);
			set.add(Character.toLowerCase(c));
		}
		System.out.print(set.size()==26? "YES" : "NO");
	}
}