---
id: "37369313307159"
titulo: "Lançamento Contábil Extemporâneo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37369313307159-Lan%C3%A7amento-Cont%C3%A1bil-Extempor%C3%A2neo"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:12:52Z"
rotulos: ["Configuração", "ECD", "Ocorrências", "Contabilização", "Financeiro", "Lançamento Contábil Extemporâneo", "manter a data real do fato gerado", "inclusão do lançamento contábil", "SPED Contábil", "Extemporâneo"]
---

# Lançamento Contábil Extemporâneo

O **lançamento contábil extemporâneo** é utilizado quando o fato contábil ocorreu em um período anterior, mas o registro no sistema é feito em um mês posterior, geralmente porque o período original já foi fechado.

Esse recurso permite **manter a data real do fato gerado**, sem precisar reabrir o mês contábil.

#### Cenários de Uso

Use o lançamento extemporâneo em situações como:

- **Identificação tardia** de fatos contábeis
- **Ajustes ou correções** após o fechamento do mês
- **Lançamentos necessários** para atendimento de auditoria
- **Regularização de informações** antes da geração da ECD

#### Procedimento:

##### Para registrar um lançamento contábil extemporâneo, siga o passo a passo abaixo:

##### **(1)** Acesse a tela ''Lançamentos Contábeis'' (Contabilidade » Arquivos » Lançamentos contábeis).

##### **(2)**Clique em ''+'' (Novo Lançamento) para criar um novo lançamento.

- Será aberto o **pop-up para inclusão do lançamento contábil**

**(3)** No pop-up, preencha os dados do lançamento:

- Empresa
- Conta Débito
- Conta Crédito
- Valor
- Histórico
- **Data de Movimento** (data contábil em que o lançamento será registrado)

Até este ponto, o preenchimento é idêntico a um lançamento comum.

**(4)** Marque o lançamento como **''Extemporâneo''**.

- Ao selecionar essa opção, o sistema habilita automaticamente o campo **''Dt. Ocorrência Extem''**.

![Imagem 1: Ao selecionar essa opção, o sistema habilita automaticamente o campo '' Dt. Ocorrência Extem'' .](https://ajuda.sankhya.com.br/hc/article_attachments/37403985211927)

**(5)** No campo **''Dt. Ocorrência Extem.''**, registre a data em que o fato contábil realmente ocorreu.

#### Exemplo Prático

##### Datas informadas no lançamento

- **Data de Movimento:** 01/12/2025
- **Dt. Ocorrência Extemporânea:** 01/11/2025

Neste cenário:

- O lançamento é **registrado contabilmente em dezembro**
- O **fato contábil pertence ao mês de novembro**, já encerrado

Por isso, o lançamento deve ser marcado como **extemporâneo**.

#### Comportamento do Sistema

Mesmo com a **Data de Movimento em dezembro**, o sistema:

- Mantém o lançamento no período atual
- **Registra a data real do fato** através da Dt. Ocorrência Extemporânea
- Utiliza essa data para fins de **escrituração digital**

#### Reflexo na ECD (SPED Contábil)

Ao gerar a **ECD**, o sistema considera a **Data de Ocorrência Extemporânea**, e não a data de movimento do lançamento.

**Exemplo de registros gerados na ECD:**

```
|I200|0020111202400000100|01112024|3000,00|N||
|I250|03.03.01.04.00038||1500,00|D|123||||
|I250|03.01.01.01.00002||1500,00|C|123||||
```

#####

##### Interpretação

- **Registro I200**

  - Data do lançamento: **01/11/2024**
  - Valor total: **3.000,00**
  - Indicador de lançamento normal (`N`)
- **Registro I250**

  - Contas de débito e crédito
  - Valores equilibrados
  - Preserva a integridade do lançamento contábil

**OBSERVAÇÃO**: Mesmo que o lançamento tenha sido feito em dezembro, a ECD será escriturada com a data de **novembro**, pois esta é a data real do fato contábil.

**INFORMAÇÕES ADICIONAIS:** O lançamento extemporâneo será refletido na ECD no período da ocorrência, sem a necessidade de reabrir o mês contábil. Essa abordagem garante aderência às regras do SPED Contábil e mantém a rastreabilidade necessária para auditoria e fiscalização.
