---
id: "15413280182167"
titulo: "Não preparado para agrupar contas a receber"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15413280182167-N%C3%A3o-preparado-para-agrupar-contas-a-receber"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:56:59Z"
rotulos: ["Configuração", "Contas", "Parceiro", "Financeiro", "CORE_E00733", "Mensagem: Erro ao agrupar contas a receber.", "Causa: Opção \"Agrupar pagamentos\" marcada indevidamente.", "Solução: Desmarcar \"Agrupar pagamentos\" para tipo de título \"Receita\".", "Erro"]
---

# Não preparado para agrupar contas a receber

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16581963927575) MENSAGEM:**

[CORE\_E00733] Não preparado para agrupar contas a receber.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16581963934743) CAUSA:**

Ocorre ao marcar a opção Agrupar pagamentos para gerar a remessa de títulos de receita.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16581963933975) SOLUÇÃO:**

Para gerar remessa de tipo de título receita, não pode ser marcado a opção **'Agrupar pagamentos"**, visto que ela serve somente para tipo de títulos "Despesa" e que o ideal é marcar as opções **"gerar nosso número"** e **" gerar linha digitável".**

Abaixo temos a documentação do artigo [Geração Arquivo de Remessa - Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es) referente a opção Agrupar Pagamentos.
"**Agrupar Pagamentos:** quando marcada, agrupará títulos de mesmo "Parceiro" e mesmo "Vencimento" para a geração do arquivo de remessa. Ao agrupar os títulos, será registrada no "Financeiro", no campo Nosso Número dos títulos agrupados, a informação: "PG + o Nro. único de um dos títulos".

Habilitando a marcação de agrupar pagamentos, a geração do arquivo de remessa só ocorrerá para títulos de despesa, que não estejam baixados e que não possuam o "Nosso Número" preenchido com "PG + o Nro único de um dos títulos". Caso alguma dessas situações não sejam satisfeitas, o sistema emitirá uma mensagem de alerta e não fará a geração do arquivo."
