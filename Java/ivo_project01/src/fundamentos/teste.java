package fundamentos;
import java.util.Scanner;

class maiormenormaiormenor{
	public static void main(String[] args) {
		Scanner entrada1 = new Scanner(System.in);
		System.out.println("Digite um número: ");
		double resp1 = entrada1.nextDouble();
		Scanner entrada2 = new Scanner(System.in);
		System.out.println("Digite um número: ");
		double resp2 = entrada2.nextDouble();
		Scanner entrada3 = new Scanner(System.in);
		System.out.println("Digite um número: ");
		double resp3 = entrada3.nextDouble();
		
		if (resp1 > resp2 && resp2 > resp3){
			System.out.println("Maior:");
			System.out.println(resp1);
			System.out.println("Menor:");
			System.out.println(resp3);
		}
		else if (resp1 > resp3 && resp3 > resp2) {
			System.out.println("Maior:");
			System.out.println(resp1);
			System.out.println("Menor:");
			System.out.println(resp2);
		} 
		else if (resp2 > resp1 && resp1 > resp3){
			System.out.println("Maior:");
			System.out.println(resp2);
			System.out.println("Menor:");
			System.out.println(resp3);
		} 
		else if (resp2 > resp3 && resp3 > resp1){
			System.out.println("Maior:");
			System.out.println(resp2);
			System.out.println("Menor:");
			System.out.println(resp1);
		} 
		else if (resp3 > resp2 && resp2 > resp1){
			System.out.println("Maior:");
			System.out.println(resp3);
			System.out.println("Menor:");
			System.out.println(resp1);
		}
		else if (resp3 > resp1 && resp1 > resp2){
			System.out.println("Maior:");
			System.out.println(resp3);
			System.out.println("Menor:");
			System.out.println(resp2);
		} 
	}
}
		
					
				
			
		
	
