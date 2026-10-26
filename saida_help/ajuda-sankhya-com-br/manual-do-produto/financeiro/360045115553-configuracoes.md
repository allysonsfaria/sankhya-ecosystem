---
id: "360045115553"
titulo: "Configurações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115553-Configura%C3%A7%C3%B5es"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:44:48Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contas", "Parceiro", "Crédito", "Financeiro", "Rotina Exclusiva de Parceiro", "br.com.sankhya.mgefin.opcredito.configcredito", "Configurações manual", "Natureza Tops Título Conta", "data retroativa filtro 1º vencimento", "valor de baixa taxa mensal administradora", "Operações de Crédito"]
---

# Configurações

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312524698391) Módulo: Financeiro > Rotinas > Operações de Crédito
```

---

**Importante:** esta rotina é exclusiva de um Parceiro e habilitada por parâmetro específico.

As Operações de Crédito visam:

- Acompanhar e transformar um Prospect em cliente;
- Fazer a geração de um novo cartão de crédito para este novo cliente;
- Configurar taxas para este novo tipo de título.

Antes de iniciar o processo de autorização e validação de Sistema de Crédito, é necessário que você entre nesta tela e configure os campos de acordo com sua necessidade; essa configuração influenciará na geração dos títulos.

![Imagem 2: Antes de iniciar o processo de autorização e validação de Sistema de Crédito, é necessário que você entre nesta tela e…](https://ajuda.sankhya.com.br/hc/article_attachments/360083339933)

Além de você informar a **"Natureza de Receita e Despesa"**, **"Tops de Despesa e Receita"**, **"Tipo de Título"** e **"Conta"**, poderá habilitar as seguintes funcionalidades:

A marcação **"Aceita data da venda retroativa?"**, quando habilitada, fará com que o filtro seja realizado considerando a data do primeiro vencimento informada, verificando a partir da data atual, até a data de primeiro vencimento a quantidade em dias, por exemplo, 15 dias. Com isso, deverão vim negociações em que o prazo máximo para pagamento, se aproxime mais.

Quando a marcação **"Filtrar tipo de negociação pelo 1º vencimento?"** estiver habilitada, fará com que o sistema permita alterar a data de venda para uma data retroativa, na tela Registro de Borderô.

#### Outras configurações desta rotina específica

O parâmetro **"VLRBAIXAZERO - Aceita valor de Baixa igual a zero"**, será utilizado em situações onde o parceiro antecipe pagamentos, possibilitando baixar uma fatura com valor igual a zero.

Na aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) da tela [Cadastro de Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), o campo **"Taxa mensal de Administradora"** será utilizado para aplicar a taxa quando o Tipo de Negociação for uma operação financiada pela administradora. O sistema aplicará o percentual de taxa em cada parcela.

**(1)**Considere o seguinte exemplo: Taxa de 10%.

**(2)**Se faturar 100/2, irá gerar duas parcelas de R$ 55,00.

**(2)**Se não tiver taxa, irá gerar duas parcelas de R$ 50,00.
