---
id: "360042624774"
titulo: "The value '' of element 'Serie' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624774-The-value-of-element-Serie-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:39Z"
rotulos: ["Configuração", "NF-e", "TOP", "NFS-e", "Valor Inválido da Série", "Erro", "Documentos Eletrônicos"]
---

# The value '' of element 'Serie' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16482834154135) MENSAGEM:**

cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type 'tsSerieRps'. cvc-type.3.1.3: The value '' of element 'Serie' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482862120087) SOLUÇÃO:**

Para correção, siga os passos abaixo:

**(1)** Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

"**Outras Opções**"(...)>>"**Controle de Numeração**".

![Imagem 3: " Outras Opções "(...)>>" Controle de Numeração ".](https://ajuda.sankhya.com.br/hc/article_attachments/14536719263255)

Ao clicar nesta opção será aberto o pop-up "**Controle Numeração TOP**". Caso a numeração da empresa tenha série, esta deve ser informada e o 'Tipo de Numeração', por exemplo, ser 'Empresa/Série', 'Matriz/Série' (...).

O "**Tipo de Numeração**" é configurado na aba "**Impressão**" da TOP.

Importante: As Prefeituras determinam como será a composição da SÉRIE, se utilizará Alfa Numérico ou apenas Número ou Letras.

**Exemplo:** Séries: U, 1A, 1.

O lançamento da série pode ser feito manualmente na nota, caso não tenha sido informado no faturamento, ou tratar-se de um lançamento manual.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16482834162071) CAUSA:**

Quando for emitida uma NF-e/NFS-e e não for informado valor no campo 'Série' do Cabeçalho da Nota, apresentará esta rejeição.
