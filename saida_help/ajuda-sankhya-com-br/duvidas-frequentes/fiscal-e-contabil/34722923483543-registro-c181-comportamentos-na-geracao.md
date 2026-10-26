---
id: "34722923483543"
titulo: "Registro C181 – Comportamentos na geração do SPED Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34722923483543-Registro-C181-Comportamentos-na-gera%C3%A7%C3%A3o-do-SPED-Fiscal"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:26:47Z"
rotulos: ["Configuração", "Impostos", "EFD", "SPED Fiscal", "geração do SPED Fiscal", "(UF)7xx", "Registro C181", "Comportamentos na geração do SPED Fiscal", "Informações Complementares das Operações de Devolução de Saídas de Mercadorias Sujeitas à Substituição Tributária (ICMS-ST)", "(UF)600", "ICMS-ST"]
---

# Registro C181 – Comportamentos na geração do SPED Fiscal

Na escrituração do **Registro C181 – Informações Complementares das Operações de Devolução de Saídas de Mercadorias Sujeitas à Substituição Tributária (ICMS-ST)**, podem ser observados dois comportamentos distintos na aplicação, a depender do código de ajuste utilizado.

Este registro é responsável por detalhar operações de devolução em que houve ressarcimento ou estorno de valores de ICMS-ST, garantindo a consistência das informações transmitidas ao **SPED Fiscal (EFD ICMS/IPI)**.

### Comportamento 1 – Códigos iniciados por (UF)7xx

Quando são utilizados **códigos de ajuste iniciados por (UF)7xx** (como o (UF)713, vinculado ao (UF)213), o sistema realiza:

- O **cálculo correto do estorno** do ICMS-ST;
- O **preenchimento automático dos campos** do registro C181, incluindo a aplicação da fórmula definida no Guia Prático da EFD ICMS/IPI:

```
Campo 13 + Campo 14 – Campo 17 = Campo 20
```

(1)** Ou seja:**
VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA + VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA – VL\_UNIT\_ICMS\_OP\_CONV\_SAIDA = VL\_UNIT\_ICMS\_ST\_CONV\_COMPL

### Comportamento 2 – Código de ajuste (UF)600

Já, quando é utilizado o **código de ajuste (UF)600**, aplicável em operações de devolução com estorno de ressarcimento, o sistema não executa o mesmo comportamento observado nos códigos (UF)7xx:

- O cálculo de estorno não é realizado automaticamente.
- Os campos esperados do registro C181 não são preenchidos conforme código iniciados com 7.

### Parametrização e Origem dos Códigos

Os códigos de ajuste, como o (UF)600 ou os iniciados por (UF)7xx, não são informados diretamente pelo usuário. Eles têm origem na **tabela 5.7 – Códigos de Motivos de Restituição e Complementação ICMS ST**, onde estão cadastrados os respectivos motivos e seus ajustes relacionados.

Essa parametrização deve ser feita na tela **“Códigos de Motivos de Restituição e Complementação ICMS ST”**, garantindo a correta aplicação das naturezas de operação e o reflexo adequado nos registros fiscais.
