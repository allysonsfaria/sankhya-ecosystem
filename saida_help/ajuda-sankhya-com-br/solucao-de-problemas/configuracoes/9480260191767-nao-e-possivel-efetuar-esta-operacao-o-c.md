---
id: "9480260191767"
titulo: "Não é possível efetuar esta operação. O cálculo de frete não pode ser zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9480260191767-N%C3%A3o-%C3%A9-poss%C3%ADvel-efetuar-esta-opera%C3%A7%C3%A3o-O-c%C3%A1lculo-de-frete-n%C3%A3o-pode-ser-zero"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:40Z"
rotulos: ["Configuração", "Parceiro", "Transporte", "CORE_E02149", "Restrição no Cálculo de Frete", "Erro"]
---

# Não é possível efetuar esta operação. O cálculo de frete não pode ser zero

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18604072997911) MENSAGEM:**

[CORE\_E02149]  Não é possível efetuar esta operação. O cálculo de frete não pode ser zero.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18604104864663) SITUAÇÃO:**

Ao vincular a nota a transportadora na ordem de despacho a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18604104869143) CAUSA:**

Normalmente ocorre quando o campo 'Transportadora própria' do cadastro do parceiro está desmarcado.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18604073016343) SOLUÇÃO:**

Acesse o cadastro de **Parceiros** (Configurações » Cadastros » Parceiros) na aba Identificação, campo "Transportadora própria" e selecionar o mesmo.

![Imagem 5: Acesse o cadastro de Parceiros (Configurações » Cadastros » Parceiros) na aba Identificação, campo " Transportadora…](https://ajuda.sankhya.com.br/hc/article_attachments/18604073018135)

Quando você efetuar a marcação **"Transportadora própria"**, estará indicando que o parceiro é ou possui a própria transportadora, portanto, não será gerado pedido de frete para ela na conclusão da [Ordem de Despacho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110253).

**Observação:**

O erro pode ocorrer em outras situações, caso o campo já esteja marcado e persista a mensagem o cenário deve ser avaliado pelo Service Desk.
