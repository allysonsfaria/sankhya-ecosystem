---
id: "35006040384023"
titulo: "Integração de Férias Sankhya x Férias Pontotel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com a Pontotel"
atualizado_em: "2026-09-26T01:41:45Z"
rotulos: ["Configuração", "Integração", "ID: br.com.sankhya.rh.ProgramacaoFeriasMais", "Férias", "LOGTABOPER", "Pontotel", "Integração Sankhya <> Pontotel", "Log de Alterações do Gateway", "Pessoas+"]
---

# Integração de Férias Sankhya x Férias Pontotel

**Módulo**: Pessoas+ / Integrações
**Caminho de Acesso**: Menu Principal > Integrações > Férias > Sankhya x Pontotel

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#1-descri%C3%A7%C3%A3o-da-funcionalidade)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#2-pr%C3%A9-requisitos)
- [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#3-diagrama-de-fluxo)
- [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#4-jornada-de-uso)
- [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#5-pontos-de-aten%C3%A7%C3%A3o)
- [6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#6-dicas-de-usabilidade)
- [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#faq-%E2%80%93-d%C3%BAvidas-frequentes)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-Sankhya-x-F%C3%A9rias-Pontotel#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **integração de férias entre Sankhya e Pontotel** automatiza o lançamento, atualização e exclusão de períodos de férias dos colaboradores. 

Os registros feitos no Sankhya Om são sincronizados com a Pontotel, refletindo diretamente na folha de ponto e cadastro do colaborador. O fluxo contempla também a exclusão automática de lançamentos e permite configurar se o colaborador será removido do REP-P durante as férias, garantindo maior controle e agilidade na gestão de jornadas.

### 2. Pré-requisitos

- **Permissões necessárias**
  - Ter contratado e implementado o Pessoal+ e o Sankhya Om.
  - Ter realizado o [setup de integração Sankhya/Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063).
- **Parâmetros essenciais**
  - Habilitação do recurso Log de Alterações do Gateway (parâmetro LOGTABOPER - Ativar armazenamento de log de modificações em tab = ligado na tela Preferências do Sankhya Om).
- **Configurações relacionadas**
  - Base Sankhya online e responsiva durante as consultas.
  - Token válido e URL atualizada no [Gateway](https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway).
  - Folha do colaborador destravada no período a ser abonado.
  - Data de saída das férias preenchida (folha calculada).

### 3. Diagrama de Fluxo

![Imagem 1: 3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/35006040378903)

### 4. Jornada de Uso

**4.1.** O colaborador faz a requisição de férias e aguarda a aprovação da solicitação e o preenchimento da data de saída (folha calculada).

![Imagem 2: 4.1. O colaborador faz a requisição de férias e aguarda a aprovação da solicitação e o preenchimento da data de saída…](https://ajuda.sankhya.com.br/hc/article_attachments/35011007430167)

**4.2.** O sistema sincroniza automaticamente o lançamento para a Pontotel, abonando o período na folha do colaborador.

- Cadastro na Pontotel

  ![Imagem 3: Cadastro na Pontotel](https://ajuda.sankhya.com.br/hc/article_attachments/35011007430935)
- Folha na Pontotel 

  ![Imagem 4: Folha na Pontotel](https://ajuda.sankhya.com.br/hc/article_attachments/35010969830295)

  É possível definir se os lançamentos integrados no cadastro e folha do colaborador devem removê-lo do REP-P durante as férias. Caso seja removido, ele não estará disponível nos coletores para registro de ponto.

O fluxo contempla a criação/atualização e também a exclusão de férias, que devem ser realizadas no Sankhya Om. O lançamento será atualizado ou removido da Pontotel, desde que a folha esteja destravada.

**4.3.** Campos integrados: férias (Sankhya) → férias (Pontotel)

| **Campo Sankhya** | **Campo Pontotel** | **Descrição** |
| --- | --- | --- |
| Tabela consultada no Sankhya: TFPFER | | |
| CODEMP | Código do funcionário | O código do empregador e código do funcionário são utilizados para identificar na Pontotel o empregado cujo período deverá ser abonado. O código do cadastro do empregado na Pontotel deverá ter código igual à concatenação CODEMP+CODFUNC. |
| CODFUNC |
| CODEMP | Código | Código único que identifica o lançamento na Pontotel e permite que o mesmo seja identificado o equivalente no Sankhya. |
| CODFUNC |
| DTINIAQUI |
| SEQUENCIA |
| DTSAIDA | Início | Início do período de férias. |
| DTSAIDA | Fim | Final do período de férias. Note que é considerado DTSAIDA, que deve estar preenchido no Sankhya Om. |
| NUMDIASFER |

### 5. Pontos de Atenção

- Se o cadastro das férias for realizado diretamente na Pontotel e posteriormente cadastrado no Sankhya Om, caso ele seja excluído no Sankhya Om, não refletirá na Pontotel.
- Não é possível lançar férias se houver outros lançamentos sobrepostos (dispensa, afastamento, outras férias).
- Férias sem data de saída ou apenas com data prevista não são integradas.
- Caso a folha esteja travada, é necessário destravá-la para que o lançamento seja integrado ou excluído.

### 6. Dicas de Usabilidade

- Verificar sempre se a folha está destravada antes de lançar ou excluir férias.
- Utilizar filtros para identificar períodos sobrepostos e evitar erros de integração.
- Ativar a configuração de remoção do REP-P para garantir que o colaborador não registre ponto durante as férias.

### 7. Casos de Uso

✅ **Exemplo Real:** 

Lançamento de férias aprovado no Sankhya Om, com data de saída preenchida e folha destravada, refletindo automaticamente na Pontotel.

❌ **Erro Comum:** 

Tentativa de integrar férias com folha travada ou período sobreposto, impedindo a sincronização

## FAQ – Dúvidas Frequentes

1. **O que acontece se a folha estiver travada durante a integração de férias?**

   O lançamento não será integrado ou excluído. É necessário destravar a folha para prosseguir.
2. **Posso atualizar o período de férias diretamente na Pontotel?**

   Não. Alterações devem ser feitas no Sankhya para garantir a sincronização correta.
3. **Como funciona a exclusão de férias?**

   Ao excluir o lançamento no Sankhya, ele será removido automaticamente na Pontotel, desde que a folha esteja destravada.
4. **O colaborador pode registrar ponto durante as férias?**

   Apenas se a configuração de remoção do REP-P não estiver ativada.
5. **Quais campos são integrados entre Sankhya e Pontotel?**

   Código do empregado, período de início e fim das férias, número de dias, e status de abono.

## Artigos Relacionados

- [Setup inicial de integração Sankhya <> Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063)
- [Consulta de Férias](https://ajuda.sankhya.com.br/hc/pt-br/articles/15368063417111)
- [Integração de Empresas Sankhya x Empregadores Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919)
- [Integração de Funcionários Sankhya x Empregados Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031)
- [Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207)
- [Integração de Escalas Pontotel e Carga Horária Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887)
- [Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959)
- [Integração de Usuários (Sankhya) x Usuários (Pontotel)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951)
- [Integração de Apontamentos e Faltas Pontotel x Verbas e Faltas Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/35056595712279)
