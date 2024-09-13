import java.io.*;
public class Main61A{
	public static void main(String[] args)throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		long n1 = Long.parseLong(bf.readLine(),2);
		String str = bf.readLine();
		long n2 = Long.parseLong(str,2);
		long ans = n1^n2;
		String answer = Long.toBinaryString(ans);
		long gap = str.length() - answer.length();
		while(gap-->0) answer = "0"+answer;
		System.out.print(answer);
	}
}