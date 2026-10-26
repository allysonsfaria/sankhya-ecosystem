---
id: "30451446729239"
titulo: "Baixa e recebimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30451446729239-Baixa-e-recebimento"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Venda Mais"
atualizado_em: "2026-07-29T13:12:48Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Recebimento", "Financeiro", "Baixa Automática", "Configurações Venda Mais", "Venda Mais", "Status Venda Mais", "Baixa e Conciliação"]
---

# Baixa e recebimento

Os títulos **A Receber** do Venda Mais podem ser configurados para baixa automática. Quando essa opção está ativada, o sistema processa a baixa dos novos títulos gerados, comparando os dados de **Nosso Número**, **Código de Operação** e **Conta Bancária**, que devem ser compatíveis para execução dessa operação. 

A baixa ocorre com base nos títulos **pagos pelo parceiro de crédito no dia anterior**.

### Configurações necessárias para a baixa automática

![Imagem 1: Configurações necessárias para a baixa automática](https://ajuda.sankhya.com.br/hc/article_attachments/30451446727575)

As configurações para a baixa automática devem ser realizadas na tela **Configurações Venda Mais**, aba **Processos** > **Configurar rotinas** > **Baixa e Conciliação** por meio dos seguintes campos:

- **Baixa automática**: deve ser definida para **Realizar na data de pagamento**;
- **Hora da execução**: determine a hora para executar a baixa automática dos títulos pagos no dia anterior pelo parceiro de crédito;
- **Permitir baixa com divergência de valores:** se habilitada, permitirá que divergências de valor entre um título X no sistema, e esse mesmo título no repasse do parceiro de crédito, sejam ignoradas e permita a baixa do título. Neste caso, o valor enviado pelo parceiro de crédito irá sobrepor os valores apresentados para o título no sistema;
- **TOP baixa boleto**: informe a TOP responsável pela baixa do título, sendo que esta deve estar  **Ativa** e que **Tipo de Movimento** seja **R-Recebimento**;
- **Lançamento**: indique o lançamento do respectivo financeiro (tela [Históricos Lançamentos Bancários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606694)).

### Conferência da baixa

Para verificar se um título do Venda Mais foi baixado automaticamente, acesse a aba **Lançamento** na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) e consulte o campo **Histórico**. Caso a baixa tenha ocorrido automaticamente, a seguinte mensagem será exibida:

**“Baixado automaticamente VM”**

### Ocorrências de baixa

Se a baixa automática não for realizada devido a alguma restrição interna, o sistema registrará um log detalhado no botão **Outras Opções** > **Venda Mais** > **Ocorrências Venda Mais**, na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753). 

![Imagem 2: Se a baixa automática não for realizada devido a alguma restrição interna, o sistema registrará um log detalhado no…](https://ajuda.sankhya.com.br/hc/article_attachments/30474365721367)

Algumas situações que podem impedir a baixa são:

- período contábil fechado;
- liberações de limite pendentes;
- conta bancária sem saldo suficiente;
- ausência de configurações necessárias.

Caso ocorra algum bloqueio, verifique o log para identificar e corrigir a causa do problema antes de tentar a baixa novamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30451446729239-Baixa-e-recebimento#top)
