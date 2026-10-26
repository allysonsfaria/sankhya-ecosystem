---
id: "360043006773"
titulo: "Informada modalidade de determinação da BC da ST como MVA e informado o campo pMVAST [nItem: nnn] "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043006773-Informada-modalidade-de-determina%C3%A7%C3%A3o-da-BC-da-ST-como-MVA-e-informado-o-campo-pMVAST-nItem-nnn"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:13Z"
rotulos: ["ERRONF", "#Naves", "Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "933", "[933- Rejeição]", "NT última Data 01/09/2021", "Remova MVA se modalidade não for 4"]
---

# Informada modalidade de determinação da BC da ST como MVA e informado o campo pMVAST [nItem: nnn] 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16456698494871) MENSAGEM:**

[933- Rejeição]: Informada modalidade de determinação da BC da ST diferente de MVA e informado o campo pMVAST [nItem: nnn]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16456684017175) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Sistema atualizado para versões abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16456684022935) Sistema atualizado para versões abaixo:

- 3.32b37 ou superior
- 3.31b206 ou superior
- 3.30b351 ou superior

![Imagem 4: Para mais informações sobre como realizar o processo de atualização verifique os artigos:](https://ajuda.sankhya.com.br/hc/article_attachments/16456684025751) Para mais informações sobre como realizar o processo de atualização verifique os artigos:

[Atualização do sistema SankhyaOM via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596634)

[Atualização do sistema JIVAEVO via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043012853)

![Imagem 5: Acesse a tela " Empresa " (Caminho de acesso: Comercial » Preferências ), vá até a aba " NF-e/NFC-e" e defina o campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/16456684027415) Acesse a tela "**[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)"** (Caminho de acesso: Comercial » Preferências), vá até a aba "**NF-e/NFC-e"** e defina o campo "**Versão NT" = Última (Nota Técnica 2021.004):**

![Imagem 6: Acesse a tela " Empresa " (Caminho de acesso: Comercial » Preferências ), vá até a aba " NF-e/NFC-e" e defina o campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/14445115763351)

![Imagem 7: Acesse a tela " Preferências" (Caminho de acesso: Configurações » Avançado ):](https://ajuda.sankhya.com.br/hc/article_attachments/16456684031383) Acesse a tela "**Preferências"** (Caminho de acesso: Configurações » Avançado):

- Parâmetro **"DATINIULTNTNFE"** - Data Início da última nota técnica da NF-e = **[01/09/2021**]

![Imagem 8: Parâmetro "DATINIULTNTNFE" - Data Início da última nota técnica da NF-e = (01/09/2021 )](https://ajuda.sankhya.com.br/hc/article_attachments/11989595199895)

![Imagem 9: Acesse a tela " Alíquotas de ICMS ": (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de…](https://ajuda.sankhya.com.br/hc/article_attachments/16456698514455) Acesse  a tela "[**Alíquotas de ICMS**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)": (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS) e observe:

**(2)** O campo "**Margem Lucro (MVA)"** não deverá ter valor quando  o campo "**Modalidade BC ICMS ST"** for diferente de "**Margem Valor Agregado (%)"**.

![Imagem 10: Após os ajustes, gere o Lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16456684047383) Após os ajustes, gere o Lote novamente.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16456684025751) CAUSA:**

Quando emitida uma nota, cuja 'Modalidade BC ICMS ST', tag <modBCST> esteja preenchida com valor diferente de 'Margem Valor Agregado (%)' e a tag <pMVAST> for gerada.

Modalidade de determinação da BC do ICMS ST, tag <modBCST>:

0 = Preço tabelado ou máximo sugerido; 
1 = Lista Negativa (valor); 
2 = Lista Positiva (valor); 
3 = Lista Neutra (valor); 
4 = Margem Valor Agregado (%);
5 = Pauta (valor);

**![Imagem 12: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16456684052119) OBSERVAÇÕES:**

![Imagem 13: Regra de Validação opcional a critério da UF.](https://ajuda.sankhya.com.br/hc/article_attachments/16456684022935) Regra de Validação opcional a critério da UF.

![Imagem 14: ( NT 2021.004) ) - Nota Técnica:](https://ajuda.sankhya.com.br/hc/article_attachments/16456684027415) (**NT2021.004)**) - Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=>
