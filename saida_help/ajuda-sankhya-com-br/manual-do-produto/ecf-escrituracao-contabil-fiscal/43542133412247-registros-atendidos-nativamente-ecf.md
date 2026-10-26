---
id: "43542133412247"
titulo: "Registros atendidos nativamente - ECF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43542133412247-Registros-atendidos-nativamente-ECF"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > ECF (Escrituração Contábil Fiscal)"
atualizado_em: "2026-09-16T19:21:57Z"
---

# Registros atendidos nativamente - ECF

Este artigo apresenta o **mapa de registros da ECF – Escrituração Contábil Fiscal**, organizado por bloco e na mesma sequência em que os registros aparecem no arquivo digital. Use-o como referência rápida para identificar a que informação cada registro corresponde, conferir se a escrituração do ano-calendário contém os registros esperados e localizar a origem de uma inconsistência apontada na validação do arquivo.

A ECF substituiu a DIPJ e é onde se apuram o **IRPJ** e a **CSLL**. Sua estrutura começa pela abertura e pelos parâmetros de tributação (**Bloco 0**), passa pelo plano de contas e seu mapeamento para o referencial (**Bloco J**) e pelos saldos contábeis recuperados da ECD (**Bloco K**), segue pelo e-Lalur e e-Lacs (**Bloco M**) e pelos blocos de cálculo específicos de cada forma de tributação (**N**, **P**, **T** e **U**), terminando nas declarações e informações complementares (**Blocos Q, V, W, X e Y**) e no encerramento do arquivo (**Bloco 9**).

**Observação:** nem todos os blocos abaixo são gerados em todas as escriturações. Os blocos de cálculo são mutuamente exclusivos e seguem a forma de tributação informada no registro 0010 — **N** para o Lucro Real, **P** para o Lucro Presumido, **T** para o Lucro Arbitrado e **U** para as imunes e isentas. Os blocos **V** (DEREX) e **W** (Declaração País-a-País) só se aplicam às empresas enquadradas nessas obrigações.

| Bloco | Registro | Descrição |
| --- | --- | --- |
| **Bloco 0** Abertura, Identificação e Referências | **0000** | Abertura do Arquivo Digital e Identificação da Pessoa Jurídica |
| **0001** | Abertura do Bloco 0 |
| **0010** | Parâmetros de Tributação |
| **0020** | Parâmetros Complementares |
| **0021** | Parâmetros de Identificação dos Tipos de Programa |
| **0030** | Dados Cadastrais |
| **0035** | Identificação das SCP |
| **0930** | Identificação dos Signatários da ECF |
| **0990** | Encerramento do Bloco 0 |
| **Bloco J** Plano de Contas e Mapeamento | **J001** | Abertura do Bloco J |
| **J050** | Plano de Contas do Contribuinte |
| **J051** | Plano de Contas Referencial |
| **J100** | Centro de Custos |
| **J990** | Encerramento do Bloco J |
| **Bloco K** Saldos das Contas Contábeis e Referenciais | **K001** | Abertura do Bloco K |
| **K030** | Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário |
| **K155** | Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período) |
| **K156** | Mapeamento Referencial do Saldo |
| **K355** | Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento |
| **K356** | Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento |
| **K990** | Encerramento do Bloco K |
| **Bloco M** Livro Eletrônico de Apuração do Lucro Real (e-Lalur) e Livro Eletrônico de Apuração da Base de Cálculo da CSLL (e-Lacs) | **M001** | Abertura do Bloco M |
| **M030** | Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real |
| **M300** | Demonstração do Lucro Real – Lançamentos da Parte A do e-Lalur |
| **M310** | Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lalur |
| **M312** | Números dos Lançamentos Relacionados à Conta Contábil |
| **M990** | Encerramento do Bloco M |
| **Bloco N** Cálculo do IRPJ e da CSLL – Lucro Real | **N001** | Abertura do Bloco N |
| **N990** | Encerramento do Bloco N |
| **Bloco P** Lucro Presumido | **P001** | Abertura do Bloco P |
| **P990** | Encerramento do Bloco P |
| **Bloco Q** Livro Caixa | **Q001** | Abertura do Bloco Q |
| **Q990** | Encerramento do Bloco Q |
| **Bloco T** Lucro Arbitrado | **T001** | Abertura do Bloco T |
| **T990** | Encerramento do Bloco T |
| **Bloco U** Imunes e Isentas | **U001** | Abertura do Bloco U |
| **U990** | Encerramento do Bloco U |
| **Bloco V** Declaração DEREX | **V001** | Abertura do Bloco V |
| **V990** | Encerramento do Bloco V |
| **Bloco W** Declaração País-a-País (Country-by-Country Report) | **W001** | Abertura do Bloco W |
| **W990** | Encerramento do Bloco W |
| **Bloco X** Informações Econômicas | **X001** | Abertura do Bloco X |
| **X990** | Encerramento do Bloco X |
| **Bloco Y** Informações Gerais | **Y001** | Abertura do Bloco Y |
| **Y990** | Encerramento do Bloco Y |
| **Bloco 9** Encerramento do Arquivo Digital | **9001** | Abertura do Bloco 9 |
| **9900** | Registros do Arquivo |
| **9990** | Encerramento do Bloco 9 |
| **9999** | Encerramento do Arquivo Digital |
