---
id: "360044617553"
titulo: "Report 'subLivroSaidaP2' exceeded the limit of 200 maximum pages"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617553-Report-subLivroSaidaP2-exceeded-the-limit-of-200-maximum-pages"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:46Z"
rotulos: ["Configuração", "Relatórios", "Fiscal", "Preferências", "Solução: Aumente o parâmetro \"MAXPAGRELATORIO\" para um valor maior.", "Geração: Gere o relatório novamente após ajustar o parâmetro.", "Mensagem: Relatório 'subLivroSaidaP2' excedeu limite de 200 páginas.", "Erro"]
---

# Report 'subLivroSaidaP2' exceeded the limit of 200 maximum pages

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16415640619159) MENSAGEM:**

Report 'subLivroSaidaP2' exceeded the limit of 200 maximum pages.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16415640621335) SOLUÇÃO:**

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16415640622871) Acesse: Configurações » Avançado » Preferências

- Parâmetro **"MAXPAGRELATORIO":** aumentar o valor no campo Inteiro.
- Exemplo: Inteiro = 200. Aumentar para Inteiro = 900 ou superior.

![Imagem 4: Acesse: Livros Fiscais » Relatórios » Registro de Saída e gere novamente o relatório.](https://ajuda.sankhya.com.br/hc/article_attachments/16415640625303) Acesse: Livros Fiscais » Relatórios » Registro de Saída e gere novamente o relatório.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16415662814999) CAUSA:**

Ocorre quando o relatório de Saída possui um grande volume de informação e será gerado com várias páginas, então é necessário aumentar o valor no parâmetro para suportar a quantidade de registros e páginas.
