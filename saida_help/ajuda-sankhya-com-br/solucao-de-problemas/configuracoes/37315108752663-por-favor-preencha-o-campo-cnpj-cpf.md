---
id: "37315108752663"
titulo: "Por favor, preencha o campo 'CNPJ / CPF'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37315108752663-Por-favor-preencha-o-campo-CNPJ-CPF"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-11T19:26:59Z"
rotulos: ["Configuração", "Parceiro", "Preferências", "Identificação", "Erro", "Parceiros estrangeiros sem CNPJ/CPF", "Parceiros não estrangeiros", "CNPJ/CPF", "Parceiro estrangeiro", "Identificação de Estrangeiro"]
---

# Por favor, preencha o campo 'CNPJ / CPF'

**MENSAGEM:**

Por favor, preencha o campo 'CNPJ / CPF'

![Imagem 1: Por favor, preencha o campo 'CNPJ / CPF'](https://ajuda.sankhya.com.br/hc/article_attachments/37393334385559)

**SITUAÇÃO:**

Ao cadastrar um parceiro estrangeiro, o sistema exibe a mensagem acima mesmo com o endereço corretamente configurado como fora do Brasil.

**SOLUÇÃO:**

Para parceiros estrangeiros, não é obrigatório informar **CNPJ / CPF**. Porém, como a configuração do layout é global, quando o campo está marcado como **obrigatório**, o sistema exige o preenchimento independentemente do tipo de parceiro.

Para corrigir:

**(1)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(2)** Na aba **''Identificação''** no campo ''**CNPJ / CPF''**, desmarque a opção **“Campo obrigatório”**.

**(3)** Em seguida, acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(4)** Desabilite os parâmetros:

- **ACEITACGCBRANCO** – Aceita CGC/CPF de Parceiro em branco?
- **ACEITACGCBRANF2** – Aceita CGC/CPF de Parceiro em branco (F2)?

Com essa configuração, o sistema permitirá o cadastro de **parceiros estrangeiros sem CNPJ/CPF** e continuará exigindo o preenchimento para **parceiros não estrangeiros**, garantindo a validação correta.

**CAUSA:**

Esse comportamento ocorre porque o campo **“CNPJ / CPF”** está configurado como **obrigatório** no layout do cadastro de parceiros. Essa configuração é **global** e se aplica a todos os parceiros, inclusive os estrangeiros.
