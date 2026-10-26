---
id: "28557713063447"
titulo: "Manual de Importação de XML da Pré-nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28557713063447-Manual-de-Importa%C3%A7%C3%A3o-de-XML-da-Pr%C3%A9-nota"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:37:48Z"
rotulos: ["Fiscal", "NF-e", "br.com.sankhya.core.cad.produtos", "XML", "Importação", "Manual de Importação de XML da Pré-nota", "Importar Pre-Nota", "br.com.sankhya.CabecalhoImportacao", "Documentos Eletrônicos", "Comércio Exterior"]
---

# Manual de Importação de XML da Pré-nota

### 1. Importação de D.I no Layout de Nota fiscal Eletrônica

Comércio Exterior > Rotinas

Na tela de **“Portal de Importação”** foi criada a opção **“Importar Pre-Nota”**, na qual é possível importar alguns dados a partir do XML da Pre-Nota (que e o Layout de XML de Nota Fiscal Eletrônica (NF-e)), conforme o [Manual de Integração - Contribuinte](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=d/NN9SSgick=).

Ao clicar no Botão **“Importar Pre-Nota”** será aberto um pop-up em que o usuário deverá clicar em **“Escolher Arquivos”.** Então, selecione o XML salvo no diretório escolhido e clique em **"Enviar"**.

![Imagem 1: Ao clicar no Botão “Importar Pre-Nota” será aberto um pop-up em que o usuário deverá clicar em “Escolher Arquivos”.…](https://ajuda.sankhya.com.br/hc/article_attachments/28557713052951)

Seguem os dados que são possíveis importar através do XML da Pre-nota:

(1)**Aba Geral:**

- Número da DIRegistro da DI
- Data Desembaraço
- Local Desembaraço

(1)** Aba Itens:**

- Nro. AdiçãoVlr.Frete
- Vlr.Seguro
- Vlr.AFRMM
- Base II
- Aliq.IIVlr.II
- Base Pis
- Aliq.PIS
- Vlr.PIS
- Base Cofins
- Aliq.Cofins
- Vlr.Cofins
- Base IPI
- Aliq.IPI
- Vlr.IPI
- Base ICMS
- Aliq.ICMS
- Vlr.ICMS

**![Imagem 2: Atenção:](https://ajuda.sankhya.com.br/hc/article_attachments/28557713054999) Atenção:**

**(2)** Ao empregar a importação do XML da Pré-nota é importante observar que o sistema não realiza o cálculo automático dos impostos e não assegura a precisão dos rateios. Isso ocorre porque o sistema adota os valores presentes no XML, desconsiderando, portanto, as configurações de rateio associadas aos Incoterms;

**(2)**Os campos de Peso Bruto e Peso Líquido não são automaticamente atualizados, uma vez que os valores correspondentes não estão identificados por itens no XML da Pré-nota. Portanto, ao optar por esta funcionalidade, é essencial inserir manualmente os valores durante o lançamento da nota, na aba **"Transporte"**, caso estes diferem do cálculo automático realizado pelo sistema;

**(2)**Os valores que não possuem TAGS próprias no Layout de XML da Pré-nota, são lançados na TAG <vOutro>, sendo assim o sistema não consegue identificar;

**(2)** O Modelo utilizado para realizar a importação tem que ser conforme o Layout XML de Nota fiscal Eletrônica 4.0;

**(2)** O XML deve estar em formato UTF-8;

**(2)**Para o sistema fazer a integração com dos itens, o mesmo utiliza o campo **“Referência Produto XML”**. Nesses campos informe o código que o produto vem na tag </cProd>.

![Imagem 3: (2) Para o sistema fazer a integração com dos itens, o mesmo utiliza o campo “Referência Produto XML” . Nesses campos…](https://ajuda.sankhya.com.br/hc/article_attachments/28557713059863)

### 2. Ratear Valores Destaque

Comércio Exterior > Rotinas

Na tela **"Portal de Importação"**, no botão **“Outras Opções”,** foi criada a rotina **“Ratear Valores Destaque”**, para que o usuário que usa a rotina **“Importação DI”** consiga identificar os valores importados no campo **“Vlr.Destaque”**.
Conforme supracitado, o sistema não consegue identificar os valores da TAG <vOutro>, ao importar o XML da Pré-nota. Então, acesse o botão Outras opções e clique na opção **“Ratear Valores Destaque”**.

![Imagem 4: Na tela "Portal de Importação" , no botão “Outras Opções”, foi criada a rotina “Ratear Valores Destaque” , para que o…](https://ajuda.sankhya.com.br/hc/article_attachments/28558000065815)

Após clicar na opção acima, o sistema irá abrir um pop-up com todas as despesas cadastradas no Incoterms, vinculado ao processo de importação.
Identifique os valores de cada despesa de importação, somada no campo Vlr.Destaque. Após identificar o valor total, clique em OK.
O sistema preencherá os valores na aba **“Despesas de Importação”** e criará as informações conforme a configuração de cada despesa no cadastro do Incoterms.

![Imagem 5: Após clicar na opção acima, o sistema irá abrir um pop-up com todas as despesas cadastradas no Incoterms, vinculado ao…](https://ajuda.sankhya.com.br/hc/article_attachments/28558000073623)
