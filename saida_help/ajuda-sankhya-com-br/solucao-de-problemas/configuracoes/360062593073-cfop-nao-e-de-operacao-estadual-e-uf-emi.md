---
id: "360062593073"
titulo: "CFOP não é de Operação Estadual e UF emitente igual à UF destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360062593073-CFOP-n%C3%A3o-%C3%A9-de-Opera%C3%A7%C3%A3o-Estadual-e-UF-emitente-igual-%C3%A0-UF-destinat%C3%A1rio"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:41Z"
rotulos: ["Fiscal", "NF-e", "SEFAZ", "Impostos", "CFOP", "#publicadoHyago", "#validadoSilvio", "523", "Rejeição 523: Incompatibilidade entre CFOP e UF", "Rejeição 523"]
---

# CFOP não é de Operação Estadual e UF emitente igual à UF destinatário

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16302421294871) MENSAGEM**:

[Rejeição 523]: O CFOP não é de operação Estadual e UF emitente igual à UF do destinatário

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16302421297815) SOLUÇÃO:**

![Imagem 3: Trata-se de uma operação DENTRO do Estado?](https://ajuda.sankhya.com.br/hc/article_attachments/16302431032983) Trata-se de uma operação DENTRO do Estado?

- Nesse caso será necessário ajustar o CFOP informado para um **CFOP que inicie com 1 ou 5**. Visto que caso o  CFOP inicie por 2 ou 6 (operação interestadual) a UF do emitente deve ser obrigatoriamente **diferente da do destinatário.**

![Imagem 4: Trata-se de uma operação FORA do Estado?](https://ajuda.sankhya.com.br/hc/article_attachments/16302431034391) Trata-se de uma operação FORA do Estado?

- Nesse caso será necessário que o endereço do emitente (UF) seja diferente do endereço do destinatário (UF). Verifique o cadastro do parceiro, redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16302421301783)CAUSA:**

Essa validação em questão, confronta a UF do endereço do emitente e do destinatário com o **CFOP.**  Caso o CFOP que foi informado não atenda a operação, ou seja, uma operação estadual com **CFOP** iniciado com 2 ou 6, será retornada a rejeição.
