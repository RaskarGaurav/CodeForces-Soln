import java.io.*;
public class Main486A{
	public static void main(String[] args)throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		long n = Long.parseLong(bf.readLine());

		long even = (n/2)*(n/2 + 1);
		long odd = n%2==0? n*n/4 : (n/2 +1)*(n/2 +1);
		long total = even -odd;
		System.out.print(total);
	}
}