---
id: "9653540742295"
titulo: "O campo Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) é obrigatório para o Tipo de Pagamento 99 - Outros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9653540742295-O-campo-Descri%C3%A7%C3%A3o-do-Tipo-de-Pagto-NFC-e-NF-e-CF-e-Outros-%C3%A9-obrigat%C3%B3rio-para-o-Tipo-de-Pagamento-99-Outros"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-19T12:24:26Z"
rotulos: ["Configuração", "NF-e", "XML", "Financeiro", "NFC-e", "CORE_E06920", "Obrigatoriedade do Campo Descrição para Tipo de Pagamento 99", "CF-e"]
---

# O campo Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) é obrigatório para o Tipo de Pagamento 99 - Outros

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19351116297879) MENSAGEM:**

[CORE\_E06920] O campo Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) é obrigatório para o Tipo de Pagamento 99 - Outros.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19351116299671) SITUAÇÃO:**

Ao confirmar uma NF-e ou cadastrar um tipo de título a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19351119840663) CAUSA:**

Ocorre quando o campo Tipo de pgto para NFC-e / NF-e / CF-e é definido como 99 -outros e o campo Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) não é preenchido.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19351116305815) SOLUÇÃO:**

Acesse a tela **Tipo de título** (Caminho de acesso à tela: Financeiro » Arquivos » Cadastros » Tipos de Título) e, se o campo Tipo de pgto para NFC-e /NF-e /CF-e for igual à opção 99 - Outros, preencha campo **"Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros)".** Assim, o sistema irá completar a tag <xPag> para que o preenchimento do campo Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) seja identificado no XML.

![Imagem 5: Acesse a tela Tipo de título (Caminho de acesso à tela: Financeiro » Arquivos » Cadastros » Tipos de Título) e, se o…](https://ajuda.sankhya.com.br/hc/article_attachments/19351119849495)
