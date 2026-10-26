---
id: "360043862594"
titulo: "Como ajustar 'Natureza da Operação' impressa no DANFE?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043862594-Como-ajustar-Natureza-da-Opera%C3%A7%C3%A3o-impressa-no-DANFE"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-09-02T18:20:36Z"
rotulos: ["Configuração", "NF-e", "DANFE", "CFOP", "natureza", "operação", "naturezadaoperação", "\"Natureza da Operação\" não está de acordo", "Ajustar 'Natureza da Operação' DANFE", "Verificar CFOP utilizado", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Como ajustar 'Natureza da Operação' impressa no DANFE?

**SITUAÇÃO:**

Ao imprimir o DANFE, o campo Natureza da Operação pode apresentar uma descrição diferente da esperada.

Esse comportamento depende da configuração da TOP e da descrição do CFOP utilizado na nota fiscal.

![Imagem 1: Esse comportamento depende da configuração da TOP e da descrição do CFOP utilizado na nota fiscal.](https://ajuda.sankhya.com.br/hc/article_attachments/360099281033)

O DANFE segue a seguinte prioridade:

1. **Natureza da Operação (SPED)** informada na TOP (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) → essa descrição será impressa no DANFE.
2. Caso o campo esteja em branco, o sistema utilizará a **Descrição do CFOP** do lançamento.

**SOLUÇÃO:**

Para ajustar a descrição do CFOP:

Identifique qual o CFOP utilizado no respectivo lançamento;

Sintonize com o contador se o código CFOP está correto. Para ajuste da descrição, acesse a tela **"CFOP"** (Comercial >> Arquivo >> Cadastros);

Localize o CFOP utilizado e ajuste o campo **"Descrição"** conforme esperado.

**IMPORTANTE:**

- O ajuste será válido para as próximas emissões. Caso precise, cancele a NF-e indevida e refaça o faturamento;
- Se na mesma nota existir mais de um CFOP, será considerada a descrição do nItem 1.
