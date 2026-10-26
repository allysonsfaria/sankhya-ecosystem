---
id: "27972005552663"
titulo: "Chamar API - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27972005552663-Chamar-API-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Ações e automações"
atualizado_em: "2026-09-23T17:37:00Z"
rotulos: ["Configuração", "Segurança", "Integração", "API", "Analytics Studio", "Documentos Eletrônicos"]
---

# Chamar API - Analytics Studio

O passo de ação Chamar API permite que os usuários executem chamadas HTTP REST utilizando dados dinâmicos obtidos a partir das views configuradas no [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio). Cada linha gerada na view representa uma chamada de API, onde as variáveis configuradas no body, headers ou URL serão substituídas pelos valores correspondentes da linha. Caso uma view não seja configurada, será executada uma única chamada, sem a utilização de variáveis.

![Imagem 1: O passo de ação Chamar API permite que os usuários executem chamadas HTTP REST utilizando dados dinâmicos obtidos a…](https://ajuda.sankhya.com.br/hc/article_attachments/27972794452759)

---

### Funcionamento

- **Configuração da View (Opcional):** o usuário pode configurar uma view utilizando SQL, para selecionar os dados que deseja utilizar nas chamadas de API. Cada coluna da view se torna uma variável disponível para ser utilizada na configuração da chamada de API. Se nenhuma view for configurada, a chamada será realizada uma única vez, sem a utilização de variáveis.
- **Uso das Variáveis:** as variáveis das colunas podem ser utilizadas no body, headers ou URL da chamada de API, utilizando o formato $nome\_da\_variavel, onde nome\_da\_variavel é o nome da coluna da view, sempre em letras minúsculas. Exemplo:

Para uma coluna chamada ID\_CLIENTE, a variável será $id\_cliente.

- **Body Personalizado:**
  - **Com Body Personalizado:** se o usuário ativar a marcação **"Habilitar body personalizado"**, ele pode criar um corpo de requisição customizado, utilizando as variáveis da view.
  - **Sem Body Personalizado:** caso a marcação não seja ativada, o body padrão será gerado automaticamente com base nos campos e valores retornados pela view, seguindo o formato JSON.
- **Execução:** para cada linha retornada pela view, será realizada uma nova chamada de API, substituindo as variáveis pelos valores correspondentes da linha. Se não houver view configurada, apenas uma chamada será realizada com o body padrão ou personalizado.
- **Registro de Logs:** todas as chamadas realizadas são registradas na tabela INT\_HTTP\_REQUEST\_LOG, permitindo que o usuário acompanhe o status e resultado de cada chamada.

### Estrutura de Configuração

#### Tipo de Chamada

- **GET:** recupera informações de um endpoint.
- **POST:** cria um novo registro no endpoint.
- **PUT:** atualiza um registro existente.
- **DELETE:** remove um registro existente.

#### URL

Informe a URL do endpoint que deseja acessar. Exemplo:

<https://api.exemplo.com/v1/clientes> 

#### Headers

Adicione os headers necessários para a autenticação e formatação da requisição. Por exemplo:

- **Content-Type:** application/json
- **Authorization:** Bearer $api\_key

#### Body

Informe o corpo da requisição no formato JSON. Utilize as variáveis geradas pela view para dinamizar os dados enviados.

- **Com Body Personalizado Ativado:** por exemplo:

```
{

  "cliente_id": "$id_cliente",

  "nome": "$nome_cliente",

  "email": "$email_cliente"

}
```

- **Sem Body Personalizado:** o body será gerado automaticamente com base nos campos e valores da view. Se a view retornar os seguintes dados:

![Imagem 2: Sem Body Personalizado: o body será gerado automaticamente com base nos campos e valores da view. Se a view retornar os…](https://ajuda.sankhya.com.br/hc/article_attachments/27972797938839)

O body de cada chamada será:

```
{

  "id_cliente": "1",

  "nome_cliente": "João da Silva",

  "email_cliente": "joao@example.com"

}

{

  "id_cliente": "2",

  "nome_cliente": "Maria Souza",

  "email_cliente": "maria@example.com"

}
```

#### Variáveis Disponíveis

Após configurar a view, todas as colunas retornadas estarão disponíveis como variáveis, com os nomes das colunas convertidos para minúsculas. Utilize o nome exato das colunas prefixadas com $ para utilizá-las na configuração. Exemplo prático:

**Configuração da View:**

```
SELECT 

  ID AS ID_CLIENTE, 

  NOME AS NOME_CLIENTE, 

  EMAIL AS EMAIL_CLIENTE 

FROM 

  CAD_CLIENTES 

WHERE 

  STATUS = 'ATIVO'
```

**Configuração da Chamada de API:**

- **Tipo de Chamada:** POST
- **URL:** <https://api.exemplo.com/v1/clientes>
- **Headers:**
  - **Content-Type:** application/json
  - **Authorization:** Bearer $api\_key

- **Body (Com Body Personalizado Ativado):**

```
{

  "id": "$id_cliente",

  "nome": "$nome_cliente",

  "email": "$email_cliente"

}
```

#### Logs de Requisição

Todos os logs de chamadas serão armazenados na tabela INT\_HTTP\_REQUEST\_LOG, contendo informações como:

- **ID:** identificador único do log.
- **DHREQUEST:** data e hora da requisição.
- **DHRESPONSE:** data e hora da resposta.
- **REQUESTBODY:** corpo da requisição enviada.
- **RESPONSEBODY:** corpo da resposta recebida.
- **HTTPSTATUSCODE:** código de status HTTP retornado.
- **STATUS:** status da execução da chamada (concluído, erro, entre outras).

### Considerações Finais

- **Tratamento de Erros:** sempre verifique o status das chamadas nas tabelas de log para identificar possíveis erros e realizar correções nas configurações.
- **Segurança:** mantenha as chaves de API e outros dados sensíveis protegidos e configure permissões adequadas para o acesso às views.

---

![Imagem 3: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157369727639) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
