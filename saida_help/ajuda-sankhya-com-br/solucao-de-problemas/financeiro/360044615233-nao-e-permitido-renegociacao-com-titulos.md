---
id: "360044615233"
titulo: "Não é permitido renegociação com títulos de competências (Mês/Ano) diferentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615233-N%C3%A3o-%C3%A9-permitido-renegocia%C3%A7%C3%A3o-com-t%C3%ADtulos-de-compet%C3%AAncias-M%C3%AAs-Ano-diferentes"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:55:17Z"
rotulos: ["Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "Causa: Parâmetro \"MANTEMDTENTSAI\" ativado.", "Solução: Desligar o parâmetro \"MANTEMDTENTSAI\".", "Mensagem: Renegociação não permitida com competências diferentes.", "Erro"]
---

# Não é permitido renegociação com títulos de competências (Mês/Ano) diferentes

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16426948170775) MENSAGEM:**

Não é permitido renegociação com títulos de competências (Mês/Ano) diferentes.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16426948176919) SOLUÇÃO:**

- Essa situação ocorre devido a criação do parâmetro **"MANTEMDTENTSAI",** que determina a geração de títulos de renegociação com 'Data Entrada e Saída' igual à dos títulos renegociados.
- Quando selecionado mais de um título na renegociação o sistema vai assumir a maior 'Data Entrada e Saída' dentre eles.
- Com esse parâmetro ligado, o sistema **não permitirá** renegociação de títulos com 'Data Entrada e Saída' de competência(Mês) diferentes.

Dessa forma, caso não deseje trabalhar com esse comportamento, desligue o parâmetro:

![Imagem 3: Acesse a tela "Preferências" (Caminho de acesso: Configurações » Avançado » Preferências ).](https://ajuda.sankhya.com.br/hc/article_attachments/16426919941527) Acesse a tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências).

![Imagem 4: Busque pela chave MANTEMDTENTSAI .](https://ajuda.sankhya.com.br/hc/article_attachments/16426919944087) Busque pela chave MANTEMDTENTSAI**.**

![Imagem 5: Provavelmente ele estará "Ligado" , classifique-o como "Desligado" .](https://ajuda.sankhya.com.br/hc/article_attachments/16426919947159) Provavelmente ele estará **"Ligado"**, classifique-o como **"Desligado"**.

![Imagem 6: Após a realização do procedimento acima, refaça a Renegociação.](https://ajuda.sankhya.com.br/hc/article_attachments/16426948198167) Após a realização do procedimento acima, refaça a Renegociação.

**![Imagem 7: CAUSA](https://ajuda.sankhya.com.br/hc/article_attachments/16426919955479) CAUSA**

Ocorre ao tentar renegociar títulos com 'Data Entrada e Saída' de competência(Mês) diferentes.
