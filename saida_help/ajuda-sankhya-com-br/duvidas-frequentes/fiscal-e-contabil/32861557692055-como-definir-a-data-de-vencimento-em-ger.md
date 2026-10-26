---
id: "32861557692055"
titulo: "Como definir a data de vencimento em Gerar Financeiro do ICMS Normal Op. Própria a Recolher?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32861557692055-Como-definir-a-data-de-vencimento-em-Gerar-Financeiro-do-ICMS-Normal-Op-Pr%C3%B3pria-a-Recolher"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:30:11Z"
rotulos: ["Configuração", "Relatórios", "Registro de Apuração do ICMS", "ICMS", "EFD", "Preferências", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Data de Emissão", "Como definir a data de vencimento em", "Gerar Financeiro do ICMS Normal Op. Própria a Recolher"]
---

# Como definir a data de vencimento em Gerar Financeiro do ICMS Normal Op. Própria a Recolher?

**SITUAÇÃO:**

Ao utilizar a funcionalidade do botão **"Gerar Financeiro do ICMS Normal Op. Própria a Recolher"**, disponível na tela **"Registro de Apuração do ICMS"** (Livros Fiscais » Relatórios » Registro de Apuração do ICMS), observa-se que a data de vencimento do título financeiro está sendo definida para o mês subsequente à data de negociação, desconsiderando o período de apuração.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32861570462615) SOLUÇÃO:**

**(1)** Para que o financeiro seja gerado com a data de vencimento desejada, acesse a tela **"Empresa"** (Comercial > ''Preferências), na aba ''**EFD – Escrituração Fiscal Digital''** e, em seguida, acesse a sub-aba ''**Geração de Financeiro do ICMS Normal Op. Própria a Recolher''.** No campo ''**Dia de vencimento''**, insira o dia desejado para o vencimento.

![Imagem 2: (1) Para que o financeiro seja gerado com a data de vencimento desejada, acesse a tela "Empresa" (Comercial >…](https://ajuda.sankhya.com.br/hc/article_attachments/33376441569047)

**(2)** Na tela **"Registro de Apuração do ICMS"** (Livros Fiscais » Relatórios » Registro de Apuração do ICMS), o campo **"Data de Emissão"** é o que determina a data de vencimento gerada ao utilizar a opção Gerar Financeiro do ICMS Normal Op. Própria a Recolher.

**Exemplo:** Se a data de emissão for **31/01/2024**, o sistema tomará como referência o dia configurado em Empresa > Preferências e determinará o vencimento para o mês subsequente, resultando em **12/02/2024**.

![Imagem 3: Exemplo: Se a data de emissão for 31/01/2024 , o sistema tomará como referência o dia configurado em Empresa >…](https://ajuda.sankhya.com.br/hc/article_attachments/33376414713879)

**Observação:** O sistema sempre leva em consideração a Data de Emissão informada e, com base nessa data, gera a data de vencimento para o mês subsequente, utilizando o dia configurado no campo Dia de Vencimento da seção Geração de Financeiro do ICMS Normal Op. Própria a Recolher.
