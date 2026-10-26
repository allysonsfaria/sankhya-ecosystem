---
id: "37097505979671"
titulo: "1130 Rejeição: Mais de um documento fiscal referenciado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097505979671-1130-Rejei%C3%A7%C3%A3o-Mais-de-um-documento-fiscal-referenciado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-01T12:19:33Z"
rotulos: ["NF-e", "Portal de Vendas", "XML", "SEFAZ", "Rejeição", "Passos para resolver", "Erro", "Como Resolver", "Artigo atualizado KCS", "NF-e com mais de uma referência", "Documento fiscal referenciado", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# 1130 Rejeição: Mais de um documento fiscal referenciado [nItem: 999]

MENSAGEM

Rejeição 1130: Mais de um documento fiscal referenciado.

SITUAÇÃO

A Rejeição ocorre porque foi referenciado mais de uma chave de acesso em um tipo de nota fiscal que exige apenas um documento de origem, como é o caso de uma **NF-e complementar**

  SOLUÇÃO

Para solucionar esta rejeição, siga os passos abaixo:

Acesse os Portais de Vendas / Compras  (Comercial » Consulta » Portal de Vendas/Portal de Compras).
 Localize o documento que originou a emissão da NF-e e verifique os documentos vinculados à operação no botão **"Documentos Relacionados".**
Caso existam múltiplas notas fiscais referenciadas, identifique qual documento deve permanecer vinculado à nota fiscal.

**(4)**Será preciso gerar novamente a nota fiscal para que o XML seja criado com apenas uma ocorrência da tag **DFeReferenciado**.

**CAUSA**

A rejeição ocorre porque o XML da NF-e foi gerado com mais de um documento referenciado na tag **DFeReferenciado**, situação não permitida para esse tipo de operação.

Conforme a **Nota Técnica NFe 2025.002**, a referência de múltiplos documentos é permitida apenas nos seguintes casos:

- **Nota de Débito** (tpNFDebito = 3 – Débitos de notas fiscais não processadas na apuração);
- **Nota Fiscal de Devolução** (finNFe = 4).

Conforme a regra de validação:

![Imagem 1: Conforme a regra de validação:](https://centraldeatendimento.totvs.com/hc/article_attachments/38335061927575)
