---
id: "360044217293"
titulo: "Mensagem 'Overflow Numérico'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044217293-Mensagem-Overflow-Num%C3%A9rico"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:24Z"
rotulos: ["Configuração", "Relatórios", "Financeiro", "CORE_E02510", "CORE_E03050", "Overflow Numérico", "Campos insuficientes", "Aumentar tamanho campo", "Erro"]
---

# Mensagem 'Overflow Numérico'

**MENSAGEM**

[CORE\_E03050]: 'Overflow Numérico'

[CORE\_E02510] Overflow Numérico

**SITUAÇÃO**

Após inserir os dados no filtro e gerar o relatório é apresentado a mensagem.

**SOLUÇÃO**

**(1)** Identifique qual relatório está apresentando o erro (exemplo: relatório 902 - Extrato Bancário Conciliado).

**(2)** Entre em contato com a equipe de **"Unidade"** responsável pela customização de relatórios.

**(3)** Solicite que seja realizada a adaptação do relatório no **"iReport"** ou no modelo **"JRXML"**, ajustando o tamanho dos campos para comportar adequadamente as informações.

**OBSERVAÇÃO:**

A mensagem 'Overflow Numérico' pode ocorrer em outras rotinas da aplicação. Neste caso recomenda-se realizar a abertura do chamado pelo Portal do Cliente, inserindo o Log do sistema para análise.

**CAUSA**

Esta mensagem ocorre geralmente quando o relatório possui campos, como NRO.NOTA ou NRO.DOC com tamanho insuficiente para receber informação.
