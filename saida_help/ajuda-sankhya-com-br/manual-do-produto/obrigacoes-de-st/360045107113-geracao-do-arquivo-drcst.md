---
id: "360045107113"
titulo: "Geração do Arquivo DRCST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Obrigações de ST"
atualizado_em: "2026-09-15T17:20:48Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Livros Fiscais", "SEFAZ", "br.com.sankhya.mgeliv.mov.geracaoarquivodrcst", "Geração do Arquivo DRCST manual", "Notas fiscais valores e itens do ICMS-ST", "Filtros gerar arquivo configurar tela anexar documentos", "Campos obrigatórios perfis registros únicos", "Documentos Eletrônicos", "ICMS-ST", "DRCST"]
---

# Geração do Arquivo DRCST

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/16312439495703) Módulo: Livros Fiscais > Conexão
```

---

Nessa tela serão apresentadas todas as Notas Fiscais pertencentes ao Ressarcimento, Restituição e Complementação de ICMS-ST, assim como seus respectivos valores e itens, para facilitar a validação das informações.

Além da possibilidade de realizar a geração do arquivo .txt nesta rotina, também será possível visualizar os documentos utilizados na formação do arquivo.

**Observação:** alguns registros são únicos no arquivo, portanto, caso haja a tentativa de inclusão de mais de um dos registros abaixo, será apresentada uma mensagem informando que o **"Registro X"** é único no arquivo e não será possível adicionar outro registro na tabela:

- Registro 0001;
- Registro 0005;
- Registro 0100;
- Registro 0990;
- Registro H001;
- Registro H005;
- Registro H990;
- Registro 2001;
- Registro 2100;
- Registro R9001;
- Registro R9990;
- Registro R9999.

Dessa forma, por meio dos links abaixo você pode consultar as funcionalidades da tela Geração do Arquivo DRCST:

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#abageral) |  | [Aba 0150](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#aba0150) |
| --- | --- | --- |
| [Outras Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#outrasinformaes) |  | [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#botesnotopodatela) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#botooutrasopes...) |  | [Botão Configuração de Tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#bot%C3%A3oconfigura%C3%A7%C3%A3odetela) |
| [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#parmetrosqueinfluenciamestarotina) |  |  |

## Aba Geral

Acima dessa aba teremos o Painel Principal da tela, onde estão agrupados   os dados que servirão de base para todo o restante da Geração do Arquivo DRCST.

![Imagem 2: Acima dessa aba teremos o Painel Principal da tela, onde estão agrupados os dados que servirão de base para todo o…](https://ajuda.sankhya.com.br/hc/article_attachments/9636308200087)

No campo **"Empresa"** selecione a empresa que será informada na declaração.

Os campos **"Dt. Inicial"** e **"Dt.Final"** deverão obrigatoriamente, estarem definidos como o primeiro e o último dia do mês respectivamente.

Na aba Geral, teremos:

O campo **"Perfil de Apresentação do Arquivo"** possibilitará a geração consolidada da DRCST, em que você poderá selecionar as seguintes opções **"Perfil A"**, **"Perfil B"**, **"Perfil C"** e **"Perfil D"**.

**Nota:** ao selecionar a opção Perfil D, o campo **"Versão do Layout"** ficará indisponível. Além de que, quando essa opção for definida, as seguintes informações serão geradas:

- Campos **"CNPJ Declarante/Participante"** dos Registros 2112, 2113, 2114, 2130, 2131, 2132 e 2134;
- Geração dos Registros 0150 e H011.

**Observação:** assim, ao processar o arquivo, podemos ver que no registro 9900 será considerada a geração do registro 0150 e do H011. Lembrando que o registro H011 é atrelado ao registro H010, ou seja, se houver um registro H010, também terá um H011.

Ao habilitar a marcação **"Permitir notas de vendas para SN com CST 60 sem retenção ST no R2113?"**, as notas fiscais de venda para parceiros do Simples Nacional que possuem o CST 60 e não tem ICMS ST retido, serão geradas no registro 2113. Dessa forma, o cálculo do campo **"Vlr. do crédito decorrente da Saída p/optante do Simples Nacional"** da sub-aba **"2110"** (localizada na aba **"2100"**) ocorrerá da seguinte maneira:

```
    ![Imagem 3: Ao habilitar a marcação "Permitir notas de vendas para SN com CST 60 sem retenção ST no R2113?" , as notas fiscais de…](https://ajuda.sankhya.com.br/hc/article_attachments/16312439505175) Base de Cálculo do ICMS ST da Operação Anterior (ITE.BASESUBSTITANT) *
     70% * (Alíquota Efetiva do ICMS / 100)
```

Você utilizará a marcação **"Permite itens de entrada c/ Tributação 60 s/ valor.ant. informado?"** quando houverem notas fiscais que têm CST 060 e que não possuem valores de ICMS ST de operações anteriores destacados. Sendo assim, você poderá escolher dentre as seguintes opções:

- **Trazer considerando Vlrs do ST Normal:** Ao selecionar essa opção, o sistema buscará as notas fiscais que possuem CST e que os valores de ICMS ST foram destacados nos campos **"Vlr. substituição"** e **"Vlr. substituição"** na grade itens da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens);
- **Trazer sem valores:** Por essa opção, as notas que possuem CST 060 e aquelas não possuem valores de ICMS ST de operações anteriores serão buscadas no sistema;
- **Não trazer:** Por meio dessa, o sistema não trará nenhuma nota fiscal que possua CST 060 que não tenha de ICMS ST anterior informado.

Nos campos a seguir você informará uma lista de Nro.(s) Único (s) que não foram trazidos na utilização do Filtro Padrão da geração do Registro 2113, porém cada um deste terá sua especificidades.

No campo **"Lista de notas reg. 2113 - Venda à consumidor final:"** insira os números correspondentes à Venda ou Devolução de Venda considerando o Tipo de Operação de Saída como sendo **"10 - Venda à consumidor final"**. As notas aqui inseridas serão utilizadas no processo da geração da DRCST independente do Filtro exigido para o registro.

Em **"Lista de notas reg. 2113 - Venda p/ outra unidade da federação:"**, considera-se neste campo a lista de Nro. Único referente à Venda ou Devolução de Venda, ao considerar o Tipo de Operação de Saída igual a 20 - Venda para outra unidade de federação. As notas informadas aqui serão inseridas no processo da geração da DRCST independente do filtro exigido para o registro.

No campo **"Lista de notas reg. 2113 - Venda para Simples Nacional"** o permitirá que uma lista de Nro. Único de Notas que não foram trazidas no filtro padrão da geração do Registro 2113 (Venda ou Devolução de Venda), ao considerar o Tipo de Operação de Saída igual a 30 - Venda para Simples Nacional. As notas informadas aqui serão inseridas no processo da geração da DRCST independente do filtro exigido para o registro.

Informe no campo **"Lista de notas reg. 2130:"** uma lista de de Nro. Único de Notas referentes à Compra ou Devolução de Compra. As notas aqui informadas serão inseridas no processo da geração da DRCST independente do Filtro exigido para o registro.

**Observação:**ao inserir os dados nos campos citados acima, você deverá informar a nota e a sequência do(s) iten(s) em que a nota será vinculada, por exemplo:

123456: 1,5 , ou seja, nunota: sequência, sequência.

Caso deseje inserir mais de uma nota, as informações deverão ser separadas por ponto e vírgula. Observe:

123456:1,5;5678:7,8.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#top)

## Aba 0150

![Imagem 4: Aba 0150](https://ajuda.sankhya.com.br/hc/article_attachments/4416255391511)

Ao preencher o campo **"CNPJ Declarante/Participante"** o Registro 2112, do campo 07 será preenchido. Sendo que, este registro trata-se dos Totais dos documentos fiscais de vendas a consumidor final da mercadoria identificada no Registro 2110 emitido por ECF (Código 02, 2D E 60).

Esse registro deverá identificar a qual empresa a movimentação está vinculada e gerar o CNPJ da mesma no campo correspondente, portanto:

- **Registro 2112 - Campo 07:** informe o CNPJ do declarante e do participante da Tabela do Registro 0150 (tamanho 14 caracteres);
- **Registro 2113 - Campo 17:** Informe o CNPJ do declarante e do participante da Tabela do Registro 0150 (tamanho 14 caracteres). Com o preenchimento deste, o Registro **"2114"** será impactado;
- **Registro 2130 - Campo 27:** Preencha com o CNPJ do declarante e do participante da Tabela do Registro 0150 (tamanho 14 caracteres). Tem ainda que, os  registros **"2131"**, **"2132"** e **"2134"** serão impactados com o Registro 2130.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#top)

## Outras Informações

![Imagem 5: Outras Informações](https://ajuda.sankhya.com.br/hc/article_attachments/4416263083543)

Em relação ao campo **"Tipo de Operação de Saída"** localizado na sub-aba **"2113"** da aba **"2100"** (aba "2110"), será possível definir o tipo de modalidade como indicador para regra de apuração. Assim, neste campo teremos três opções para seleção:

- 10 - Venda à consumidor final;
- 20 - Venda para outra unidade da federação;
- 30 - Venda para Simples Nacional.

**Nota:** a opção **"10 - Venda à consumidor final"** será o código que identificará o Tipo de Operação de Saída no campo 3 do Registro 2113 do Arquivo da DRCST. Assim, se você selecionar esta opção, o sistema seguirá com a seguinte regra para a geração da apuração:

Calcular o Valor Ponderado Médio Unitário do produto considerando:

- **Entradas:** Valor ponderado médio entradas = VPMe;
- **Saídas:** Valor ponderado médio saídas = VPMs.

**Observação:** a Base de Cálculo do ICMS ST utilizada para o cálculo do Valor Ponderado Médio das Entradas para Consumidor Final, será o valor da base destacada na Nota Fiscal de Compra e, a utilizada para o cálculo do Valor Ponderado Médio das Saídas, será o valor total dos produtos (preço praticado).

Posteriormente, realize a multiplicação dos valores médios unitários, considerando a quantidade vendida e, após, subtrair a entrada e a saída. Observe:

```
![Imagem 6: Posteriormente, realize a multiplicação dos valores médios unitários, considerando a quantidade vendida e, após,…](https://ajuda.sankhya.com.br/hc/article_attachments/16312439505175) (VPMe x quantidade vendida) - (VPMs x quantidade vendida) = BC ICMS ST a Restituir ou
         Complementar
```

De forma que, caso VPMe > VPMs, deve-se realizar a restituição e, sendo VPMe < VPMs, deve-se efetuar a complementação.

Após calculado o valor da Base de Cálculo do ICMS a Restituir ou a Complementar, aplique a alíquota efetiva, ou seja, a alíquota interna: BC ICMS Restituir x alíquota efetiva / BC ICMS Complementar x alíquota efetiva.

![Imagem 7: Após calculado o valor da Base de Cálculo do ICMS a Restituir ou a Complementar , aplique a alíquota efetiva, ou seja,…](https://ajuda.sankhya.com.br/hc/article_attachments/4416255712919)

O campo **"Responsável pela Retenção do ICMS-ST"** localizado na aba **"2100"**, sub-aba **"2130"** tem a finalidade de informar ao fisco qual é o responsável pelo recolhimento do ICMS-ST, com o intuito de realizar a Apuração da DRCST e preencher de forma adequada o campo 8 do Registro 2130. Neste campo, teremos as seguintes opções:

- **1 - Remetente Direto:** Selecionamos esta opção quando a responsabilidade de recolhimento do ST é do remetente da mercadoria, ou seja, quando o remetente da mercadoria for o substituto tributário;
- **2 - Remetente Indireto:** Esta opção deverá ser selecionada quando, na operação de entrada, o remetente da mercadoria for substituído, ou seja, o ICMS ST não foi retido na Nota Fiscal, ou quando o fornecedor do fornecedor quem recolheu;
- **3 - Próprio Declarante:** Você selecionará esta opção quando o ICMS ST das operações tenha sido recolhido pelo próprio declarante, ou seja, o pagamento do ICMS ST foi realizado pelo contribuinte que está solicitando o ressarcimento.]

Os Registros **"2131"** e **"2134"** serão gerados somente se o documento fiscal identificado no Registro 2130 se referir à entrada de mercadoria com o campo **"Responsável pela Retenção do ICMS-ST"** preenchido com a opção **"2 - Remetente Indireto"**. Além disso, referente ao Registro 2134, não haverá preenchimento das informações de Base ICMS ST Anterior.

**Observação:** o Registro especificados acima, serão gerados somente se os seus registros pais (2100, 2110, 2120, 2130) forem gerados seguindo a mesma estrutura de outros registros que dependem de seus seus registros pais para que estes possam ser gerados.

Referente ao campo **"Vlr. do ICMS-ST"** do Registro **"2130"**, teremos que quando o Responsável pela Retenção for o Código 1, informe o valor destacado no documento fiscal de entrada como Valor do ICMS ST. Utiliza-se neste caso, o valor do ICMS ST Normal (Vlr. Substituição da ITE). Porém, quando o Responsável pela Retenção for código 2 ou 3, informe o valor que foi destacado na tag com a informação do ICMS ST Anterior.

Destaca-se que no campo **"Responsável pela Retenção do ICMS-ST"**, quando a NF de entrada informada no Registro 2130 tiver a informação do ICMS ST Normal, o sistema retornará esse campo como Remetente Direto (Cód. 1). E ao informar neste mesmo Registro a NF Entrada com a informação do ICMS ST Anterior, o sistema retornará este campo como Remente Indireto (Cód. 2).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#top)

## Botões no topo da tela

A Geração do Arquivo DRCST é composta por abas e também por botões, que executam diversas funções dentro desta rotina. Vejamos sobre eles:

![Imagem 8: Filtros: Este botão abre o assistente de configuração de filtros personalizados para a tela.](https://ajuda.sankhya.com.br/hc/article_attachments/16312398640919) **Filtros:** Este botão abre o assistente de configuração de filtros personalizados para a tela.

![Imagem 9: Modo grade (F6)/Configurar grade: Por meio deste botão, alterna-se a visualização da tela entre modo grade e modo…](https://ajuda.sankhya.com.br/hc/article_attachments/16312439517591) **Modo grade [F6]/Configurar grade:** Por meio deste botão, alterna-se a visualização da tela entre modo grade e modo formulário; além disto, configura-se a grade da maneira almejada, ou seja, pode-se selecionar, ordenar ou ocultar as colunas da forma mais confortável para o usuário.

![Imagem 10: Cadastrar Demonstrativo p/ Apuração do Ressarcimento de ST (F8): Por meio deste botão, tem-se a inicialização da…](https://ajuda.sankhya.com.br/hc/article_attachments/16312439522967) **Cadastrar Demonstrativo p/ Apuração do Ressarcimento de ST [F8]:** Por meio deste botão, tem-se a inicialização da Geração do Arquivo DRCST.

![Imagem 11: Anterior e Próximo: Teremos aqui, os botões de navegação entre os registros já cadastrados.](https://ajuda.sankhya.com.br/hc/article_attachments/16313169975447) **Anterior e Próximo:** Teremos aqui, os botões de navegação entre os registros já cadastrados.

![Imagem 12: Excluir (F9): Ao acionar este botão, o registro selecionado será excluído.](https://ajuda.sankhya.com.br/hc/article_attachments/16313158774295) **Excluir [F9]:** Ao acionar este botão, o registro selecionado será excluído.

![Imagem 13: Duplicar: Este botão replica o registro selecionado, criando um novo com as configurações equivalentes àquele…](https://ajuda.sankhya.com.br/hc/article_attachments/16313169979671) **Duplicar:** Este botão replica o registro selecionado, criando um novo com as configurações equivalentes àquele primeiramente selecionado.

![Imagem 14: Atualizar: Por meio deste botão, recarrega-se toda a tela de Geração do Arquivo DRCST .](https://ajuda.sankhya.com.br/hc/article_attachments/16313169981847) **Atualizar:** Por meio deste botão, recarrega-se toda a tela de Geração do Arquivo DRCST.

![Imagem 15: Processar: Ao acionar este botão, o sistema processará os documentos e preencherá as tabelas dos registros, mantendo o…](https://ajuda.sankhya.com.br/hc/article_attachments/16313158781847) **Processar:** Ao acionar este botão, o sistema processará os documentos e preencherá as tabelas dos registros, mantendo o saldo inicial caso o mesmo já tenha sido calculado.

**Observação:** ao clicar nesse botão, quando houver alguma inconsistência relacionada às notas de compras ou devolução de vendas (falta de **"Chave Nfe"** ou **"Sequência Fiscal"**) será apresentada a seguinte mensagem:

**"Existe notas inconsistentes para a empresa X neste período. Verifique no menu Outras Opções, Registros Inconsistentes".**

Para ajustar essas inconsistências, você pode acessar a Central e realizar os ajustes ou através do [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354), importando o XML e clicando no botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Ajustar notas para DRCST (Chave e Sequência Fiscal)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#ajustarnotasparadrcst(chaveesequ%C3%AAnciafiscal)).

![Imagem 16: Gerar Arquivo: Através deste botão, será gerado o arquivo .txt exigido pela P ortaria SEF N. 378/2018 .](https://ajuda.sankhya.com.br/hc/article_attachments/16313158783767) **Gerar Arquivo:** Através deste botão, será gerado o arquivo .txt exigido pela Portaria SEF N. 378/2018.

**Nota:** antes da geração correta do Bloco H, especificamente o H010, deveremos realizar a [Contagem de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694-Contagem-de-Estoque) ou a [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514-C%C3%B3pia-de-Estoque) para que seja calculada a quantidade final das compras e vendas do período de escrituração, sendo que esta, deverá sempre ser realizada no último dia do mês da apuração.

![Imagem 17: Exportar grade para PDF: Este botão apresenta opções de exportação e visualização das informações da tela. Neste…](https://ajuda.sankhya.com.br/guide-media/01H6743AM7C5181E5VX745E5ZA) **Exportar grade para PDF:** Este botão apresenta opções de exportação e visualização das informações da tela. Neste poderemos **"Exportar para PDF"**, **"Exportar para planilha"** ou **"Exportar para cubo"**.

![Imagem 18: Anexo: Por meio deste botão pode-se anexar qualquer documento que seja relevante para a rotina de Geração do Arquivo…](https://ajuda.sankhya.com.br/guide-media/01H6748806TF4YTBWEJSKWJX68) **Anexo:** Por meio deste botão pode-se anexar qualquer documento que seja relevante para a rotina de Geração do Arquivo DRCST.

![Imagem 19: Outras Opções: As funcionalidades disponibilizadas por este botão podem ser visualizadas no link Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/16313170002455) **Outras Opções:** As funcionalidades disponibilizadas por este botão podem ser visualizadas no link [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#botooutrasopes...)

![Imagem 20: Configuração da Tela: Por meio deste botão, pode-se realizar a configuração da tela e suas respectivas abas e campos de…](https://ajuda.sankhya.com.br/hc/article_attachments/16313158800919) **Configuração da Tela:** Por meio deste botão, pode-se realizar a configuração da tela e suas respectivas abas e campos de forma mais proveitosa e adequada para o usuário. Além disto, será possível determinar como ocorrerá a geração da numeração da tela, seja **"Automática"** ou **"Manual"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#top)

## Botão Outras Opções...

O botão **"Outras Opções..."** é acionado por meio do ícone ![Botão](https://ajuda.sankhya.com.br/guide-media/01H3M65J642CXVYNCAVGNG33DV) localizado no alto da tela:

![Imagem 22: O botão "Outras Opções..." é acionado por meio do ícone localizado no alto da tela:](https://ajuda.sankhya.com.br/hc/article_attachments/4416263333911)

Aqui, teremos as funcionalidades:

**Marcar Arquivo como Confirmado:**  Esta opção quando acionada irá alterar a marcação **"Arquivo Confirmado?"** localizada na aba **"Geral"** desta tela. Uma vez que o arquivo foi confirmado, você não poderá mais processar os dados, apenas gerar o arquivo. Desta forma, este botão será útil para que, uma vez entregue o arquivo, os dados não sejam alterados.

**Nota:** apenas os usuários que possuírem permissão para alteração nesta tela (realizada na tela [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos)) poderão utilizar esta opção.

**Desmarcar Arquivo como Confirmado:** Esta opção desmarcará a opção Arquivo Confirmado? da aba Geral.

**Reprocessar registros totalizadores:** A opção **"Reprocessar registros totalizadores"** irá reprocessar e totalizar os registros da DRCST, uma vez que seja necessário deletar algum registro que impactará na apuração.

**Descartar registros 2110 com quantidade de compras insuficiente:** Esta opção desconsiderará os registros que não possuem quantidade de compras o suficiente para realização da Apuração da DRCST.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#top)

## Botão Configuração de Tela

![Imagem 23: Botão Configuração de Tela](https://ajuda.sankhya.com.br/hc/article_attachments/4416263349015)

Por meio do botão ![Imagem 24: Por meio do botão "Configuração da Tela" , você terá acesso à marcação "Consid. a qtd. das vendas para geração das…](https://ajuda.sankhya.com.br/hc/article_attachments/16313158800919) **"Configuração da Tela"**, você terá acesso à marcação **"Consid. a qtd. das vendas para geração das devoluções no registro 2110"** em que, se você optar por não marcar esta opção, ao processar o registro em questão será possível visualizar no registro 2110, o registro 2113.

Ao marcá-la o processamento dos registros ocorrerá de modo a considerar a quantidade de vendas positiva ao realizar as devoluções, para tanto, no registro 2113 a nota de devolução não será exibida.

Além disso, teremos também a marcação "Exibe somente registros 2110 com compra insuficiente", que deverá ser efetuada apenas quando desejar-se a demonstração dos Registros 2110 (aba "2100", sub-aba "2110" desta tela) com compra insuficiente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#top)

## Parâmetros que influenciam esta rotina

Através do parâmetro **"Data início para compras para o DRCST - DTINICOMDRST"** será possível limitar o período de busca das Notas de Compras para a Apuração da DRCST, assim, o sistema selecionará as notas de entradas a partir da data configurada neste parâmetro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107113-Gera%C3%A7%C3%A3o-do-Arquivo-DRCST#top)
