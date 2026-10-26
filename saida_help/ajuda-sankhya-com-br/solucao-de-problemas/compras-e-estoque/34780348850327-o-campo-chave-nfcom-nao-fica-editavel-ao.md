---
id: "34780348850327"
titulo: "O campo \"Chave NFCom\" não fica editável ao registrar nota de compra de serviço de comunicação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34780348850327-O-campo-Chave-NFCom-n%C3%A3o-fica-edit%C3%A1vel-ao-registrar-nota-de-compra-de-servi%C3%A7o-de-comunica%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-09-09T11:17:45Z"
rotulos: ["Configuração", "Fiscal", "TOP", "NFCom", "não fica editável", "de compra de serviço de comunicação", "Configurador de Layout da Nota", "62 - Nota Fiscal Eletrônica de Serviços de Comunicação", "O campo \"Chave NFCom\"", "ao registrar nota", "Chave NFCom", "NF-e/NFC-e/CF-e", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "CORE_E08149"]
---

# O campo "Chave NFCom" não fica editável ao registrar nota de compra de serviço de comunicação

**MENSAGEM**

[CORE\_E08149] TOP com NFCom de Terceiros deve ter a chave NFCom informada com 44 caracteres e sem espaço em branco.

**SITUAÇÃO**

Ao registrar a nota de compra de serviço de comunicação, o sistema exige o preenchimento do campo **"Chave NFCom"**, porém o campo permanece não editável. Na tela **"Configurador de Layout da Nota"** (Configurações >> Avançado >> Configurador de Layout da Nota) não é possível marcar o campo **"Editável"**.

![Imagem 1: Ao registrar a nota de compra de serviço de comunicação, o sistema exige o preenchimento do campo "Chave NFCom" , porém…](https://ajuda.sankhya.com.br/hc/article_attachments/34780371250327)

**SOLUÇÃO**

Para garantir o correto funcionamento e a editabilidade do campo, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP). Na aba **"NF-e/NFC-e/CF-e"**, configure o campo **"Modelo de documento"** para **"62 - Nota Fiscal Eletrônica de Serviços de Comunicação"**.

![Imagem 2: (1) Acesse a tela "Tipos de Operação - TOP" (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP). Na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/35706640938647)

**(2)** No mesmo cadastro da TOP, acesse a aba **"NFCom"** e configure o campo **"NFCom"** como **"Terceiros"**.

![Imagem 3: (2) No mesmo cadastro da TOP, acesse a aba "NFCom" e configure o campo "NFCom" como "Terceiros" .](https://ajuda.sankhya.com.br/hc/article_attachments/35706647425431)

**(3)** Caso o problema persista após a configuração da TOP, altere o layout da tela **"Central de Compras"** (Comercial >> Compras >> Central de Compras) de **Flex** para **HTML5**, pois o campo **"Chave NFCom"** possui funcionalidade de edição no layout HTML5.

**OBSERVAÇÕES:**

- Não configure o campo **"Chave NFCom"** como obrigatório no **"Configurador de Layout da Nota"**. O sistema valida automaticamente o preenchimento ao confirmar a nota e exibirá mensagem caso o campo esteja vazio.
- A chave NFCom deve conter exatamente **44 caracteres numéricos**, sem espaços ou caracteres especiais.
- Certifique-se de que não há configurações conflitantes na TOP.

![Imagem 4: Certifique-se de que não há configurações conflitantes na TOP.](https://ajuda.sankhya.com.br/hc/article_attachments/35706640949911)

**CAUSA**

O campo **"Chave NFCom"** permanece bloqueado se a TOP não estiver configurada corretamente para o modelo 62 (NFCom de Terceiros). Adicionalmente, o uso do layout **Flex** (que está em processo de descontinuação) pode restringir a editabilidade do campo em comparação ao layout **HTML5**. Erros de validação também ocorrem caso a chave contenha espaços em branco ou menos de 44 dígitos.
