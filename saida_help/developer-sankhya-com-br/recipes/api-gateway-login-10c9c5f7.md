---
id: "https://developer.sankhya.com.br/recipes/api-gateway-login"
titulo: "API Gateway - Login"
url: "https://developer.sankhya.com.br/recipes/api-gateway-login"
atualizado_em: "2025-11-10T23:38:32.000Z"
---

# API Gateway - Login

```java Java
try {
  URL url = new URL("https://api.sankhya.com.br/login");
  HttpURLConnection conn = (HttpURLConnection) url.openConnection();

  conn.setRequestMethod("POST");
  conn.setRequestProperty("Content-Type", "application/json");
  conn.setRequestProperty("appkey"  , "db654b42-ea7f-11ed-a05b-0242ac120003");
  conn.setRequestProperty("token"   , "8fedf240-ea7f-11ed-a05b-0242ac120003");
  conn.setRequestProperty("username", "email.sankhya.id@valido.com");
  conn.setRequestProperty("password", "sua.senha.sankhya.id");
  conn.setDoOutput(true);

  if (conn.getResponseCode() == HttpURLConnection.HTTP_OK) {
    BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
    String inputLine;
    StringBuilder response = new StringBuilder();

    while ((inputLine = br.readLine()) != null) {
      response.append(inputLine);
    }
    br.close();
    ObjectMapper mapper = new ObjectMapper();
    try {
      this.setToken(mapper.readValue(response.toString(), Token.class));
    } catch (JsonProcessingException e) {
      throw new RuntimeException(e);
    }
  }
  conn.disconnect();
} catch (Exception e) {
  e.printStackTrace();
}
```

```json Response Example
{"success":true}
```

# URL para fazer login via API Gateway

<!-- java@2 -->

Indique aqui a URL para fazer login via API Gateway Sankhya

# Criando a conexão

<!-- java@3 -->

Cria uma conexão

# Configuração da requisição

<!-- java@5-11 -->

Configurando o cabeçalho da requisição inserindo as credenciais de acesso (AppKey, Token, usuário e senha SankhyaID).

# Valida status code da requisição de login

<!-- java@13 -->

Verifica se o retorno foi 200 com a constante HTTP_OK.

# Obtem a mensagem de retorno

<!-- java@14-20 -->

Guarda na variável "br" o retorno da requisição. Em seguida, converte o conteúdo para a variável local "response".

# Obtem token de autenticação

<!-- java@24 -->

Obtem o "bearerToken" da requisição e armazena na aplicação.
