---
id: "35039187052951"
titulo: "Integração de Usuários (Sankhya) x Usuários (Pontotel)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com a Pontotel"
atualizado_em: "2026-09-26T01:41:14Z"
rotulos: ["Configuração", "Usuários", "Relacionamento entre Usuários", "Integração", "Cadastro de Usuários", "Cadastro de Funcionário", "LOGTABOPER", "Pontotel", "Integração Sankhya <> Pontotel", "Log de Alterações do Gateway", "ID: br.com.sankhya.core.cad.usuarios", "ID: br.com.sankhya.core.cad.RelacionamentoUsuarios", "Pessoas+", "RH"]
---

# Integração de Usuários (Sankhya) x Usuários (Pontotel)

**Módulo**: Pessoas+ / Integrações
**Versão Mínima**: Pessoas+ 5.15 / Sankhya Om 4.35
**Caminho de Acesso**: Menu Principal > Integrações > Usuários

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#descri%C3%A7%C3%A3o-e-usabilidade)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#1-descri%C3%A7%C3%A3o-da-funcionalidade)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#2-pr%C3%A9-requisitos)
- [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#3-diagrama-de-fluxo)
- [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#4-jornada-de-uso)
- [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#5-pontos-de-aten%C3%A7%C3%A3o)
- [6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#6-dicas-de-usabilidade)
- [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#faq-%E2%80%93-d%C3%BAvidas-frequentes)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/35039187052951-Integra%C3%A7%C3%A3o-de-Usu%C3%A1rios-Sankhya-x-Usu%C3%A1rios-Pontotel#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **integração de usuários entre Sankhya e Pontotel permite que cadastros de usuários sejam sincronizados** automaticamente, refletindo permissões, dados pessoais e vínculo de liderança direta. 

O processo elimina a espera de 12 horas entre execuções, tornando a atualização praticamente instantânea.

Usuários criados ou atualizados no Sankhya Om são automaticamente integrados à Pontotel, com permissões ajustadas conforme regras de negócio e vínculo ao líder direto, otimizando o gerenciamento de acesso e informações entre as plataformas.

### 2. Pré-requisitos

- **Permissões necessárias**
  - Ter contratado e implementado o Pessoal+ e o Sankhya Om.
  - Ter realizado [o setup de integração Sankhya/Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063-Setup-inicial-de-integra%C3%A7%C3%A3o-Sankhya-Pontotel).
- **Parâmetros essenciais**
  - Habilitação do recurso Log de Alterações do Gateway (parâmetro LOGTABOPER - Ativar armazenamento de log de modificações em tab = ligado na tela Preferências do Sankhya Om).
- **Configurações relacionadas**
  - Base Sankhya online e responsiva durante as consultas.
  - Token válido e URL atualizada no [Gateway](https://developer.sankhya.com.br/reference/requisi%C3%A7%C3%B5es-via-gateway).
  - Módulo de liderança direta ativo na Pontotel.
  - Configuração de usuários associados aos colaboradores no Sankhya Om.

### 3. Diagrama de fluxo

![Imagem 1: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/35039366602007)

### 4. Jornada de Uso

**4.1.** O usuário cadastrado ou atualizado previamente na tela Usuários do Sankhya Om, deve ser vinculado ao cadastro do colaborador.

![Imagem 2: 4.1. O usuário cadastrado ou atualizado previamente na tela Usuários do Sankhya Om, deve ser vinculado ao cadastro do…](https://ajuda.sankhya.com.br/hc/article_attachments/35041787287191)

A permissão para cada usuário é definida automaticamente conforme o seu cadastro:

- **RH**: com opção "Pertence ao DP/RH" ativa;

  ![Imagem 3: RH : com opção "Pertence ao DP/RH" ativa;](https://ajuda.sankhya.com.br/hc/article_attachments/35041787289239)
- **Supervisor**: colaboradores com liderados;

  ![Imagem 4: Supervisor : colaboradores com liderados;](https://ajuda.sankhya.com.br/hc/article_attachments/35041787290647)
- **Funcionário**: colaborador que bate ponto, não pertence ao DP/RH e não tem liderados.

O líder direto do funcionário é associado conforme cadastro no Sankhya Om.

![Imagem 5: O líder direto do funcionário é associado conforme cadastro no Sankhya Om.](https://ajuda.sankhya.com.br/hc/article_attachments/35041787295127)

![Imagem 6: O líder direto do funcionário é associado conforme cadastro no Sankhya Om.](https://ajuda.sankhya.com.br/hc/article_attachments/35041787296535)

**4.2.** Campos integrados: usuários (Sankhya) → usuários (Pontotel)

| **Campo Sankhya** | **Campo Pontotel** | **Descrição** |
| --- | --- | --- |
| Tabela consultada no Sankhya: TFPFUN, TSIUSU e TCSRUS | | |
| NOMEUSU | Nome | Nome do usuário |
| EMAIL | E-mail | Caso o colaborador não tenha um e-mail válido, é possível criar um endereço pela integração para criar o usuário. Ex: 118-demonst000@criarusuariopontotel.com.br |
| CPF | CPF | CPF válido |
| PERTENCEDP | Permissão | Com o CODEMP e CODFUNC do cadastro, a integração busca na tabela TFPFUN o cadastro   do funcionário relacionado a esse usuário:   1. Consulta na TFPFUN o campo PERTENCEDP do cadastro do funcionário:   1.1 se estiver com PERTENCEDP = "S", envia a permissão como "RH".   2. Consulta na TCSRUS (tabela de relacionamento de usuários), pelo CODUSU, se o colaborador possui liderados (campo CODUSUREL):   2.1 se tiver colaborador(s) liderados, a permissão é "Supervisor".   3. Se não tiver colaborador relacionado, verifica na TFPFUN se está dispensado de ponto (DISPENSAPONTO):   3.1 se, DISPENSAPONTO = N, a permissão é de "Funcionário".   4. Se na TFPFUN, PERTENCEDP = N e na TCSRUS não possui dados no campo CODUSUREL e DISPENSAPONTO = S, não cria usuário. |
| DISPENSAPONTO |
| CODUSUREL |
| CODUSU | Código | Código do usuário |
| CODEMP | Empregado | O empregado relacionado é identificado pelo CODEMP e CODFUNC |
| CODFUNC |
| CODEMPLIDER | Líder direto | Se o colaborador não está dispensado de ponto, é integrado com o líder direto associado a ele. |
| CODFUNCLIDER |
| CPF | Senha | Senha padrão na criação é o CPF, que pode ser alterada. |

### 5. Pontos de Atenção

- O código do usuário deve ser igual nas duas plataformas.
- Usuários sem CPF, dispensados de ponto, sem liderados e que não pertencem ao DP não são integrados.
- Se o campo "DTLIMACESSO" estiver preenchido no cadastro do colaborador com data igual ou superior à execução do fluxo impede integração.
- O sistema Pontotel demite automaticamente o usuário quando o colaborador vinculado é demitido. Esse comportamento é do próprio sistema Pontotel (e não da integração).
- A integração pode criar e-mail automaticamente para usuários sem e-mail cadastrado no Sankhya Om. Caso não deseje esse email seja criado, é só desativar a opção no setup da integração.
- A integração pode atualizar automaticamente as permissões dos usuários conforme regras de permissões.
- Para usar permissões personalizadas, desative a atualização automática no setup e ajuste manualmente no cadastro de usuários.
- A integração não exclui usuários; exclusão deve ser manual.

### 6. Dicas de Usabilidade

- Configurar permissões personalizadas diretamente na Pontotel, desativando atualização automática via integração.
- Manter o cadastro do líder direto sempre atualizado no Sankhya Om para refletir corretamente na Pontotel.
- Verificar a validade do token e a URL do Gateway para evitar falhas de conexão.

### 7. Casos de Uso

✅ **Exemplo Real:** 

Usuário cadastrado no Sankhya como DP, com CPF e funcionário vinculado, recebe permissão RH na Pontotel automaticamente.

❌ **Erro Comum:** 

Usuário sem CPF ou dispensado de ponto não é integrado, gerando ausência de acesso na Pontotel.

## FAQ – Dúvidas Frequentes

1. **O usuário precisa ter CPF para ser integrado?**

   Sim, o CPF é obrigatório para integração.
2. **Como definir permissões personalizadas na Pontotel?**

   Desative a atualização automática de permissões via integração e ajuste manualmente no cadastro do usuário.
3. **O que acontece se o colaborador for demitido no Sankhya?**

   O usuário correspondente será demitido na Pontotel automaticamente.
4. **Usuários sem e-mail podem ser integrados?**

   Sim, a integração pode criar um e-mail padrão, se configurado.
5. **A integração exclui usuários?**

   Não, exclusões devem ser feitas manualmente na Pontotel.

## Artigos Relacionados

- [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)
- [Relacionamento entre usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598154)
- [Setup inicial de integração Sankhya <> Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34875102231063)
- [Integração de Empresas Sankhya x Empregadores Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34891901568919)
- [Integração de Funcionários Sankhya x Empregados Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/34973663307031)
- [Integração de Locais de Trabalho Sankhya x Pontotel (Departamento + Cidade de Trabalho)](https://ajuda.sankhya.com.br/hc/pt-br/articles/34944782141207)
- [Integração de Escalas Pontotel e Carga Horária Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34981462276887)
- [Integração de Férias Sankhya x Férias Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35006040384023)
- [Integração de Ocorrências Sankhya x Dispensas e Afastamentos Pontotel](https://ajuda.sankhya.com.br/hc/pt-br/articles/35032053719959)
- [Integração de Apontamentos e Faltas Pontotel x Verbas e Faltas Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/35056595712279)
