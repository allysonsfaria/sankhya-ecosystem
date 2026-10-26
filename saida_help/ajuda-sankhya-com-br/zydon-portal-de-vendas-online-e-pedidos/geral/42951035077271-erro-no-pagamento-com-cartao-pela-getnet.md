---
id: "42951035077271"
titulo: "Erro no pagamento com cartão pela Getnet: como verificar o que causou"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951035077271-Erro-no-pagamento-com-cart%C3%A3o-pela-Getnet-como-verificar-o-que-causou"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T13:51:26Z"
rotulos: ["zydon", "sync_hc", "zydon_213266004302", "sync_hash_8004975d4f39"]
---

# Erro no pagamento com cartão pela Getnet: como verificar o que causou

Quando um pagamento com cartão pela **Getnet** falha, é possível verificar a causa do erro diretamente no painel do Zydon Pay, identificando se o problema é do emissor do cartão, do gateway ou de dados incorretos.

## Como verificar o erro

1. No Zydon Admin, acesse **Zydon Pay → Transações**.
2. Localize a transação com falha e clique para ver os detalhes.
   ![Imagem 1: Localize a transação com falha e clique para ver os detalhes.](https://ajuda.sankhya.com.br/hc/article_attachments/42951035198999)
3. Verifique o **código de retorno** e a **mensagem de erro** exibidos pela Getnet.
   ![Imagem 2: Verifique o código de retorno e a mensagem de erro exibidos pela Getnet.](https://ajuda.sankhya.com.br/hc/article_attachments/42951062055319)

## Códigos de erro mais comuns

- **Não autorizado pelo emissor:** o banco do cliente recusou. Oriente o cliente a contatar o banco ou usar outro cartão.
- **Dados inválidos:** número, CVV ou data de validade incorretos. Peça ao cliente para redigitar os dados.
- **Limite insuficiente:** o cliente não tem limite disponível. Sugira outro cartão ou forma de pagamento.
- **Cartão bloqueado:** o cliente deve contatar o banco emissor.

> **💡 Dica:** para recusas persistentes do emissor, oriente o cliente a ligar para o banco antes de tentar novamente — bancos bloqueiam temporariamente após múltiplas tentativas recusadas.

## Perguntas frequentes

**O cliente foi cobrado mesmo com erro?**
Não — transações recusadas não geram cobrança. O valor pode aparecer como reserva temporária, mas é liberado em até 72h.

---

### 🚀 Teste grátis por 15 dias!

[admin.zydon.com.br/criacao-conta](https://admin.zydon.com.br/criacao-conta)
