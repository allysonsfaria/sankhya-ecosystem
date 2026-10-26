---
id: "18605288904983"
titulo: "cvc-complex-type.2.4.a: Invalid content was found starting with element 'xPag'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18605288904983-cvc-complex-type-2-4-a-Invalid-content-was-found-starting-with-element-xPag"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:52:20Z"
rotulos: ["CORE_E04895", "Configuração", "NF-e", "Movimentação Financeira", "XML", "Financeiro", "Preencha tipo de pagamento", "Refaça o financeiro", "Verifique tipo de título"]
---

# cvc-complex-type.2.4.a: Invalid content was found starting with element 'xPag'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18605288898327) **MENSAGEM:**

[CORE\_E04895] cvc-complex-type.2.4.a: Invalid content was found starting with element 'xPag'.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18605233575703)CAUSA:**

Ocorre quando no XML não está sendo informado qual é o tipo de título (pagamento) referente a nota

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18605272625431)SOLUÇÃO:**

- Abra a nota em questão na central;
- No Rodapé da nota, campo 'Tipo de Título' verifique qual o tipo de título que está sendo utilizado na nota em questão;
- Acesse a tela 'Tipo de Título';
- Aba Geral ;
- Campo: 'Tipo de pgto para NFC-e / NF-e / CF-e'
- Preencha qual é o tipo de pagamento referente aquela nota/título
  - Exemplo: Tipo de título "Dinheiro"
  - Informar dinheiro no campo citado
- Após o ajuste acesse a central novamente e refaça o financeiro da nota
- Gere lote novamente.
