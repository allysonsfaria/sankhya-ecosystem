---
id: "26489794129815"
titulo: "Configuração de Outros Impostos para EFD REINF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26489794129815-Configura%C3%A7%C3%A3o-de-Outros-Impostos-para-EFD-REINF"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:43:00Z"
rotulos: ["Configuração", "Fiscal", "Central de Vendas", "Impostos", "CONSIMPRETNOTA", "GERIMPOSTO", "Financeiro", "EFD Reinf", "Configurações para Geração dos Eventos do REINF Grupo 4000 - 2023", "Configuração de Outros Impostos para EFD REINF", "Código de Receita - DARF", "Eventos Periódicos", "RETIMPPARCNOTA"]
---

# Configuração de Outros Impostos para EFD REINF

Este artigo tem como objetivo explicar as formas disponíveis no sistema para o cálculo dos impostos retidos e como eles serão tratados, tanto na perspectiva do [EFD Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553) quanto na perspectiva do Financeiro.

Neste cenário, espera-se que todos os impostos (IRRF, CSLL, PIS e COFINS) sejam retidos sem que a base de cálculo dos impostos CSLL, PIS e COFINS, calculados no Financeiro, seja reduzida pelo valor do IRRF calculado na nota.

Para isso, é necessário que os impostos que têm data de fato gerador com base na nota, sejam calculados na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), e os demais impostos, que têm data de fato gerador com base no pagamento, sejam calculados no Financeiro. Desse modo, realize as seguintes configurações pertinentes ao EFD Reinf:

