---
id: "15413819369751"
titulo: "Não preparado para agrupar títulos já agrupados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15413819369751-N%C3%A3o-preparado-para-agrupar-t%C3%ADtulos-j%C3%A1-agrupados"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:56:58Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Financeiro", "CORE_E00735", "Solução: Verificar e desagrupar títulos problemáticos antes de gerar novamente.", "Mensagem: Erro ao agrupar títulos já agrupados.", "Causa: Títulos já agrupados anteriormente.", "Erro"]
---

# Não preparado para agrupar títulos já agrupados

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16539643079447) MENSAGEM:**

[CORE\_E00735] Não preparado para agrupar títulos já agrupados.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16539643098135) CAUSA:**

Ocorre ao tentar agrupar títulos que já estão agrupados.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16539643082775) SOLUÇÃO:**

![Imagem 4: Agrupar Pagamentos: quando marcada, agrupará títulos de mesmo "Parceiro" e mesmo "Vencimento" para a geração do arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/16539643083799) Agrupar Pagamentos: quando marcada, agrupará títulos de mesmo "Parceiro" e mesmo "Vencimento" para a geração do arquivo de remessa. Ao agrupar os títulos, será registrada no "Financeiro", no campo "Nosso Número" dos títulos agrupados, a informação: "PG + o Nro. único de um dos títulos".

![Imagem 5: Habilitando a opção de agrupar pagamentos, a geração do arquivo de remessa só ocorrerá para títulos de despesa, que não…](https://ajuda.sankhya.com.br/hc/article_attachments/16539616139031) Habilitando a opção de agrupar pagamentos, a geração do arquivo de remessa só ocorrerá para títulos de despesa, que não estejam baixados e que não possuam o "Nosso Número" preenchido com "PG + o Nro único de um dos títulos".

![Imagem 6: Caso alguma dessas situações não sejam satisfeitas, o sistema emitirá uma mensagem de alerta e não fará a geração do…](https://ajuda.sankhya.com.br/hc/article_attachments/16539643092375) Caso alguma dessas situações não sejam satisfeitas, o sistema emitirá uma mensagem de alerta e não fará a geração do arquivo.

![Imagem 7: Se o processo de geração for interrompido, inicie o processo novamente, já que vários títulos poderão ter preenchido o…](https://ajuda.sankhya.com.br/hc/article_attachments/16539643096599) Se o processo de geração for interrompido, inicie o processo novamente, já que vários títulos poderão ter preenchido o campo "Nosso Número" durante a corrida.

Portanto, o usuário deve verificar qual título teve um problema e também verificar a existência de títulos já agrupados. Caso seja identificado algum problema, retire e gere o novamente
