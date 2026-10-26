---
id: "35042230651415"
titulo: "WMS_E00819: não foi encontrado endereço de checkout disponível no momento que seja compatível com a área se conferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35042230651415-WMS-E00819-n%C3%A3o-foi-encontrado-endere%C3%A7o-de-checkout-dispon%C3%ADvel-no-momento-que-seja-compat%C3%ADvel-com-a-%C3%A1rea-se-confer%C3%AAncia"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:08Z"
rotulos: ["Conferência", "Configuração", "WMS", "Estoque", "Endereços", "Consulta de Checkouts", "Erro", "Situação do Checkout", "Nível de Endereço", "WMS_E00819", "Não foi encontrado endereço de checkout disponível no momento que seja compatível com a área de conferência", "Exclusivo para Conferência"]
---

# WMS_E00819: não foi encontrado endereço de checkout disponível no momento que seja compatível com a área se conferência

**MENSAGEM**

[WMS\_E00819] Não foi encontrado endereço de checkout disponível no momento que seja compatível com a área de conferência.

**SITUAÇÃO**

A mensagem aparece quando o usuário tenta realizar uma operação de conferência no sistema WMS e todos os endereços de checkout vinculados à área de conferência já estão ocupados ou indisponíveis.

**SOLUÇÃO**

**(1)** Acesse a tela **"Consulta de Checkouts"** (WMS » Consultas » Consulta de Checkouts) e filtre a área de conferência utilizada.

**(2)** Selecione em **"Situação do Checkout"** a opção **"Disponível"** para verificar todos os endereços disponíveis para a área de conferência.

**(3)** Caso não exista nenhum endereço de checkout disponível, acesse a tela **"Endereço de Armazenamento"** (WMS » Cadastros » Endereço de Armazenamento).

**(4)** Na seção **"Nível de Endereço"**, crie um endereço para checkouts e um endereço com a marcação **"Exclusivo para Conferência"**.

**(5)** Após criar os endereços, acesse a tela **"Área de Conferência"** (WMS » Cadastros » Área de Conferência).

**(6)** Na aba **"Endereços"**, vincule os códigos reduzidos dos endereços de checkouts criados à área de conferência.

**CAUSA**

A mensagem ocorre quando todos os endereços de checkout vinculados à área de conferência já estão ocupados ou não há endereços configurados para a área de conferência específica.
