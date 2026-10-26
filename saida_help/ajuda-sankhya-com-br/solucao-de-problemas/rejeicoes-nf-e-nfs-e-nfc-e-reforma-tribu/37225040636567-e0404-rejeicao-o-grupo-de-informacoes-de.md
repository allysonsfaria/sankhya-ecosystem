---
id: "37225040636567"
titulo: "E0404 Rejeição: O grupo de informações de endereço da atividade de evento ocorrido no exterior não deve ser informado quando o município do local da prestação for informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225040636567-E0404-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-da-atividade-de-evento-ocorrido-no-exterior-n%C3%A3o-deve-ser-informado-quando-o-munic%C3%ADpio-do-local-da-presta%C3%A7%C3%A3o-for-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:15Z"
rotulos: ["Cidades", "Portal de Vendas", "SEFAZ", "Erro", "Documento de Prestação de Serviços (DPS)", "Grupo de informações de endereço", "Atividade de evento ocorrido no exterior", "Município do local da prestação", "Documentos Eletrônicos"]
---

# E0404 Rejeição: O grupo de informações de endereço da atividade de evento ocorrido no exterior não deve ser informado quando o município do local da prestação for informado na DPS.

**MENSAGEM**

E0404 Rejeição: O grupo de informações de endereço da atividade de evento ocorrido no exterior não deve ser informado quando o município do local da prestação for informado na DPS.

**SITUAÇÃO**

Ao transmitir o **Documento de Prestação de Serviços (DPS)**, o sistema apresenta a rejeição E0404, indicando que foram informados **simultaneamente** o município do local da prestação e o grupo de informações de endereço da atividade de evento ocorrido no exterior.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas) e localize o documento que apresentou a rejeição.

**(2)** Na grade **''Cabeçalho''**, verifique se o campo **''Cidade''** está preenchido. Caso esteja, identifique se a prestação de serviço realmente ocorreu no território nacional.

**(3)** Caso a prestação de serviço tenha ocorrido **no exterior**:

- Remova a informação do campo "Cidade";
- Preencha o **grupo de informações de endereço da atividade de evento ocorrido no exterior** com os dados corretos do local onde o serviço foi prestado.

**(4)** Caso a prestação de serviço tenha ocorrido **no território nacional**:

- Mantenha preenchido o campo "Cidade" com o código do município brasileiro;
- Remova as informações do **grupo de endereço da atividade de evento ocorrido no exterior**.

**(5)** Salve as alterações realizadas no documento.

**(6)** Transmita novamente o **Documento de Prestação de Serviços (DPS)** para a Sefaz. 

**CAUSA**

A rejeição ocorre porque a **Sefaz não permite** que sejam informados simultaneamente o **município do local da prestação** (campo utilizado para prestações realizadas no território nacional) e o **grupo de informações de endereço da atividade de evento ocorrido no exterior**. Essas informações são **mutuamente exclusivas**: quando a prestação ocorre no Brasil, deve-se informar o município brasileiro; quando ocorre no exterior, deve-se preencher o grupo específico de endereço internacional. O preenchimento de ambos gera inconsistência na validação do documento fiscal.
