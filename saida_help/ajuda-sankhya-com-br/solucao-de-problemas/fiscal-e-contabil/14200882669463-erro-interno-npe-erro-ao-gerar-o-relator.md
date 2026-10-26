---
id: "14200882669463"
titulo: "Erro Interno (NPE). Erro ao gerar o relatório em Livros Fiscais » Relatórios » Registro da Produção e do Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14200882669463-Erro-Interno-NPE-Erro-ao-gerar-o-relat%C3%B3rio-em-Livros-Fiscais-Relat%C3%B3rios-Registro-da-Produ%C3%A7%C3%A3o-e-do-Estoque"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-09-16T11:39:01Z"
rotulos: ["Configuração", "Relatórios", "Livros Fiscais", "Estoque", "Erro interno ao gerar relatório", "Desative o parâmetro \"DISABLEHTML5\" e gere o relatório novamente", "Incompatibilidade com o layout Flex", "Erro"]
---

# Erro Interno (NPE). Erro ao gerar o relatório em Livros Fiscais » Relatórios » Registro da Produção e do Estoque

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16775992869911) MENSAGEM:**

Erro Interno (NPE). Erro ao gerar o relatório em Livros Fiscais » Relatórios » Registro da Produção e do Estoque.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16775992871831) SOLUÇÃO:**

Verifique se o parâmetro **"DISABLEHTML5"** está ligado. Caso esteja, desligue o parâmetro, pois ele é responsável por desabilitar o layout HTML 5 de todas as telas do sistema.

![Imagem 3: Verifique se o parâmetro "DISABLEHTML5" está ligado. Caso esteja, desligue o parâmetro, pois ele é responsável por…](https://ajuda.sankhya.com.br/hc/article_attachments/14200649909143)

Após "Desligar" o parâmetro acima, acesse novamente a tela Livros Fiscais » Relatórios » **Registro da Produção e do Estoque,**preencha os campos necessários e gere o relatório clicando no botão **"Visualizar**".

![Imagem 4: Após "Desligar" o parâmetro acima, acesse novamente a tela Livros Fiscais » Relatórios » Registro da Produção e do…](https://ajuda.sankhya.com.br/hc/article_attachments/16775972285847)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16775992871191) CAUSA:**

Após realizar diversos testes, constatamos que a rotina não funciona no layout Flex, apenas no layout HTML 5.
