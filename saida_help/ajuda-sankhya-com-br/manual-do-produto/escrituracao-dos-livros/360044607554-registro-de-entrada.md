---
id: "360044607554"
titulo: "Registro de Entrada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607554-Registro-de-Entrada"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Escrituração dos livros"
atualizado_em: "2026-09-15T14:42:35Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "CNPJ", "Empresa", "Relatório", "Livros Fiscais", "Livro", "ICMS", "CFOP", "CPF", "Registro", "P1", "P1A", "br.com.sankhya.mgeliv.rel.registroentrada", "Registro de Entrada manual", "Entrada", "Obrigatório ICMS IPI", "Empresa período páginas data", "Observações resumos formatos."]
---

# Registro de Entrada

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312978434839) Módulo: Livros Fiscais > Relatórios
```

---

O livro contendo os **"Registros de Entrada"**, é obrigatório para todas as empresas comerciais, estabelecido pelo Regulamento do ICMS de cada estado, com o objetivo de registrar as notas fiscais de entrada, destacando os ICMS incidentes pelas compras.

É destinado à escrituração dos documentos fiscais relativos às entradas de mercadorias ou bens e às aquisições de serviços de transporte e de comunicação efetuadas a qualquer título pelo estabelecimento, quando contribuinte de ICMS.

Caso o contribuinte também seja uma indústria, é utilizado um mesmo livro de registro de entradas, de modelo próprio, com destaques de IPI e ICMS pelas compras de mercadorias.

![Imagem 2: Caso o contribuinte também seja uma indústria, é utilizado um mesmo livro de registro de entradas, de modelo próprio,…](https://ajuda.sankhya.com.br/hc/article_attachments/6271095937175)

Inicialmente, para geração do relatório de Registro de Entrada, defina a **"Empresa"** em que serão geradas as informações.

Na sequência, temos o campo **"Período"**, onde é estabelecido o intervalo que o relatório será gerado. Este intervalo, geralmente abrange um mês completo, mas pode-se trabalhar com períodos menores ou maiores. Visto que, os campos Empresa e Período são obrigatórios para a geração do relatório.

No campo **"Página Inicial"** é inserida a informação referente a primeira página do relatório que será gerado.

O campo **"Página Final"** é gerado automaticamente de acordo com a quantidade de páginas totais do relatório. Ao final da geração do relatório, a informação aqui apresentada, é gravada na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrosfiscais), campo **"Última página do registro de entradas"**. Além disso, ao clicar no botão **"Gravar"** o valor do campo Página inicial é atualizado com o valor do campo Página final para que na próxima geração do relatório a numeração fique em sequência.

No campo **"Data Emissão"** é feito o registro da data de emissão do relatório de entrada.

No campo **"Modelo"**, é realizada a definição do modelo de relatório a ser utilizado. São disponibilizadas duas opções para escolha:

- **P1:** Este modelo é utilizado quando a empresa é contribuinte de IPI (Indústrias);
- **P1A:** Esta marcação será selecionada quando a empresa não for contribuinte de IPI;
- **80 Colunas:** Com essa marcação selecionada, os dados do relatório serão apresentados de forma reduzida.

A seguir, trataremos das marcações que podem ser realizadas, de modo que o relatório será gerado com base no que for definido aqui. São elas:

**Imprimir observação?:** Essa marcação quando efetuada, apresenta a observação das notas no relatório, se as notas estiverem com observações informadas.

**Imprimir em linha separada:** Quando essa marcação for selecionada, a impressão dos dados da observação será realizada em linhas abaixo da linha da nota, ao invés de exibir na coluna observação. Essa marcação só está disponível para o modelo P1A.

**Alterar observação para razão social do parceiro:** Ao acionar esta marcação, tem-se a troca da observação da nota pela razão social do parceiro. Sendo que, esta marcação só estará disponível para configuração quando a marcação Imprimir observação estiver habilitada. É importante que na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao), o campo referente à **"Razão Social"** esteja preenchido.

**Imprimir Livro de Entrada:** Quando essa marcação for realizada, o relatório será emitido com o detalhamento das notas que representam as entradas. Serão exibidas as notas de Compra, Devolução de venda, Transferências de entrada, Retorno de remessas, Outras entradas, e Notas Canceladas de Entrada.

**Imprimir resumo por estado?:** Se você efetuar a marcação desse campo, será exibido o resumo do relatório do Livro de Entrada, apresentando os totais dos valores creditados, base de cálculo, o que foi isento ou não tributado, agrupando os totais por Estado.

**Saltar Página:** Esta marcação será habilitada, caso o campo anteriormente mencionado esteja marcado. Caso ela esteja realizada, o resumo será exibido na página seguinte.

**Imprimir resumo por CFO?:** Ao efetuar essa marcação, será exibido o resumo do relatório do Livro de Entrada mostrando os totais dos valores creditados, base de cálculo, o que foi isento ou não tributado agrupando por CFOP.

**Saltar Página:** Essa marcação será habilitada, caso o campo anteriormente mencionado esteja marcado. Caso ela esteja realizada, o resumo será exibido na página seguinte.

**Imprimir data/hora da emissão?:** Quando marcado, este campo irá determinar a apresentação da data e da hora da emissão do relatório em seu cabeçalho.

**Imprime modelo no título?:** Esta marcação quando efetuada, irá apresentar no cabeçalho do relatório, o modelo utilizado (P1 ou P1A).

**Imprimir CNPJ/CPF coluna Emitente?:** Esta opção quando selecionada, na coluna **"Código Emitente"** no relatório, será apresentado o CNPJ ou o CPF do parceiro.

**Imprimir base para isentas/outras?:** Esta campo se marcado, irá trazer impresso no relatório o valor da base na coluna isentas. Quando desmarcado, sendo o valor de isentas igual a zero,  o valor será apresentado em branco. Este campo estará habilitado, caso o modele utilizado, seja o modelo P1.

**Imprimir dados da NF em todas as linhas?:** Quando essa opção está marcada, em conjunto com as opções **"Gerar linhas da Nota separadamente no Livro Fiscal"** (aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrosfiscais), tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)) e **"Imprimir Livro de Entrada"**. Quando uma NF for apesentada mais de uma vez, não serão exibidos a partir da segunda aparição da nota, os campos **"Espécie"**, **"Série/Sub-Série"**, **"Número"**, **"dia"** e **"UF"**; estes ficaram omitidos.

**Imprimir apenas imobilizado:** Este campo quando marcado, serão apresentadas as notas que possuem os seguintes CFOP's 1551, 2551, 3551, 1552, 2552, 3552, 1553, 2553 e 3553.

**Totaliza Resumo por ESTADO e CFOP?:** A marcação deste campo, trabalha em conjunto com a definição realizada no campo **"Imprimir resumo por estado"**. No final do resumo de estado, serão apresentados o total do valor contábil, base de cálculo, valor creditado, isenta e outras. Este mesmo campo, quando marcado em conjunto com o Resumo por CFOP, irá realizar a totalização por grupo de CFOP.

O campo **"Formato da Impressão"**  disponibiliza duas formas de exportação dos dados na geração do relatório, auxiliando na conferência e verificação de possíveis erros. O campo pode ser definido entre os formatos PDF e Excel; caso o campo fique em branco, o padrão será o formato PDF. As referidas opções apresentam os seguintes comportamentos:

- **PDF:** Quando for selecionado o formato de impressão PDF, na visualização do relatório, o mesmo será aberto neste formato.
- **Excel:** Sendo selecionado o formato de impressão Excel, ao clicar para visualizar o relatório, o mesmo será baixado conforme as configurações do navegador que está sendo utilizado, ou seja, o arquivo poderá ser baixado automaticamente ou poderá ser aberta uma tela questionando onde você deseja salvar o arquivo. Deste modo acesse o local onde o arquivo foi baixado e realize a abertura do mesmo.

O botão **"Gerar Relatório"** é responsável pelo agrupamento das informações, e consequente apresentação destas, na tela em forma de relatório.

---

**Parâmetros que influenciam a rotina**

Quando o parâmetro **"Forçar o download de relatórios internos? - FORCEDOWNLOAD"** for habilitado, fará com que a visualização do relatório seja aberta pelo visualizador nativo do sistema operacional.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607554-Registro-de-Entrada#top)
