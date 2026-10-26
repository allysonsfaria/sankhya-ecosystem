---
id: "38858155502103"
titulo: "Atualização do Valor da Moeda DI nas Despesas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38858155502103-Atualiza%C3%A7%C3%A3o-do-Valor-da-Moeda-DI-nas-Despesas"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:01:03Z"
rotulos: ["Moeda", "Movimentação Financeira", "Atualização", "Importação", "Financeiro", "Valor da Moeda DI nas Despesas", "Valor da Moeda DI", "Moeda DI nas Despesas", "Processo de Importação"]
---

# Atualização do Valor da Moeda DI nas Despesas

##### 1. Objetivo da Rotina

##### Garantir que a alteração do valor da moeda da DI, realizada na tela ''Portal de Importação'', aba ''Despesas'', atualize automaticamente apenas as despesas cujo financeiro ainda não foi baixado.

Consideram-se **despesas não baixadas** aquelas que **ainda não passaram por baixa no financeiro** e, portanto, **permanecem passíveis de alteração**. Já para **despesas com baixa financeira realizada**, o sistema **não permite modificações**, apresentando a mensagem **Financeiro Baixado**.

Esse comportamento evita erros e preserva a integridade das informações financeiras.

##### 2. Problema Identificado

Anteriormente, ao alterar o Valor da Moeda DI, **o sistema apresentava erro (exception) caso existisse alguma despesa com financeiro já baixado**, bloqueando a atualização das demais despesas.

#####

##### 3. Novo Comportamento

**(1)** O sistema NÃO apresentará erro ao alterar o Vlr Moeda DI;

**(1)** Despesas com financeiro NÃO baixado terão seus valores atualizados automaticamente;

**(1)** Despesas com financeiro já baixado NÃO terão seus valores alterados;

**(1)** O processo ocorrerá de forma automática após salvar a alteração.

#####

##### 4. Processo Operacional

**(1)** Gere um **Processo de Importação**.

**(2)** Adicione duas ou mais despesas com financeiro, utilizando a mesma moeda da DI.

**(3)** Realize a baixa financeira de uma das despesas.

**(4)** Acesse a aba ''**Geral''** do ''Portal de Importação'' e altere o valor da moeda da DI.

**(5)** Salve a alteração.

**(6)** O sistema atualizará apenas as despesas com financeiro não baixado.

- Observe que o sistema atualizará automaticamente apenas as despesas cujo financeiro ainda não foi baixado.

##### 5. Regras e Validações

##### **(1)** Despesas com financeiro baixado permanecem inalteradas;

##### **(1)** Não será exibida mensagem de erro ao salvar;

##### **(1)** A integridade financeira é preservada.

#####

##### 6. Benefícios da Rotina

##### **(1)** Evita travamento do sistema;

##### **(1)** Elimina erros desnecessários;

##### **(1)** Garante atualização correta das despesas pendentes;

##### **(1)** Preserva despesas já liquidadas.
