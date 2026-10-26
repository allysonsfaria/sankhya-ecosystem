---
id: "15921111517591"
titulo: "Código do Município do Destinatário diverge do cadastrado na UF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15921111517591-C%C3%B3digo-do-Munic%C3%ADpio-do-Destinat%C3%A1rio-diverge-do-cadastrado-na-UF"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:55:55Z"
rotulos: ["Fiscal", "Parceiro", "NF-e", "Cidades", "SEFAZ", "Município do destinatário", "Verifique cadastros", "Consulte SEFAZ/IBGE", "Erro"]
---

# Código do Município do Destinatário diverge do cadastrado na UF

**![Imagem 1: MENSAGEM](https://ajuda.sankhya.com.br/hc/article_attachments/15921121765015)  MENSAGEM**

Rejeição 482: Código do Município do Destinatário diverge do cadastrado na UF

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15921082474391) CAUSA:**

Quando for emitida uma NF-e e o Código do Município (cMun) do Destinatário (Parceiro) informado no cadastro de  endereço do Parceiro for diferente do Código do Município que consta no Cadastro do Contribuinte para o mesmo Destinatário  (Parceiro), será retornado a rejeição "482 - Código do Município do Destinatário diverge do cadastrado na UF.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15921098634519) SOLUÇÃO:**

![Imagem 4: Consulte o cadastro do parceiro na SEFAZ, para isso acesse o Cadastro Centralizado de Contribuinte através do link…](https://ajuda.sankhya.com.br/hc/article_attachments/15922095870359) Consulte o cadastro do parceiro na SEFAZ, para isso acesse o Cadastro Centralizado de Contribuinte através do  link <https://dfe-portal.svrs.rs.gov.br/NFE/CCC>     

- No XML: O campo associado a validação é o **<cMun>**, dentro do grupo **<dest>**

-<dest>

<CNPJ>99999999000191</CNPJ>

<xNome>NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL</xNome>

<enderDest>

<xLgr>Avenida MARCOS DE FREITAS COSTA</xLgr>

<nro>369</nro>

<xBairro>DANIEL FONSECA</xBairro>

<cMun>3170206</cMun>

<xMun>Uberlandia</xMun>

<UF>MG</UF>

<CEP>38400328</CEP>

<cPais>1058</cPais>

<xPais>Brasil</xPais>

</enderDest>

<indIEDest>1</indIEDest>

<IE>0627671100055</IE>

<email></email>

</dest>

![Imagem 5: Consulte também o código do Município do destinatário no campo cMun, se está de acordo com a UF (UF) informada, o mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/15922099936919) Consulte também o código do Município do destinatário no campo cMun, se está de acordo com a UF (UF) informada, o mesmo deve estar igual ao cadastrado no [site do IBGE](https://cidades.ibge.gov.br/)

[( https://cidades.ibge.gov.br/)](https://cidades.ibge.gov.br/)

Segue regra de validação da Sefaz :

![Imagem 6: Segue regra de validação da Sefaz :](https://ajuda.sankhya.com.br/hc/article_attachments/15920808909847)

**Referência:**

- Nota Técnica 2015/002 (v. 1.30) -
- <http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=>