![Imagem 1: Na tela Código de Receita - DARF , cadastre o código da receita que será atribuído a geração dos impostos…](https://ajuda.sankhya.com.br/hc/article_attachments/26489957717015) Na tela [Código de Receita - DARF](https://ajuda.sankhya.com.br/hc/pt-br/articles/6217174835095), cadastre o código da receita que será atribuído a geração dos impostos Agregado/CSRF/PCC.

![Imagem 2: Na tela Código de Receita - DARF , cadastre o código da receita que será atribuído a geração dos impostos…](https://ajuda.sankhya.com.br/hc/article_attachments/26505170668823)

![Imagem 3: Em Preferências da Empresa , além de configurar a aba EFD - Reinf conforme a necessidade do Parceiro , informe as datas…](https://ajuda.sankhya.com.br/hc/article_attachments/26491646064919) Em [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), além de configurar a aba [EFD - Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaefdreinf) conforme a necessidade do Parceiro, informe as datas que servirão de parâmetro para a geração dos rendimentos e o **"Código de Receita para atribuir Agregado/CSRF/PCC"**.

![Imagem 4: Em Preferências da Empresa , além de configurar a aba EFD - Reinf conforme a necessidade do Parceiro , informe as datas…](https://ajuda.sankhya.com.br/hc/article_attachments/26505661483031)

Defina também quais os eventos serão gerados na sub-aba **"Eventos Periódicos"**.

![Imagem 5: Defina também quais os eventos serão gerados na sub-aba "Eventos Periódicos" .](https://ajuda.sankhya.com.br/hc/article_attachments/26505907918103)

![Imagem 6: Na tela Tipos de Operação - TOP , aba Impostos , ative as marcações pertinentes aos impostos que serão calculados com…](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), ative as marcações pertinentes aos impostos que serão calculados com base na nota: **"Tem FUNRURAL/INSS"**, **"Tem IRF"**, **"Tem ISS"** e **"Gerar informações do EFD Reinf Grupo 4000?"**.

![Imagem 7: Na tela Tipos de Operação - TOP , aba Impostos , ative as marcações pertinentes aos impostos que serão calculados com…](https://ajuda.sankhya.com.br/hc/article_attachments/26505745329175)

![Imagem 8: No Cadastro de Parceiros , deve-se configurar a seção Informações para REINF da aba Fiscal conforme a necessidade do…](https://ajuda.sankhya.com.br/hc/article_attachments/26491733029399) No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), deve-se configurar a seção [Informações para REINF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#REINF) da aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal) conforme a necessidade do Parceiro. Além disso, as marcações correspondentes aos impostos que serão calculados com base na nota devem ser habilitadas: **"Calcula FUNRURAL/INSS"**, **"Calcula IRF"** e **"Retém ISS"**.

![Imagem 9: No Cadastro de Parceiros , deve-se configurar a seção Informações para REINF da aba Fiscal conforme a necessidade do…](https://ajuda.sankhya.com.br/hc/article_attachments/26505828419991)

![Imagem 10: Na tela Cadastro de Serviço , aba Impostos , preencha os campos que são obrigatórios para que o documento seja gerado…](https://ajuda.sankhya.com.br/hc/article_attachments/26506737608599) Na tela [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), preencha os campos que são obrigatórios para que o documento seja gerado no EFD Reinf, sendo eles: **"Tem ISS"**, **"Tem IRF"**, **"% IRF"**, **"% Red. Base IRF"**, **"Tipo de Serviço"**, **"Classificação Cessão M.d.Obra"**, **"Tem INSS?"**, **"Perc. Red. Base Icms Efetivo"**, **"% INSS"** e **"% Red. Base INSS"**.

Informe o código de **"Tributação IRRF - Exterior IRRF"**, se for o caso.

![Imagem 11: Informe o código de "Tributação IRRF - Exterior IRRF" , se for o caso.](https://ajuda.sankhya.com.br/hc/article_attachments/26506962307223)

**Observação**: ao utilizar um item do tipo produto na nota, para que o sistema gere as informações corretamente é necessário vincular um **"Código Natureza Rendimento"** a esse cadastro.

![Imagem 12: Confira o link Configurações para geração dos eventos do REINF Grupo 4000 para mais detalhes.](https://ajuda.sankhya.com.br/hc/article_attachments/26506962309143) Confira o link [Configurações para geração dos eventos do REINF Grupo 4000](https://ajuda.sankhya.com.br/hc/pt-br/articles/11814510069271-Configura%C3%A7%C3%B5es-para-gera%C3%A7%C3%A3o-dos-eventos-do-REINF-Grupo-4000-2023) para mais detalhes.

Para que o cálculo dos impostos sejam realizados nos moldes descritos acima, é necessário configurar o IRRF de modo que a retenção seja realizada na Central de Vendas. Para isso, observe as seguintes configurações:

- A marcação **"Tem IRF"** deve estar habilitada na aba Impostos da tela Tipos de Operação - TOP;
- No Cadastro de Parceiros, aba Fiscal, a marcação **"Calcula IRF"** deve estar ativada;
- Na aba Impostos do Cadastro de Serviço, a marcação Tem IRF deve estar ligada e a alíquota a ser tributada deve estar indicada no campo %IRF.

Na perspectiva de outros impostos (PIS, COFINS e CSLL), deve-se configurar a tela [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834), conforme abaixo:

- No campo **"Base para Impostos do Financeiro"** selecione a opção **"Valor do Pagamento"**. Isso se deve ao fato de que, em casos de baixas parciais ou documentos parcelados, em cada lançamento financeiro o imposto será retido com base no valor do desdobramento do título;
- Nas abas [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaparceiro), [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abatop), [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaempresa) e [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaservio), deverão ser incluídas as regras de cálculo que indicarão que o imposto **"Na Nota"** será considerado como **"Já Incluso"** e no **"Financeiro de Origem Estoque"** será considerado como **"Subtrair"**;
- Insira o **"Cód. Receita"** nas abas que se fizerem necessárias.

**Observação**: considerando que se utilize parcelas de impostos em suas movimentações, é necessário criar as parcelas correspondentes a cada imposto na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173), indicando um parceiro diferente do parceiro da nota. Na tela Impostos, deve ser indicado que não haverá cálculo para os parceiros dos impostos.

![Imagem 13: Os parâmetros abaixo devem estar configurados conforme indicado para que a tratativa do imposto retido a título de IRF…](https://ajuda.sankhya.com.br/hc/article_attachments/26507823481879) Os parâmetros abaixo devem estar configurados conforme indicado para que a tratativa do imposto retido a título de IRF seja devidamente aplicada, de modo que o valor do financeiro e, consequentemente, a base de cálculo dos demais impostos não seja impactada:

- Reter impostos (ISS,INSS,IRF) p/ Parc. da nota? - RETIMPPARCNOTA = ligado;
- Gerar impostos (ISS,INSS,IRF) no financeiro? - GERIMPOSTO = desligado;
- Considerar impostos retidos no valor da nota? - CONSIMPRETNOTA = desligado.
