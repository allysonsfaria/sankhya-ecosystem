---
id: "https://developer.sankhya.com.br/recipes/jape-string-to-timestamp"
titulo: "Jape - String to Timestamp"
url: "https://developer.sankhya.com.br/recipes/jape-string-to-timestamp"
atualizado_em: "2025-11-10T23:38:33.000Z"
---

# Jape - String to Timestamp

```java Java
private void stringToTimestamp() {
		String dateFormatPattern = "yyyy-MM-dd hh:mm:ss.SSS";
		String dateString = "2021-04-22 08:28:35.0";
		try {
			SimpleDateFormat dateFormat = new SimpleDateFormat(dateFormatPattern);
			Date parsedDate = dateFormat.parse(dateString);
			Timestamp timestamp = new Timestamp(parsedDate.getTime());
			System.out.println(timestamp);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
```

```json Response Example
{"success":true}
```

# Entrada do parâmetro de representação

<!-- java@2 -->

Entrada do parâmetro de representação da data,

# String com a data propriamente dita

<!-- java@3 -->

String com a data propriamente dita

# Try catch - Prevenção de erros

<!-- java@4-9 -->

Por padrão. é criado um try catch para garantir que a sessão será fechada, prevenindo erros.

# Atribuição do SimpleDateFormat

<!-- java@5 -->

Atribuição do SimpleDateFormat

# Parseamento da data através do dateformat

<!-- java@6 -->

Parseamento da data através do dateformat  informado, dateString = "2021-04-22 08:28:35.0";

# Conversão do date em Timestamp

<!-- java@7 -->

Conversão do date em Timestamp - Timestamp padrão mais utilizado pela Sankhya

# Finalização

<!-- java@10 -->

Time stamp já definido. programa concluído;
