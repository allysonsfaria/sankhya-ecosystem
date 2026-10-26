---
id: "7063265092375"
titulo: "Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7063265092375-Transporte-pr%C3%B3prio-por-conta-do-Destinat%C3%A1rio-e-CNPJ-Base-ou-CPF-do-Transportador-difere-do-CNPJ-Base-ou-CPF-do-Destinat%C3%A1rio"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:15:17Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Transporte", "848", "Transporte Próprio e CNPJ/CPF do Transportador", "Regra de validação"]
---

# Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16455156591639) MENSAGEM**:

[848-Rejeição]: Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16455156596375) SOLUÇÃO:**

Se for NF-e de saída e Modalidade do Frete = 4, o CNPJ Base ou CPF do transportador deve ser **IGUAL** ao CNPJ Base ou CPF do Destinatário.

**![Imagem 3: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16455156606103) OBSERVAÇÃO:**

Regra de validação não se aplica quando CNPJ/CPF do transportador não for informado.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16455156609431) CAUSA:**

O erro ocorre quando a modalidade do frete é igual a 4 e o CNPJ ou CPF do transportador é diferente do CNPJ Base ou CPF do Destinatário.
