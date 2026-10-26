---
id: "360043026753"
titulo: "CPF do destinatário inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043026753-CPF-do-destinat%C3%A1rio-inv%C3%A1lido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:56Z"
rotulos: ["ERRONF", "ERROCTE", "Configuração", "Parceiro", "SEFAZ", "237", "CPF do destinatário inválido", "Corrija o CPF do destinatário", "Verifique o parceiro padrão NFC-e", "Erro", "Artigo atualizado KCS", "Varejo - KCS"]
---

# CPF do destinatário inválido

**Mensagem:**

[237] Rejeição: CPF do destinatário inválido

**Causa:**

A rejeição 237 ocorre quando o sistema tenta emitir uma nota e o CPF do destinatário é informado com sequência numérica incorreta, dígito de controle inválido, ou quando o parceiro padrão de NFC-e não está corretamente vinculado nas preferências da empresa.

**Solução:**

Para correção, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros).

Na aba **"Identificação"**, localize o campo **"CNPJ / CPF"** e insira os 11 dígitos do CPF, sem pontos, traços ou espaços em branco.

**(2)** Após informar um CPF válido, refaça o cabeçalho da nota e gere um novo lote.

**Observações:**

**(1)** Para a emissão de NFC-e(modelo 65) ao consumidor final não contribuinte (não identificado), certifique-se de que o **“Parceiro padrão da NFC-e**”, vinculado nas preferências da empresa (**Comercial >> Preferências >> Empresa**), na aba **“Documentos Fiscais Eletrônicos”**, sub-aba **“NFE-e/NFC-e”**, aba **"NFC-e"** , esteja corretamente configurado.

Recomenda-se que o parceiro padrão esteja com o campo CNPJ/CPF em branco em seu cadastro. Caso seja necessário informar um valor genérico (ex.: 00000000000), orientamos consultar o manual do contribuinte do respectivo estado, pois a validação pode variar conforme as regras de cada SEFAZ estadual.

**(1)** Caso o campo **CNPJ/CPF** esteja obrigatório, é necessário habilitar o parâmetro **ACEITACGCBRANCO**. Esse parâmetro pode ser ativado apenas para realizar o ajuste do cadastro e, posteriormente, desabilitado. Se, mesmo após a ativação do parâmetro, o campo continuar obrigatório, será necessário revisar as configurações do campo nas configurações da tela.

**(1)** Caso trate-se de **parceiro estrangeiro** seguir com as orientações recomendadas em: [**Quais as principais configurações para emissão de nota de exportação?**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042535474), atentando-se ao parâmetro "**CODPAISBRASIL**" e ao campo  **"Identificação de Estrangeiro".**

**Nota:** O sistema permite vincular apenas um parceiro padrão de NFC-e por empresa. Caso a empresa trabalhe com múltiplos perfis de preço e necessite de diferentes consumidores padrão, considere esta limitação sistêmica.
