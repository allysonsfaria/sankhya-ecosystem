---
id: "43541824013719"
titulo: "Registros atendidos nativamente - ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43541824013719-Registros-atendidos-nativamente-ECD"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > ECD"
atualizado_em: "2026-09-16T18:29:39Z"
---

# Registros atendidos nativamente - ECD

Este artigo apresenta o **mapa de registros da ECD – Escrituração Contábil Digital**, organizado por bloco e na mesma sequência em que os registros aparecem no arquivo digital. Use-o como referência rápida para identificar a que informação cada registro corresponde, conferir se a escrituração do período contém os registros esperados e localizar a origem de uma inconsistência apontada na validação do arquivo.

A ECD substitui a escrituração em papel do Diário, do Razão e dos livros auxiliares, e sua estrutura segue a ordem do leiaute: abertura, identificação e cadastro de participantes (**Bloco 0**), plano de contas, saldos e lançamentos contábeis (**Bloco I**), demonstrações contábeis, termos e signatários (**Bloco J**) e controle e encerramento do arquivo (**Bloco 9**).

**Observação:** nem todos os registros abaixo são gerados em todas as escriturações. A presença de cada um depende do tipo de escrituração contábil (livro Diário, Diário com Escrituração Resumida, Razão Auxiliar, entre outros), das características da empresa e das configurações adotadas. Os registros **J801** e **J932**, por exemplo, só se aplicam quando a ECD é transmitida em substituição a uma escrituração anterior.

| Bloco | Registro | Descrição |
| --- | --- | --- |
| **Bloco 0** Abertura, Identificação e Referências | **0000** | Abertura do Arquivo Digital e Identificação do Empresário ou da Sociedade Empresária |
| **0001** | Abertura do Bloco 0 |
| **0007** | Outras Inscrições Cadastrais da Pessoa Jurídica |
| **0020** | Escrituração Contábil Descentralizada |
| **0035** | Identificação das SCP |
| **0150** | Tabela de Cadastro do Participante |
| **0180** | Identificação do Relacionamento com o Participante |
| **0990** | Encerramento do Bloco 0 |
| **Bloco I** Lançamentos Contábeis | **I001** | Abertura do Bloco I |
| **I010** | Identificação da Escrituração Contábil |
| **I012** | Livros Auxiliares ao Diário ou Livro Principal |
| **I015** | Identificação das Contas da Escrituração Resumida a que se Refere a Escrituração Auxiliar |
| **I030** | Termo de Abertura do Livro |
| **I050** | Plano de Contas |
| **I051** | Plano de Contas Referencial |
| **I052** | Indicação dos Códigos de Aglutinação |
| **I075** | Tabela de Histórico Padronizado |
| **I100** | Centro de Custos |
| **I150** | Saldos Periódicos – Identificação do Período |
| **I155** | Detalhe dos Saldos Periódicos |
| **I157** | Transferência de Saldos de Plano de Contas Anterior |
| **I200** | Lançamento Contábil |
| **I250** | Partidas do Lançamento |
| **I350** | Saldo das Contas de Resultado Antes do Encerramento – Identificação da Data |
| **I355** | Detalhes dos Saldos das Contas de Resultado Antes do Encerramento |
| **I990** | Encerramento do Bloco I |
| **Bloco J** Demonstrações Contábeis | **J001** | Abertura do Bloco J |
| **J005** | Demonstrações Contábeis |
| **J100** | Balanço Patrimonial |
| **J150** | Demonstração do Resultado do Exercício (DRE) |
| **J210** | DLPA – Demonstração de Lucros ou Prejuízos Acumulados / DMPL – Demonstração de Mutações do Patrimônio Líquido |
| **J215** | Fato Contábil que Altera a Conta Lucros Acumulados, a Conta Prejuízos Acumulados ou Todo o Patrimônio Líquido |
| **J800** | Outras Informações |
| **J801** | Termo de Verificação para Fins de Substituição da ECD |
| **J900** | Termo de Encerramento |
| **J930** | Signatários da Escrituração |
| **J932** | Signatários do Termo de Verificação para Fins de Substituição da ECD |
| **J935** | Identificação dos Auditores Independentes |
| **J990** | Encerramento do Bloco J |
| **Bloco 9** Controle e Encerramento do Arquivo Digital | **9001** | Abertura do Bloco 9 |
| **9900** | Registros do Arquivo |
| **9990** | Encerramento do Bloco 9 |
| **9999** | Encerramento do Arquivo Digital |
