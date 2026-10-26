---
id: "44030398199959"
titulo: "Itens da seleção já foram enviados para Expedição no WMS e existem Ordens de Carga não foi encerrada. Deseja encerrar a expedição para estas Ordens de Carga?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44030398199959-Itens-da-sele%C3%A7%C3%A3o-j%C3%A1-foram-enviados-para-Expedi%C3%A7%C3%A3o-no-WMS-e-existem-Ordens-de-Carga-n%C3%A3o-foi-encerrada-Deseja-encerrar-a-expedi%C3%A7%C3%A3o-para-estas-Ordens-de-Carga"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-10-07T12:16:47Z"
rotulos: ["WMS - KCS", "Parâmetros do Sistema", "Expedição no WMS", "ENCERRAOCMANUAL", "Ordem de Carga (OC)"]
---

# Itens da seleção já foram enviados para Expedição no WMS e existem Ordens de Carga não foi encerrada. Deseja encerrar a expedição para estas Ordens de Carga?

**MENSAGEM**

Itens da seleção já foram enviados para Expedição no WMS e existem Ordens de Carga não foi encerrada. Deseja encerrar a expedição para estas Ordens de Carga?

**SITUAÇÃO**

Ao enviar uma seleção de notas/pedidos para a Expedição

**SOLUÇÃO**

Essa mensagem é uma **confirmação esperada**, e não um erro. Ela é apresentada quando o sistema identifica que não existem mais itens pendentes de envio para a **Ordem de Carga (OC)**, mas ela ainda não foi registrada como encerrada no WMS.

**(1)** Se a separação/expedição da Ordem de Carga estiver concluída, **confirme a mensagem**. O sistema marcará a OC como enviada/encerrada.

**(2)** Para definir manualmente quando uma OC deve ser encerrada, ajuste o parâmetro:

- Acesse ''**Parâmetros do Sistema''** (Configurações > Avançado).
- Localize o parâmetro **''ENCERRAOCMANUAL - Encerrar ordem de carga manualmente?''**
- Por padrão, o parâmetro permanece **desligado**.

**ATENÇÃO:** ao ativar esse parâmetro, o sistema exigirá a confirmação para encerrar a OC sempre que não houver mais itens pendentes de envio.

**CAUSA**

A mensagem é apresentada durante o envio de itens para a Expedição quando as seguintes condições são atendidas simultaneamente:

- **Não existem mais itens pendentes de envio** para a Ordem de Carga, indicando que essa foi a última leva.
- **A Ordem de Carga ainda não está registrada como enviada ao WMS ou encerrada**
- O parâmetro ''ENCERRAOCMANUAL'' está desativado, permitindo que o encerramento da Ordem de Carga seja realizado automaticamente pelo sistema.
