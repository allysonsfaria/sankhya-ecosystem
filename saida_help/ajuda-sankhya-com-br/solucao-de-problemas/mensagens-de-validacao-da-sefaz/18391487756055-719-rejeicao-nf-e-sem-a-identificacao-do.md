---
id: "18391487756055"
titulo: "719 - Rejeição: NF-e sem a identificação do destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18391487756055-719-Rejei%C3%A7%C3%A3o-NF-e-sem-a-identifica%C3%A7%C3%A3o-do-destinat%C3%A1rio"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:52:36Z"
rotulos: ["NF-e", "XML", "SEFAZ", "719", "Rejeição 719", "Identificação do Destinatário", "Erro", "Identificação de Estrangeiro"]
---

# 719 - Rejeição: NF-e sem a identificação do destinatário

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18391460556695) **MENSAGEM:**

719 - Rejeição: NF-e sem a identificação do destinatário.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18391481521431)CAUSA:**

Ao realizar a emissão de uma NF-e (mod. 55) sem a identificação do Destinatário (grupo **<dest>**, tags **<CNPJ>**, **<CPF>** ou **<idEstrangeiro>**), o órgão autorizador retorna a rejeição “719 – NF-e sem identificação do Destinatário”.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18391496278551)SOLUÇÃO:**

Localize a nota rejeitada e acione no Botão "NF-e" a opção "Gerar XML da NF-e em arquivo para conferência", encontre no XML o grupo **<infNFe>**/**<dest>** que deve conter uma das opções de identificação (**<CNPJ>**, **<CPF>** ou **<idEstrangeiro>**).

Se não tiver informação nessas Tags será apresentada a mensagem de erro e para corrigir é necessário popular o campo "Identificação de Estrangeiro" na aba identificação conforme as informações do seu fornecedor ou popular o campo "CNPJ" com "00000000000000" se não tiver nenhuma informação. 

![Imagem 4: Se não tiver informação nessas Tags será apresentada a mensagem de erro e para corrigir é necessário popular o campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/18399943730071)
