---
id: "10212764566295"
titulo: "Para NFC-e com Parceiro padrão e com nota com valor acima de  R$ XX,XX é obrigatório informar o campo 'CPF/CNPJ Adquirente' e opcional 'Nome Adquirente'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10212764566295-Para-NFC-e-com-Parceiro-padr%C3%A3o-e-com-nota-com-valor-acima-de-R-XX-XX-%C3%A9-obrigat%C3%B3rio-informar-o-campo-CPF-CNPJ-Adquirente-e-opcional-Nome-Adquirente"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:15Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Central de Vendas", "SEFAZ", "CORE_E02538", "Requisitos para Emissão de NFC-e com Valor Elevado"]
---

# Para NFC-e com Parceiro padrão e com nota com valor acima de  R$ XX,XX é obrigatório informar o campo 'CPF/CNPJ Adquirente' e opcional 'Nome Adquirente'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19550546973335) MENSAGEM:**

[CORE\_E02538] Para NFC-e com Parceiro padrão e com nota com valor acima de R$ XX,XX é obrigatório informar o campo 'CPF/CNPJ Adquirente' e opcional 'Nome Adquirente'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19550571224087) SITUAÇÃO:**

Ao realizar a emissão da NFC-e informando somente o Nome do Adquirente ao confirmar nota na Central de Vendas a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19550546987415) CAUSA:**

Ocorre quando o NFC-e emitido possui apenas parceiro padrão informado e o valor está acima do permitido.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19550546991383) SOLUÇÃO:**

A SEFAZ estipulou um valor máximo de R$ **10.000,00** (dez mil reais) para uma NFC-e que não possua os dados completos do destinatário (ausência parcial ou total da tag <dest>).

Cada SEFAZ Estadual pode e estipulou valores diferentes para seu estado. Então, consulte a Legislação Estadual e verifique o valor máximo permitido pela SEFAZ.

Confira no link abaixo um artigo com mais informações de como emitir um NFC-e para consumidor padrão.

[Como emitir NFC-e para Consumidor Padrão Identificado? – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863514-Como-emitir-NFC-e-para-Consumidor-Padr%C3%A3o-Identificado-)
