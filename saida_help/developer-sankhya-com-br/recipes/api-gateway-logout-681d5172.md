---
id: "https://developer.sankhya.com.br/recipes/api-gateway-logout"
titulo: "API Gateway - Logout"
url: "https://developer.sankhya.com.br/recipes/api-gateway-logout"
atualizado_em: "2025-11-10T23:38:47.000Z"
---

# API Gateway - Logout

```java Java
try {
  URL url = new URL("https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=MobileLoginSP.logout&outputType=json");
  HttpURLConnection conn = (HttpURLConnection) url.openConnection();

  conn.setRequestMethod("GET");
  conn.setRequestProperty("Content-Type", "application/json");
  conn.setRequestProperty("appkey", "db654b42-ea7f-11ed-a05b-0242ac120003");
  conn.setRequestProperty("Authorization", "Bearer " + this.token.getBearerToken());
  conn.setDoOutput(true);

  if (conn.getResponseCode() == HttpURLConnection.HTTP_OK) {
    System.out.println(new Date() + " - Logoff realizado com sucesso!");
  }
  else {
    System.out.println(new Date() + " - Erro " + conn.getResponseCode() + " ao tentar fazer Logoff!");
  }

  conn.disconnect();

} catch (Exception e) {
  e.printStackTrace();
}
```

```json Response Example
{"success":true}
```

# URL para fazer logout via API Gateway

<!-- java@2 -->

Indique aqui a URL para fazer logout via API Gateway Sankhya.

# Criando a conexão

<!-- java@3 -->

Cria uma conexão

# Configuração da requisição

<!-- java@5-9 -->

Configurando o cabeçalho da requisição inserindo as credenciais de acesso (AppKey e BearerToken).

# Valida status code da requisição de login

<!-- java@11-12 -->

Verifica se o retorno foi 200 com a constante HTTP_OK e confirma Logout
