---
id: "42426494698775"
titulo: "DCTF Cruzamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426494698775-DCTF-Cruzamentos"
trilha: "ASIS: Auditoria e validação de erros fiscais > Perguntas Frequentes > Guia de uso Kolossus"
atualizado_em: "2026-08-03T12:20:21Z"
rotulos: ["asis", "sync_hc", "asis_52941269448723", "sync_hash_349ccd04d3f3"]
---

# DCTF Cruzamentos

A Receita Federal do Brasil (RFB) realiza periodicamente, uma série de cruzamentos automatizados com a sua base de dados, a fim de estimular a conformidade tributária das pessoas jurídicas.

Sendo assim, todas as obrigações acessórias transmitidas ao fisco são utilizadas para comparação de dados com o objetivo de identificar possíveis créditos tributários.

A DCTF é a declaração mais utilizada para cruzamento de informações da pessoa jurídica, realizando confronto de  dados da DCTF com as demais obrigações acessórias as quais os contribuintes estão sujeitos, pode-se verificar inconsistências das mais diversas ordens, inclusive, indícios de omissão de receitas.

Neste contexto é possível entender a importância do cruzamento de informações entre a DCTF e as demais obrigações acessórias, para evitar malha e outros controles fiscais, chamando a atenção do Fisco.

Na plataforma Kolossus,  é possível efetuar os seguintes cruzamentos:

**DCTF VS ECAC**

Neste cruzamento é possível identificar se os débitos informados na DCTF foram pagos, para tanto é utilizado o arquivo DCTF e os comprovantes de arrecadação de DARF disponíveis no ECAC.

Por este cruzamento é possível:

-  Identificar os débitos declarados na DCTF que possuem vinculação de pagamento   sem efetiva correspondência de pagamento no e-CAC, sendo possível identificar débitos declarados e ainda não recolhidos ( Regra 2899);

- Identificar pagamentos no e-CAC que não possuem vinculação na DCTF, sendo possível identificar possíveis pagamentos a maior (Regra 2899);

- Identificar  divergência na data de vencimento informada na ficha Pagamentos da DCTF e no DARF recolhido pelo relatório do ECAC (Regra 2901);

-Emitir relatório analítico de pagamentos na DCTF e ECAC e ainda relatório com comparação dos débitos pagos e declarados (Regras: 2897; 2898; 2896).

**DCTF VS PERDCOMP**

Esse cruzamento é utilizado para analisar- se as informações que constam na DCTF referente à compensação por PERDCOMP, conferem com o PERDCOMP transmitido, esta análise é importante para evitar divergência e equívocos na declaração da compensação.

Por este cruzamento é possível:

-  Identificar débito declarados na DCTF, vinculados a compensação sem efetiva correspondência no PERDCOMP. (Regra 2977);

- Emitir relatório analítico de débitos compensados informados na DCTF e com PERDCOMP transmitido, e ainda relatório comparativo de débitos compensados informados em ambas as declarações.

**DCTF vs ECAC vs PERDCOMP**

Por este cruzamento é possível ter uma visão mais clara dos débitos declarados e a quitação do mesmo, seja por pagamento ou compensação.

Por este cruzamento é possível:

-   Identificar débitos declarados na DCTF que não foram encontrados na relação de  DARFS recolhidos e DARFs recolhidos não escrituradas na DCTF( Regra 3784);

- Identificar  débitos declarados na DCTF que não foram encontrados no PER\_DCOMP e a PER\_DCOMPS não escrituradas na DCTF( Regra 3785);

- Relatório comparativo com valores declarados na DCTF, PERDCOMP e recolhimento de DARF, por código de receita (Regra 3267).

**DIRF vs DCTF**

Esse cruzamento tem o objetivo de validar se as retenções informadas na DIRF foram declaradas como débito na DCTF, assim é possível confirmar se as retenções foram declaradas na DCTF evitando chamar atenção do Fisco.

Por este cruzamento é possível:

- Emitir relatório analítico por códigos de receita, relacionando os débitos  que não foram apresentados na DCTF ou DIRF, vice versa (Regra 2814);

- Relatório de validação dos valores declarados na DCTF e DIRF por código de receita  (Regra 2803);

- Emitir relatórios analíticos dos débitos informados na DCTF e DIRF ( Regra 2804 e 2805);

-Validação de pagamento de retenção. (Regra 3025)

**ECF vs DCTF**

Divergência entre a DCTF e ECF é facilmente identificada pela Receita Federal.

Por este cruzamento é possível:

- Emitir relatório comparativo de valores escriturados na ECF referente a IRPJ, CSLL,  IRRF,CIDE, IOF; PIS, COFINS, IOF, IPI    com o valor total informado na DCTF referente ao grupo de tributo correspondente para o mesmo período.

**EFD- Contribuições vs DCTF**

Esse cruzamento tem o objetivo de validar se os valores de PIS e COFINS apurados na EFD-Contribuições foram declarados na DCTF.

Por este cruzamento é possível:

-Emitir relatório analítico por códigos de receita, relacionando os débitos que não foram apresentados na EFD contribuições e DCTF, vice-versa (Regra 2893);

-  Emitir relatório comparativo dos valores de PIS e COFINS informados na EFD-contribuições e DCTF ( Regras 2890 e 2892).

**SPED FISCAL vs DCTF**

Esse cruzamento tem o objetivo de validar  o IPI apurado no Sped Fiscal com o declarado na DCTF.

Por este cruzamento é possível:

- Confrontar valor de IPI a recolher apurado no Sped Fiscal  e o declarado na DCTF (Regra 2887);

- Relatórios analíticos com os valores totais de IPI  no Sped Fiscal a recolher e  relatório com os valores declarados na DCTF ( Regra 2888 e 2889);

- Análise de ausência de escrituração na DCTF ( 3052).

Para os cruzamentos com obrigações anuais, é necessário que a plataforma tenha os arquivos de todas as DCTFs do período.
