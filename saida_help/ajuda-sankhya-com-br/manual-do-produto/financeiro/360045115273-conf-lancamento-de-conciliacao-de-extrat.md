---
id: "360045115273"
titulo: "Conf. Lançamento de Conciliação de Extrato Bancário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115273-Conf-Lan%C3%A7amento-de-Concilia%C3%A7%C3%A3o-de-Extrato-Banc%C3%A1rio"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:44:20Z"
rotulos: ["AJUDA DO SKW", "manual", "Movimentação Financeira", "baixa", "bancário", "conciliação", "Conf. Lançamento de Conciliação de Extrato Bancário", "conferência", "configuração", "financeiro", "lançamentos", "br.com.sankhya.cfg.lanc.conc.extrato.banc", "Conf. Lançamento de Conciliação de Extrato Bancário manual", "Extrato", "banco", "Conciliação Bancária", "Identifica despesas no arquivo", "Define TOP para baixa de despesas", "Conciliação Extrato Bancário", "Extrato Bancário"]
---

# Conf. Lançamento de Conciliação de Extrato Bancário

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312459996951) Módulo: Financeiro > Avançado
```

---

Esta tela faz parte das configurações da rotina de [Conciliação Extrato Bancário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214).

**Importante:** alguns registros com parâmetros deverão ser configurados nesta tela, sendo que, estes servirão somente para lançamento, baixa e conciliação das despesas que o sistema identificará no arquivo. Estas despesas são aquelas que não constam no sistema ainda, apenas no arquivo. Sendo assim, serão apresentadas no momento da conciliação no passo despesas.

![Imagem 2: Importante: alguns registros com parâmetros deverão ser configurados nesta tela, sendo que, estes servirão somente para…](https://ajuda.sankhya.com.br/hc/article_attachments/27296079265559)

A conciliação de extrato bancário pode ser realizada de duas formas:

![Imagem 3: Arquivo texto](https://ajuda.sankhya.com.br/hc/article_attachments/17153796453143) **Arquivo texto**

Configure o **Layout EDI:**

- Acesse a tela [Configuração Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033).
- Configure o Layout EDI e marque a opção **"Conciliação Extrato Bancário"**.
- Nesta tela, defina como o sistema identifica as despesas e receitas no arquivo, usando os campos **Histórico** e **Categoria de Lançamento (EDI)**.

![Imagem 4: Inclua configurações tanto para despesa quanto para receita . A ausência de uma delas impacta a identificação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/27249935415063) Inclua configurações tanto para **despesa** quanto para **receita**. A ausência de uma delas impacta a identificação dos valores, o cálculo dos totais e a conciliação automática.

Configure os totais da conciliação:

- Acesse a tela **Conf. Lançamento de Conciliação de Ext. Bancário**.
- Preencha os campos de configuração desta tela.

![Imagem 5: Preenchimento obrigatório ou os Totais Selecionados não somam os valores dos registros não conciliados.](https://ajuda.sankhya.com.br/hc/article_attachments/27249935415063) Preenchimento obrigatório ou os **Totais Selecionados** não somam os valores dos registros não conciliados.

![Imagem 6: Arquivo OFX](https://ajuda.sankhya.com.br/hc/article_attachments/17153796462999) **Arquivo OFX**

Faça a configuração de lançamento de conciliação de extrato no campo **"Tipo de Transação (OFX)"**, que é utilizado para controlar os registros configurado, desse modo, deve ser inserido o mesmo conteúdo da tag <**TRNTYPE**> do arquivo OFX. Além de que, sistema irá utilizar a tag <**MEMO**> para identificar o Histórico informado.

**Observação:** pode-se inserir no campo Histórico, por exemplo, IOF% de forma que não será necessário informar data, visto que é uma taxa paga mensalmente. Esse campo é sensitivo, ou seja, se no arquivo disponibilizado pelo banco, as letras forem minúsculas, no sistema deve ser igual, do contrário, o lançamento não será identificado.

Na [Conciliação Extrato Bancário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214), é possível realizar a geração automática dos financeiros de despesas bancárias e a baixa dos financeiros lançados ao utilizar uma [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) diferente daquela do lançamento financeiro. Para que isso ocorra, informe no campo **"Tipo de Operação Baixa"** a TOP responsável pela realização dessa baixa.

![Imagem 7: O sistema permitirá a inclusão apenas de lançamentos de despesas, sem a possibilidade de registrar receitas por meio da…](https://ajuda.sankhya.com.br/hc/article_attachments/27249935415063) O sistema permitirá a inclusão apenas de lançamentos de despesas, sem a possibilidade de registrar receitas por meio da Conciliação Extrato Bancário.

No campo **"Parceiro"**, insira o parceiro credor, ou seja, para quem a empresa apresenta uma determinada despesa.
