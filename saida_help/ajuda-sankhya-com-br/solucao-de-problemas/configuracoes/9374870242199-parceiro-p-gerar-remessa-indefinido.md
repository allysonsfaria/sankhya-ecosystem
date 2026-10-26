---
id: "9374870242199"
titulo: "Parceiro p/gerar Remessa indefinido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9374870242199-Parceiro-p-gerar-Remessa-indefinido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:24Z"
rotulos: ["Configuração", "Parceiro", "Remessa", "TOP", "CORE_E03218", "Parceiro para gerar Remessa indefinido", "Erro"]
---

# Parceiro p/gerar Remessa indefinido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18585924476311) MENSAGEM:**

[CORE\_E03218]  Parceiro p/gerar Remessa indefinido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18585924480407) SITUAÇÃO:**

Ao fazer um lançamento como Compra Entrega Futura a geração da Remessa entrega futura fica bloqueada e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18585924486935) CAUSA:**

Quando as informações de geração de nota de remessa não estão devidamente configurados.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18585907833495) SOLUÇÃO:**

Necessário verificar no cadastro do **Tipo de operação TOP** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) se o check-box "Gerar se parc.destinatário" está flegado e se o campo "Tipo Operação Remessa" está devidamente preenchido.

![Imagem 5: Necessário verificar no cadastro do Tipo de operação TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) se…](https://ajuda.sankhya.com.br/hc/article_attachments/18585924501143)

A TOP de Venda ou Compra deve ter este quadro preenchido com a TOP de Remessa e então, na Confirmação da Nota, será gerada a Nota de Remessa. Se a marcação **"Gerar se parc. destinatário preenchido"** estiver realizada, a remessa será gerada apenas se na nota de venda ou de compra estiver informado o **"Parceiro Destinatário"**. E então, este será usado como Parceiro da Nota de Remessa.
