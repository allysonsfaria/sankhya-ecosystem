---
id: "360043128133"
titulo: "Obrigatória as informações do responsável técnico(NT2018.005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043128133-Obrigat%C3%B3ria-as-informa%C3%A7%C3%B5es-do-respons%C3%A1vel-t%C3%A9cnico-NT2018-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:10Z"
rotulos: ["ERRONF", "Configuração", "Fast Service", "NF-e", "XML", "SEFAZ", "NFC-e", "972", "Informações do Responsável Técnico obrigatórias", "Documentos Eletrônicos"]
---

# Obrigatória as informações do responsável técnico(NT2018.005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16086166338711) MENSAGEM:**

972-Rejeição: Obrigatória as informações do responsável técnico.(NT2018.005)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16086137256983) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Sistema Sankhya W atualizado nas versões abaixo ou superior:](https://ajuda.sankhya.com.br/hc/article_attachments/16086166344855) Sistema **Sankhya W** atualizado nas versões abaixo ou superior:

- 3.30b58 [Release]
- 3.29b220 [Release]
- 3.28b383 [Release]

**![Imagem 4: Observação: Caso a emissão seja NFC-e (Fast Service) , esse deve estar atualizado para versão 4.28.0.16 ou superior.](https://ajuda.sankhya.com.br/hc/article_attachments/16086137262231) Observação:** Caso a emissão seja NFC-e**(Fast Service)**, esse deve estar atualizado para versão 4.28.0.16 ou superior.

![Imagem 5: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16086166350103) Acesse: Configurações » Avançado » Preferências

- Parâmetro **"DATINIULTNTNFE - Data Início da última nota técnica da NF-e":** 06/05/2019

![Imagem 6: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16086137266583) Acesse: Comercial » Preferências » Empresa

Aba: **"NF-e / NFC-e"**

- Campo "**Versão NT":** Última (Nota Técnica 2018.005)

**Tag no XML:**

<infRespTec>
          <CNPJ>26314062000161</CNPJ>
          <xContato>Fabio Tulio Felippe</xContato>
          <email>marketing@sankhya.com.br</email>
          <fone>3432390700</fone>
</infRespTec>

A rejeição causada pela não exigência do estado da tag será: **225 - Rejeição: Falha no Schema XML do lote de NFe.**

![Imagem 7: Após os ajustes necessários, gere novo lote da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16086166357655) Após os ajustes necessários,  gere novo lote da nota.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16086166360727) CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e o grupo de informações do responsável técnico **(infRespTec)** não for informado, haverá a rejeição.

![Imagem 9: Observação :](https://ajuda.sankhya.com.br/hc/article_attachments/16086137262231) **Observação**:

![Imagem 10: Nota Técnica (NT2018.005):](https://ajuda.sankhya.com.br/hc/article_attachments/16086166344855) **Nota Técnica**(NT2018.005):

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=j/im9zMlcIE=>
