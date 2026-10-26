---
id: "360042624674"
titulo: "Solução do erro: The value '' of element 'Numero' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624674-Solu%C3%A7%C3%A3o-do-erro-The-value-of-element-Numero-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:41Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "Correção do Erro: Valor Inválido no Campo 'Número'", "Erro", "Documentos Eletrônicos"]
---

# Solução do erro: The value '' of element 'Numero' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16447216039447) MENSAGEM:**

cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type 'tsNumeroEndereco'.cvc-type.3.1.3: The value '' of element 'Numero' is not valid.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16447216045207) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Tela Parceiros (Caminho de acesso: Configurações » Cadastros » Parceiros )](https://ajuda.sankhya.com.br/hc/article_attachments/16447216047639) Tela [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) (Caminho de acesso: Configurações » Cadastros » Parceiros)

- Aba: "**Endereço"**
- Campo: "**Número"** - Informe um valor válido ou '**S/N**'

![Imagem 4: Após os ajustes redigite a Empresa/Parceiro da nota e gere lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16447216053399) Após os ajustes redigite a Empresa/Parceiro da nota e gere lote novamente.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16447216055831) CAUSA:**

Esta mensagem ocorre quando é emitido uma NF-e e o cadastro do Parceiro(Cliente) da nota não possui o número do endereço.
