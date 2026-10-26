---
id: "29320805357591"
titulo: "Parcela GNRE sendo gerada com o parceiro incorreto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29320805357591-Parcela-GNRE-sendo-gerada-com-o-parceiro-incorreto"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:37:14Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Impostos", "GNRE", "Financeiro", "Endereço para ICMS", "Parcela GNRE sendo gerada com o parceiro incorreto"]
---

# Parcela GNRE sendo gerada com o parceiro incorreto

**(1)**Ao gerar uma nota que tem Guia (parcela) referente a GNRE, o parceiro do título fica incorreto. Abaixo estão alguns passos a serem verificados para correção do problema

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29320816543767) SOLUÇÃO:**

![Imagem 2: Através do parâmetro "Endereço para ICMS - ENDICMS" , configure qual dos endereços no Cadastro de Parceiros (entrega,…](https://ajuda.sankhya.com.br/hc/article_attachments/29320805340823) Através do parâmetro **"Endereço para ICMS - ENDICMS"**, configure qual dos endereços no Cadastro de Parceiros (entrega, recebimento ou principal) o sistema irá utilizar para calcular ICMS. Esta opção é utilizada quando os endereços cadastrados para o parceiro são de cidades diferentes.

Se, por exemplo, foi configurado como "Principal", o sistema busca o parceiro GNRE vinculado ao estado do endereço do parceiro vinculado ao cabeçalho da nota.

![Imagem 3: Se dentro do "Tipo de negociação" , aba "Parcelas" , a parcela referente a guia do GNRE não possui fórmula, quer dizer…](https://ajuda.sankhya.com.br/hc/article_attachments/29320816550807) Se dentro do **"Tipo de negociação"**, aba **"Parcelas"**, a parcela referente a guia do GNRE não possui fórmula, quer dizer que o vínculo do parceiro pode estar configurado dentro da tela **"Fórmula p/ Parcelas Independentes"**. Nela pode estar configurado o parceiro errado para o estado em questão, nesse caso corrija e salve.
