---
id: "360042640354"
titulo: "Não é de Operação com Exterior e Código País destinatário difere de 1058 (Brasil)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042640354-N%C3%A3o-%C3%A9-de-Opera%C3%A7%C3%A3o-com-Exterior-e-C%C3%B3digo-Pa%C3%ADs-destinat%C3%A1rio-difere-de-1058-Brasil"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:40Z"
rotulos: ["ERRONF", "#RevisadoBraga", "Configuração", "Fiscal", "Parceiro", "NF-e", "SEFAZ", "511", "Código País Diferente de 1058", "Documentos Eletrônicos"]
---

# Não é de Operação com Exterior e Código País destinatário difere de 1058 (Brasil)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16086768270999) MENSAGEM:**

511-Rejeição: Não é de Operação com Exterior e Código País destinatário difere de 1058 (Brasil).(NT2015/002)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16086768272791) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16086768274327) Acesse: Configurações » Cadastros » Parceiros

- Aba: "**Identificação**";
- Campo **"Identificação de Estrangeiro":** Preencha adequadamente, de acordo com instruções do contador;
- Caso a venda não seja com Parceiro Exterior, considere verificar os cadastro de Endereço (Cidade, Pais, UF).

![Imagem 4: Após os ajustes, gere novamente a NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16086768279191) Após os ajustes, gere novamente a NF-e.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16086738885015) CAUSA:**

Quando for emitida uma NF-e de Operação Estadual ou Operação Interestadual e o Código do País do Destinatário do documento for diferente de 1058 (Brasil), a NF-e será rejeitada.

**Exceção a regra:**

1. Se o campo "<**idEstrangeiro**>" estiver preenchido é permitido que o Código do País (cPais) seja diferente de 1058 (Brasil).
