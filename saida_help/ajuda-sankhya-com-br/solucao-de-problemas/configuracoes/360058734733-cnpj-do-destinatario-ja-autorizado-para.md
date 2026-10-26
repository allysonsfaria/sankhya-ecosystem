---
id: "360058734733"
titulo: "CNPJ do destinatário já autorizado para download"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058734733-CNPJ-do-destinat%C3%A1rio-j%C3%A1-autorizado-para-download"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:27:05Z"
rotulos: ["#criadoRoger", "Configuração", "Empresa", "Parceiro", "NF-e", "XML", "SEFAZ", "ticket#41931", "324", "CNPJ Autorizado para Download"]
---

# CNPJ do destinatário já autorizado para download

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16249991793815) MENSAGEM**:

324-Rejeição: CNPJ do destinatário já autorizado para download

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16249991795607) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Parceiros Aba: "Acesso ao XML da NF-e/CTe" Verifique o parceiro vinculado a este…](https://ajuda.sankhya.com.br/hc/article_attachments/16250013855767) Acesse: Configurações » Cadastros » Parceiros
Aba: **"Acesso ao XML da NF-e/CTe"**

Verifique o parceiro vinculado a este cadastro, assim como seu CPF (não informe no campo Parceiro o mesmo código do parceiro deste cadastro).

![Imagem 4: Acesse: Comercial » Preferências » Empresa Aba: "Contador" Os dados do Contador não pode ser os mesmo dados do Parceiro…](https://ajuda.sankhya.com.br/hc/article_attachments/16250013857047) Acesse: Comercial » Preferências » Empresa
Aba: **"Contador"**
Os dados do Contador não pode ser os mesmo dados do Parceiro da nota (efetue o ajuste caso os dados sejam os mesmos, solicite apoio da equipe Fiscal da empresa).

![Imagem 5: Após os ajustes, exclua e fature novamente a nota e gere Lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16249983335575) Após os ajustes, exclua e fature novamente a nota e gere Lote.

**Artigos relacionados:**

- [Como gerar a tag <autXML> com os dados do Contador no XML ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044344033)

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16250013858455) OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16250013867671)CAUSA:**

Quando for emitida uma NF-e **e o CNPJ do destinatário** for informado no **Grupo de Autorização para obter XML**, será retornada a rejeição.
