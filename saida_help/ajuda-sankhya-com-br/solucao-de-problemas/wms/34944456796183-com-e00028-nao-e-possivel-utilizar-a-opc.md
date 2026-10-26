---
id: "34944456796183"
titulo: "COM_E00028: não é possível utilizar a opção 'Detalhar lote pela conferência' em Conferências de Entrada (Pedidos e Notas de Compra)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34944456796183-COM-E00028-n%C3%A3o-%C3%A9-poss%C3%ADvel-utilizar-a-op%C3%A7%C3%A3o-Detalhar-lote-pela-confer%C3%AAncia-em-Confer%C3%AAncias-de-Entrada-Pedidos-e-Notas-de-Compra"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:22Z"
rotulos: ["Conferência", "Configuração", "TOP", "Estoque", "Configuração de Conferência", "Erro", "Não é possível utilizar a opção 'Detalhar lote pela conferência' em Conferências de Entrada", "COM_E00028", "(Pedidos e Notas de Compra)", "Detalhar lote pela conferência"]
---

# COM_E00028: não é possível utilizar a opção 'Detalhar lote pela conferência' em Conferências de Entrada (Pedidos e Notas de Compra)

**MENSAGEM**

[COM\_E00028] Não é possível utilizar a opção 'Detalhar lote pela conferência' em Conferências de Entrada (Pedidos e Notas de Compra).

**SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta realizar uma conferência de entrada (pedidos e notas de compra) com a configuração **"Detalhar lote pela conferência"** habilitada.

**SOLUÇÃO**

**(1)** Acesse a tela **"Configuração de Conferência"** (Comercial Configuração Configuração de Conferência).

**(2)** Identifique qual código de conferência está vinculado à TOP utilizada.

**(3)** Dentro da configuração de conferência, desmarque a opção **"Detalhar lote pela conferência"**.

**CAUSA**

O erro ocorre porque a marcação **"Detalhar lote pela conferência"** está habilitada, porém o processo de conferência de compra não explode lote. Esta funcionalidade é específica apenas para conferências de saída.
