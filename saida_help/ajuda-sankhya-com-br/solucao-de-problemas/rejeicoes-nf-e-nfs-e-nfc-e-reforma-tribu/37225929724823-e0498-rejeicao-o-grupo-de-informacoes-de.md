---
id: "37225929724823"
titulo: "E0498 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o fornecedor for identificado pelo NIF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225929724823-E0498-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-deve-ser-informado-obrigatoriamente-quando-o-fornecedor-for-identificado-pelo-NIF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:27Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "SEFAZ", "Identificação de Estrangeiro", "Nro. do NIF – Número de Identificação Fiscal", "Informações para REINF", "Indicativo do NIF", "Beneficiário com NIF", "Grupo de informações de endereço no exterior"]
---

# E0498 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o fornecedor for identificado pelo NIF.

**MENSAGEM**

E0498 Rejeição: O grupo de informações de endereço no exterior deve ser informado obrigatoriamente quando o fornecedor for identificado pelo NIF.

**SITUAÇÃO**

Ao emitir um documento fiscal (NF-e ou NFC-e) para um **fornecedor estrangeiro** que foi identificado pelo **NIF (Número de Identificação Fiscal)**, o sistema rejeitou a nota porque **as informações de endereço no exterior não foram preenchidas** no cadastro do parceiro.

**SOLUÇÃO**

Para corrigir esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **fornecedor estrangeiro** que está sendo utilizado no documento fiscal rejeitado.

**(2)** Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o número do NIF ou documento equivalente.

**(3)** Na aba **''Fiscal''**, seção **''Informações para REINF''**, verifique se o campo **''Indicativo do NIF''** está configurado com a opção **''Beneficiário com NIF''**.

**(4)** Preencha obrigatoriamente o campo **"Nro. do NIF – Número de Identificação Fiscal"** com o número fornecido pelo órgão de administração tributária do país de origem do fornecedor.

**(5)** Na aba **''Endereço''**, preencha as **informações completas do endereço no exterior**, incluindo:

- Logradouro
- Número
- Complemento (se houver)
- Bairro
- Cidade
- País
- Código Postal

**(6)**  Certifique-se de que o campo **"UF"** do endereço esteja configurado como **"EX"** (Exterior).

**(7)**  Salve as alterações realizadas no cadastro do parceiro.

**(8)** Retorne ao documento fiscal rejeitado e realize uma **nova tentativa de transmissão** para a SEFAZ. 

**CAUSA**

A rejeição ocorre porque a **SEFAZ exige que, quando um fornecedor estrangeiro for identificado pelo NIF** (Número de Identificação Fiscal), o **grupo de informações de endereço no exterior seja obrigatoriamente preenchido** no documento fiscal.

Esta é uma **regra de validação da SEFAZ** para garantir a correta identificação e rastreabilidade de operações com parceiros internacionais. Sem o endereço completo no exterior, o documento não pode ser validado e é rejeitado automaticamente.
