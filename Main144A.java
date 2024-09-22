import java.io.*;
import java.util.*;
public class Main144A{
	public static void main(String[] args)throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		List<Integer> ls = new ArrayList<>(n);
		StringTokenizer st = new StringTokenizer(bf.readLine());
		bf.close();
		for(int i=0; i<n; i++){
			ls.add(Integer.parseInt(st.nextToken()));
		}
		int mx = ls.indexOf(Collections.max(ls));
		int mn = ls.lastIndexOf(Collections.min(ls));
		System.out.print(mx<mn? mx+n-mn-1 : mx+n-mn-2);
	}
}