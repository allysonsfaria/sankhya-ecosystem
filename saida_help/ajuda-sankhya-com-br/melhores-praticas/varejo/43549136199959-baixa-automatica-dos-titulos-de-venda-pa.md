---
id: "43549136199959"
titulo: "Baixa automática dos títulos de venda pagos em dinheiro no PDV Web NFC-e?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549136199959-Baixa-autom%C3%A1tica-dos-t%C3%ADtulos-de-venda-pagos-em-dinheiro-no-PDV-Web-NFC-e"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-10-07T19:49:34Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Baixa automática dos títulos de venda pagos em dinheiro no PDV Web NFC-e?

No **PDV Web**, ao realizar vendas com pagamento em dinheiro para **NFC-e**, o título financeiro gerado pode permanecer pendente de baixa, exigindo uma ação manual do usuário para concluir o processo.

Essa situação pode gerar dúvidas sobre as configurações necessárias para automatizar a baixa dos títulos e evitar retrabalho no setor financeiro.

Para que os títulos gerados nas vendas com pagamento em dinheiro sejam baixados automaticamente, é necessário configurar corretamente o **Tipo de Título** utilizado no recebimento e validar o parâmetro responsável pela baixa automática.

#### **(1)** Como configurar o tipo de título para permitir baixa automática no PDV Web?

Para que o título gerado na venda seja baixado automaticamente, acesse: **Financeiro » Arquivos » Cadastros » Tipos de Título.**

Localize o **Tipo de Título** utilizado para os recebimentos em dinheiro e, na aba **Fast Service**, habilite as opções:

- **Utiliza no Fast Service**
- **Baixa automática**

Essas configurações permitem que o título seja baixado durante o processo de finalização da venda no PDV Web, sem a necessidade de realizar a baixa manualmente.

Além disso, verifique se o campo **Tipo de pgto para NFC-e / NF-e / CF-e** está configurado corretamente como **01 - Dinheiro**.

Essa configuração garante que o tipo de título esteja corretamente associado à forma de pagamento em dinheiro utilizada na emissão do documento fiscal.

Para que o sistema realize a baixa automaticamente sem solicitar confirmação ao usuário, habilite o parâmetro: **Baixar título na central sem perguntar? - BXARTITSEMPERG.**

**CAUSA**

Essas configurações contribuem para automatizar o processo de baixa dos títulos de vendas realizadas em dinheiro no **PDV Web NFC-e**, reduzindo a necessidade de intervenções manuais e proporcionando maior agilidade e controle sobre o processo financeiro.
