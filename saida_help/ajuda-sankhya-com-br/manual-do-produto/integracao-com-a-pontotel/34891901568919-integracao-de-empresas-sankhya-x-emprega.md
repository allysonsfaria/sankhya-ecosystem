---
id: "34891901568919"
titulo: "Integração de Empresas Sankhya x Empregadores Pontotel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com a Pontotel"
atualizado_em: "2026-09-26T01:41:07Z"
rotulos: ["Configuração", "Empresa", "Integração", "Configurações Gateway", "Pontotel", "API integração Sankhya", "Setup inicial", "Módulo de integração", "Integração Sankhya <> Pontotel", "Pessoas+"]
---

# Integração de Empresas Sankhya x Empregadores Pontotel

**Módulo**: Pessoas+ / Integrações
**Caminho de Acesso**: Menu Principal > Integrações > Cadastro de Empresas/Empregadores

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#1-descri%C3%A7%C3%A3o-da-funcionalidade)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#2-pr%C3%A9-requisitos)
- [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#3-diagrama-de-fluxo)
- [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#4-jornada-de-uso)
- [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#5-pontos-de-aten%C3%A7%C3%A3o)
- [6. Dicas de Usabilidade](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/carine.araujo/Downloads/%23%20Integra%C3%A7%C3%A3o%20de%20Empresas%20Sankhya%20x%20Empre.md#6-dicas-de-usabilidade)
- [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#faq-%E2%80%93-d%C3%BAvidas-frequentes)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919-Integra%C3%A7%C3%A3o-de-Empresas-Sankhya-x-Empregadores-Pontotel#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **integração entre empresas cadastradas na Sankhya e empregadores na Pontotel** automatiza o processo de sincronização dos dados, garantindo que as informações estejam sempre atualizadas entre as plataformas.

As empresas criadas, atualizadas ou inativadas no Sankhya Om serão refletidas automaticamente no cadastro de empregadores da Pontotel, agilizando o processo e reduzindo erros manuais. O fluxo contempla empresas com CNPJ e CPF, facilitando o controle e a gestão dos empregadores vinculados aos colaboradores que registram ponto.

### 2. Pré-requisitos

- **Permissões necessárias**
  - Ter contratado e implementado o Pessoal+ e o Sankhya Om;
  - Ter realizado o [setup de integração Sankhya/Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063).
- **Parâmetros essenciais**
  - Habilitação do recurso Log de Alterações do Gateway (parâmetro LOGTABOPER - Ativar armazenamento de log de modificações em tab = ligado na tela Preferências do Sankhya Om).
  - Cadastros das empresas realizados na Sankhya com Índice de optante de registro eletrônico como "1 - Optou pelo registro eletrônico".
- **Configurações relacionadas**
  - Base Sankhya online e responsiva durante as consultas.
  - Token válido e URL atualizada no [Gateway](https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway).

### 3. Diagrama de fluxo

![Imagem 1: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/34891927931927)

### 4. Jornada de Uso

**4.1. Cadastro/Alteração/Inativação de empresa na Sankhya**

- O usuário realiza o cadastro ou atualização de empresas, garantindo que estejam ativas e marcadas como optantes pelo registro eletrônico.

  ![Imagem 2: O usuário realiza o cadastro ou atualização de empresas, garantindo que estejam ativas e marcadas como optantes pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/34892844495255)

**4.2. Execução automática da integração**

- A cada 12 horas, o sistema verifica as empresas elegíveis e sincroniza os dados com a Pontotel.

**4.3. Atualização do cadastro de empregadores na Pontotel**

- Novos empregadores são criados ou atualizados conforme as informações do Sankhya Om.

**4.4. Associação de colaboradores**

- Os colaboradores são vinculados ao empregador correspondente, garantindo que o registro de ponto seja corretamente associado.

**4.5. Campos integrados: empresa (Sankhya) → empregador (Pontotel)**

| **Campo Sankhya** | **Campo Pontotel** | **Descrição** |
| --- | --- | --- |
| Tabelas consultadas no Sankhya: TFPEMP e TSIEMP | | |
| RAZAOSOCIAL | Razão Social | Razão social que aparece no cadastro do empregador na Pontotel. |
| Nome Fantasia | Nome fantasia que aparece no cadastro do empregador na Pontotel. |
| CODEMP | Código | Código que faz a relação de equivalência entre as empresas/empregadores existentes nas bases. |
| CGC | CNPJ | Se for preenchido na Sankhya com um CNPJ, o mesmo refletirá no campo CNPJ do cadastro de empregador na Pontotel. |
| CPF | Se for preenchido na Sankhya com um CPF, o mesmo refletirá no campo CPF do cadastro de empregador na Pontotel. |
| ATIVO | INATIVO | Se estiver ativo, será integrado para Pontotel. Caso seja inativado, no Sankhya (N), será refletido como inativo na Pontotel, se anteriormente integrado. |
| INDOPTREGELETRON | - | Critério de elegibilidade para passar pelo fluxo de integração. |

### 5. Pontos de Atenção

- O campo "código" é o identificador de equivalência entre Sankhya e Pontotel e não deve ser alterado.
- Empresas sem preenchimento dos campos obrigatórios ("Índice de optante de registro eletrônico", "código" e "descrição" da empresa, "CPF" ou "CNPJ") não serão integradas.
- Caso uma empresa seja inativada no Sankhya Om, o empregador correspondente será inativado na Pontotel.
- Se houver empregador já cadastrado na Pontotel com o mesmo código da empresa cadastrada no Sankhya Om, os dados do empregador já existente na Pontotel serão atualizados conforme constam na empresa de código correspondente na Sankhya.
- Caso não deseje integrar algum empregador (exemplo: empresa só de autônomos dispensados de controle de ponto), altere a configuração da empresa para diferente de "1 - optou de registro eletrônico".
- A associação do colaborador ao empregador deve ser feita no Sankhya Om; se o empregador não for integrado, o cadastro do colaborador não será criado/atualizado na Pontotel.
- Se o empregador for cadastrado diretamente na Pontotel e associado a um colaborador não registrado no Sankhya Om, os dados desse colaborador serão atualizados na Pontotel conforme o empregador vinculado a ele na Sankhya.
- Se o log de alterações não estiver habilitado na tela Preferências ou se as mudanças não impactarem diretamente a funcionalidade na Sankhya, os dados só serão enviados para a Pontotel na execução de consistência diária, e não nas execuções recorrentes.

### 6. Dicas de Usabilidade

- Manter o cadastro de empresas sempre atualizado para evitar inconsistências na integração.
- Verificar periodicamente o status do token e da URL no Gateway para garantir a continuidade da integração.

### 7. Casos de Uso

✅ **Exemplo Real:**

Cadastro de uma nova empresa com CNPJ e índice de optante de registro eletrônico marcado como "1". Após a execução da integração, o empregador é criado automaticamente na Pontotel.

❌ **Erro Comum:**

Empresa cadastrada sem o campo "1" preenchido. 

Resultado: empregador não integrado à Pontotel.

## FAQ – Dúvidas Frequentes

1. **Posso integrar empresas cadastradas apenas com CPF?**

   Sim, desde que o campo CPF esteja preenchido e a empresa seja optante pelo registro eletrônico.
2. **O que acontece se eu alterar o código da empresa na Sankhya?**

   A referência de equivalência entre Pontotel e Sankhya será perdida, podendo causar inconsistências.
3. **Empresas inativas na Sankhya são excluídas na Pontotel?**

   Não, apenas o status do empregador é atualizado para inativo.
4. **Preciso cadastrar manualmente empregadores na Pontotel?**

   Apenas se a integração não estiver habilitada ou configurada corretamente.

## Artigos Relacionados

- [Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293)
- [Setup inicial de integração Sankhya <> Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063)
- [Integração de Funcionários Sankhya x Empregados Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031)
- [Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207)
- [Integração de Escalas Pontotel e Carga Horária Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887)
- [Integração de Férias Sankhya x Férias Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023)
- [Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959)
- [Integração de Usuários (Sankhya) x Usuários (Pontotel)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951)
- [Integração de Apontamentos e Faltas Pontotel x Verbas e Faltas Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/35056595712279)
