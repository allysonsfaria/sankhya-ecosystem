---
id: "7791345915287"
titulo: "Informe o Tipo de Operação para CTe-OS em Outras Opções > Preferências para Importar CTe > CT-e de Terceiros > Tipo de Operação CTe-OS "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7791345915287-Informe-o-Tipo-de-Opera%C3%A7%C3%A3o-para-CTe-OS-em-Outras-Op%C3%A7%C3%B5es-Prefer%C3%AAncias-para-Importar-CTe-CT-e-de-Terceiros-Tipo-de-Opera%C3%A7%C3%A3o-CTe-OS"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:13:04Z"
rotulos: ["CT-e", "Configuração", "XML", "Importação", "TOP", "não apagar", "#validadoRaiane", "CORE_E03198", "Informe Tipo de Operação CTe-OS", "Defina Tipo de Operação no Portal de Importação XML", "Erro ao processar XML de CT-e OS sem configuração correta", "Documentos Eletrônicos"]
---

# Informe o Tipo de Operação para CTe-OS em Outras Opções > Preferências para Importar CTe > CT-e de Terceiros > Tipo de Operação CTe-OS 

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16540822107415) MENSAGEM**:

Informe o Tipo de Operação para CTe-OS em Outras Opções > Preferências para Importar CTe > CT-e de Terceiros > Tipo de Operação CTe-OS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16540838654999) SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo:

![Imagem 3: Entre no portal de importação de XML clique no botão: Outras opções -> Preferências para Importar CTe > CT-e de…](https://ajuda.sankhya.com.br/hc/article_attachments/16540838658071) Entre no portal de importação de XML clique no botão: Outras opções -> Preferências para Importar CTe > CT-e de Terceiros,

![Imagem 4: Em seguida, informe o tipo de operação utilizado para importar documentos do modelo 67 no campo " Tipo de Operação…](https://ajuda.sankhya.com.br/hc/article_attachments/16540822116887) Em seguida, informe o tipo de operação utilizado para importar documentos do modelo 67 no campo **"Tipo de Operação CTe-OS"**;

![Imagem 5: Em seguida, informe o tipo de operação utilizado para importar documentos do modelo 67 no campo " Tipo de Operação…](https://ajuda.sankhya.com.br/hc/article_attachments/16540822119703)

![Imagem 6: Caso não encontre a TOP que configurou para tal documento lembre-se que o tipo de operação precisa ter uma configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/16540822121623) Caso não encontre a TOP que configurou para tal documento lembre-se que o tipo de operação precisa ter uma configuração específica em alguns campos:

| **1-Modelo do documento(Aba NF-e/NFC-e):** '67- Conhecimento Transporte Eletrônico Outros Serviços';  **2-NF-e(Aba NF-e/NFC-e):** 'Terceiros';  **3-Tipo de movimento:** 'I-Financeiro'; |
| --- |

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16540822125975)CAUSA:**

O erro ocorre pois ao tentar processar o xml de um documento modelo CT-e OS no portal de importação de xml, caso existe uma top informada no campo Tipo Operação CT-e OS (Outras Opções > Preferências para Importar CTe > CT-e de Terceiros).
