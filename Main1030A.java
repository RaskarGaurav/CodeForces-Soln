import java.io.*;
import java.util.*;
public class Main1030A{
	public static void main(String[] args)throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		StringTokenizer st = new StringTokenizer (bf.readLine());
		boolean flag = false;
		while(n-->0){
			if(Integer.parseInt(st.nextToken())==1){
				flag = true;
				break;
			}
		}
		System.out.print(flag? "HARD":"EASY");
	}
}