---
id: "360044600654"
titulo: "Processo Geração dos Registros do DIFAL no EFD (Sped Fiscal)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-10-16T16:40:59Z"
rotulos: ["Registros", "Fiscal", "DIFAL", "Geração", "Ajuste da Apuração de ICMS e ICMS ST", "Registro de Apuração do ICMS", "Geração ICMS/IPI", "Sped Fiscal", "Geração do EFD (Sped Fiscal) - Registros do DIFAL manual", "ICMS", "Impostos", "EFD", "Guia da EFD para Emenda Constitucional 87/2015"]
---

# Processo Geração dos Registros do DIFAL no EFD (Sped Fiscal)

**Módulo:** Livros Fiscais

**Telas envolvidas:** [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953) · [Registro de Apuração do ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153) · Ajuste da Apuração de ICMS e ICMS ST

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal#oque)
- [Registros incluídos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal#registros)
- [Como a apuração é gravada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal#apuracao)
- [Tipos de apuração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal#tipos)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal#atencao)

## O que é e para que serve

A **Emenda Constitucional nº 87/2015** trata das alterações do ICMS para operações interestaduais destinadas ao consumidor final não contribuinte do imposto — a sistemática de cobrança sobre a circulação de mercadorias e sobre prestações de serviços de transporte interestadual e intermunicipal e de comunicação que destinem bens e serviços a consumidor final. Em 06/01/2016 foi publicado o novo Guia da EFD, com o detalhamento das especificações técnicas do **Ato Cotepe ICMS nº 61, de 30 de dezembro de 2015**.

Para atender a essa emenda, foram incluídos os registros do Diferencial de Alíquota (DIFAL) no EFD ICMS/IPI e passou a ser obrigatória a abertura e o fechamento dos registros do Bloco K. Este artigo explica como o sistema apura e grava o ICMS DIFAL e o ICMS FCP para a geração do arquivo.

---

## Registros incluídos

Para atender à EC 87/2015 foram incluídos os registros `C101`, `D101`, `E300`, `E310`, `E311`, `E312`, `E313` e `E316`, além da obrigatoriedade de **Abertura** e **Fechamento** dos registros do **Bloco K**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal#sumario)

---

## Como a apuração é gravada

O processo segue três etapas encadeadas:

1. Lance as notas fiscais da empresa nos **Portais**.
2. Gere o Livro Fiscal na tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953) — os dados são salvos na tabela `TGFLIV`.
3. Realize a apuração do ICMS da empresa no período na tela [Registro de Apuração do ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153) — os dados são gravados na tabela `TGFAJA`.

A gravação na `TGFAJA` distingue o tipo de imposto pelos campos `CODUF` e `TIPIMPOSTO`:

| **Imposto** | **CODUF** | **TIPIMPOSTO** | **Gravação** |
| --- | --- | --- | --- |
| ICMS (normal) | 0 | C | Apuração geral; a UF não é considerada. |
| ICMS DIFAL | UF específica | D | Gravado por UF. |
| ICMS FCP | UF específica | F | Gravado por UF. |

No exemplo abaixo, a apuração do ICMS é gravada de forma geral, com `CODUF = 0` e `TIPIMPOSTO = 'C'`:

![Registros da tabela TGFAJA com a apuração do ICMS gravada com CODUF igual a 0 e TIPIMPOSTO igual a C](https://ajuda.sankhya.com.br/hc/article_attachments/8983240370967)

Apuração do ICMS na TGFAJA. Captura: 03/2023

Para o ICMS DIFAL (`TIPIMPOSTO = 'D'`), os registros são salvos por UF — no exemplo, para as UFs `1` (SP) e `2` (MG):

![Registros da tabela TGFAJA com a apuração do ICMS DIFAL gravada separadamente para as UFs 1 (SP) e 2 (MG)](https://ajuda.sankhya.com.br/hc/article_attachments/8983483273623)

Apuração do ICMS DIFAL por UF na TGFAJA. Captura: 03/2023

O ICMS FCP (`TIPIMPOSTO = 'F'`) segue a mesma lógica. No exemplo, não houve cálculo do Fundo de Combate à Pobreza para a UF `1` (SP), somente para a UF `2` (MG):

![Registros da tabela TGFAJA com a apuração do ICMS FCP gravada apenas para a UF 2 (MG)](https://ajuda.sankhya.com.br/hc/article_attachments/8983537638295)

Apuração do ICMS FCP por UF na TGFAJA. Captura: 03/2023

**ℹ️ Nota**

O sistema conta com a Apuração para o DIFAL; para a geração dos dados, deve-se seguir o processo já existente.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal#sumario)

---

## Tipos de apuração

Os tipos de apuração gravados na `TGFAJA` são:

1. Saídas com Débito do Imposto
2. Outros débitos
3. Estorno de créditos
4. Total Débitos
5. Entradas com Crédito do Imposto
6. Outros créditos
7. Estorno de débitos
8. Sub Total
9. Saldo Credor do Período Anterior
10. Total Créditos
11. SALDO DEVEDOR (Débito - Crédito)
12. Deduções do imposto apurado
13. IMPOSTO A RECOLHER
14. SALDO CREDOR (Crédito - Débito) a Transportar
15. Saldo Credor Produzir do Período Anterior

A tela [Registro de Apuração do ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153) grava automaticamente os tipos 1, 4, 5, 8, 9, 10, 11, 13, 14 e 15. Os tipos 2, 3, 6, 7 e 12, além dos tipos **100 - Débito especial** e **101 - Controle do ICMS extra-apuração**, são inseridos pela tela **Ajuste da Apuração de ICMS e ICMS ST**.

Para o ICMS DIFAL e o ICMS FCP são gravados os mesmos tipos de apuração acima, com exceção do tipo **15 - Saldo Credor Produzir do Período Anterior**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654-Processo-Gera%C3%A7%C3%A3o-dos-Registros-do-DIFAL-no-EFD-Sped-Fiscal#sumario)

---

## Pontos de atenção

- A distinção do imposto na `TGFAJA` é feita pelo par `CODUF`/`TIPIMPOSTO`: ICMS normal grava com `CODUF = 0` e `TIPIMPOSTO = 'C'`; DIFAL e FCP gravam por UF, com `'D'` e `'F'` respectivamente.
- DIFAL e FCP não gravam o tipo de apuração **15 - Saldo Credor Produzir do Período Anterior**.
- Os ajustes complementares (outros débitos, estorno de créditos, outros créditos, estorno de débitos, deduções, débito especial e controle do ICMS extra-apuração) são inseridos manualmente pela tela **Ajuste da Apuração de ICMS e ICMS ST**.
- Para o contexto do DIFAL Partilhado, consulte a [Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414).
