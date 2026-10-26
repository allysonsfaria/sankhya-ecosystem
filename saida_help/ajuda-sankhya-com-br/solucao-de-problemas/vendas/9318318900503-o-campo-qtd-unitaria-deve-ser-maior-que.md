---
id: "9318318900503"
titulo: "O campo 'qtd. Unitária' deve ser maior que zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9318318900503-O-campo-qtd-Unit%C3%A1ria-deve-ser-maior-que-zero"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-24T12:43:35Z"
rotulos: ["Nota Fiscal", "TOP", "Preferências", "Financeiro", "CORE_E03233", "Parâmetro", "Erro ao lançar nota com quantidade zero", "Configurar 'TOPQTDZERO' nas Preferências", "Campo 'qtd. Unitária' deve ser > zero", "Erro"]
---

# O campo 'qtd. Unitária' deve ser maior que zero

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19302032228631) MENSAGEM:**

[CORE\_E03233] O campo 'qtd. Unitária' deve ser maior que zero.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19302054678167) SITUAÇÃO:**

Ao lançar uma nota com quantidade zero a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19302032234647) CAUSA:**

Inserir itens com quantidade unitária zerada sem informar no parâmetro **'TOP para aceitar Qtd. igual a zero - TOPQTDZERO'** a TOP que foi utilizada.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19302032245399) SOLUÇÃO:**

Acesse a tela 'Preferências' (Caminho de acesso: Configurações » Avançado » Preferências), busque o parâmetro **'TOP para aceitar Qtd. igual a zero - TOPQTDZERO'** e nele informe o Tipo de Operação TOP utilizada no lançamento. Assim, será possível aceitar Qtd. igual a zero. Feito isso, poderá ser inserido itens com quantidade unitária zerada.

![Imagem 5: Acesse a tela 'Preferências' (Caminho de acesso: Configurações » Avançado » Preferências) , busque o parâmetro 'TOP…](https://ajuda.sankhya.com.br/hc/article_attachments/19302054687639)
