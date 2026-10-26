---
id: "360043365273"
titulo: "Nota possui valor de ISS mas os dados não estão nas tabelas de impostos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365273-Nota-possui-valor-de-ISS-mas-os-dados-n%C3%A3o-est%C3%A3o-nas-tabelas-de-impostos"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:14Z"
rotulos: ["#PUBLIFER", "CORE_E03910", "ISS", "Configuração", "Central de Vendas", "Impostos", "CORE_E05946", "NFS-e", "Revisar configurações de ISS e atualizar nota", "ISS não localizado na tabela de impostos", "Verificar/ajustar dados de ISS em todos os itens"]
---

# Nota possui valor de ISS mas os dados não estão nas tabelas de impostos

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16113707677079) MENSAGEM:**

[CORE\_E03910] Nota possui valor de ISS mas os dados não estão nas tabelas de impostos.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16113722796695) CAUSA:**

Mensagem apresentada, quando na emissão de NFS-e não são localizadas informações de ISS na tabela de impostos (TGFDIN).

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16113707679767) SOLUÇÃO:**

![Imagem 4: Abra a nota através da "Central de Vendas/Compras" , selecione na grade Itens o primeiro produto.](https://ajuda.sankhya.com.br/hc/article_attachments/16113722779415) Abra a nota através da **"Central de Vendas/Compras"**, selecione na grade Itens o primeiro produto.

![Imagem 5: No botão "Outras Opções (...)" » "Consultar/alterar dados dos impostos do Item" verifique se foi gerada uma linha para…](https://ajuda.sankhya.com.br/hc/article_attachments/16113722783511) No botão **"Outras Opções [...]"** » **"Consultar/alterar dados dos impostos do Item"** verifique se foi gerada uma linha para o Imposto ISS. Realize essa análise para todos os itens.

![Imagem 6: No botão "Outras Opções (...)" » "Consultar/alterar dados dos impostos do Item" verifique se foi gerada uma linha para…](https://ajuda.sankhya.com.br/hc/article_attachments/14556973722263)

![Imagem 7: No botão "Outras Opções (...)" » "Consultar/alterar dados dos impostos do Item" verifique se foi gerada uma linha para…](https://ajuda.sankhya.com.br/hc/article_attachments/14556996460311)

![Imagem 8: Em caso negativo, revise as configurações relacionadas ao cálculo desse imposto detalhadas no artigo: " Alíquotas de…](https://ajuda.sankhya.com.br/hc/article_attachments/16113722786199) Em caso negativo, revise as configurações relacionadas ao cálculo desse imposto detalhadas no artigo: **"[Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014)"**.

**(2)** Alíquotas de ISS

**(2)** Cadastro de **"Serviços"** » Aba **"Impostos"** » Campo **"ISS"**

**(2)** **"[Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"** » Aba **"Propriedades"** » Campo ISS

**(2)** Cadastro de **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)"** » Aba **"Fiscal"** » **"Retém ISS"**

**(2)** Cadastro de **"[Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** » Aba **"Livro Fiscal"** (Atualização livros de ISS / Modelo Documento ISS / Código CFPS).

![Imagem 9: Revisado os cadastros acima, caso exista algum ajuste, ou comprove estarem de acordo com o cálculo previsto, redigite o…](https://ajuda.sankhya.com.br/hc/article_attachments/16113722791703) Revisado os cadastros acima, caso exista algum ajuste, ou comprove estarem de acordo com o cálculo previsto, redigite o cabeçalho da nota, forçando a atualização das informações. Em seguida, gere um novo lote da NFS-e.
