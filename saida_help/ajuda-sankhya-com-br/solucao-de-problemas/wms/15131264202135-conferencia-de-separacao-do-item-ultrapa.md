---
id: "15131264202135"
titulo: "Conferência de separação do item ultrapassou a quantidade do pedido sem emitir aviso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15131264202135-Confer%C3%AAncia-de-separa%C3%A7%C3%A3o-do-item-ultrapassou-a-quantidade-do-pedido-sem-emitir-aviso"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:57:29Z"
rotulos: ["Conferência", "Configuração", "WMS", "Estoque", "Preferências", "Ativar EMIAVCONFSAIDA", "Conferência sem aviso de quantidade excedida", "Validar quantidade na conferência"]
---

# Conferência de separação do item ultrapassou a quantidade do pedido sem emitir aviso

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16591550167831) SITUAÇÃO:**

No superwaba, ao realizarmos a conferência de separação do item, o conferente faz a leitura da etiqueta do item um a um, mas ao ultrapassar a quantidade do pedido, o sistema não emitiu nenhum aviso. Permitindo assim que o conferente fizesse a leitura de quantidade superior à quantidade do item do pedido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16591561028119) SOLUÇÃO:**

Para ser possível validar a quantidade na conferência de item a item, ative o parâmetro **"EMIAVCONFSAIDA"** e desligue a preferência **"Tratar sobra ao final da conferência?".** Assim, o sistema realiza a validação da quantidade ao bipar o cód. de barras do produto na conferência.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16591550171927) CAUSA:**

Identificado que quando o parâmetro EMIAVCONFSAIDA está ativado em conjunto com a preferência **Tratar sobra ao final da conferência?,** o sistema valida a quantidade na conferência só ao fazer o envio da mesma.
