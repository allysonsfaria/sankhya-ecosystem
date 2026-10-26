---
id: "360042637934"
titulo: "MDF-e já está encerrado na base de dados da SEFAZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042637934-MDF-e-j%C3%A1-est%C3%A1-encerrado-na-base-de-dados-da-SEFAZ"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:48Z"
rotulos: ["ERROMDFE", "MDF-e", "Configuração", "SEFAZ", "609", "Rejeição", "Rejeição 609: MDF-e Encerrado", "Documentos Eletrônicos"]
---

# MDF-e já está encerrado na base de dados da SEFAZ

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16444223671831) MENSAGEM:**

[609-Rejeição]: MDF-e já está encerrado na base de dados da SEFAZ.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16444223673111) SOLUÇÃO:**

Considere o comportamento da Aplicação, conforme abaixo:

**(1)** Pode ser verificada e ajustada caso necessário a numeração, acessando:

(2)** "[Viagens de Transporte (MDF-e)"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514)** (Caminho de acesso: Comercial » Rotinas » Viagens de Transporte (MDF-e)), botão: "**Outras Opções.**.."»"**Controle de Numeração**"

**(2)** Campo: **"Último Código"**.

Este campo traz a informação do último número de MDF-e gerado. Caso algum usuário tenha alterado equivocadamente o valor deste campo, considere ajustar para o último número de MDF-e gerado.

Caso esteja correto. Considere lançar uma nova MDF-e para que o sistema busque o próximo número de MDF-e disponível para uso.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16444196502039) CAUSA:**

Ocorre quando for emitida um MDF-e com a mesma numeração, série, CNPJ de um outro MDF-e que já havia sido encerrado, haverá a rejeição.
