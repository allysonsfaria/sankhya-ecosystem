---
id: "9676470205207"
titulo: "Dia para \"Data de Referência\" deve ser 01"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9676470205207-Dia-para-Data-de-Refer%C3%AAncia-deve-ser-01"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:06:42Z"
rotulos: ["Configuração", "Contrato", "Financeiro", "CORE_E01346", "Data referência dia 01", "Parâmetro FATCONTDIA1 ligado", "Desligar parâmetro", "Erro", "FATCONTDIA1"]
---

# Dia para "Data de Referência" deve ser 01

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18979140128791) MENSAGEM:**

[CORE\_E01346] Dia para "Data de Referência" deve ser 01.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18979156704919) SITUAÇÃO:**

Ao faturar o contrato informando uma data diferente de 01 a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18979156721175) CAUSA:**

Tentar informar uma data diferente de 01 no faturamento de contratos quando o parâmetro "**Contratos Mensais sempre com referência no dia 1 -  FATCONTDIA1"** estiver ligado.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18979156729239) SOLUÇÃO:**

Se o parâmetro "**Contratos Mensais sempre com referência no dia 1 -  FATCONTDIA1"** estiver ligado, não será possível digitar uma data diferente do dia 1º (primeiro). Caso seja informada, o sistema apresentará a mensagem citada. Assim, desligue o parâmetro.

![Imagem 5: Se o parâmetro " Contratos Mensais sempre com referência no dia 1 - FATCONTDIA1" estiver ligado, não será possível…](https://ajuda.sankhya.com.br/hc/article_attachments/18979140178711)

Segue abaixo o manual da rotina para mais informações.

[Contratos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos)
