---
id: "1500007977841"
titulo: "Financeiro com impostos não pode ser parcialmente compensado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007977841-Financeiro-com-impostos-n%C3%A3o-pode-ser-parcialmente-compensado"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-09-28T13:21:54Z"
rotulos: ["Configuração", "Movimentação Financeira", "Impostos", "Financeiro", "FIN_E00299", "#publicadoHyago", "Financeiro com impostos", "Configuração de retenção no Financeiro", "Ativar \"Retém outros impostos\"", "Erro"]
---

# Financeiro com impostos não pode ser parcialmente compensado

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16336090185239) MENSAGEM**:

[FIN\_E00299] Financeiro com impostos não pode ser parcialmente compensado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16336090187799) SOLUÇÃO:**

Este é um comportamento do sistema onde se tem uma configuração para a correção, a retenção parcial será aceita se o parâmetro **"Retém outros impostos- RETOUTROSIMP"** estiver ativada. Verifique se os impostos configurados nesses títulos são devidos,  estando corretos, habilite o parâmetro e assim será possível fazer a compensação parcial.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16336075295639) CAUSA:**

Caso as configurações realizadas na tela "Impostos" tenham sido definidas para que tenha-se a retenção no Financeiro, não haverá retenção na nota. A cada valor a ser pago (valor de desdobramento), o sistema calcula o valor do imposto a ser retido e verifica se este é igual ou maior que o mínimo exigido; se sim, haverá a retenção na compensação; se não, não haverá retenção.

**Artigo de referência: [Compensação de Títulos por Valor Mínimo do Imposto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602414-Compensa%C3%A7%C3%A3o-de-T%C3%ADtulos-por-Valor-M%C3%ADnimo-do-Imposto)**
