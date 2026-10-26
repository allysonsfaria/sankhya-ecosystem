---
id: "34944782141207"
titulo: "Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com a Pontotel"
atualizado_em: "2026-09-26T01:41:18Z"
rotulos: ["Configuração", "Departamento", "Integração", "ID: br.com.sankhya.cadastro.funcionarios", "LOGTABOPER", "Pontotel", "Integração Sankhya <> Pontotel", "Log de Alterações do Gateway", "Pessoas+", "Cidade de Trabalho"]
---

# Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)

**Módulo**: Pessoas+ / Integrações
**Caminho de Acesso**: Menu Principal > Integrações > Cadastro de Locais de Trabalho

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#1-descri%C3%A7%C3%A3o-da-funcionalidade)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#2-pr%C3%A9-requisitos)
- [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#3-diagrama-de-fluxo)
- [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#4-jornada-de-uso)
- [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#5-pontos-de-aten%C3%A7%C3%A3o)
- [6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#6-dicas-de-usabilidade)
- [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#faq-%E2%80%93-d%C3%BAvidas-frequentes)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207-Integra%C3%A7%C3%A3o-de-Locais-de-Trabalho-Sankhya-x-Pontotel-Departamento-Cidade-de-Trabalho#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **integração automatiza o cadastro e atualização dos Locais de Trabalho na Pontotel**, a partir da combinação Departamento + Cidade de Trabalho **dos funcionários cadastrados na Sankhya**. 

O processo garante que os locais estejam sempre sincronizados, facilitando a associação correta dos empregados para registro de ponto e eliminando erros manuais. 

A integração ocorre automaticamente a cada 12 horas, trazendo agilidade e precisão para a gestão dos locais.

### 2. Pré-requisitos

- **Permissões necessárias**
  - Ter contratado e implementado o Pessoal+ e também o Sankhya Om;
  - Ter realizado o [setup de integração Sankhya/Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063).
- **Parâmetros essenciais**
  - Habilitação do recurso Log de Alterações do Gateway (parâmetro LOGTABOPER - Ativar armazenamento de log de modificações em tab = ligado na tela Preferências do Sankhya Om).
  - Funcionários devem possuir controle de ponto e associação de Departamento + Cidade de Trabalho correspondentes.
  - Não pode existir outro local previamente cadastrado na Pontotel com o mesmo código (CODDEP+CODCIDTRAB) na Sankhya.
  - Cadastro das cidades na Sankhya deve estar correto e sem inconsistências.
- **Configurações relacionadas**
  - Base Sankhya online e responsiva durante as consultas.
  - Token válido e URL atualizada no [Gateway](https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway).

### 3. Diagrama de fluxo

![Imagem 1: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/34944837165079)

### 4. Jornada de Uso

**4.1. Cadastro/Alteração de funcionário na Sankhya**

- O usuário preenche **Departamento** e **Cidade de Trabalho** no cadastro do colaborador.

  ![Imagem 2: O usuário preenche Departamento e Cidade de Trabalho no cadastro do colaborador.](https://ajuda.sankhya.com.br/hc/article_attachments/34952956343575)

**4.2. Execução automática da integração**

- A cada 12 horas, o sistema verifica colaboradores elegíveis e sincroniza os Locais de Trabalho na Pontotel.

**4.3. Atualização do cadastro de locais na Pontotel**

- Novos locais são criados ou atualizados conforme as informações do Sankhya Om.

  ![Imagem 3: Novos locais são criados ou atualizados conforme as informações do Sankhya Om.](https://ajuda.sankhya.com.br/hc/article_attachments/34952963271319)

**4.4. Associação de empregados**

- Os colaboradores são vinculados ao local correspondente, garantindo o registro de ponto correto.

**4.5. Campos integrados: departamento e cidade de trabalho (Sankhya) → local de trabalho (Pontotel)**

| **Campo Sankhya** | **Campo Pontotel** | **Descrição** |
| --- | --- | --- |
| Tabelas consultadas no Sankhya: TFPFUN, TFPDEP e TSICID | | |
| CODDEP + CODCIDTRAB -   DESCRDEP - NOMECID | Nome | Concatenação da descrição do código do departamento + código da cidade de trabalho + nome do departamento + cidade de trabalho do empregado. |
| CODDEP + CODCIDTRAB | Código | Concatenação do CODDEP + CODCIDTRAB. |
| UFNOMECID | Estado | UFNOMECID da tabela de cidades, associada ao CODCIDTRAB. |
| NOMECID | Cidade | Identificado na tabela de cidades pelo código da cidade de trabalho atribuída ao funcionário. |
| - | Sobreaviso | Cria como possui sobreaviso, mas não atualiza esse campo. |
| - | Empregadores | Associa a todos os empregadores ativos   na Pontotel na criação. Na atualização, associar a novos empregadores criados, se houver. |
| DESCRDEP - NOMECID - UFNOMECID | Endereço AFD | Concatenação da descrição do departamento + cidade de trabalho do empregado + UF da cidade de trabalho. |
| - | Sincronizar com REPP | Mantém sempre o local sincronizado com o REPP. |
| - | Aparece no acompanhamento | Mantém o local sempre no acompanhamento. |

### 5. Pontos de Atenção

- O código do local (CODDEP+CODCIDTRAB) é o identificador de equivalência entre Sankhya e Pontotel e não deve ser alterado.
- Locais não serão integrados se houver inconsistências no cadastro da cidade de trabalho ou se o campo não estiver preenchido no Sankhya Om.
- Se o local já existir na Pontotel com o mesmo código, os dados serão atualizados.
- A associação do empregado ao local deve ser feita na Sankhya; se o local não for integrado, o cadastro do empregado não será criado/atualizado na Pontotel.
- Alterações que não sensibilizem o log de alterações só serão integradas na execução de consistência diária.

### 6. Dicas de Usabilidade

- Utilizar filtros no Sankhya Om para visualizar funcionários com Departamento e Cidade de Trabalho preenchidos.
- Manter o cadastro das cidades atualizado e padronizado para evitar falhas na integração.
- Verificar periodicamente o status do token e da URL no Gateway para garantir a continuidade da integração.

### 7. Casos de Uso

✅ **Exemplo Real:**
Cadastro de funcionário com Departamento "Administrativo" e Cidade de Trabalho "Goiás". Após a execução da integração, o local "Administrativo - Goiás" é criado automaticamente na Pontotel.

❌ **Erro Comum:**
Funcionário cadastrado sem Cidade de Trabalho preenchida no Sankhya Om. 

Resultado: local não integrado e empregado não criado/atualizado na Pontotel.

## FAQ – Dúvidas Frequentes

1. **Posso integrar locais de trabalho cadastrados apenas com Departamento?**

   Não, é obrigatório preencher também a Cidade de Trabalho.
2. **O que acontece se eu alterar o código do local na Pontotel?**

   A referência de equivalência entre Pontotel e Sankhya será perdida, podendo causar inconsistências.
3. **Locais inativos na Sankhya são excluídos na Pontotel?**

   Não, apenas o status do local é atualizado para inativo.
4. **Preciso cadastrar manualmente locais de trabalho na Pontotel?**

   Apenas se a integração não estiver habilitada ou configurada corretamente.

## Artigos Relacionados

- [Setup inicial de integração Sankhya <> Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063)
- [Integração de Empresas Sankhya x Empregadores Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919)
- [Integração de Funcionários Sankhya x Empregados Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031)
- [Integração de Escalas Pontotel e Carga Horária Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887)
- [Integração de Férias Sankhya x Férias Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023)
- [Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959)
- [Integração de Usuários (Sankhya) x Usuários (Pontotel)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951)
- [Integração de Apontamentos e Faltas Pontotel x Verbas e Faltas Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/35056595712279)
