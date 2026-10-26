---
id: "360043105173"
titulo: "RNTRC informado inexistente.(NT2015/001)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043105173-RNTRC-informado-inexistente-NT2015-001"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:00Z"
rotulos: ["ERROMDFE", "MDF-e", "SEFAZ", "Transporte", "681", "Rejeição 681: RNTRC Informado Inexistente", "RNTRC", "RNTRCFROTAPROP", "Documentos Eletrônicos", "Rejeição SEFAZ"]
---

# RNTRC informado inexistente.(NT2015/001)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16482744696343) MENSAGEM:**

[681-Rejeição]: RNTRC informado inexistente.(NT2015/001)

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482744705303) SITUAÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: A Sefaz passou a validar as informações dos dados do RNTRC, caso seja enviado tal informação.](https://ajuda.sankhya.com.br/hc/article_attachments/16482744711063) A Sefaz passou a validar as informações dos dados do RNTRC, caso seja enviado tal informação.

![Imagem 4: A Sefaz passou a validar as informações dos dados do RNTRC, caso seja enviado tal informação.](https://ajuda.sankhya.com.br/hc/article_attachments/360060881073)

Diante disso, é preciso identificar se o veículo utilizado no transporte está com as informações sobre RNTRC corretos.

Para consultar o RNTRC, acesse o Portal da ANTT:

<https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/>

![Imagem 5: Se for veículo da empresa (frota própria), acesse:](https://ajuda.sankhya.com.br/hc/article_attachments/16482744714391) Se for veículo da empresa (frota própria), acesse:

- Configurações » Cadastros » Empresas
- Aba: **"Naturezas"**
- Campo: **"RNTRC [Informe o RNTRC correto da Empresa]"**

![Imagem 6: Se for veículo de terceiro, acesse:](https://ajuda.sankhya.com.br/hc/article_attachments/16482744718359) Se for veículo de terceiro, acesse:

- Configurações » Cadastros » Veículos
- Aba: **"Propriedades"**
- Campo: **"RNTRC  [Informe o RNTRC correto do veiculo]"**

![Imagem 7: Caso a RNTRC esteja inválida ou não possui o respectivo cadastro, desligue o parâmetro " Enviar RNTRC da empresa para…](https://ajuda.sankhya.com.br/hc/article_attachments/16482744722199) Caso a RNTRC esteja inválida ou não possui o respectivo cadastro, desligue o parâmetro  **"Enviar RNTRC da empresa para frota própria? - RNTRCFROTAPROP"** e gere novamente a MDF-e. Assim, as informações do RNTRC não serão encaminhadas no XML, validando a aprovação da MDF-e. A SEFAZ trata esta informação como opcional.

Este parâmetro está disponível **a partir** das versões:

- 3.26b85 [Release]
- 3.25b255 [Release]
- 3.24b366 [Release]

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16482744726679) CAUSA:**

Quando for emitido um MDF-e (modelo 58) e o **RNTRC** (Registro Nacional de Transportadores Rodoviários de Carga), informado no grupo **infANTT**ou**prod**não existir na base da ANTT (Agência Nacional de Transportes Terrestres), haverá a rejeição.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482736281239) OBSERVAÇÃO:**

(**NT2015/001**) - Nota Técnica:

<https://mdfe-portal.sefaz.rs.gov.br/Site/DownloadArquivoNovo/?tipoArquivo=3&nomeArquivo=MDFe_Nota_Tecnica_2015_001.pdf>
