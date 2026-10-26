---
id: "360042563934"
titulo: "Informada modalidade de determinação da BC da ST como MVA e não informado o campo pMVAST [nItem: nnn]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042563934-Informada-modalidade-de-determina%C3%A7%C3%A3o-da-BC-da-ST-como-MVA-e-n%C3%A3o-informado-o-campo-pMVAST-nItem-nnn"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:43Z"
rotulos: ["ERRONF", "#Naves", "Configuração", "NF-e", "XML", "Atualização", "SEFAZ", "Impostos", "932", "NT última; Data: 01/09/2021", "Informe \"Margem Lucro\" se MVA", "[932 - Rejeição]", "MVA"]
---

# Informada modalidade de determinação da BC da ST como MVA e não informado o campo pMVAST [nItem: nnn]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16459781601175) MENSAGEM:**

[932 - Rejeição]: Informada modalidade de determinação da BC da ST como MVA e não informado o campo pMVAST [nItem: nnn]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16459781610647) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Sistema atualizado para versões abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16459781616023) Sistema atualizado para versões abaixo:

- 3.32b37 ou superior
- 3.31b206 ou superior
- 3.30b351 ou superior

Para mais informações sobre como realizar o processo de atualização verifique os artigos: 
[Atualização do sistema SankhyaOM via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596634)

[Atualização do sistema JIVAEVO via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043012853)

Caso utilize nossos produtos **Mitra** e **MGE Comercial,** atualize também o release para a última versão disponível no Place: **4.30.0.4** . Atualize também o SanNFe para a versão mais recente (**SanNFe 2.42b5 ou superior**), disponível em nossa área de Downloads.

![Imagem 4: Acesse a tela " Empresa " (Caminho de acesso: Comercial » Preferências ), na aba " NF-e/NFC-e" e preencha o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16459781620759) Acesse a tela "**[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)"** (Caminho de acesso: Comercial » Preferências), na aba "**NF-e/NFC-e"** e preencha o campo **"Versão NT"** com a opção**Última (Nota Técnica 2021.004):**

![Imagem 5: Acesse a tela " Empresa " (Caminho de acesso: Comercial » Preferências ), na aba " NF-e/NFC-e" e preencha o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/14473951479319)

![Imagem 6: Acesse a tela " Preferências " (Caminho de acesso: Configurações » Avançado ):](https://ajuda.sankhya.com.br/hc/article_attachments/16459781624727) Acesse a tela "**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Caminho de acesso: Configurações » Avançado):

- Busque o parâmetro **"DATINIULTNTNFE"** - Data Início da última nota técnica da NF-e' e preencha com **01/09/2021**

![Imagem 7: Busque o parâmetro "DATINIULTNTNFE" - Data Início da última nota técnica da NF-e' e preencha com 01/09/2021](https://ajuda.sankhya.com.br/hc/article_attachments/11989861550615)

Se  o campo "**Modalidade BC ICMS ST"** for igual a "**Margem Valor Agregado (%)"**, informe o campo "**Margem Lucro (MVA)"**

![Imagem 8: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16459812514071) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

![Imagem 9: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/14474066406551)

![Imagem 10: Dessa forma, no XML será gerado:](https://ajuda.sankhya.com.br/hc/article_attachments/16459812516503) Dessa forma, no XML será gerado:

![Imagem 11: Dessa forma, no XML será gerado:](https://ajuda.sankhya.com.br/hc/article_attachments/14474091144471)

![Imagem 12: Após os ajustes, gere o Lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16459812525719) Após os ajustes, gere o Lote novamente.

**![Imagem 13: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16459812528919) CAUSA:**

Quando emitida uma nota, cuja 'Modalidade BC ICMS ST', tag <modBCST> , esteja preenchida com o valor 'Margem Valor Agregado (%)' e o campo 'Margem Lucro (MVA)', tag <pMVAST>,  não for gerada.

Modalidade de determinação da BC do ICMS ST, tag <modBCST>:

0 = Preço tabelado ou máximo sugerido;
1 = Lista Negativa (valor);
2 = Lista Positiva (valor);
3 = Lista Neutra (valor);
4 = Margem Valor Agregado (%);
5 = Pauta (valor);

**![Imagem 14: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16459812536727) OBSERVAÇÃO:**

**(1)** Regra de Validação opcional a critério da UF.

**(1)** ([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota Técnica.
