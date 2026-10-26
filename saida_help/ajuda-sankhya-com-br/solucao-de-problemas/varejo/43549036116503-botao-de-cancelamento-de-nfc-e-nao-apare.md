---
id: "43549036116503"
titulo: "Botão de cancelamento de NFC-e não aparece no checkout"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549036116503-Bot%C3%A3o-de-cancelamento-de-NFC-e-n%C3%A3o-aparece-no-checkout"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-09-24T19:37:57Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Botão de cancelamento de NFC-e não aparece no checkout

### SITUAÇÃO

Ao acessar o Sankhya Checkout e tentar cancelar uma NFC-e pelo menu Gerenciamento de NFC-e, a opção "Cancelar" pode não estar disponível. Esse comportamento ocorre quando a NFC-e já foi integrada ao Sankhya ERP.

### SOLUÇÃO

Se o botão "Cancelar" não estiver visível no Checkout, o procedimento deve ser feito pelo retaguarda:

**(1)** Acesse o SankhyaOM(ERP) e abra o **Portal de Vendas**.

**(2)** Localize a NFC-e desejada e realize o cancelamento diretamente por lá.

**Observação:** O cancelamento pelo ERP só será possível se o documento ainda estiver dentro do prazo legal de cancelamento definido pela SEFAZ do seu estado.

Para ter mais tempo de cancelar as notas diretamente pelo caixa antes que elas subam para o retaguarda, você pode ajustar o tempo de integração:

**(1)** No Sankhya Checkout, acesse **Menu > Preferências > aba Integração**.

**(2)** Ajuste o campo **Intervalo de Integração com o ERP (minutos)** para 30 minutos. Com essa configuração, a NFC-e permanecerá no Checkout por 30 minutos antes de ser enviada ao ERP, permitindo o cancelamento direto no caixa.

![Imagem 1: (2) Ajuste o campo Intervalo de Integração com o ERP (minutos) para 30 minutos. Com essa configuração, a NFC-e…](https://ajuda.sankhya.com.br/hc/article_attachments/43736862300055)

Alternativas: O que fazer se o prazo da SEFAZ for excedido?

Se o prazo legal de cancelamento estipulado pela SEFAZ(estadual) já foi ultrapassado, o sistema (tanto o Checkout quanto o ERP) não conseguirá mais cancelar a nota de forma padrão. Neste cenário:

- Consulte a possibilidade de **cancelamento extemporâneo** junto à SEFAZ do seu estado.
- Caso não seja permitido, será necessário emitir uma **NF-e de devolução/estorno**, referenciando a chave da NFC-e original para regularizar a operação e os impostos.

**Importante:** Sempre consulte o contador da empresa para garantir que o procedimento adotado (extemporâneo ou devolução) esteja em conformidade com a legislação vigente do seu estado.
