---
id: "34875102231063"
titulo: "Setup inicial de integração Sankhya <> Pontotel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com a Pontotel"
atualizado_em: "2026-09-26T01:41:03Z"
rotulos: ["Configuração", "Configurações Gateway", "Pontotel", "API integração Sankhya", "Setup inicial", "Módulo de integração", "Integração Sankhya <> Pontotel", "Sankhya", "Admin"]
---

# Setup inicial de integração Sankhya <> Pontotel

**Módulo**: Admin (Gestão Pontotel)
**Caminho de Acesso**: Menu Principal > Admin > Integração > Módulo de Integração

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#1-descri%C3%A7%C3%A3o-da-funcionalidade)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#2-pr%C3%A9-requisitos)
- [3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#4-jornada-de-uso)
- [4. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#5-pontos-de-aten%C3%A7%C3%A3o)
- [5. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#6-dicas-de-usabilidade)
- [6. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#faq-%E2%80%93-d%C3%BAvidas-frequentes)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O Módulo de Integração permite ao cliente realizar o setup inicial dos fluxos de integração entre **Sankhya** e **Pontotel**, de forma autônoma e centralizada. 

O usuário insere credenciais e configurações básicas, valida as informações e acompanha o status das integrações em ondas evolutivas (setup, parametrizações, pré-visualizações e ativações). 

Atualmente, estão disponíveis fluxos de integração de cadastros que enviam e recebem dados entre Sankhya e Pontotel. Eles abrangem:

- Empregadores;
- Empregados;
- Usuários;
- Locais de trabalho;
- Escalas e jornadas;
- Apontamentos e Faltas;
- Ocorrências e Afastamentos;
- Férias.

As integrações permitem que os dados entre Sankhya e Pontotel sejam refletidos de forma mais rápida e eficiente, trazendo benefícios como:

- **sincronização imediata** - não é preciso esperar o agendamento a cada 12 horas;
- **maior desempenho** - são processados apenas os dados alterados desde a última sincronização bem-sucedida, acelerando o fluxo.

### 2. Pré-requisitos

- **Permissões necessárias**
  - Acesso ao menu Admin > Integração (RH, TI ou Implantação).
  - Permissão para editar configurações do account do cliente.
- **Parâmetros essenciais**
  - Usuário Sankhya SK, Senha SK, Token SK.
  - CPF do responsável pela integração.
  - Domínio corporativo de e-mail (opcional).
  - URL base Sankhya (informativa).
- **Configurações relacionadas**
  - Token válido e URL atualizada no [Gateway](https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway).
  - Processo de criação de tenants na LinkAPI (temporário)

### 3. Jornada de Uso

1. O usuário acessa Menu Principal > Admin > Integração > Módulo de Integração.

2. Preenche o formulário com:

- Usuário Sankhya (SK)
- Senha Sankhya (SK)
- Token Sankhya (SK)
- CPF do responsável pela integração
- Domínio corporativo
- URL base Sankhya (opcional)

3. Consulta os informativos ("i") ao lado dos campos para instruções.

4. Envia o formulário. 

5. O sistema valida as credenciais via Gateway.

- Quando válido, cria um card no Trello e inicia a criação do tenant (LinkAPI).
- Se inválido, o usuário recebe um feedback de erro e instruções para correção.

6. O usuário acompanha as notificações e status via Trello.

7. Nas ondas seguintes, realiza as parametrizações e valida as pré-visualizações antes de ativar cada fluxo.

### 4. Pontos de Atenção

- O fluxo inicial é liberado primeiro para Implantação (SC), depois para clientes.
- O usuário de integração é gerado com padrão (ex.: integcliente@pontotel.com.br).
- Validação falha: deve revisar usuário/senha/token e configuração do gateway.
- A criação do tenant LinkAPI é feita manualmente pelo QA até a internalização.
- A Implantação (SC) precisa de visibilidade das tentativas para apoiar clientes.

### 5. Dicas de Usabilidade

- Ter credenciais Sankhya e CPF do responsável em mãos antes de abrir o formulário.
- Usar o ícone ("i") para instruções rápidas de onde buscar os dados.
- Garantir liberação dos IPs do serviço no firewall antes de testar.
- Salvar prints de erros para facilitar diagnósticos.
- Acompanhar o card no Trello para status da validação.

### 6. Casos de Uso

✅ **Exemplo real:** 

RH preenche credenciais corretas e CPF; sistema valida e cria o tenant; cliente recebe confirmação e parametriza regras.

❌ **Erro comum:** 

TI informa token incorreto; validação falha e mensagem orienta correção do token.

## FAQ – Dúvidas Frequentes

1. **Quem deve preencher o formulário de integração?**

   RH (com apoio do TI) deve preencher as informações iniciais. TI precisa garantir gateway e token.
2. **O que faço se a validação das credenciais falhar?**

   Verifique usuário, senha e token. Peça ao TI para confirmar gateway e liberar acesso de rede. Em caso de dúvida, abra chamado com implantação/SC.
3. **O que acontece depois que envio o formulário com sucesso?**

   O sistema valida as credenciais, cria card para validação e inicia criação do tenant (temporário); nas ondas seguintes, você parametriza e valida pré-visualizações.
4. **Posso fazer todo o setup sozinho?**

   Sim, o módulo foi criado para dar autonomia. Alguns passos (gateway, token, liberações de rede) requerem suporte do TI.
5. **E a LinkAPI?**

   A criação de tenants na LinkAPI é tratada manualmente pelo QA até internalização do processo.

## Artigos Relacionados

- [Integração de Empresas Sankhya x Empregadores Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919)
- [Integração de Funcionários Sankhya x Empregados Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031)
- [Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207)
- [Integração de Escalas Pontotel e Carga Horária Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887)
- [Integração de Férias Sankhya x Férias Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023)
- [Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959)
- [Integração de Usuários (Sankhya) x Usuários (Pontotel)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951)
- [Integração de Apontamentos e Faltas Pontotel x Verbas e Faltas Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/35056595712279)
