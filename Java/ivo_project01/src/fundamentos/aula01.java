package fundamentos;
import java.util.Scanner;

public class aula01 {
	public static void main(String[] args) {
	}
}

class OperadorExemplo{
	public static void main(String[] args) {
		int a = 10;
		int b = 10;
		System.out.println(a++ + ++a);
		System.out.println(a);
		System.out.println(b++ + b++);
		System.out.println(b);
	}
}

class OperadorExemplo2{
	public static void main(String[] args) {
		int c = 10;
		int d = -10;
		boolean e = true;
		boolean f = false;
		System.out.println(~c);
		System.out.println(~d);
		System.out.println(!e);
		System.out.println(!f);
	}
}

class soma{
	public static void main(String[] args) {
		int x = 3;
		int y = 4;
		int z = 7;
		System.out.println((x + y)/z);
		System.out.println(!((x > y) && (x < z)));
		if(x++ >= y) {
			System.out.println(--z);
		}
		else {
			System.out.println(z++);
		}
	}
}

class ifelse{
	public static void main(String[] args) {
		int idade = 15;
		if (idade < 18) {
			System.out.println("Não pode entrar.");
		}
		else {
			System.out.println("Pode entrar.");
		}
	}
}

class inputteste{
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um número: ");
		double resp = entrada.nextDouble();
		System.out.println(resp);
	}
}

class positivonegativo{
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um número: ");
		double resp = entrada.nextDouble();
		if (resp > 0) {
			System.out.println("Positivo");
		}
		else {
			System.out.println("Negativo");
		}
	}
}

class maiormenor{
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

class diasdasemana{
	public static void main(String[] args) {
		Scanner entrada1 = new Scanner(System.in);
		System.out.println("Digite um número: ");
		double resp = entrada1.nextDouble();
		if (resp == 1) {
			System.out.println("Domingo");
		}
		else if (resp == 2) {
			System.out.println("Segunda-Feira");
		}
		else if (resp == 3) {
			System.out.println("Terça-Feira");
		}
		else if (resp == 4) {
			System.out.println("Quarta-Feira");
		}
		else if (resp == 5) {
			System.out.println("Quinta-Feira");
		}
		else if (resp == 6) {
			System.out.println("Sexta-Feira");
		}
		else if (resp == 7) {
			System.out.println("Sábado");
		}
		else {
			System.out.println("Valor inválido.");
		}
	}
}

class mediadenotas{
	public static void main(String[] args) {
		Scanner entrada1 = new Scanner(System.in);
		System.out.println("Nota 1: ");
		double nota1 = entrada1.nextDouble();
		do {
			Scanner entrada1 = new Scanner(System.in);
			System.out.println("Nota 1: ");
			double nota1 = entrada1.nextDouble();
		} while (nota1 <= 10 && nota1 >= 0);
		
		Scanner entrada2 = new Scanner(System.in);
		System.out.println("Nota 2: ");
		double nota2 = entrada2.nextDouble();
		do {
			Scanner entrada2 = new Scanner(System.in);
			System.out.println("Nota 1: ");
			double nota2 = entrada2.nextDouble();
		} while (nota1 <= 10 && nota1 >= 0);
		
		System.out.println("Média:");
		System.out.println((nota1 + nota2)/2);
				
	}
}

