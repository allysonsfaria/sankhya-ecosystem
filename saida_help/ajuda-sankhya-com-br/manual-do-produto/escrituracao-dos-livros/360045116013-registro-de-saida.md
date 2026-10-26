---
id: "360045116013"
titulo: "Registro de Saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116013-Registro-de-Sa%C3%ADda"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Escrituração dos livros"
atualizado_em: "2026-09-15T14:42:49Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Impressão", "Relatórios", "Livros Fiscais", "P2", "P2A", "br.com.sankhya.mgeliv.rel.registrosaida", "Registro de Saída manual", "Livro", "Saída", "IPI", "ICMS", "CFOP", "Registro", "Obrigatório para empresas inclui notas fiscais e ICMS", "Resumo por estado/CFOP dados adicionais formatos PDF/Excel", "Define empresa período e modelo do relatório"]
---

# Registro de Saída

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313042824471) Módulo: Livros Fiscais > Relatórios
```

---

O Livro dos **"Registros de Saída"** é obrigatório para todas as empresas comerciais, estabelecido no Regulamento do ICMS, com o objetivo de registrar as notas fiscais de saída, destacando-se o ICMS incidente pelas saídas de produtos, a qualquer título, do estabelecimento.

Caso o contribuinte seja também indústria, é utilizado um mesmo livro de registro de saídas, de modelo próprio, com destaques de IPI e ICMS pelas vendas de mercadorias.

![Imagem 2: Caso o contribuinte seja também indústria, é utilizado um mesmo livro de registro de saídas, de modelo próprio, com…](https://ajuda.sankhya.com.br/hc/article_attachments/6343158930199)

Inicialmente, para geração do relatório de Registro de Saída, define-se sobre qual empresa serão geradas as informações; esta definição é feita através do campo **"Empresa"**.

Na sequência, teremos o campo **"Período"**, onde é estabelecido o intervalo que o relatório será gerado. Esse intervalo, geralmente abrange um mês completo, mas pode-se trabalhar com períodos menores ou maiores. Visto que, os campos Empresa e Período são obrigatórios para a geração do relatório.

No campo **"Página Inicial"** é inserida a informação referente a primeira página do relatório que será gerado.

O campo **"Página Final"** é gerado automaticamente de acordo com a quantidade de páginas totais do relatório. Ao final da geração do relatório, a informação aqui apresentada, é gravada na tela **"Financeiro > Preferências > Empresa > aba Livros Fiscais > campo Última página do registro de saídas"**. Além disso, ao clicar no botão "Gravar" o valor do campo Página inicial é atualizado com o valor do campo Página final para que na próxima geração do relatório a numeração fique em sequência.

No campo **"Data Emissão"** é feito o registro da data de emissão do relatório de saída.

No campo **"Modelo"**, é realizada a definição do modelo de relatório a ser utilizado. São disponibilizadas duas opções para escolha:

- **P2:** Este modelo é utilizado, quando a empresa é contribuinte de IPI (Indústrias);
- **P2A:** Esta marcação é efetuada, quando a geração do relatório for feita por empresas não contribuintes de IPI.
- **80 Colunas:** Com essa marcação selecionada, os dados do relatório serão apresentados de forma reduzida.

Abaixo, tem-se as marcações a serem realizadas, de modo que o relatório será gerado com base no que for aqui definido. São eles:

**Uma nota por linha?:** Ao efetuar esta marcação, na geração do relatório, será gerada uma única linha, agrupando cada Nota Fiscal no Livro de Saída.

**Imprimir observação?:** Essa opção quando marcada, realiza a apresentação/impressão da observação presente nas notas fiscais de saída.

**Alterar observação para razão social do parceiro:** Ao acionar essa marcação, tem-se a troca da observação da nota pela razão social do parceiro. Sendo que, esta marcação só estará disponível para configuração quando a marcação Imprimir observação? estiver habilitada.

**Imprimir livro de saída?:** Quando essa opção é marcada, no relatório são apresentadas todas as notas que representam saídas da empresa, ou seja, vendas, devolução de compra, transferências de saída, remessas, outras saídas, notas canceladas de saída e notas com numerações inutilizadas. Serão apresentados o detalhamento os valores debitados, a base de cálculo, o que foi isento ou não tributado e as alíquotas de ICMS (tanto para P2 e P2A) e as alíquotas de IPI (relatório P2). Além da substituição tributária, quanto tiver ocorrido  substituição tributária na nota.

**Imprimir resumo por estado?:** Quando esta marcação for efetuada, será exibido o resumo do relatório do Livro de Saída, apresentando os totais dos valores debitados, base de cálculo, o que foi isento ou não tributado, agrupando os totais por Estado.

**Imprimir resumo por CFO?:** Efetuando-se esta marcação, será exibido o resumo do relatório do Livro de Saída mostrando os totais dos valores debitados, base de cálculo, o que foi isento ou não tributado agrupando por CFOP.

**Imprimir dados da NF em todas as linhas?:** Quando esta opção está marcada, em conjunto com as opções **"Gerar linhas da Nota separadamente no Livro Fiscal"** (Comercial > Preferências > Empresa) e **"Imprimir Livro de Saída"**. Quando uma NF for apesentada mais de uma vez, não serão exibidos a partir da segunda aparição da nota, os campos **"Espécie"**, **"Série/Sub-Série"**, **"Número"**, **"dia"** e **"UF"**; estes ficaram omitidos.

**Imprimir redução de Pauta por ST em isentas?:** Este campo, se marcado serão impressos no relatório, os valores da redução de pauta na coluna isentas na linha da substituição tributária. Quando desmarcado o valor é apresentado em branco.

**Formato da Impressão:** Este campo disponibiliza duas formas de exportação dos dados na geração do relatório, auxiliando na conferência e verificação de possíveis erros. O campo pode ser definido entre os formatos PDF e Excel; caso o campo fique em branco, o padrão será o formato PDF. As referidas opções apresentam respectivamente os seguintes comportamentos:

- **PDF:** Quando for selecionado o formato de impressão PDF, na visualização do relatório, o mesmo será aberto neste formato.
- **Excel:** Sendo selecionado o formato de impressão Excel, ao clicar para visualizar o relatório, o mesmo será baixado conforme as configurações do navegador que está sendo utilizado, ou seja, o arquivo poderá ser baixado automaticamente ou poderá ser aberta uma tela o questionando em qual local deseja salva-lo. Deste modo deve-se acessar o local onde o arquivo foi baixado e abri-lo.

**Imprime modelo no título?:** Esta marcação quando efetuada, irá apresentar no cabeçalho do relatório, o modelo utilizado (P2 ou P2A).

**Imprimir data/hora da emissão?:** Quando marcado, este campo irá determinar a apresentação da data e da hora da emissão do relatório em seu cabeçalho.

**Agrupar CFO diferentes?:** Marcando-se esta opção, serão agrupadas as informações CFOP's diferentes na nota, mas para isso, a opção **"Uma nota por linha"** deve estar marcada. Esta opção é incompatível com a marcação **"Separar linhas de alíquotas de IPI diferentes"**.

**Imprimir apenas imobilizado:** Este campo se marcado, fará com que sejam exibidas apenas notas com CFOP's: 5551, 6551, 7551, 5552, 6552, 7552, 5553, 6553 e 7553.

**4 casas decimais p/Vlr ICMS?:** Essa opção quando marcada, realiza a impressão de apenas quatro casa na coluna de valor de ICMS no relatório.

**Totaliza Resumo por ESTADO e CFOP?:** A marcação desse campo, trabalha em conjunto com a definição realizada no campo **"Imprimir resumo por estado"**. No final do resumo de estado, serão apresentados o total do valor contábil, base de cálculo, valor debitado, isenta e outras. Este mesmo campo, quando marcado em conjunto com o Resumo por CFOP, irá realizar a totalização por grupo de CFOP.

**Separar linhas de alíquotas de IPI diferentes?:** Esta marcação quando efetuada, serão geradas as linhas agrupadas por alíquota  de IPI, quando a opção **"Uma nota por linha"** estiver desmarcada.

O botão **"Gerar Relatório"** é responsável pelo agrupamento das informações, e consequente apresentação destas na tela em forma de relatório.

---

**Parâmetros que influenciam a rotina**

Quando o parâmetro **"Forçar o download de relatórios internos? - FORCEDOWNLOAD"** for habilitado, fará com que a visualização do relatório seja aberta pelo visualizador nativo do sistema operacional.

Com o parâmetro **"Usar Dt. Ent/Saida na Ger. do Liv. Fis de Saida-USADTSAILIVSAI"** ligado, o sistema irá considerar a data informada no campo **"Dt. do Movimento"** (localizado na tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI#abageral)) para gerar o relatório de saída. Caso ele esteja desligado, será considerada a **"Dt. do documento"** (presente na tela Cadastro Livro ICMS/IPI, aba Geral) do livro fiscal para gerar o relatório de saída. 

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116013-Registro-de-Sa%C3%ADda#top)
