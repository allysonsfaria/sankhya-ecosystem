---
id: "37222755106711"
titulo: "E0223 Rejeição: O NIF ou cNaoNIF do tomador deve ser informado quando o grupo de informações de endereço no exterior do tomador de serviços foi informado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222755106711-E0223-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-tomador-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-tomador-de-servi%C3%A7os-foi-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:27Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "SEFAZ", "NFS-e", "Passos para resolver", "como resolver", "Identificação de Estrangeiro", "NIF ou cNaoNIF", "Nro. do NIF – Número de Identificação Fiscal", "Indicativo do NIF", "Tomador de serviços localizado no exterior", "Endereço do tomador", "Código que justifique a ausência do NIF"]
---

# E0223 Rejeição: O NIF ou cNaoNIF do tomador deve ser informado quando o grupo de informações de endereço no exterior do tomador de serviços foi informado.

**MENSAGEM**

E0223 Rejeição: O NIF ou cNaoNIF do tomador deve ser informado quando o grupo de informações de endereço no exterior do tomador de serviços foi informado.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e** para um **tomador de serviços localizado no exterior**, o sistema apresenta a rejeição E0223, indicando que as informações de identificação fiscal do tomador estrangeiro não foram preenchidas corretamente no cadastro.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **tomador de serviços estrangeiro**.

**(2)** Na aba **"Identificação"**, verifique se o campo **"País"** está preenchido com um país diferente do Brasil, confirmando que se trata de um parceiro do exterior.

**(3)** Na aba **"Fiscal"**, localize e preencha obrigatoriamente um dos seguintes campos:

- **"Nro. do NIF - Número de Identificação Fiscal''**: informe o número de identificação fiscal do tomador no país de origem, quando disponível;
- **"Indicativo do NIF"**: caso o tomador não possua NIF, selecione o código apropriado que justifique a ausência do número de identificação fiscal.

**(4)** Certifique-se de que o **endereço do tomador** esteja corretamente preenchido com as informações do país de origem, incluindo cidade e país.

**(5)** Salve as alterações realizadas no cadastro do parceiro.

**(6)** Retorne à **NFS-e** e realize um novo lançamento ou gere novamente o lote da nota fiscal.

**CAUSA**

A rejeição ocorre porque a **Sefaz exige** que, quando o tomador de serviços possui **endereço no exterior**, seja informado obrigatoriamente o **NIF** (Número de Identificação Fiscal) ou o **código que justifique a ausência do NIF** (cNaoNIF). Esta validação garante a **correta identificação fiscal** do tomador estrangeiro para fins de tributação e controle fiscal das operações internacionais.
