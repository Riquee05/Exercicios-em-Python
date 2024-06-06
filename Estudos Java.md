Nível Iniciante:
Hello World:


    public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
    }

Exercício Básico:


    public class Calculadora {
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 5;
        
        int soma = num1 + num2;
        int subtracao = num1 - num2;
        int multiplicacao = num1 * num2;
        double divisao = (double) num1 / num2; // Convertendo um dos operandos para double para obter resultado com ponto flutuante
        
        System.out.println("Soma: " + soma);
        System.out.println("Subtração: " + subtracao);
        System.out.println("Multiplicação: " + multiplicacao);
        System.out.println("Divisão: " + divisao);
    }
    }

Nível Intermediário:
Exercício de Estruturas de Dados:


    import util.ArrayList;

    public class ListaNomes {
    public static void main(String[] args) {
        ArrayList<String> nomes = new ArrayList<>();
        
        // Adicionando nomes à lista
        nomes.add("Alice");
        nomes.add("Bob");
        nomes.add("Carol");
        
        // Iterando e imprimindo os nomes
        for (String nome : nomes) {
            System.out.println(nome);
        }
    }
    }

Projeto Pequeno (Cadastro de Pessoas):


    public class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }
    }

    import util.ArrayList;

    public class CadastroPessoas {
    public static void main(String[] args) {
        ArrayList<Pessoa> pessoas = new ArrayList<>();
        
        // Criando algumas pessoas e adicionando ao cadastro
        pessoas.add(new Pessoa("Alice", 25));
        pessoas.add(new Pessoa("Bob", 30));
        pessoas.add(new Pessoa("Carol", 35));
        
        // Iterando e imprimindo as pessoas cadastradas
        for (Pessoa pessoa : pessoas) {
            System.out.println("Nome: " + pessoa.getNome() + ", Idade: " + pessoa.getIdade());
        }
    }
    }

Nível Avançado:
Tratamento de Exceções:


    public class Divisao {
    public static void main(String[] args) {
        int dividendo = 10;
        int divisor = 0;
        
        try {
            int resultado = dividendo / divisor;
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Erro: divisão por zero.");
        }
    }
    }

Concorrência em Java (Threads):


    public class Contador extends Thread {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(Thread.currentThread().getName() + ": " + i);
            try {
                Thread.sleep(1000); // Aguarda 1 segundo
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        Contador t1 = new Contador();
        Contador t2 = new Contador();
        
        t1.setName("Thread 1");
        t2.setName("Thread 2");
        
        t1.start();
        t2.start();
    }
    }

Estes são apenas exemplos simples para cada nível. Você pode expandir esses exemplos e criar projetos mais complexos à medida que avança em seu aprendizado em Java.