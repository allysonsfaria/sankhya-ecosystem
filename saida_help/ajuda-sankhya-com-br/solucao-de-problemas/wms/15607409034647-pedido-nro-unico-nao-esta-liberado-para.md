---
id: "15607409034647"
titulo: "Pedido nro único: não está liberado para faturamento. Separação: X \"situação no WMS\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15607409034647-Pedido-nro-%C3%BAnico-n%C3%A3o-est%C3%A1-liberado-para-faturamento-Separa%C3%A7%C3%A3o-X-situa%C3%A7%C3%A3o-no-WMS"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-08-14T12:53:50Z"
rotulos: ["Configuração", "WMS", "Faturamento", "Estoque", "CORE_E05085", "CORE_E05685", "Pedido Não Liberado para Faturamento: Situação da Separação no WMS", "Artigo atualizado KCS", "WMS - KCS"]
---

# Pedido nro único: não está liberado para faturamento. Separação: X "situação no WMS"

O **"Faturamento Automático"** no WMS Sankhya possui configurações específicas que permitem automatizar o processo de geração de notas fiscais. No entanto, é importante compreender as **"limitações nativas"** do sistema e as **"configurações disponíveis"** para otimizar o processo conforme as necessidades do negócio.

Este artigo esclarece as possibilidades de configuração do faturamento automático, especialmente quanto ao **"controle por status de carga"** e à **"configuração de cobrança para impressão de boletos"**.

### Limitação do Faturamento por Status de Carga e Mensagens de Erro

O WMS Sankhya **não possui nativamente** a funcionalidade de gerar faturamento automático considerando o status das ordens de carga. Isso significa que **não é possível configurar** o sistema para faturar somente quando toda a carga estiver com o status **"Conferência Validada"**.

Ao tentar faturar, o sistema pode apresentar as seguintes mensagens caso a expedição não tenha sido finalizada:

**"[CORE\_E05085]"**: Pedido nro único: não está liberado para faturamento. Separação: X **"Situação no WMS"**.

**Solução:** Verifique a situação da expedição e prossiga no processo até que a situação altere para **"Conferência Validada"**. Caso seja necessário faturar antes desta etapa, verifique o parâmetro **"Permite faturar antes da conferência de volumes? - FATANTESCONFVOL"**, que quando ativado, permite faturar o pedido com situação diferente da conferência validada.

**Alternativas:** Para processos que exigem controle rigoroso por status, realize o **"faturamento manual"** após validar que todas as cargas estão com o status adequado, ou considere o desenvolvimento de uma **"customização específica"**.

###

###
