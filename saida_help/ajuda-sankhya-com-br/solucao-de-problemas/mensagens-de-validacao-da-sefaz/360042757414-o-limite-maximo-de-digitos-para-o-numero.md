---
id: "360042757414"
titulo: "O limite máximo de dígitos para o número aleatório foi configurado como 9 e o permitido é 8"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042757414-O-limite-m%C3%A1ximo-de-d%C3%ADgitos-para-o-n%C3%BAmero-aleat%C3%B3rio-foi-configurado-como-9-e-o-permitido-%C3%A9-8"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:09Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Impostos", "Limite de Dígitos para Número Aleatório", "Erro", "Documentos Eletrônicos"]
---

# O limite máximo de dígitos para o número aleatório foi configurado como 9 e o permitido é 8

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16452253831191) **MENSAGEM:**

O limite máximo de dígitos para o número aleatório foi configurado como 9 e o permitido é 8.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16452253837079) SOLUÇÃO:**

![Imagem 3: Verifique possível indisponibilidade do evento de recepção da SEFAZ.](https://ajuda.sankhya.com.br/hc/article_attachments/16452253841431) Verifique possível indisponibilidade do evento de recepção da SEFAZ.

- Essa verificação pode ser realizada contactando a SEFAZ do seu Estado (Contador poderá auxiliar) e/ou através do site da SEFAZ: [Consulta Disponibilidade](http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY=)
- Caso essa indisponibilidade esteja ocorrendo, faz-se necessário aguardar que o serviço retorne a operação, para prosseguir com a geração do lote.

![Imagem 4: Versão NF-e definida de forma incoerente com o esperado:](https://ajuda.sankhya.com.br/hc/article_attachments/16452253841431) Versão NF-e definida de forma incoerente com o esperado:

- Acesse a tela "**[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)"** (Caminho de acesso: Comercial » Preferências), selecione a empresa emitente e, na aba "**NF-e/NFC-e"**, busque o campo "**Versão NF-e/NFC-e"**:

![Imagem 5: Acesse a tela " Empresa " (Caminho de acesso: Comercial » Preferências ), selecione a empresa emitente e, na aba "…](https://ajuda.sankhya.com.br/hc/article_attachments/14393139982103)

- Caso não existam particularidades para seu Estado, essa opção deve estar definida como "Versão NFe e NFCe 4.0".
- Se o conteúdo for diferente do acima, realize o ajuste, gere um novo lote.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16452253845015) CAUSA:**

Mensagem apresentada na emissão de NF-e, normalmente causada por indisponibilidade do evento de recepção da SEFAZ.
