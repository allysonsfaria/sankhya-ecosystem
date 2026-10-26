---
id: "37097471381527"
titulo: "321 Rejeição: NF-e de devolução de mercadoria não possui documento fiscal referenciado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097471381527-321-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-de-mercadoria-n%C3%A3o-possui-documento-fiscal-referenciado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:42Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "Devolução", "Passos para resolver", "Erro", "Como Resolver", "Documento fiscal referenciado", "NF-e de devolução de mercadoria", "SankhyaW", "Devolução de mercadoria", "Documentos Eletrônicos"]
---

# 321 Rejeição: NF-e de devolução de mercadoria não possui documento fiscal referenciado

**MENSAGEM**

321 Rejeição: NF-e de devolução de mercadoria não possui documento fiscal referenciado

**SITUAÇÃO**

Ao realizar a emissão de uma NF-e de devolução de mercadoria pela tela **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas) no SankhyaW, o documento é rejeitado pela SEFAZ. Ao acessar a opção **"Ver Acompanhamento"**, é possível consultar o detalhe da rejeição, que indica a ausência de documento fiscal referenciado na NF-e de devolução.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Selecione a TOP de devolução que está sendo utilizada.

**(3)** Acesse a aba **"NF-e/NFC-e"**.

**(4)** Localize e marque a opção **"Buscar NF de origem p/ referenciar na NF-e"**.

**(5)** Salve as alterações.

**(6)** Caso a nota já tenha sido rejeitada:

- Inutilize a numeração da devolução rejeitada;
- Exclua o registro da devolução.

**(7)** Para realizar uma nova devolução corretamente:

- Selecione a NF-e de origem (Venda/Compra);
- Clique no botão **"Devolv./Estor."**;
- Selecione os produtos que serão devolvidos ou toda a nota.

**(8)** Para casos em que a nota de origem não é NF-e ou não possui informações no sistema, utilize o campo **"ChaveNFeRef"** na nota de devolução para que seja gerada a tag de referência adequada.

**CAUSA**

Conforme a Nota Técnica 2013/005, a SEFAZ exige que toda NF-e com finalidade igual a **"4 - Devolução de mercadoria"** contenha a informação do documento fiscal referenciado que está sendo devolvido. Quando esta informação não é fornecida, a SEFAZ retorna a rejeição 321.

Esta validação ocorre porque é necessário estabelecer o vínculo entre a nota de devolução e a nota original para fins de controle fiscal. O sistema precisa da marcação **"Buscar NF de origem p/ referenciar na NF-e"** na TOP para que possa automaticamente preencher o grupo de documentos referenciados na NF-e, incluindo a chave da NFe original (tag <refNFe>).
