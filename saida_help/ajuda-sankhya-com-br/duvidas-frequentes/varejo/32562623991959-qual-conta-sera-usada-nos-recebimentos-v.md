---
id: "32562623991959"
titulo: "Qual conta será usada nos recebimentos via PIX API com Baixa Automática?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32562623991959-Qual-conta-ser%C3%A1-usada-nos-recebimentos-via-PIX-API-com-Baixa-Autom%C3%A1tica"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T14:31:01Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Financeiro", "PIX", "Passos para resolver", "Razão do erro", "Detalhe do erro", "conta usada", "recebimentos via PIX API", "com Baixa Automática"]
---

# Qual conta será usada nos recebimentos via PIX API com Baixa Automática?

**(1)** Ao receber um pagamento via **PIX API**, tendo o **tipo de título configurado para baixa automática**, muitos usuários têm dúvida sobre qual **conta será usada para registrar o recebimento**.

Nessa configuração, **a baixa do título ocorre automaticamente** após a confirmação do pagamento via PIX. E a **conta bancária que será considerada** para esse recebimento **não é a conta do banco do PIX**. Em vez disso, o **sistema utiliza** **a** **conta vinculada ao usuário do caixa logado** no momento da operação.

Essa lógica é usada para manter o controle financeiro alinhado com os caixas dos usuários. De modo especial, em operações de frente de loja, nas quais cada operador deve ter controle individualizado dos recebimentos.

#### Imagem 1: Dica: Dica:

Caso queira garantir que os valores caiam sempre na conta correta, **desative a baixa automática** para títulos pagos via PIX e oriente o **Financeiro** a realizar a baixa manual com a seleção apropriada da conta.
