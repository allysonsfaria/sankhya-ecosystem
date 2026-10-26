---
id: "14045554294807"
titulo: "Comissão múltipla não gera financeiro na tela Fechamento de Comissão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14045554294807-Comiss%C3%A3o-m%C3%BAltipla-n%C3%A3o-gera-financeiro-na-tela-Fechamento-de-Comiss%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:59:36Z"
rotulos: ["Configuração", "Parceiro", "Comissão", "Financeiro", "Vendedores", "Problema de Geração Financeira na Tela de Fechamento de Comissão", "Comissão múltipla"]
---

# Comissão múltipla não gera financeiro na tela Fechamento de Comissão

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16867765328791) SITUAÇÃO:**

Comissão múltipla não gera financeiro na tela Fechamento de Comissão.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16867758240663)CAUSA:**

Ocorre devido a configurações divergentes.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16867758233239)SOLUÇÃO:**

Verifique as seguintes configurações abaixo:

**(1)** Tela **Vendedores/compradores** (Configurações » Cadastros » Vendedores/Compradores), aba **"Geral"**, campo **"Tipo de fechamento de Comissão":** Financeiro

![Imagem 4: Observações:](https://ajuda.sankhya.com.br/hc/article_attachments/16867765338391) **Observações:**

A configuração do Tipo de Fechamento de Comissão sofre influência quando se usa o parâmetro  **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"**, da seguinte forma:

**"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"** - Ligado: busca o tipo de fechamento na tela **"Fórmula de Comissão",** aba **"Integração"**, campo Tipo de Integração, ou seja, se estiver ligado acesse a tela Fórmula de comissão campo "Tipo de Integração" na aba Integração deve estar marcado como Financeiro.

 **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"** - Desligado: desconsidera a premiação e verifica o parâmetro **"Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"**.

**Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"**. - Ligado: olha no cadastro do vendedor, campo Tipo de fechamento de Comissão, então se não trabalha com premiação basta ligar esse parâmetro para que o financeiro seja gerado.

**Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"**. - Desligado: Não olha o Tipo de fechamento de Comissão e o financeiro não será gerado.
