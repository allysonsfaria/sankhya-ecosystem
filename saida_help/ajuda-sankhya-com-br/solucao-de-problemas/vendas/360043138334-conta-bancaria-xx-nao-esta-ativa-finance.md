---
id: "360043138334"
titulo: "Conta Bancária XX não está ativa. Financeiro de número único XXXXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043138334-Conta-Banc%C3%A1ria-XX-n%C3%A3o-est%C3%A1-ativa-Financeiro-de-n%C3%BAmero-%C3%BAnico-XXXXXX"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:37Z"
rotulos: ["#validadoElisangela", "Configuração", "Contas", "Movimentação Financeira", "Financeiro", "Refaturar pedido após ajuste", "Conta bancária inativa", "Verificar e ajustar cadastro", "Erro"]
---

# Conta Bancária XX não está ativa. Financeiro de número único XXXXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16120837600919) MENSAGEM:**

Erro durante o processo de faturamento.
Número único 344572. General SQL error.
SQL50001 Conta Bancaria XX não esta ativa. Financeiro de número único XXXXXX

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16120830273047) SITUAÇÃO:**

Ao tentar efetuar o Faturamento de um Pedido, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16120837606807) SOLUÇÃO:**

O sistema faz as seguintes considerações para buscar a Conta Bancaria. São elas:

**(2)** Se houver Banco e Conta no Tipo de Negociação, aba: **"[Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)"**, sistema usará essas informações ou;

**(2)** Se houver o número de Conta Bancária no Parâmetro **"CONTAPADRAOFIN"**, o sistema usará essa informação ou;

**(2)** Se houver o número da Conta bancária no cadastro do Parceiro, campo **"Conta Bancaria Empresa"** ou;

**(2)** Se houver banco vinculado ao Tipo de Negociação e a conta deste banco marcada como **"Conta padrão para emissão"**, quando existir mais de uma pega a de menor código, preferindo a conta que seja exclusiva da empresa, mas aceitando contas não exclusivas.

**(2)** Se a conta não for preenchida pelos requisitos acima o sistema verifica se a empresa possui uma conta: Padrão para emissão / **"Emite"**: Sim / **"Exclusiva da empresa"**: Sim

Após essas considerações, analise o cadastro da Conta

![Imagem 4: Acesse: Configurações » Cadastros » Bancários » Contas:](https://ajuda.sankhya.com.br/hc/article_attachments/16120830276759) Acesse: Configurações » Cadastros » Bancários » Contas:

**(2)** Aba: **"Cadastros"**

**"Ativa":** Sim
**"Exclusiva da Empresa":** SIM/NÃO

**(2)** Aba: **"Boleto(s)/Duplicatas"**
**"Emite":** Sim

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação:](https://ajuda.sankhya.com.br/hc/article_attachments/16120837613847) Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação:

**(2)** Aba: **"Características"**

(2)** "Imprimir boleto/duplicata?"** Diferente de Proibido.

![Imagem 6: Após os ajustes, fature novamente o pedido.](https://ajuda.sankhya.com.br/hc/article_attachments/16120830280215) Após os ajustes, fature novamente o pedido.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16120837617559) CAUSA:**

Ocorre quando a conta informada no financeiro do Pedido/Nota não está ATIVA.
