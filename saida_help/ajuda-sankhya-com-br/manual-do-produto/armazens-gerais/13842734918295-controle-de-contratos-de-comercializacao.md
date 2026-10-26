---
id: "13842734918295"
titulo: "Controle de Contratos de Comercialização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o"
trilha: "Manual do Produto > Suprimentos e Estoque > Armazéns Gerais"
atualizado_em: "2026-07-29T15:05:59Z"
rotulos: ["Configuração", "Relatórios", "WMS", "Contrato", "TOP", "Estoque", "Controle de Contratos de Comercialização", "ID: br.com.sankhya.armazem.cad.movEstoqDisComerc", "consolidação contratos comercialização"]
---

# Controle de Contratos de Comercialização

```
 ![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42313214836887) Módulo: Armazéns Gerais > Rotinas        ![Versão](https://ajuda.sankhya.com.br/hc/article_attachments/42313214838935) Versão disponível: a partir da 4.19
```

---

Nesta tela, confira a consolidação das movimentações realizadas nos contratos de comercialização. 

![essencial](https://ajuda.sankhya.com.br/hc/article_attachments/16027299639319) Para acessar essa rotina, libere o opcional **"30935 - Comercialização de Grãos/W"**.

| Funcionalidades da tela | |
| --- | --- |
| [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#PaineldeFiltros) | [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#PainelPrincipal) |
| [Aba Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#AbaLan%C3%A7amentos) | [Aba Dif. Físico x Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#AbaDif.F%C3%ADsicoxFiscal) |
| [Totalizadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#Totalizadores) |  |

### Painel de Filtros

Para localizar os contratos pode-se utilizar os seguintes filtros:

![Imagem 4: Para localizar os contratos pode-se utilizar os seguintes filtros:](https://ajuda.sankhya.com.br/hc/article_attachments/17883424298903)

Em **"Filtros rápidos"**, informe a **"Empresa"**, o **"Parceiro"**, a **"Safra"**, o **"Produto"** e o código do registro do **"Contrato"**.

Marque a **"Situação do Contrato"** dentre as opções **"Ativo"**, **"Cancelado"** ou **"Finalizado"**.

Por fim, conforme o cadastro do contrato assinale a **"Modalidade do Contrato"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#top)

### Painel Principal

Com os filtros configurados, clique em **"Aplicar"**, assim, no Painel Principal serão apresentados os seguintes dados:

| - Empresa; - Parceiro; - Endereço; - Inscrição Estadual; | - Safra; - Produto; - Situação Contrato; - Tipo do Contrato. |
| --- | --- |

#### Imagem 5: Tipo do Contrato.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#top)

### Aba Lançamentos

Nessa aba, serão registrados os lançamentos que correspondem à quantidade física entregue do contrato selecionado. No entanto, a exibição desses lançamentos irá observar configurações diferentes em relação ao [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) dos lançamentos, conforme o tipo do contrato:

**(1)** Se o contrato for de venda:

- Tipo de movimento: **"V-Venda"** ou **"D-Devolução"**;
- Movimento Armazém: **"Venda"**;
- Atualização de Estoque: **"Baixar (V-Venda)"** ou **"Entrar (D-Devolução de Venda)"**.

**(1)** Já se o contrato for de compra:

- Tipo de movimento: **"C-Compra"** ou **"E-Devolução de Compra"**;
- Movimento Armazém: **"Compra"**;
- Atualização de Estoque: **"Entrar (C-Compra)"** ou **"Baixar (E-Devolução de Compra)"**.

![Imagem 6: Atualização de Estoque: "Entrar (C-Compra)" ou "Baixar (E-Devolução de Compra)" .](https://ajuda.sankhya.com.br/hc/article_attachments/17883424311831)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#top)

### Aba Dif. Físico x Fiscal

Essa aba será apresentada quando a **"Modalidade do Contrato"** for igual à **"Compra"**. Nela, pode-se verificar as diferenças entre o físico e o fiscal em contratos de compras e, desta forma, gerar as devidas regularizações para que o estoque físico fique conforme o fiscal declarado.

Na parte superior da aba, pode-se acompanhar a situação do contrato por meio do campo **"Status"**. Nele, poderão ser apresentadas as seguintes classificações:

- **Pendência de Complemento Fiscal:** este status será apresentado se a Diferença Físico x Fiscal for maior que zero;
- **Pendência de Devolução Fiscal:** esta classificação será exibida se a Diferença Físico x Fiscal for menor que zero;
- **Sem diferença:** se a Diferença Físico x Fiscal for igual à zero.

![Imagem 7: Sem diferença: se a Diferença Físico x Fiscal for igual à zero.](https://ajuda.sankhya.com.br/hc/article_attachments/17883398088727)

Ao clicar no botão **"Gerar Nota"**, um pop-up será exibido para realizar a regularização fiscal. Preencha os campos necessários e clique em **"Confirmar"**. Em seguida, o **"N° Único"** da nota gerada será exibido. Se desejar visualizar a nota no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953), acione o botão **![Imagem 8: Ao clicar no botão "Gerar Nota" , um pop-up será exibido para realizar a regularização fiscal. Preencha os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/17883398100503) "Lançador"**.

![essencial](https://ajuda.sankhya.com.br/hc/article_attachments/16027299639319) O botão Gerar nota ficará inativo caso o Status seja igual à Sem diferença.

---

#### Colunas da aba Dif. Físico x Fiscal

Será apresentada na coluna **"Diferença"** a subtração entre a **"Qtd.Romaneio"** e a **"Qtd.Compra"**.

Na coluna **"Classificação"**, pode-se obter as seguintes classificações:

- **Fiscal a Maior:** se a Qtd.Romaneio for maior do que zero e menor do que a Qtd.Compra;
- **Físico a Maior:** quando a Qtd.Romaneio for maior do que zero e maior do que a Qtd.Compra;
- **Complemento Fiscal:** se a Qtd.Romaneio for nula, o **"N° Nota Compra"** maior do que zero, a **"Atualização Livro ICMS"** for igual à **"Livro de Entrada"** e a **"Atualização do Estoque"** igual à **"Nenhuma"**;
- **Devolução Fiscal:** conforme a Qtd. Romaneio for igual a zero, a N° Nota Compra menor do que zero, a Atualização Livro ICMS igual à **"Saídas"** e Atualização do Estoque igual à Nenhuma;
- **Romaneio sem NF Compra:** se a Qtd. Romaneio for maior do que zero e não houver nota de destino vinculada.

**Observação:** as configurações de **"Atualização Livro ICMS"** e **"Atualização do Estoque"** são efetuadas na tela [Tipo de Operação -TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), nas abas [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal) e [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque), respectivamente. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#top)

### Totalizadores

No Painel inferior, os totalizadores serão apresentados conforme a **"Modalidade de Contrato"**. Observe:

![Imagem 10: No Painel inferior , os totalizadores serão apresentados conforme a "Modalidade de Contrato" . Observe:](https://ajuda.sankhya.com.br/hc/article_attachments/17883398106263)

**(1)** Se a Modalidade do contrato for **"Venda"**, serão apresentados os totalizadores:

- **Quantidade Negociada:** exibe a quantidade negociada do contrato;
- **Quantidade Entregue:** apresenta o total dos documentos apresentados na coluna **"Quantidade"** da aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#AbaLan%C3%A7amentos);
- **Quantidade Pendente:** mostra a **"Quantidade Negociada"** menos a **"Quantidade Entregue"**;
- **Valor Total Negociado:** indica o valor total negociado do contrato;
- **Valor Total Entregue:** exibe o valor total das notas apresentadas na aba Lançamentos;
- **Valor Total Pendente:** apresenta o **"Valor Total Negociado"** menos **"Valor Total Entregue"**.

**(1)** Caso a Modalidade do Contrato seja **"Compra"**, além dos totalizadores apresentados anteriormente, serão exibidos os seguintes dados:

- **Quantidade Fiscal Entregue:** é apresentado o total da quantidade das notas do tipo **"C - Compra"**, que tenham o **"Movimento Armazém"** igual à **"Compra"** e **"Atualização de Livro Fiscal"** igual à **"Entrada"** menos o total da quantidade das notas do tipo **"D - Devolução de Compra"**, que tenham o Movimento Armazém igual à **"Compra"** e Atualização de Livro Fiscal igual à **"Saídas"**.
- **Diferença Físico x Fiscal:** mostra a **"Quantidade Entregue"** menos a **"Quantidade Fiscal Entregue"**.

![Imagem 11: Implementamos uma nova forma de configurar como os contratos de compra e venda de grãos atualizam seus saldos. Agora,…](https://ajuda.sankhya.com.br/hc/article_attachments/33541732902423) Implementamos uma nova forma de configurar como os contratos de compra e venda de grãos atualizam seus saldos. Agora, existe uma nova opção na **Tipo de Operação (TOP)** que permite definir se a movimentação deve "Entrar" (para compras) ou "Baixar" (para vendas) no saldo do contrato, mesmo que não haja atualização de estoque.

Essa melhoria garante que **todos os lançamentos**, incluindo aqueles que não mexem no estoque (como certas notas fiscais de compra), sejam **corretamente considerados no consumo do contrato**. Isso resolve as inconsistências entre os registros de estoque e os financeiros, oferecendo uma visão mais precisa dos seus contratos.

**O que você precisa saber após essa melhoria:**

Para aproveitar essa funcionalidade, o administrador do sistema precisa ativar um novo parâmetro chamado **"Atualização gerencial em contratos comerc. grãos"**. Uma vez ativado, o campo **"Atualização do Saldo dos Contratos"** será exibido nas configurações da **Tipo de Operação (TOP)**, na aba **Armazéns**, para os seguintes tipos de movimento:

- **C (Compras)**
- **E (Devolução de Compras)**
- **V (Vendas)**
- **D (Devolução de Vendas)**

Ao configurar sua TOP, você poderá escolher entre as opções: **Entrar (E)**, **Baixar (B)** ou **Não Atualizar (NULL)**.

- **Para Contratos de Compra:**
  - Movimentos de **Compra (C)** devem ter a TOP configurada para **"Entrar"** no saldo.
  - Movimentos de **Devolução de Compra (E)** devem ter a TOP configurada para **"Baixar"** do saldo.
- **Para Contratos de Venda:**
  - Movimentos de **Venda (V)** devem ter a TOP configurada para **"Baixar"** do saldo.
  - Movimentos de **Devolução de Venda (D)** devem ter a TOP configurada para **"Entrar"** no saldo.

Essa configuração garantirá que os relatórios na aba **"Lançamentos"** do **Controle de Contratos de Comercialização** e na aba **"Dif. Físico x Fiscal"** apresentem dados mais precisos e integrados, refletindo todas as movimentações contratuais. Os totalizadores e as validações de tolerância excedente também considerarão essa nova configuração.

**Antes vs Depois**

| Situação | Antes da Melhoria | Depois da Melhoria |
| --- | --- | --- |
| **Visão do Contrato** | Lançamentos de pesagem (que atualizam estoque) e notas fiscais (que atualizam custos) eram vistos separadamente, causando divergências no saldo do contrato e relatórios. | O saldo do contrato é atualizado de forma integrada, considerando todos os lançamentos que afiram o contrato (pesagem e nota fiscal), mesmo que não atualizem estoque, eliminando divergências. |
| **Relatórios de Estoque e Custos (Kardex)** | O Kardex apresentava inconsistências, pois movimentos que atualizavam estoque não influenciavam os custos, e vice-versa, comprometendo a confiabilidade das análises. | O Kardex e os relatórios de custo agora refletem todas as movimentações contratuais de forma integrada, proporcionando análises mais confiáveis e uma visibilidade completa da operação. |
| **Regularização Fiscal** | A busca por Tipos de Operação (TOPs) para regularizações fiscais (Devolução ou Complemento) poderia não considerar cenários onde o estoque não era atualizado. | A busca por TOPs para regularizações fiscais foi aprimorada para incluir opções que consideram a nova configuração de atualização do saldo do contrato, facilitando os ajustes necessários. |

**Alterações Técnicas**

- **Parâmetros novos ou alterados**:
  - `ATUGERCONTGRAO`: Novo parâmetro que, ao ser **Ligado**, exibe o campo `Atualização do Saldo dos Contratos (ATUSALDOCONT)` na TOP para Tipos de Movimento C, E, V, D.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13842734918295-Controle-de-Contratos-de-Comercializa%C3%A7%C3%A3o#top)
