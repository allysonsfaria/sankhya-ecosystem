---
id: "37341632615191"
titulo: "Transportadora não é mantida ao duplicar Pedido, Orçamento ou Nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37341632615191-Transportadora-n%C3%A3o-%C3%A9-mantida-ao-duplicar-Pedido-Or%C3%A7amento-ou-Nota"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:13:17Z"
rotulos: ["Pedidos", "Configuração", "Transportadora", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "duplicação", "copiar transportadora na duplicacao", "dulicacao transportadora", "duplicar", "duplicar pedido", "duplicar transportadora", "copiar transportadora na duplicação", "transportadora duplicacao", "Orçamentos"]
---

# Transportadora não é mantida ao duplicar Pedido, Orçamento ou Nota

Ao duplicar um Pedido ou Orçamento, a transportadora informada no lançamento original **não é copiada** para o novo documento, obrigando o usuário a preenchê-la manualmente.

Esse comportamento está relacionado ao parâmetro: ''**LIMPAROC – Limpar Ordem de Carga ao duplicar Pedido/Nota?''**

Quando esse parâmetro está habilitado, ao duplicar um pedido ou nota, o sistema:

- Limpa o campo **Ordem de Carga** do novo lançamento;
- Remove automaticamente a transportadora, pois ela está vinculada à Ordem de Carga.

Portanto, mesmo que o pedido original tenha transportadora cadastrada, ela **não será copiada** para o pedido duplicado enquanto o parâmetro estiver ativo.

**Procedimento para corrigir:**

Para que a transportadora seja mantida ao duplicar Pedidos ou Orçamentos, siga os passos abaixo:

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** Busque pelo parâmetro ''LIMPAROC – Limpar Ordem de Carga ao duplicar Pedido/Nota?''.

**(3)** Para que a transportadora seja mantida ao duplicar pedidos ou orçamentos, **desative** este parâmetro.

**(4)** Após a alteração, realize novamente a duplicação do documento e verifique se a transportadora foi copiada corretamente.
