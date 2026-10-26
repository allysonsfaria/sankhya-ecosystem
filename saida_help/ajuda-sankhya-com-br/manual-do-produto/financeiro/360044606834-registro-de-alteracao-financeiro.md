---
id: "360044606834"
titulo: "Registro de Alteração Financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606834-Registro-de-Altera%C3%A7%C3%A3o-Financeiro"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:40:51Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "Ocorrências", "Financeiro", "Registro", "Alteração", "br.com.sankhya.registroalteracaofinanceiro", "Registro de Alteração Financeiro manual", "Acompanhamento de instruções de títulos", "Período Número Situação Tipo Conta Bancária", "Feita com cuidado registrada na tabela TGFRAFEXC", "EDI Bancário"]
---

# Registro de Alteração Financeiro

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312375727767)Módulo: Financeiro > EDI Bancário
```

---

Por meio da tela Registro de Alteração Financeiro você tem a possibilidade de acompanhamento das instruções de um título (entrada, baixa e alteração).

É possível localizar as instruções desejadas, utilizando de vários filtros, tais como, **"Período de Alteração"**, **"Nro. Único Financeiro"**, **"Nro. Remessa"** e **"Ocorrência"**.

Além disto, você buscar pelas instruções de acordo com a **"Situação"** de acordo com as seguintes marcações:

- A enviar;
- Enviada;
- Processada;
- Baixada;
- Renegociada;
- Rejeitada.

É possível também buscar as instruções por meio de seu **"Tipo"**:

- Alteração;
- Entrada;
- Baixa.

Por fim, você pode identificar as instruções de um título de acordo com a [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025236514-Contas) à qual a Ocorrência está relacionada.

![Imagem 2: Por fim, você pode identificar as instruções de um título de acordo com a Conta Bancária à qual a Ocorrência está…](https://ajuda.sankhya.com.br/hc/article_attachments/8761460208791)

Além de consultar as instruções que foram geradas para um determinado título, você pode executar a exclusão de uma instrução. A ação de exclusão se torna necessária em possíveis erros de lançamento ou edições sobre um título cuja conta bancária possua monitoramento.

**Importante:** a exclusão de uma instrução deverá ser executada com cautela, visto que não é possível gerar uma nova instrução a não ser a partir de uma edição no título. Visando auxiliar no controle destas ações, esta função pode ser habilitada/desabilitada a partir dos [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) à tela.

**Observação:** quando forem excluídas as informações dessa tela, as informações da TFGRAF serão salvas na tabela TGFRAFEXC. É uma tabela de log que armazena as informações das exclusões de títulos que sejam de uma conta bancária do tipo API DO BANCO.
Na tabela TGFRAFEXC foi adicionado o campo DTEXC que guarda a data da exclusão, para monitoramento e auditoria.

**Observação:** a exclusão de um registro vinculado a uma conta configurada para emitir boletos por meio de API será salva na tabela auxiliar TGFRAF\_exc.

![Imagem 3: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16580441476247) Acesse também:

[Controle/monitoramento de Cobranças Registradas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111753)

[Ocorrências de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606374)
