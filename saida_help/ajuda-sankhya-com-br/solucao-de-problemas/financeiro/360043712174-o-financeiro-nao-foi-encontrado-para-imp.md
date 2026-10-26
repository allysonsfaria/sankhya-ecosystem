---
id: "360043712174"
titulo: "O Financeiro não foi encontrado para imprimir boleto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712174-O-Financeiro-n%C3%A3o-foi-encontrado-para-imprimir-boleto"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:49Z"
rotulos: ["#RevisadoBraga", "CORE_E01398", "Configuração", "Impressão", "Contas", "Parceiro", "Movimentação Financeira", "Boleto", "Financeiro", "Ajuste configurações e vinculações", "Financeiro não encontrado", "Configurações incorretas para boletos"]
---

# O Financeiro não foi encontrado para imprimir boleto

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17292624482711) **MENSAGEM:**

[CORE\_E01398]: O Financeiro não foi encontrado para imprimir boleto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17292624488471) SOLUÇÃO:**

Revise as configurações abaixo, de acordo com o lançamento efetuado, e caso algum deles não seja respeitado, a mensagem será apresentada na tentativa de impressão de boleta.

![Imagem 3: Acesse: Configurações » Cadastros » Bancários » Contas](https://ajuda.sankhya.com.br/hc/article_attachments/17292595205655) Acesse: Configurações » Cadastros » Bancários » Contas

Aba: **"Boleto(s)/Duplicatas"**

- Emite: marcado
- Impressora: informe o nome da Impressora
- Tipo Impressora: selecione uma das opções
- Modelo: configure em '**Financeiro » Relatórios » Modelos de Boleto(s)**', um modelo padrão ou personalizado, e vincule em '**Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)**', para ser informado neste campo

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação](https://ajuda.sankhya.com.br/hc/article_attachments/17292595212183) Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação

Aba: **"Características"**
Subtipo: **Diferente** de 'A vista'

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/17292624522135) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba: **"Impressão"**

Campo **"Imprimir Boleto/Duplicata"**: **Diferente** de 'Proibido'

![Imagem 6: Acesse: Financeiro » Rotinas » Movimentação Financeira](https://ajuda.sankhya.com.br/hc/article_attachments/17292595243031) Acesse: Financeiro » Rotinas » Movimentação Financeira

Certifique-se que o(s) titulo(s) não estejam Baixados - Campo **"Data de Baixa"** e **"Valor de Baixa"** - preenchidos e Data de Vencimento não seja igual data de negociação.

![Imagem 7: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/17292624539031) Acesse: Configurações » Cadastros » Parceiros

Aba: **"Informações"**

**Geração de boleto nas centrais:** use as opções disponíveis para impressão e envio de boleto por e-mail pela Central de Vendas

![Imagem 8: Após os ajustes, considere efetuar a impressão do boleto novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/17292624550423) Após os ajustes, considere efetuar a impressão do boleto novamente.

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17292595273367) IMPORTANTE:**

Para tipo de negociação à vista, ou seja, Data de Vencimento igual data de negociação, a impressão de boleto ocorrerá somente através da rotina 'Impressão de Boletos'. Para mais detalhes: [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094)

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17292595289239) CAUSA:**

Ocorre quando uma das opções acima estão em desacordo para a geração de boleto.
