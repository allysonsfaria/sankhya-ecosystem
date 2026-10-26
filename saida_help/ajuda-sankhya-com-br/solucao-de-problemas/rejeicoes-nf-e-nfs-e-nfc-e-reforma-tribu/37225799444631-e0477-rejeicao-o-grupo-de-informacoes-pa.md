---
id: "37225799444631"
titulo: "E0477 Rejeição: O grupo de informações para o fornecedor deve ser informado obrigatoriamente para o tipo de documento de dedução/redução informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225799444631-E0477-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-para-o-fornecedor-deve-ser-informado-obrigatoriamente-para-o-tipo-de-documento-de-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:38Z"
rotulos: ["Configuração", "Parceiro", "Central de Vendas", "SEFAZ", "NFS-e", "Erro", "Declaração Prévia de Serviços (DPS)", "Informações do fornecedor", "CNPJ ou CPF do fornecedor", "Tipo de documento de dedução ou redução", "XML da DPS"]
---

# E0477 Rejeição: O grupo de informações para o fornecedor deve ser informado obrigatoriamente para o tipo de documento de dedução/redução informado na DPS.

**MENSAGEM**

E0477 Rejeição: O grupo de informações para o fornecedor deve ser informado obrigatoriamente para o tipo de documento de dedução/redução informado na DPS.

**SITUAÇÃO**

Ao emitir uma **Declaração Prévia de Serviços (DPS)**, o usuário informou um **tipo de documento de dedução ou redução** que exige obrigatoriamente a identificação do fornecedor, porém **não preencheu as informações do grupo de fornecedor** no documento fiscal. Com isso, a Sefaz rejeitou o documento com a mensagem E0477.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento que está apresentando a rejeição.

**(2)** Abra o documento e identifique qual tipo de documento foi informado que exige a identificação do fornecedor.

**(3)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(4)** No campo **''Identificação''**, preencha obrigatoriamente as **informações do fornecedor** no grupo correspondente, incluindo:

- CNPJ ou CPF do fornecedor;
- Razão Social ou Nome Demais dados cadastrais exigidos;

**(5)** Salve as alterações realizadas no documento.

**(6)** Gere novamente o arquivo XML da DPS e transmita o documento para a Sefaz.

**CAUSA**

A rejeição ocorre quando o **tipo de documento de dedução ou redução** informado na DPS exige obrigatoriamente a **identificação do fornecedor**, mas o **grupo de informações do fornecedor não foi preenchido** no documento fiscal. A Sefaz valida que determinados tipos de documentos de dedução necessitam da completa identificação do fornecedor para garantir a rastreabilidade e a conformidade fiscal das operações declaradas.
