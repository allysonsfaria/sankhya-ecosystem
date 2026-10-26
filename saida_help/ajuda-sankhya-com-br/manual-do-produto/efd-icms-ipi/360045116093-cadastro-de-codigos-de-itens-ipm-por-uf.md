---
id: "360045116093"
titulo: "Cadastro de Códigos de itens (IPM) por UF no registro 1400"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD ICMS/IPI"
atualizado_em: "2026-09-30T11:14:44Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Fiscal", "ICMS", "TOP", "EFD", "Códigos de itens (IPM) por UF no registro 1400", "Índice de Participação dos Municípios", "br.com.sankhya.mgeliv.codigoitemipmregistro1400", "Códigos de itens (IPM) por UF no registro 1400 manual", "Configurar Código UF e Item", "Preencher abas e parâmetros conforme guia", "Gerar Registro 1400 EFD ICMS/IPI"]
---

# Cadastro de Códigos de itens (IPM) por UF no registro 1400

**Módulo:** Livros Fiscais › Avançado

**Caminho de acesso:** Menu Principal › Livros Fiscais › Avançado › Escrituração Fiscal Digital › Códigos de itens (IPM) por UF no registro 1400

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#oque)
- [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#comousar)
- [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#geral)
- [Abas Grupo de Produto, Produto e Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#particularizacao)
- [Aba Fórmula IPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#formula)
- [Importação de tabela SPED](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#importacao)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#atencao)

## O que é e para que serve

Diversas empresas têm a obrigatoriedade de gerar, no EFD ICMS/IPI, o registro `1400` - Informações sobre valores agregados. Segundo o [Guia Prático EFD - ICMS/IPI - Versão 2.0.20](http://sped.rfb.gov.br/arquivo/show/1986), no campo `COD_ITEM_IPM` (Campo 2 - Código do item), cada Unidade Federativa pode criar a sua própria tabela, listando quais códigos e operações devem ser apresentados no registro. IPM é a sigla de **Índice de Participação dos Municípios**.

No **Cadastro de Códigos de itens (IPM) por UF no registro 1400**, você configura esses códigos por UF, para que o registro `1400` do EFD ICMS/IPI seja gerado conforme as especificações de código do item e de operações definidas por cada estado. A geração do arquivo em si é feita na tela [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI).

![Tela Códigos de itens (IPM) por UF no registro 1400 com a grade de códigos cadastrados e as abas de configuração](https://ajuda.sankhya.com.br/hc/article_attachments/8493966390551)

Tela Códigos de itens (IPM) por UF no registro 1400. Captura: 03/2023

---

## Como usar a tela

O cadastro pode ser feito de duas maneiras: por **inserção manual** ou pelo botão de importação ![Ícone do botão Importar Tabela](https://ajuda.sankhya.com.br/guide-media/01H3HF95F4QQ1GPWYH0JDKZX45), no alto da tela. Na inclusão manual, preencha inicial e obrigatoriamente o **Código UF** (o estado a que os códigos de itens pertencem) e o **Código Item** (o código de item para IPM).

Ao atribuir o código, o sistema verifica os cadastros nesta ordem de prioridade: **Geral › Tipos de Operação › Grupo de Produto › Produto › Fórmula IPM**.

**ℹ️ Nota**

Para que o **Código do Item** seja impresso no registro `1400`, é necessário realizar os cadastros das abas **Grupo de Produto**, **Produto** e **Tipos de Operação**.

![Inclusão manual de um código, com os campos obrigatórios Código UF e Código Item](https://ajuda.sankhya.com.br/hc/article_attachments/8493975682455)

Campos Código UF e Código Item. Captura: 03/2023

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#sumario)

---

## Aba Geral

- **Descrição do Código de Item para IPM** — a descrição do código.
- **Data Inicial de vigência** — obrigatória; início do período de vigência do código.
- **Data Final de vigência** — opcional; quando informada, o código não é mais exibido no arquivo após essa data, pois indica o encerramento da vigência.

![Aba Geral com os campos Descrição do Código de Item para IPM, Data Inicial e Data Final de vigência](https://ajuda.sankhya.com.br/hc/article_attachments/8493976905111)

Aba Geral. Captura: 03/2023

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#sumario)

---

## Abas Grupo de Produto, Produto e Tipos de Operação

As três abas têm o mesmo propósito: particularizar o uso do código de item, restringindo-o respectivamente por [Grupo de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os), [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos) ou [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP). É por meio desses cadastros que o código do item passa a ser impresso no registro `1400`: o valor do campo **Código Item** é enviado ao Campo 2 - `COD_ITEM_IPM` e vinculado às notas no momento da geração do registro.

![Abas Grupo de Produto, Produto e Tipos de Operação para restringir o uso do código de item](https://ajuda.sankhya.com.br/hc/article_attachments/8494031053719)

Abas de particularização do código. Captura: 03/2023

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#sumario)

---

## Aba Fórmula IPM

Disponível a partir da versão 4.33 do sistema, esta aba permite criar fórmulas para preencher o registro `1400` da [EFD Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI), em conformidade com a legislação estadual.

- ![Ícone do botão Construtor](https://ajuda.sankhya.com.br/hc/article_attachments/24099504734231) **Construtor** — botão que permite criar as fórmulas, vinculadas às tabelas `TGFCAB`, `TGFITE`, `TGFDIN` e `TGFLIV`.
- **Tipo de Movimento (TOP)** — os Tipos de Operação identificam o Tipo de Movimento: Compra, Venda, Devoluções e Transferências.
- **Restrição obrigatória** — deve haver restrição por Grupo de Produto e/ou Produto. Se houver restrição por Grupo de Produto, o código IPM é gerado apenas para os produtos desse grupo e, nesse caso, a aba **Produto** não precisa estar preenchida.

Após inserir a referência de lançamentos na tela EFD Fiscal ICMS/IPI e clicar em ![Ícone do botão Processar](https://ajuda.sankhya.com.br/hc/article_attachments/24257053230615) **Processar** e depois em ![Ícone do botão Gerar](https://ajuda.sankhya.com.br/hc/article_attachments/24257053236503) **Gerar**, o arquivo TXT do registro `1400` passa a incluir o código criado.

**⚠️ Atenção**

Quando a Fórmula IPM é preenchida, o sistema desconsidera cinco parâmetros na geração do registro 1400: `CFOPNAODED1400`, `IBGEPARC1400`, `UFSVENREG1400`, `UFSNAODED1400` e `UFSCTEOUTUF1400`.

![Aba Fórmula IPM com o campo Fórmula e o botão Construtor](https://ajuda.sankhya.com.br/hc/article_attachments/24256959399447)

Aba Fórmula IPM. Captura: 06/2024

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#sumario)

---

## Importação de tabela SPED

Pelo botão **Importar Tabela**, no alto da tela, é possível carregar arquivos do [SPED - Sistema Público de Escrituração Digital](http://sped.rfb.gov.br/) (seção [Sped Tabelas](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)) em formato `.txt` com os códigos e operações por estado. O fluxo é:

1. Ao acionar o botão, abre-se o pop-up **Informe os parâmetros**, que permite informar uma sigla de UF válida caso o arquivo não a possua.
2. Em seguida, um novo pop-up permite buscar e escolher o documento `.txt`.

Cada linha do arquivo tem os campos separados por barra vertical, por exemplo:

```
SPDIPAM11|Compras escrituradas de mercadorias de produtores agropecuários paulistas por município de origem.|01012015|
```

**ℹ️ Nota**

Ao importar um arquivo, os registros podem já existir. A opção **Manter Registros na Importação**, disponível no botão **Configuração da Tela** (canto superior direito), permite preservar ou modificar os registros existentes, evitando duplicidades.

![Pop-up Informe os parâmetros, para informar a sigla da UF na importação do arquivo](https://ajuda.sankhya.com.br/hc/article_attachments/8494232263319)

Pop-up Informe os parâmetros. Captura: 03/2023

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#sumario)

---

## Pontos de atenção

- Para a geração normal do registro `1400`, os parâmetros `CFOPNAODED1400` (CFOPs que geram Não Dedutíveis no registro 1400) e `UFSNAODED1400` (UFs que geram Não Dedutíveis no registro 1400) devem estar configurados com as devidas UFs e CFOPs.
- Ao usar a **Aba Fórmula IPM** (4.33+), os cinco parâmetros do registro 1400 são desconsiderados — ver a seção [Aba Fórmula IPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093-Cadastro-de-C%C3%B3digos-de-itens-IPM-por-UF-no-registro-1400#formula).
- Informar a **Data Final de vigência** faz o código deixar de aparecer no arquivo após essa data.
- O **Processar** e o **Gerar** ocorrem na tela EFD Fiscal ICMS/IPI, não neste cadastro.
