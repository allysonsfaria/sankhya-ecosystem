---
id: "30705340927127"
titulo: "A Empresa x não contém alíquota configurada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30705340927127-A-Empresa-x-n%C3%A3o-cont%C3%A9m-al%C3%ADquota-configurada"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:34:58Z"
rotulos: ["Configuração", "Alíquota de ISS", "Cidades", "Impostos", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "CORE_E08013", "A Empresa x não contem alíquota configurada"]
---

# A Empresa x não contém alíquota configurada

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30705340912279) **MENSAGEM:**

[CORE\_E08013] A Empresa x não contém alíquota configurada

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30705340916247)SOLUÇÃO:**

Acesse a tela  **"Serviço"** (Configurações >> Cadastros >> Produtos >> Serviço), na aba **"Aliquotas de ISS"**, verifique se existe uma regra de aliquota de ISS criada para a empresa emitente da NFS-e com a cidade que será a incidência do imposto.

![Imagem 3: Acesse a tela "Serviço" (Configurações >> Cadastros >> Produtos >> Serviço) , na aba "Aliquotas de ISS" , verifique se…](https://ajuda.sankhya.com.br/hc/article_attachments/30705353849751)

Após a criação da regra, acesse novamente a NFS-e e mande gerar o lote ou confirmar a Nota.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30705353852695)CAUSA:**

Emissão de Nota fiscal de Serviço onde não foi encontrado regra de alíquota de ISS para a empresa e município de incidência.
