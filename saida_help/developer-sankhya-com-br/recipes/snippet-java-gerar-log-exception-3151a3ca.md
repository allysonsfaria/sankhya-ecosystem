---
id: "https://developer.sankhya.com.br/recipes/snippet-java-gerar-log-exception"
titulo: "Snippet Java- Gerar LOG Exception"
url: "https://developer.sankhya.com.br/recipes/snippet-java-gerar-log-exception"
atualizado_em: "2025-11-10T23:38:36.000Z"
---

# Snippet Java- Gerar LOG Exception

```java Java
try{
		//funcionalidades que podem por ventura gerar um erro a ser tratado.
}catch(Exception e){
	StringWriter sw = new StringWriter();
	PrintWriter pw = new PrintWriter(sw);
	e.printStackTrace(pw);
	System.out.println(sw.toString());
}
```

```json Response Example
{"success":true}
```

# Try catch

<!-- java@1-8 -->

try catch padrão

# Atribuição do erro

<!-- java@3 -->

Qualquer erro entrará no try catch

# Objeto que guardará a string

<!-- java@4 -->

StringWriter sw, recebe a string do erro.

# PrintWriter - Processamento do stratcktracer

<!-- java@5 -->

PrintWriter processa o stratcktracer

# PrintStackTrace - impressão

<!-- java@6 -->

por padrão o printStackTrace é executado sem passar argumento

# Tratamento da string - impressão no console da string gerada.

<!-- java@7 -->

Tratamento da string - impressão no console da string gerada, além de imprimir a mesma pode ser salva em uma tabela de LOG's para ser acessada em outros momentos
