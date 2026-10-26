---
id: "37229535482135"
titulo: "E0298 REJEIÇÃO: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o intermediário for identificado pelo NIF e o emitente por CNPJ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229535482135-E0298-REJEI%C3%87%C3%83O-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-intermedi%C3%A1rio-for-identificado-pelo-NIF-e-o-emitente-por-CNPJ"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:56Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "NIF", "Emitente identificado por CNPJ", "Grupo de informações de endereço no exterior do intermediário", "Intermediário identificado pelo NIF", "Número de Identificação Fiscal do exterior", "EX - Exterior", "Documentos Eletrônicos"]
---

# E0298 REJEIÇÃO: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o intermediário for identificado pelo NIF e o emitente por CNPJ

**MENSAGEM**

E0298 REJEIÇÃO: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o intermediário for identificado pelo NIF e o emitente por CNPJ

**SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e com **intermediário identificado pelo NIF** (Número de Identificação Fiscal do exterior) e o **emitente identificado por CNPJ**, o documento fiscal é rejeitado pela Sefaz quando o **grupo de informações de endereço no exterior do intermediário** não está preenchido.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **intermediário da operação**.

**(2)** Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o ''**NIF do intermediário''**.

**(3)** Ainda na aba **"Identificação"**, localize a seção de **endereço do parceiro** e preencha obrigatoriamente os seguintes campos relacionados ao **endereço no exterior**:

- **"País"**: selecione o país de origem do intermediário;
- **"Logradouro"**: informe o endereço completo no exterior;
- **"Número"**: informe o número do endereço;
- **"Cidade"**: informe a cidade no exterior;
- **"Estado/Província"**: informe o estado ou província, se aplicável;
- **"Código Postal"**: informe o código postal do endereço no exterior

**(4)** Certifique-se de que o campo **"UF"** esteja configurado como **"EX - Exterior"** para identificar corretamente que se trata de um endereço no exterior.

**(5)** Salve as alterações realizadas no cadastro do parceiro.

**(6)** Realize um novo lançamento da NF-e ou NFC-e e tente transmitir o documento fiscal novamente.

**CAUSA**

A rejeição ocorre devido à **validação da Sefaz** que exige o preenchimento obrigatório do **grupo de informações de endereço no exterior** quando o intermediário da operação é identificado pelo **NIF** (Número de Identificação Fiscal do exterior) e o emitente do documento fiscal é identificado por **CNPJ**. Sem o preenchimento completo dos dados de endereço no exterior do intermediário, o documento fiscal não atende aos requisitos legais e é rejeitado pela Sefaz.
