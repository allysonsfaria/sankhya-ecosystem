---
id: "37225862271127"
titulo: "E1538 Rejeição: O NIF ou cNaoNIF do fornecedor deve ser informado quando o grupo de informações de endereço no exterior do fornecedor de serviços for informado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225862271127-E1538-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-fornecedor-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-fornecedor-de-servi%C3%A7os-for-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:33Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "SEFAZ", "Fornecedor estrangeiro", "NIF ou cNaoNIF", "Número de Identificação Fiscal (NIF)", "Informações de endereço no exterior", "Indicativo de dispensa/não exigência do NIF", "Endereço no exterior"]
---

# E1538 Rejeição: O NIF ou cNaoNIF do fornecedor deve ser informado quando o grupo de informações de endereço no exterior do fornecedor de serviços for informado.

**MENSAGEM**

E1538 Rejeição: O NIF ou cNaoNIF do fornecedor deve ser informado quando o grupo de informações de endereço no exterior do fornecedor de serviços for informado.

**SITUAÇÃO**

Ao emitir um documento fiscal com **fornecedor estrangeiro**, o sistema identificou que foram informadas as **informações de endereço no exterior**, porém não foi preenchido o **Número de Identificação Fiscal (NIF)** ou o **indicativo de dispensa/não exigência do NIF** no cadastro do parceiro. Esta inconsistência resulta na rejeição do documento pela Sefaz.

**SOLUÇÃO**

Para corrigir a rejeição, configure adequadamente o cadastro do parceiro estrangeiro seguindo os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o fornecedor estrangeiro.

**(2)** Acesse a aba **"Identificação"** e verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o número do passaporte ou documento legal que identifique o fornecedor estrangeiro.

**(3)** Na aba **"Fiscal"**, localize o campo **"Indicativo do NIF"** e selecione uma das opções abaixo, conforme a situação do fornecedor:

- **Beneficiário com NIF:** quando o fornecedor possui Número de Identificação Fiscal fornecido pelo órgão de administração tributária do país de origem;
- **Beneficiário dispensado do NIF:** quando o fornecedor está dispensado de possuir NIF;
- **País não exige NIF:** quando o país de origem do fornecedor não exige este tipo de identificação fiscal.

**(4)** Caso tenha selecionado a opção **"Beneficiário com NIF"**, preencha o campo **"Nro. do NIF – Número de Identificação Fiscal"** que será habilitado automaticamente. Este campo deve conter no mínimo 5 e no máximo 20 caracteres/números.

**(5)** Salve as alterações realizadas no cadastro do parceiro.

**(6)** Realize um novo lançamento do documento fiscal.

**CAUSA**

A rejeição ocorre quando o documento fiscal é emitido para um **fornecedor estrangeiro** com informações de **endereço no exterior** preenchidas, mas sem a devida configuração do **Número de Identificação Fiscal (NIF)** ou do **indicativo de dispensa/não exigência do NIF** no cadastro do parceiro. A Sefaz exige que, ao informar o grupo de endereço no exterior, seja obrigatoriamente indicado o NIF ou a justificativa de sua ausência através do campo "Indicativo do NIF".
