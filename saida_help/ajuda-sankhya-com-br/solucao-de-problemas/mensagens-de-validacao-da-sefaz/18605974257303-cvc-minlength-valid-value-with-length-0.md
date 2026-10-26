---
id: "18605974257303"
titulo: "cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type 'tsCodigoNbs'. cvc-type.3.1.3: The value '' of element 'CodigoNbs' is not valid."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18605974257303-cvc-minLength-valid-Value-with-length-0-is-not-facet-valid-with-respect-to-minLength-1-for-type-tsCodigoNbs-cvc-type-3-1-3-The-value-of-element-CodigoNbs-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:52:17Z"
rotulos: ["Configuração", "XML", "Impostos", "Prefeituras", "NFS-e", "Valor vazio para 'CodigoNbs'", "Brasília exige Código NBS", "Consulte manual preencha e ajuste"]
---

# cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type 'tsCodigoNbs'. cvc-type.3.1.3: The value '' of element 'CodigoNbs' is not valid.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18605974231319) **MENSAGEM:**

cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type 'tsCodigoNbs'.
cvc-type.3.1.3: The value '' of element 'CodigoNbs' is not valid.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18606019968151)CAUSA:**

O erro ocorre quando a prefeitura de Brasília espera que via Web Service seja encaminhado o Código NBS de acordo com serviço.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18605988817303)SOLUÇÃO:**

- Acesse o manual que está linkado abaixo e verificar qual o código correto de acordo com o serviço (CodigoNbs)
  - Link: [Manual NBS Brasília](https://drive.google.com/file/d/1b4iEQqeKHd3mH5RUDr86DRh7-juVB2_3/view?usp=sharing)
- Após conferir qual o código, acesse a tela de "**Serviços**"
- Aba > Impostos
- Campo "Código NBS"
- Insira o código no campo informado
- Gere lote
- Após a geração do lote caso o erro persista, retire o XML da tabela TGFNFSE campo XMLRPS e verifique se a tag <CodigoNbs> está preenchida corretamente de acordo com o código que foi informado
- Caso não duplique a nota que a mesma será aprovada.
