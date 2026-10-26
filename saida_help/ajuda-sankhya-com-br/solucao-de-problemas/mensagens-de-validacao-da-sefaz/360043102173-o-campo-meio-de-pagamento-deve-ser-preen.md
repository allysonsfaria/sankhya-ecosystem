---
id: "360043102173"
titulo: "O campo Meio de Pagamento deve ser preenchido com a opção Sem Pagamento (NT2016/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102173-O-campo-Meio-de-Pagamento-deve-ser-preenchido-com-a-op%C3%A7%C3%A3o-Sem-Pagamento-NT2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:28Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Financeiro", "871", "Campo Meio de Pagamento Incorreto", "Erro", "Documentos Eletrônicos"]
---

# O campo Meio de Pagamento deve ser preenchido com a opção Sem Pagamento (NT2016/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16484717321111) MENSAGEM:**

[871 - Rejeição]: O campo Meio de Pagamento deve ser preenchido com a opção Sem Pagamento.  

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16484688314903) SOLUÇÃO:**

Avaliar a seguinte regra:

- Caso a NF-e possua finalidade 3 (NF-e Ajuste) ou 4 (Devolução), o campo **"tPag"** deve ser gerado com valor 90 – Sem pagamento.
- Caso a NF-e possua duplicatas, o campo **"tPag"** será gerado com valor 14 – Duplicata Mercantil.
- Caso a NF-e não atender a nenhuma das opções anteriores, o campo **"tPag"** será gerado com valor 99 – Outros.

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Financeiro » Arquivos » Cadastros » Tipos de Título](https://ajuda.sankhya.com.br/hc/article_attachments/16484717330455) Acesse: Financeiro » Arquivos » Cadastros » Tipos de Título

- Aba: **"Geral"**
- Campo **"Tipo de pgto para NFC-e / NF-e / CF-e"**: Configure observando as regras acima

![Imagem 4: Após os ajustes, acesse novamente a nota, redigite o tipo de negociação ou fature novamente e gere lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16484717333655) Após os ajustes, acesse novamente a nota, redigite o tipo de negociação ou fature novamente e gere lote.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16484688321047) OBSERVAÇÃO:**

(**NT2016/002**) - Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=XPcFD/sRNlQ=>
