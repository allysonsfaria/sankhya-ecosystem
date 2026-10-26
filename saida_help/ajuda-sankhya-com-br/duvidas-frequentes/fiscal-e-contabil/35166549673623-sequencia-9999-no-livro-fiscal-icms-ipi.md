---
id: "35166549673623"
titulo: "Sequência 9999 no Livro Fiscal ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35166549673623-Sequ%C3%AAncia-9999-no-Livro-Fiscal-ICMS-IPI"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:25:55Z"
rotulos: ["Configuração", "Importação", "IPI", "ICMS", "TOP", "Livro Fiscal", "Sequência 9999", "Sequência 9999 no Livro Fiscal ICMS/IPI", "diferenças entre os totais da nota (TGFCAB)", "Livro Fiscal ICMS/IPI"]
---

# Sequência 9999 no Livro Fiscal ICMS/IPI

A sequência **9999** é um “alerta” criado automaticamente pelo sistema no **Livro Fiscal ICMS/IPI** sempre que há **diferenças entre os totais da nota (TGFCAB)** e os valores detalhados em itens (**TGFITE**) e impostos rateados (**TGFDIN**).

Ela não representa uma nota fiscal real, mas um registro de inconsistência que precisa ser ajustado.

![Imagem 1: Ela não representa uma nota fiscal real, mas um registro de inconsistência que precisa ser ajustado.](https://ajuda.sankhya.com.br/hc/article_attachments/35546622246423)

A sequência 9999 acontece quando:

- A **Base de ICMS no cabeçalho** não bate com a soma das bases dos itens + Proporcionalização **( aba despesas acessórias da TOP)** de impostos.
- O **Valor Contábil total da nota (VLRNOTA)** não confere com a soma de itens, frete e despesas.
- Alterações manuais foram feitas no cabeçalho sem refletir nos itens.

**SOLUÇÃO:**

**(1)** Realize as seguintes análises:

- Consulte a nota no **TGFCAB** (totais).
- Compare com os itens no **TGFITE**.
- Verifique se houve rateio de frete/despesas no **TGFDIN**.
- Cheque se a soma do **valor contábil calculado = VLRNOTA**.

**(2)** Em seguida, de acordo com as análises, execute uma das soluções abaixo:

- **Corrija rateios:** garantindo que frete e despesas estejam proporcionalizados corretamente.
- **Ajuste cabeçalho:** assegurando que `VLRBASEICMS` e `VLRNOTA` refletem os itens e rateios.

**Exemplo prático**

- **TGFCAB.VLRNOTA** = R$ 8.200,00
- **Itens (TGFITE) + Frete (TGFDIN)** = R$ 8.500,00

O sistema gera a **sequência 9999**.
Para resolver, ajuste o cabeçalho para R$ 8.500,00 e regerar o Livro Fiscal.

**Observação:** **somente para notas de importação, na TOP utilizada,** acesse a aba **"Livro fiscal"** e desative a opção **“Validar Totais da Nota na Geração do Livro?”** (para evitar novas inconsistências).
