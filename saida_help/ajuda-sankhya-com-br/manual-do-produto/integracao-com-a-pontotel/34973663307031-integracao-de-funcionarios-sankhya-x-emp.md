---
id: "34973663307031"
titulo: "Integração de Funcionários Sankhya x Empregados Pontotel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com a Pontotel"
atualizado_em: "2026-09-26T01:41:09Z"
rotulos: ["Configuração", "Integração", "ID: br.com.sankhya.cadastro.funcionarios", "LOGTABOPER", "Pontotel", "Integração Sankhya <> Pontotel", "Log de Alterações do Gateway", "Pessoas+"]
---

# Integração de Funcionários Sankhya x Empregados Pontotel

**Módulo**: Pessoas+ / Integrações
**Caminho de Acesso**: Menu Principal > Integrações > Empregados > Sankhya x Pontotel

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#1-descri%C3%A7%C3%A3o-da-funcionalidade)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#2-pr%C3%A9-requisitos)
- [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#3-diagrama-de-fluxo)
- [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#4-jornada-de-uso)
- [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#5-pontos-de-aten%C3%A7%C3%A3o)
- [6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#6-dicas-de-usabilidade)
- [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#faq-%E2%80%93-d%C3%BAvidas-frequentes)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031-Integra%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Sankhya-x-Empregados-Pontotel#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **integração de colaboradores entre Sankhya e Pontotel** automatiza o cadastro, atualização, transferência e demissão de funcionários, garantindo que as informações estejam sincronizadas entre os sistemas. 

O processo identifica funcionários não dispensados de ponto na Sankhya e cria ou atualiza os respectivos empregados na Pontotel, utilizando o código composto (CODEMP+CODFUNC) como referência. Isso elimina retrabalho manual, reduz inconsistências e agiliza a gestão de pessoal.

### 2. Pré-requisitos

- **Permissões necessárias**
  - Ter contratado e implementado o Pessoal+ e o Sankhya Om;
  - Ter realizado o [setup de integração Sankhya/Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063).
- **Parâmetros essenciais**
  - Habilitação do recurso Log de Alterações do Gateway (parâmetro LOGTABOPER - Ativar armazenamento de log de modificações em tab = ligado na tela Preferências do Sankhya Om).
- **Configurações relacionadas**
  - Base Sankhya online e responsiva durante as consultas.
  - Token válido e URL atualizada no [Gateway](https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway).

### 3. Diagrama de fluxo

![Imagem 1: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/34973901412887)

### 4. Jornada de Uso

**4.1.** O usuário realiza o cadastro ou atualização do funcionário no Sankhya Om, preenchendo todos os campos obrigatórios para a integração (Empresa, CPF, Carga Horária, Departamento, Cidade de Trabalho, Sindicato).

**4.2.** Certifica de que o funcionário está em atividade normal e que não está dispensado de ponto.

![Imagem 2: 4.2. Certifica de que o funcionário está em atividade normal e que não está dispensado de ponto.](https://ajuda.sankhya.com.br/hc/article_attachments/34974195744919)

**4.3.** Aguarda a execução automática da integração (a cada 12 horas). O sistema valida os dados e verifica se não há inconsistências.

**4.4.** O empregado é criado ou atualizado na Pontotel, refletindo as informações do Sankhya Om. Em caso de transferência ou demissão, o cadastro é atualizado conforme as regras do processo.

**4.6.** Campos integrados: funcionário (Sankhya) → empregado (Pontotel)

| **Campo Sankhya** | **Campo Pontotel** | **Descrição** |
| --- | --- | --- |
| Tabelas consultadas no Sankhya: TFPFUNC, TFPFHO, TFPEMP, TFPFCO e TSICID | | |
| Nome Funcionário | Nome | Nome cadastrado na folha |
| Dia apura ponto (Empresa) | Dia de início da folha | Dia de apuração do ponto do cadastro da Empresa |
| CPF | Senha Registro | CPF do cadastro. Pode ser alterado após a admissão. |
| Departamento | Local de Trabalho | Concatenação da informação do departamento + cidade de trabalho do empregado |
| Cidade de Trabalho |
| Empresa | Empregador | Empresa |
| Sindicato | Regra de Cálculo | Código do sindicato |
| Data admissão | Admissão | Data de admissão |
| Carga Horária | Escala | Código da carga horária |
| Dia de início da Carga Horária | Dia início da Escala | Dia de início da escala |
| Código da Empresa | Código | Concatenação do código da empresa (CODEMP) com o código do funcionário (CODFUNC) |
| Código do Funcionário |
| PIS | PIS | PIS válido (opcional) |
| RG | Identidade | RG válido (opcional) |
| CTPS | CTPS | CTPS válida (opcional) |
| Função | Função | Função atribuída ao cadastro do empregado na Sankhya |
| Email | Email | Email válido (opcional) |

### 5. Pontos de Atenção

- O código do empregado (CODEMP+CODFUNC) não deve ser alterado manualmente na Pontotel, para manter a referência entre os sistemas.
- Funcionários "Dispensados do Ponto" não são integrados.
- Em caso de duplo vínculo, será feito um novo cadastro na Pontotel, sendo o PIN padrão o CPF + "1" ao final do mesmo.
- Em caso de transferência, o cadastro atual é demitido e admitido um novo, com o mesmo PIN e informações atualizadas conforme consta no Sankhya Om.
- Não há deleção automática: exclusões no Sankhya Om devem ser replicadas manualmente na Pontotel.
- Alterações diretas na Pontotel serão sobrescritas pela próxima integração, caso não estejam atualizadas no Sankhya Om.
- Transferências e demissões exigem que não haja batidas de ponto após a data de desligamento.
- Se o log de alterações não estiver habilitado, a integração ocorrerá apenas na execução de consistência diária.

### 6. Dicas de Usabilidade

- Utilizar filtros no Sankhya Om para visualizar apenas funcionários elegíveis à integração.
- Manter o cadastro sempre atualizado para evitar falhas na sincronização.
- Para autônomos ou funcionários dispensados de controle de ponto, marcar a opção **"Dispensado de Ponto"** no cadastro.
- Realizar o setup completo da integração antes de habilitar o fluxo.

### 7. Casos de Uso

✅ **Exemplo Real:** 

Cadastro de novo funcionário no Sankhya Om com todos os dados obrigatórios preenchidos, integração automática e criação do empregado na Pontotel.

❌ **Erro Comum:** 

Alteração manual do código do empregado na Pontotel, causando perda de referência e duplicidade de cadastro.

## FAQ – Dúvidas Frequentes

1. **O que acontece se um funcionário for dispensado de ponto na Sankhya?**

   Ele não será integrado à Pontotel.
2. **Posso alterar o código do empregado na Pontotel?**

   Não. Isso causa perda de referência e duplicidade de cadastro.
3. **Como tratar transferências e demissões?**

   O cadastro é atualizado conforme as regras, desde que não haja batidas de ponto após a data de desligamento.
4. **E se o log de alterações não estiver habilitado?**

   A integração ocorrerá apenas na execução de consistência diária.

## Artigos Relacionados

- [Setup inicial de integração Sankhya <> Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Integração de Empresas Sankhya x Empregadores Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919)
- [Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207)
- [Integração de Escalas Pontotel e Carga Horária Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887)
- [Integração de Férias Sankhya x Férias Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023)
- [Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959)
- [Integração de Usuários (Sankhya) x Usuários (Pontotel)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951)
- [Integração de Apontamentos e Faltas Pontotel x Verbas e Faltas Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/35056595712279)
