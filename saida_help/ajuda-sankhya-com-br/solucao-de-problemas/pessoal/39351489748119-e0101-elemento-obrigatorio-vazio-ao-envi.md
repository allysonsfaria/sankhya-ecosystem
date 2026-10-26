---
id: "39351489748119"
titulo: "E0101 - Elemento obrigatório vazio ao enviar S-2205"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39351489748119-E0101-Elemento-obrigat%C3%B3rio-vazio-ao-enviar-S-2205"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-26T00:42:54Z"
rotulos: ["Configuração", "eSocial", "Erro", "Artigo criado KCS", "Identificação de Estrangeiro", "Sankhya RH - KCS", "S-2205", "Cadastro de Funcionários"]
---

# E0101 - Elemento obrigatório vazio ao enviar S-2205

**Mensagem**

E0101 - Elemento obrigatório vazio. Reveja o manual ou a documentação do sistema [eSocial/evtAltCadastral/alteracao/dadosTrabalhador/trablmig/condIng]

**Situação**

Ao tentar enviar o evento **"S-2205"** (Alteração de Dados Cadastrais) para o eSocial, o sistema retorna a mensagem de erro informando que um elemento obrigatório está vazio. Esta situação ocorre especificamente quando o funcionário é estrangeiro e há informações cadastrais incompletas relacionadas ao trabalhador imigrante.

**Solução**

Para corrigir o erro e enviar o evento com sucesso, siga os passos abaixo:

**(1)** Acesse o **"Cadastro do Funcionário"** (Pessoal+ » Cadastros » Configuração Funcionários) e localize o colaborador estrangeiro que apresenta o erro.

**(2)** Localize a seção de **"Dados do Trabalhador Imigrante"** no cadastro do funcionário.

![Imagem 1: (2) Localize a seção de "Dados do Trabalhador Imigrante" no cadastro do funcionário.](https://ajuda.sankhya.com.br/hc/article_attachments/41397659291159)

**(3)** Preencha obrigatoriamente os seguintes campos:

• **"Tempo de Residência do Trabalhador Imigrante"**
• **"Condição de Ingresso do Trabalhador Imigrante"**

![Imagem 2: • "Tempo de Residência do Trabalhador Imigrante" • "Condição de Ingresso do Trabalhador Imigrante"](https://ajuda.sankhya.com.br/hc/article_attachments/41397637101335)

**(4)** Salve as alterações realizadas no cadastro do funcionário.

**(5)** Acesse novamente a tela **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e gere novamente o **"S-2205"** para o funcionário.

**(6)** Envie o evento ao eSocial. Com as informações corrigidas, o envio será processado com sucesso, sem apresentação de erros.

**Causa**

O erro ocorre porque o eSocial exige informações específicas para trabalhadores estrangeiros. Quando o funcionário possui nacionalidade diferente da brasileira, os campos **"Tempo de Residência do Trabalhador Imigrante"** e **"Condição de Ingresso do Trabalhador Imigrante"** tornam-se obrigatórios para o envio do **"S-2205"**. A ausência dessas informações no cadastro impede a validação do evento pelo sistema do eSocial, resultando na mensagem de erro E0101.
