---
id: "1500008984922"
titulo: "Geração do arquivo GIA/ST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Obrigações de ST"
atualizado_em: "2026-09-15T17:20:35Z"
rotulos: ["Configuração", "Livros Fiscais", "SEFAZ", "ICMS", "Impostos", "br.com.sankhya.geracao.arquivo.giast", "GIA/ST", "Geração do arquivo GIA/ST", "Especificações Registro ICMS", "Geração Arquivo GIA/ST", "Configurações Declarante", "GIA-ST"]
---

# Geração do arquivo GIA/ST

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312913104791) Módulo: Livros Fiscais > Conexão
```

---

Nessa tela você fará a geração do Arquivo Eletrônico para Entrega da GIA/ST Nacional por UF de destino caso realize a emissão de notas fiscais com produtos sujeitos ao ICMS/ST e consumidor final de outra UF. Para saber mais sobre esse registro e a tela onde ele será gerado, consulte os links a seguir:

| [Introdução](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST#introdu%C3%A7%C3%A3o) |  | [Regras para a geração do Registro](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST#regrasparaagera%C3%A7%C3%A3odoregistro) |
| --- | --- | --- |
| [Aba Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST#abaconfigura%C3%A7%C3%B5es) |  | [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST#bot%C3%B5esdatela) |

![Imagem 2: Botões da tela](https://ajuda.sankhya.com.br/hc/article_attachments/1500013938921)

## Introdução

O Guia Nacional de Informação e Apuração do ICMS Substituição Tributária (GIA-ST), é a declaração utilizada por contribuintes de outros Estados que na condição de responsável, efetuarão a retenção do imposto a favor de outro Estado. Dado que, para realizar o envio da GIA-ST Nacional o contribuinte deve possuir a Inscrição Estadual como Substituto Tributário nos Estados ao qual enviarão o documento.

Caso o contribuinte queira desenvolver seu próprio sistema de preenchimento da GIA-ST, poderá fazê-lo, dessa forma não precisará utilizar o programa fornecido pela SEFAZ-RS. Para isso, siga as normas estabelecidas no Ajuste SINIEF 08/99, publicado no Diário Oficial da União em 28/10/99, principalmente ao que se refere ao Leiaute do Arquivo da GIA-ST – Versão 3.

A geração do arquivo deve ser realizada a partir das especificações contidas nas tabelas de registro **"A0"**, **"A1"**, **"A2"**, **"A3"** e **"A4"**. Assim, cada tabela representará uma linha no arquivo. Observe:

- A aba A0 informará o início de uma nova GIA-ST, em que todas as linhas subsequentes estarão associadas aos dados desse registro até que uma nova ocorrência do registro A0 apareça, sinalizando assim, uma nova GIA-ST, ou o final do arquivo.
- Cada registro a ser gerado nessa tela ocupará uma linha do arquivo, por exemplo, se houverem 5 registros do anexo I, então haverão 5 linhas iniciando com A1. Assim, podemos observar que o registro A0 ocorre apenas uma vez para cada GIA-ST e os registros A1, A2, A3 e A4 podem ocorrer mais de uma vez, sem limite pré-definido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST#top)

## Regras para a geração do Registro

Primeiramente, para que os dados da GIA/ST sejam processados, será necessário que algumas funções referentes à Empresa e período da geração do arquivo no sistema já tenham sido executadas. Observe:

- Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Insc. Estadual Contribuinte ST no Estado Dest.](https://ajuda.sankhya.com.br/hc/pt-br/articles/Aba%20Insc.%20Estadual%20Contribuinte%20ST%20no%20Estado%20Dest.), cadastre uma **"Inscrição Estadual"** como Substituto Tributário nos Estados a que enviarão a GIA/ST;
- Geração do ICMS/IPI na tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI);
- Conferência dos Livros Gerados que é executada na tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI);
- Realize também o registro de apuração do ICMS em [Registro de Apuração do ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS);
- Efetue o lançamento das obrigações do ICMS e ICMS ST a recolher na tela [Obrigações do ICMS e ICMS a Recolher](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher).

Destacamos ainda que, se todos os valores se referirem às operações com produtos sujeitos ao ICMS-ST para outros Estados, a **"Empresa"**, **"Referência"** e a **"UF"** devem ser selecionados conforme as operações relativas a produtos sujeitos à Substituição Tributária.

Na aba **"A0"**, se você preencher o campo **"Valor do ICMS-ST Devolução de mercadorias"** com o valor total do ICMS-ST dos itens de operações de devolução de saída, será necessário também completar a aba **"A1"** considerando as operações com ICMS-ST e/ou FCP-ST com pelo menos um dos CFOP's abaixo:

- 2201 - Devolução de venda de produção do estabelecimento;
- 2202 - Devolução de venda de mercadoria adquirida ou recebida de terceiros;
- 2203 - Devolução de venda de produção do estabelecimento, destinada à Zona Franca de Manaus ou Áreas de Livre Comércio;
- 2204 - Devolução de venda de mercadoria adquirida ou recebida de terceiros, destinada à Zona Franca de Manaus ou Áreas de Livre Comércio;
- 2208 - Devolução de produção do estabelecimento, remetida em transferência;
- 2209 - Devolução de mercadoria adquirida ou recebida de terceiros, remetida em transferência;
- 2410 - Devolução de venda de produção do estabelecimento em operação com produto sujeito ao regime de substituição tributária;
- 2411 - Devolução de venda de mercadoria adquirida ou recebida de terceiros em operação com mercadoria sujeita ao regime de substituição tributária;
- 2553 - Devolução de venda de bem do ativo imobilizado;
- 2660 - Devolução de venda de combustível ou lubrificante destinado à industrialização subsequente;
- 2661 - Devolução de venda de combustível ou lubrificante destinado à comercialização;
- 2662 - Devolução de venda de combustível ou lubrificante destinado a consumidor, ou usuário final;
- 2918 - Devolução de mercadoria remetida em consignação mercantil ou industrial;
- 2919 - Devolução simbólica de mercadoria vendida ou utilizada em processo industrial, remetida anteriormente em consignação mercantil ou industrial.

Ainda na aba A0, nos campos de Valores do ICMS/ST FCP referente aos vencimentos, serão inseridas informações das notas fiscais emitidas com ICMS de Partilha no Período para UF do EC-87/15, dado que, estas são as Operações e prestações que se destinam a bens e serviços do consumidor final não contribuinte do ICMS localizado em outra unidade federal.

O registro a ser gerado na aba **"A2"**, ocorrerá caso os lançamentos de Ressarcimentos do documento de entrada das notas de entrada sejam informados no campo **"Valor do ICMS-ST de ressarcimento"** do Registro A0, dado que, devem ser consideradas operações com ICMS-ST e/ou FCP-ST com o CFOP 2603.

Digite um valor no campo **"Crédito para o período seguinte"**, quando o resultado da seguinte fórmula for positiva:

(ICMS de Devoluções de Mercadorias + ICMS de Ressarcimentos + Total do ICMS-ST a Recolher) - (ICMS Retido por ST  + Repasse – ICMS Retido por Refinarias/Complementos)

Você preencherá o campo **"Total do ICMS-ST a Recolher"**, se a marcação **"ICMS/ST e FCP é declarado junto"** estiver habilitada. Caso o ICMS-ST e o ICMS-ST FCP forem gerados separadamente, informe no campo, somente o valor do ICMS-ST.

Os campos **"Informação complementar - 1"**, **"Informação complementar - 2"** e **"Informação complementar - 1"** podem possuir até 60 caracteres.

O preenchimento da aba **"A3"**, ocorrerá quando houverem operações de transferência com ICMS-ST para unidades do mesmo grupo de outro Estado da UF Favorecida quando a marcação **"Efetuou Transferências para UF Favorecida"** for realizada, considerando ainda, as operações de ICMS-ST e/ou FCP-ST executadas com um dos seguintes CFOP's:

- 6151 - Transferência de produção do estabelecimento;
- 6152 - Transferência de mercadoria adquirida ou recebida de terceiros;
- 6153 - Transferência de energia elétrica;
- 6155 - Transferência de produção do estabelecimento, que não deva por ele transitar;
- 6156 - Transferência de mercadoria adquirida ou recebida de terceiros, que não deva por ele transitar;
- 6408 - Transferência de produção do estabelecimento em operação com produto sujeito ao regime de substituição tributária;
- 6409 - Transferência de mercadoria adquirida ou recebida de terceiros em operação com mercadoria sujeita ao regime de substituição tributária;
- 6552 - Transferência de bem do ativo imobilizado;
- 6557 - Transferência de material de uso ou consumo;
- 6658 - Transferência de combustível ou lubrificante de produção do estabelecimento;
- 6659 - Transferência de combustível ou lubrificante adquirido, ou recebido de terceiro.

O campo **"Repasse – ICMS Retido por Refinarias/Complementos"** será preenchido pela refinaria de petróleo que efetuar o cálculo de repasse conforme relatórios recebidos de distribuidoras de combustíveis, importador e Transportador Revendedor Retalhista - TRR, em relação às operações com impostos que tenham sido anteriormente retido por outros contribuintes, ou o imposto tenha sido retido por refinaria de petróleo ou suas bases, mas que tenham sido inicialmente objeto de glosa, parcial ou total pela unidade federada devedora, sendo que, posteriormente, a glosa será revertida em favor da unidade federada credora nos termos definidos em Convênio.

Se você preencher pelo menos um dos campos pertinentes aos Valores do ICMS-ST Referente ao Vencimento, é necessário informar também a sua Data do Vencimento do ICMS-ST. Por exemplo, ao inserir um valor no campo **"Valor do ICMS-ST Referente ao 1º Vencimento"**, preencha a **"Data do 1º Vencimento do ICMS-ST"**.

O valor inserido no campo **"Pagamentos Antecipados (ST)"**, só será considerado na apuração se no campo **"Tipo Apuração"** da tela Obrigações do ICMS e ICMS ST a Recolher, for definido com a opção **"ICMS FCP"** ou **"ICMS ST FCP"**e no campo **"Código"**, uma das opções **"Antecipação do diferencial de alíquota do ICMS"**, **"Antecipação do ICMS da importação"** ou **"Antecipação tributária"**da mesma tela, for selecionada.

No processamento da geração dos registros, temos algumas particularidades. Observe:

- Se houver alguma alteração ou inserção de informações em algum campo registro A0 depois de realizar o processamento, caso você efetue o reprocessamento, os campos da aba serão limpos, pois o sistema buscará novamente a informação no sistema.
- Em relação aos campos dos registros A1, A2, A3 e A4, ao efetuar alguma alteração ou inserção manual, estas permanecerão depois do processamento. Nesse caso, se necessário, você deverá corrigir os valores na aba A0 manualmente antes do reprocessamento, do contrário, haverá erro na validação.

**Observação:** todos os valores gerados a partir dos campos da GIA-ST, referem-se às operações com produtos sujeitos ao ICMS-ST para outros Estados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST#top)

## Aba Configurações

Na aba Configurações, marque as opções que se enquadram com a Empresa selecionada, conforme abaixo:

No campo **"Declarante"**, ao assinalar a opção **"Contador"**, você deverá cadastrá-lo na aba [Contador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abacontador) da tela [Contabilidade > Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa). Caso selecione a opção **"Signatário"**, efetue o seu cadastro na aba [Signatários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abasignatrios) da tela Contabilidade > Empresa.

**Nota:** o campo **"Signatário"** será apresentado se a opção de mesmo nome for definida no campo acima. Além disso, serão filtrados nesse campo somente os Signatários que estiverem com a marcação **"Responsável Legal da empresa junto a RFB"**, da aba Signatário da tela Contabilidade > Empresa selecionada.

Referente ao campo **"Tipo Movimento"**, você poderá selecionar uma dentre as seguintes opções:

- **Substituição:** Por meio dessa, a linha 7 do documento será definida com **"N"** e a linha 8, com **"S"**;
- **Normal:** Nesta, a linha 7 e 8 serão geradas com **"N"**;
- **Sem movimento:**  Se essa opção for definida, a linha 7 será gerada com **"S"** e a 8 com **"N"**.

Habilite a marcação **"Houve transferências para filial"**, se houverem transferências do sujeito passivo por Substituição Tributária, sendo ela localizada na unidade federativa favorecida em relação aos produtos sujeitos à Substituição Tributária.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST#top)

## Botões da tela

Por meio do botão ![Imagem 3: Por meio do botão "Processar" , o sistema irá buscar e preencher os valores cada Aba/Registro, sendo que,…](https://ajuda.sankhya.com.br/hc/article_attachments/16313319441943) **"Processar"**, o sistema irá buscar e preencher os valores cada Aba/Registro, sendo que, posteriormente, você poderá realizar a conferência, validação e complemento de informações necessárias nos registros.

Quando você clicar no botão ![Imagem 4: Quando você clicar no botão "Gerar" , o sistema irá gerar um arquivo txt em uma pasta padrão selecionada no seu…](https://ajuda.sankhya.com.br/hc/article_attachments/16313319444759) **"Gerar"**, o sistema irá gerar um arquivo txt em uma pasta padrão selecionada no seu computador.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008984922-Gera%C3%A7%C3%A3o-do-arquivo-GIA-ST#top)
