---
id: "10978805503639"
titulo: "Limite de Registros na exportação de relatórios"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10978805503639-Limite-de-Registros-na-exporta%C3%A7%C3%A3o-de-relat%C3%B3rios"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:02:14Z"
rotulos: ["Configuração", "Relatórios", "Inteiro", "não apagar", "Parâmetro", "Limite de Exportação de Registros: Ajuste Necessário", "Desempenho"]
---

# Limite de Registros na exportação de relatórios

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16363069092119) MENSAGEM:**

Apenas 5000 primeiros registros a partir da primeira página serão exportados. Deseja continuar?

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16363113429015)CAUSA:**

Ao aumentar o valor desse campo para mais de 5000 registros, poderá haver impactos no desempenho do sistema, pois o mesmo irá percorrer mais linhas de registros portanto demorará mais tempo.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363069105687) SOLUÇÃO:**

Nativamente, o sistema traz o parâmetro **"QTDMAXREGEXPORT - Qtd. mx. de reg. para export. de PDF, XLS e Cubo"** no campo Inteiro com o valor de 5000. Para que os relatórios exportem mais linhas, altere esse campo para o valor desejado.

![Imagem 4: Nativamente, o sistema traz o parâmetro "QTDMAXREGEXPORT - Qtd. mx. de reg. para export. de PDF, XLS e Cubo" no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/14685098199447)
