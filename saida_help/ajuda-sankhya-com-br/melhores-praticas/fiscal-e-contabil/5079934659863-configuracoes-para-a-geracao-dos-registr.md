---
id: "5079934659863"
titulo: "Configurações para a geração dos Registros F500 e F525 no arquivo EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5079934659863-Configura%C3%A7%C3%B5es-para-a-gera%C3%A7%C3%A3o-dos-Registros-F500-e-F525-no-arquivo-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:18:14Z"
rotulos: ["Configuração", "Impostos", "Financeiro", "EFD Contribuições", "Detalhes nos registros: F525 1900", "Configure EFD Contribuições: F500 F525 F510", "Escolha Regime de Caixa: F500", "Lucro Presumido", "Regime de Caixa"]
---

# Configurações para a geração dos Registros F500 e F525 no arquivo EFD Contribuições

#### Neste artigo serão apresentadas as configurações para a geração dos registros:

**(1)** **F500 -** Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa

**(1)** **F525 -** Composição da Receita Escriturada no Período – Detalhamento da Receita Recebida pelo Regime de Caixa

![Imagem 1: Acesse a tela: Comercial » Preferências » Empresa, aba "EFD - Escrituração Fiscal Digital" e configure a geração dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16347619712535) Acesse a tela: Comercial » Preferências » Empresa, aba **"EFD - Escrituração Fiscal Digital"** e configure a geração dos registros F500, F510, F525 e 1900:

![Imagem 2: Acesse a tela: Comercial » Preferências » Empresa, aba "EFD - Escrituração Fiscal Digital" e configure a geração dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16347604141079)

![Imagem 3: Na tela: Comercial » Preferências » Empresa, acesse a aba "Regime de Apuração da Contrib. Social e Aprop. Crédito" e…](https://ajuda.sankhya.com.br/hc/article_attachments/16347619716887) Na tela: Comercial » Preferências » Empresa, acesse a aba **"Regime de Apuração da Contrib. Social e Aprop. Crédito"** e configure o campo **"Lucro Presumido/Critério Apuração"** como **"Regime de Caixa - Escrituração consolidada (Registro F500)"**:

![Imagem 4: Na tela: Comercial » Preferências » Empresa, acesse a aba "Regime de Apuração da Contrib. Social e Aprop. Crédito" e…](https://ajuda.sankhya.com.br/hc/article_attachments/5078937347479)

![Imagem 5: Acesse a tela: Configurações » Cadastros » Gerencial » Natureza de Receitas e Despesas e configure o campo " Regime…](https://ajuda.sankhya.com.br/hc/article_attachments/16347604145047) Acesse a tela: Configurações » Cadastros » Gerencial » Natureza de Receitas e Despesas e configure o campo **"Regime (EFD PIS/COFINS)"**:

![Imagem 6: Acesse a tela: Configurações » Cadastros » Gerencial » Natureza de Receitas e Despesas e configure o campo " Regime…](https://ajuda.sankhya.com.br/hc/article_attachments/5079357295639)

Ao gerar o arquivo EFD Contribuições, o sistema irá gerar o registro F500 referente a todos os financeiros de receitas baixadas no período do arquivo (Regime de Caixa), cujas naturezas estejam com a configuração do campo **'Regime (EFD PIS/COFINS)':** Regime de Caixa. 

Para os documentos gerados no financeiro de Origem estoque, o sistema buscará as informações da tabela de impostos TGFDIN. Para esses documentos o sistema realiza o cálculo utilizando um índice sobre o valor do desdobramento para chegar na base de calculo de PIS e COFINS.

**Índice exemplo:**

Vlr. produto: 50 + Vlr. frete: 50 = Vlr. total da nota: 100;

Vlr. produto 50 / Vlr. da nota: 100 = Índice: 0,5;

Vlr total da nota 100 \* Índice 0,5 = Valor da base considerada no F500 = 50.

O sistema irá processar o registro F500 apresentando as receitas recebidas no período, segmentando as informações por Código de Situação Tributária - CST, do PIS/Pasep e da Cofins e suas alíquotas.

Os dados gerados no F500 serão apresentados de forma detalhada Registro F525 e 1900.

**Importante:** O campo "Valor de desconto/Exclusões" no PVA não será alimentado.

![Imagem 7: Importante: O campo "Valor de desconto/Exclusões" no PVA não será alimentado.](https://ajuda.sankhya.com.br/hc/article_attachments/17025023834007)

De fato hoje o sistema **ainda** não está preparado para realizar esses devidos cálculos para alimentar o campo "Valor de desconto/Exclusões" no PVA. 

**Observação:** Na versão 4.11, para a geração do campo **"04-Indicador da composição da receita recebida no período"** do **"Registro F525"**, foi implementado no cadastro do **"Tipo de Título"** (Tela: 'Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título'), o campo **"Indicador de Receita (registro F525 - EFD Cont.)",**

![Imagem 8: Observação: Na versão 4.11, para a geração do campo " 04-Indicador da composição da receita recebida no período" do "…](https://ajuda.sankhya.com.br/hc/article_attachments/16347666801815)

Caso o indicador selecionado for 99-Outros, o sistema irá habilitar o campo **"Informações complem. (registro F525 - EFD Cont.)"**, no qual os dados informados serão gerados do campo 10-INFO\_COMPL.
