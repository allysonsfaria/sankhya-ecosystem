---
id: "35934605273751"
titulo: "Folha de autônomo | Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35934605273751-Folha-de-aut%C3%B4nomo-Erro-724-N%C3%A3o-foi-localizado-um-evento-de-remunera%C3%A7%C3%A3o-do-trabalhador-para-o-per%C3%ADodo-e-com-mesmo-demonstrativo-de-pagamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:21:18Z"
rotulos: ["Pagamentos", "eSocial", "Folha de Pagamento", "Autônomo", "Central do eSocial", "Erro", "Demonstrativo de Pagamento", "TFPBAS", "Folha Suplementar", "Folha Mensal", "TFPBSU", "Artigo atualizado KCS", "Sankhya RH - KCS", "Trabalhador Autônomo"]
---

# Folha de autônomo | Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento

**MENSAGEM**

Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento.

**SITUAÇÃO**

Este erro ocorre ao tentar enviar o evento **"S-1210"** (Pagamentos de Rendimentos do Trabalho com Retenção de IRRF) para o eSocial através da **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial). O sistema indica que não foi localizado um evento de remuneração correspondente para o período informado.

**SOLUÇÃO**

A solução varia conforme a causa identificada. Siga os passos abaixo de acordo com a situação:

**Para funcionários CLT (evento S-1200 não enviado):**

**(1)**Acesse a **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e verifique se o evento **"S-1200"** (Remuneração de Trabalhador) foi enviado para o período de referência correspondente.

**(2)**Caso o evento **"S-1200"** não tenha sido enviado, gere e envie este evento antes de tentar enviar o **"S-1210"**.

**(3)**Após o envio bem-sucedido do **"S-1200"**, retorne à **"Central do eSocial"** e envie o evento **"S-1210"**.

**Para trabalhadores autônomos (divergência no identificador de demonstrativo):**

**(1)**Acesse as folhas da referência em questão do autônomo — tanto a **"Folha Suplementar"** (TFPBSU) quanto a **"Folha Mensal"** (TFPBAS).

**(2)**Verifique as **"Datas de Pagamento"** de ambas as folhas. Certifique-se de que as duas folhas estejam com as datas de pagamento dentro da referência correspondente (Ex: referência 10/2025, os pagamentos devem ser entre 01/10/2025 a 31/10/2025).

**(3)**Caso as datas estejam diferentes ou fora da referência, corrija a **"Data de Pagamento"**.

**(4)**Gere e envie novamente o evento **"S-1210"** através da **"Central do eSocial"**.

**Para eventos retidos no console do eSocial:**

**(1)**Acesse o **"Console do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e verifique se há eventos retidos ou pendentes.

**(2)**Caso identifique eventos retidos, realize a exclusão destes eventos diretamente pelo console.

**(3)**Envie novamente o evento **"S-1200"** através da **"Central do eSocial"**.

**(4)**Após o envio bem-sucedido do **"S-1200"**, envie o evento **"S-1210"**.

**Para folhas de dissídio com eventos RRA não configurados:**

**(1)**Verifique se os eventos da folha de dissídio estão corretamente configurados como **"RRA"** (Rendimentos Recebidos Acumuladamente).

**(2)**Caso os eventos não estejam configurados como **"RRA"**, exclua as folhas do período de referência.

**(3)**Configure os eventos necessários como **"RRA"** na tela **"Eventos"** 

**(4)**Recalcule a folha de dissídio com os eventos corretamente configurados.

**(5)**Recalcule a folha mensal do período.

**(6)**Realize a retificação do evento **"S-1200"** através da **"Central do eSocial"**.

**(7)**Gere e envie o evento **"S-1210"**.

  **CAUSA**

O erro 724 ocorre quando o eSocial não consegue localizar o vínculo entre o evento de pagamento **"S-1210"** e o evento de remuneração correspondente (**"S-1200"**, **"S-1202"** ou **"S-1207"**). As principais causas são:

• **Evento de remuneração não enviado:** o evento **"S-1200"** do período de referência não foi gerado ou enviado ao eSocial antes da tentativa de envio do **"S-1210"**.

• **Divergência no identificador de demonstrativo:** para trabalhadores autônomos, as datas de pagamento estão em referência posterior ao cálculo, impedindo a montagem correta do IDMDEV (Ex: REF. 10/2025 com pagamento na REF. 11/2025).

• **Eventos retidos no console:** existem eventos pendentes ou retidos no console do eSocial que impedem o correto processamento dos novos eventos.

• **Configuração incorreta de eventos RRA:** em folhas de dissídio, os eventos não foram configurados como Rendimentos Recebidos Acumuladamente, causando inconsistência no envio.

• **Tipo de pagamento incompatível:** o campo **"Identificador de Recibo de Pagamento"** não está corretamente vinculado ao tipo de pagamento informado, conforme a regra: Tipo de Pagamento [1] deve estar em **"S-1200"**; Tipo [4] em **"S-1202"**; Tipo [5] em **"S-1207"**.
