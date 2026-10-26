---
id: "https://developer.sankhya.com.br/recipes/jape-date-to-string"
titulo: "Jape - Date to String"
url: "https://developer.sankhya.com.br/recipes/jape-date-to-string"
atualizado_em: "2025-11-10T23:38:33.000Z"
---

# Jape - Date to String

```java Java
private void dateToString() {
		try {
			SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss");
			String string  = dateFormat.format(new Date());
			System.out.println(string);
		} catch (Exception e) { //this generic but you can control another types of exception
			e.printStackTrace();
		}

	}
```

```json Response Example
{"success":true}
```

# Definição da máscara da string

<!-- java@3 -->

Definição da máscara da string ("dd-MM-yyyy HH:mm:ss")

# Definição da data que será formatada

<!-- java@4 -->

Definição da data que será formatada, 
new Date() data atual.

# Impressão da string no console

<!-- java@5 -->

A data será impressa no console em formato de string.

# Finalização

<!-- java@10 -->
