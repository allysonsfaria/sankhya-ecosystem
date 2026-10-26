---
id: "39936682257687"
titulo: "Manual de Uso: Configuração e Lançamento de Acréscimo de Produto na Importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39936682257687-Manual-de-Uso-Configura%C3%A7%C3%A3o-e-Lan%C3%A7amento-de-Acr%C3%A9scimo-de-Produto-na-Importa%C3%A7%C3%A3o"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T13:27:58Z"
rotulos: ["Produtos", "Configuração", "Importação", "Impostos", "Financeiro", "Regra no Incoterm", "Rateio nos Itens", "Validação Cruzada", "Vlr. Produto Embarque", "Total produtos", "Lançamento de Acréscimo de Produto na Importação", "Produto na Importação", "Despesa no Portal de Importação", "Vlr em Moeda"]
---

# Manual de Uso: Configuração e Lançamento de Acréscimo de Produto na Importação

Este manual descreve o procedimento técnico para configuração e registro da despesa de acréscimo de produto dentro do módulo de importação do ERP.

O objetivo fundamental é assegurar que valores adicionais (surcharges) sejam integrados com precisão ao custo e ao valor total das mercadorias durante o processo de nacionalização, refletindo o custo real de aquisição.

#### Configuração da Regra no Incoterm

A parametrização correta no cadastro de Incoterms é o que governa o comportamento do rateio sistêmico.

Siga as instruções abaixo para configurar o gatilho de soma: 

**(1)** Acesse a tela **''Incoterms''** (ImpEx » Cadastros » Incoterms) e selecione o Incoterm desejado (ex: **EXW - EX WORKS**).

**(2)** Localize a aba **''Naturezas''** e certifique-se de estar na sub-aba **''Geral''**.

**(3)** Insira ou edite a natureza rigorosamente as seguintes definições:

- **Sinal**: Deve estar definido como **''Soma''**.
- **Liga com a Nota de Nacionalização**: Selecione obrigatoriamente a opção **''Vlr. Produto''**. (Esta configuração é o que vincula o acréscimo ao valor unitário do item).
- **Receita/Despesa**: Selecione **''Despesa''**.
- **Grupo de Natureza**: Defina como **''Acréscimo de Produto''**.

![Imagem 1: Grupo de Natureza : Defina como ''Acréscimo de Produto'' .](https://ajuda.sankhya.com.br/hc/article_attachments/39938698352279)

#### Lançamento da Despesa no Portal de Importação

Com o Incoterm devidamente parametrizado, o próximo passo é o lançamento da despesa no processo vigente para disparar o cálculo de rateio.

**(1)** Acesse a tela **''Portal de Importação''** (ImpEx » Rotinas » Portal de Importação) e selecione o processo de importação específico.

**(2)** Navegue até a aba **''Despesas''**.

**(3)** Caso esteja configurado como opcional, a despesa deverá ser lançada manualmente, utilizando o Cód. Natureza definido no Incoterm.

**(4)** No campo **“Vlr em Moeda”**, informe o valor total do acréscimo do processo.

![Imagem 2: (4) No campo “Vlr em Moeda” , informe o valor total do acréscimo do processo.](https://ajuda.sankhya.com.br/hc/article_attachments/39938698363799)

#### Conferência do Rateio nos Itens

Após lançar a despesa, é necessário conferir se o valor foi distribuído corretamente entre os itens, conforme as regras do sistema.

**(1)** Acesse a tela ''Portal de Importação'' (ImpEx » Rotinas » Portal de Importação), na aba **''Itens''**.

**(2)** Analise a grade de itens, observando a relação entre as colunas conforme a tabela de lógica abaixo:

| Coluna | Descrição do Comportamento |
| --- | --- |
| Vlr. Acréscimo | Exibe a parcela do acréscimo (valor rateado) destinada especificamente àquele item. |
| Vlr. Total Produto | Representa o valor base/original do item antes da incidência de acréscimos. |
| Vlr. Produto Embarque | Resultado final da operação (Vlr. Total + Vlr. Acréscimo Produto). Este é o valor que será levado para a Nota de Nacionalização. |

**(3)** Certifique-se de que a soma da coluna **“Vlr. Produto Embarque”** corresponde ao valor total da mercadoria mais o acréscimo lançado no passo anterior.

![Imagem 3: (3) Certifique-se de que a soma da coluna “Vlr. Produto Embarque” corresponde ao valor total da mercadoria mais o…](https://ajuda.sankhya.com.br/hc/article_attachments/39938717560983)

#### Validação na Central de Compras

##### A etapa final é conferir a Nota de Nacionalização gerada, garantindo que os dados estejam corretos.

**(1)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e localize o documento de nacionalização gerado.

**(2)** Realize a validação em dois pontos críticos:

- Na grade **''Cabeçalho''** no campo **''Observação''**: Verifique se os dados de impostos (PIS, COFINS, II, etc.) e as referências de **DI** e **Invoice** foram transportados corretamente.
- Na grade **''Itens''**: O campo **''Total produtos''** deve refletir exatamente o valor acumulado calculado na tela ''Portal de Importação''.

**Validação Cruzada**: O campo “Total produtos” exibido na ''Central de Compras'' deve ser igual à soma da coluna “Vlr. Produto Embarque”, conferida na aba “Itens” da tela ''Portal de Importação''.

![Imagem 4: Validação Cruzada : O campo “Total produtos” exibido na ''Central de Compras'' deve ser igual à soma da coluna “Vlr.…](https://ajuda.sankhya.com.br/hc/article_attachments/39938698366871)
