---
id: "31455333341463"
titulo: "Preenchimento do campo TIPO da Tabela TCICTA para uso do importador de dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31455333341463-Preenchimento-do-campo-TIPO-da-Tabela-TCICTA-para-uso-do-importador-de-dados"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:33:00Z"
rotulos: ["Produtos", "Configuração", "Contas", "Importação", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "TCICTA", "contas de produtos", "tipo TCICTA", "importador de dados"]
---

# Preenchimento do campo TIPO da Tabela TCICTA para uso do importador de dados

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32067264150295) **SITUAÇÃO:**

Durante a importação de dados na tabela **TCICTA**, as contas contábeis associadas aos produtos não são exibidas corretamente na aba **Bens**, mesmo que a importação seja concluída sem erros e a tabela no banco esteja populada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31455333332759)SOLUÇÃO:**

Para que as contas apareçam corretamente no sistema após a importação, é fundamental preencher corretamente o campo **TIPO** na tabela **TCICTA**, conforme o tipo de conta. Abaixo está a lista dos códigos aceitos e seus respectivos significados:

| Tipo | Descrição |
| --- | --- |
| D | Conta Contábil Depreciação |
| E | Contra-Partida Depreciação |
| X | Conta Contábil Baixa Depreciação |
| B | Contra-Partida Baixa Depreciação |
| 1 | Conta Contábil Baixa Bem |
| 2 | Contra-Partida Baixa Bem |
| 3 | Conta Contábil Crédito PIS |
| 5 | Contra-Partida Crédito PIS |
| 4 | Conta Contábil Crédito COFINS |
| 6 | Contra-Partida Crédito COFINS |

**Atenção:** caso os tipos estejam preenchidos incorretamente ou em branco, o sistema não conseguirá interpretar corretamente os dados, o que impedirá a exibição das contas na aba de **"Bens",** na tela **"Produtos"**.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31455333333399)CAUSA:**

A ausência ou o preenchimento incorreto do campo **TIPO,** na importação do csv da tabela **TCICTA,** compromete a interpretação dos dados de contas contábeis vinculadas aos produtos. Isso impede que as informações sejam carregadas corretamente nas telas do sistema, mesmo que a importação ocorra sem erros aparentes.
