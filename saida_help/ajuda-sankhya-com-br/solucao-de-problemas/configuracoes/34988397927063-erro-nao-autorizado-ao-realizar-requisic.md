---
id: "34988397927063"
titulo: "Erro \"Não autorizado\" ao realizar requisições via API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34988397927063-Erro-N%C3%A3o-autorizado-ao-realizar-requisi%C3%A7%C3%B5es-via-API"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-20T23:56:54Z"
rotulos: ["Configuração", "Requisições", "Segurança", "API", "Erro", "Não Autorizado", "Erro \"Não autorizado\" ao realizar requisições via API", "Tabela de Acessos por Entidade", "Authorization Layer", "Squad Plataforma"]
---

# Erro "Não autorizado" ao realizar requisições via API

##### MENSAGEM:

##### Erro "Não autorizado" ao realizar requisições via API

**SITUAÇÃO:**

O erro ocorre quando o usuário integrador configurado no cadastro da aplicação Gateway não possui as permissões necessárias para acessar a rotina utilizada na integração.

Atualmente, o Sankhya possui **duas configurações de autorização para consumo de APIs**:

1. **Authorization Layer**: camada de autorização que valida se o usuário integrador possui permissão explícita para consumir os serviços via API.
2. **Autorização de API (tela específica)**: permite controlar, de forma centralizada, quais APIs e serviços cada usuário poderá acessar.

Quando uma dessas camadas está ativa e o usuário não possui as permissões exigidas, a requisição é bloqueada e o sistema retorna o erro "Não autorizado".

Esse mecanismo aumenta a segurança e garante maior controle sobre o acesso às integrações.

**Para mais informações sobre cada tipo de autorização, consulte:**

- [**Authorization Layer**](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API)
- [**Autorização de API**](https://ajuda.sankhya.com.br/hc/pt-br/articles/34162979696663-Como-controlar-o-acesso-de-usu%C3%A1rios-%C3%A0s-APIs-utilizando-a-tela-Autoriza%C3%A7%C3%A3o-de-API)

##### SOLUÇÃO:

Antes de realizar as liberações, identifique **qual configuração de autorização está ativa no ambiente**, pois o tratamento é diferente para cada cenário.

### Authorization Layer

Quando a **Authorization Layer** está ativa, as liberações devem ser realizadas pelas **rotinas do sistema**.

**(1)** Consulte a documentação **"Tabela de Acessos por Entidade"** para identificar quais entidades estão envolvidas na rotina que será consumida via API.

**(2)** Verifique quais **telas/rotinas** precisam ser liberadas para o usuário integrador.

- Exemplo 1: Para consultas ou cadastros na entidade **cabecalhoNota (TGFCAB)**, libere as rotinas relacionadas a pedidos, documentos ou faturamento.
- Exemplo 2: Para a entidade **AjustesDocumentos (TGFAJD)**, conceda acesso a telas como:

  - Cadastro Livro ICMS/IPI (Livros Fiscais » Arquivos » Cadastro Livro ICMS/IPI)
  - FUST/FUNTTEL (Livros Fiscais » Arquivos » FUST/FUNTTEL)

**(3)** Libere as permissões necessárias ao usuário integrador pela tela **Acessos** (Configurações » Controle de Acesso » Acessos).

### Autorização de API

Quando a configuração ativa for a **Autorização de API**, a liberação **não é feita pelas rotinas**.

Nesse caso, o acesso deve ser concedido diretamente na tela **Autorização de API**, onde o administrador define:

- Quais APIs ou serviços o usuário integrador pode consumir;
- Quais métodos estarão autorizados.

Mesmo que o usuário possua permissão nas rotinas do sistema, sem a liberação na tela **Autorização de API**, a requisição será bloqueada.

##### CAUSA:

O erro ocorre por falta de autorização do usuário integrador para acessar a rotina ou serviço da integração.

Mesmo com autenticação válida, a requisição será bloqueada quando:

- A **Authorization Layer** estiver ativa e o usuário não possuir permissão nas rotinas necessárias;
- A **Autorização de API** estiver ativa e o serviço não estiver liberado na tela específica;

O erro "Não autorizado" não indica falha técnica na API, mas sim um bloqueio intencional das camadas de segurança.

Após conceder corretamente as permissões conforme o tipo de autorização ativa, as requisições via API passam a ser processadas normalmente.
