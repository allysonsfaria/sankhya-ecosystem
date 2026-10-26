# Autenticação e Gestão de Sessão (APIs Sankhya OM)

O Sankhya disponibiliza duas formas principais de autenticação para integrações externas: o Barramento de Serviços Tradicional (`/mge/service.sbr`) e o API Gateway moderno.

---

## 1. Barramento Tradicional (/mge/service.sbr) — MobileLoginSP.login

Utilizado para chamadas XML ou JSON diretas ao servidor de aplicação (`port 8180` ou proxy reverso).

### Endpoint:
`POST https://seu-sankhya.com.br/mge/service.sbr?serviceName=MobileLoginSP.login&outputType=json`

### Payload JSON:
```json
{
  "serviceName": "MobileLoginSP.login",
  "requestBody": {
    "NOMUSU": { "$": "INTEGRADOR" },
    "INTERNO": { "$": "SenhaSegura123" },
    "KEEPCONNECTED": { "$": "S" }
  }
}
```

### Resposta de Sucesso:
```json
{
  "serviceName": "MobileLoginSP.login",
  "status": "1",
  "responseBody": {
    "jsessionid": { "$": "A8F92BC81D5..." },
    "ktoken": { "$": "..." },
    "idusu": { "$": "1" }
  }
}
```

> **Atenção:** Em todas as requisições subsequentes, envie o cookie de sessão retornado:
> `Cookie: JSESSIONID=A8F92BC81D5...`

---

## 2. API Gateway Moderno (developer.sankhya.com.br)

Utilizado em soluções integradas através do gateway central ou marketplace.

### Endpoint de Login:
`POST https://api.sankhya.com.br/login`

### Headers:
```http
Content-Type: application/json
appkey: {seu-app-key-uuid}
token: {seu-token-integracao-uuid}
username: email.sankhya.id@empresa.com.br
password: {senha-do-sankhya-id}
```

### Resposta:
Retorna `bearerToken` JWT que deve ser enviado no cabeçalho `Authorization: Bearer <token>` com validade definida (renovar antes de expirar).

---

## 3. Boas Práticas de Conexão
1. **Reaproveitamento de Sessão**: NUNCA realize login a cada requisição individual. Mantenha o `JSESSIONID` ou Bearer Token em cache de aplicação.
2. **Tratamento de Sessão Expirada**: Capture HTTP 401 ou retorno com `status="0"` indicando sessão inválida, renove o token e repita a requisição (retry pattern).
3. **Logout**: Chame `MobileLoginSP.logout` ou o endpoint de logout do gateway ao desligar a aplicação integradora para liberar conexões do pool.
