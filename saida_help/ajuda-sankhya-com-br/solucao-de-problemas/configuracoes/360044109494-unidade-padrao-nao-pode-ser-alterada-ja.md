---
id: "360044109494"
titulo: "Unidade padrão não pode ser alterada. Já existem lançamentos para este produto e unidade. Esta operação não é permitida devido a impacto no Sped Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109494-Unidade-padr%C3%A3o-n%C3%A3o-pode-ser-alterada-J%C3%A1-existem-lan%C3%A7amentos-para-este-produto-e-unidade-Esta-opera%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-permitida-devido-a-impacto-no-Sped-Fiscal"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:57Z"
rotulos: ["#criadoRoger", "#revisadohugo", "CORE_E03863", "Produtos", "Fiscal", "Movimentação Financeira", "Estoque", "Solução de problemas", "Unidade padrão", "Movimentação de estoque", "SPED Fiscal", "Erro"]
---

# Unidade padrão não pode ser alterada. Já existem lançamentos para este produto e unidade. Esta operação não é permitida devido a impacto no Sped Fiscal

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18605581645463) MENSAGEM**:

[CORE\_E03863] Unidade padrão não pode ser alterada. Já existem lançamentos para este produto e unidade. Esta operação não é permitida devido a impacto no Sped Fiscal.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/18605581653271) SOLUÇÃO**:

Considere o Comportamento da Aplicação, conforme abaixo:

![Imagem 3: Se o produto tem movimentação de estoque (Compra, Venda, Transferência, etc), por determinação Fiscal e integridade de…](https://ajuda.sankhya.com.br/hc/article_attachments/18605579440663) Se o produto tem movimentação de estoque (Compra, Venda, Transferência, etc), por determinação Fiscal e integridade de informação, **não pode ser alterado a Unidade padrão do produto.**

Recomendamos: Caso de fato precise do produto com outra Unidade.

(1)** 1ª Alternativa:**

- Faça um inventário de estoque, efetuando ajuste de saída do produto atual (Nota de Ajuste de Saída);
- Inative esse produto;
- Crie um novo produto e faça o lançamento de entrada de estoque para o novo produto, já com a Unidade Padrão correta.;

(1)** 2ª Alternativa:**

- Crie uma Unidade alternativa para este produto(Aba: Unidade alternativa), e faça os devidos lançamentos de entrada para alimentar estoque com a Unidade alternativa desejada.

![Imagem 4: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18605579431703) **CAUSA**:

Ocorre quando um produto já possui registro de movimentação de estoque e sofre alteração em sua Unidade Padrão. Não é possível tal alteração devido a restrições de integridade.
