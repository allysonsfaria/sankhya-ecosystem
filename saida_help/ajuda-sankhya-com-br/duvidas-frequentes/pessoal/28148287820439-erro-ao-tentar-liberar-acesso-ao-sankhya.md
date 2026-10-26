---
id: "28148287820439"
titulo: "Erro ao tentar liberar acesso ao Sankhya Om - Dados de cadeia ou binários seriam truncados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28148287820439-Erro-ao-tentar-liberar-acesso-ao-Sankhya-Om-Dados-de-cadeia-ou-bin%C3%A1rios-seriam-truncados"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-18T20:04:09Z"
rotulos: ["Configuração", "Erro ao tentar liberar acesso ao Sankhya Om - Dados de cadeia ou binários seriam truncados", "TSIUSU", "Erro", "Sankhya Om", "NOMEUSU"]
---

# Erro ao tentar liberar acesso ao Sankhya Om - Dados de cadeia ou binários seriam truncados

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/28149584031255) MENSAGEM:**

Dados de cadeia ou binários seriam truncados.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28149584033431) SITUAÇÃO:**

Erro ao tentar liberar acesso ao Sankhya Om pela tela: Pessoal+ » Rotinas Folha » Acessos Pessoal Mais

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28149584036375) SOLUÇÃO:**

**![Imagem 4: Verifique como está a coluna NOMEUSU da tabela TSIUSU:](https://ajuda.sankhya.com.br/hc/article_attachments/28149605337111) Verifique como está a coluna NOMEUSU da tabela TSIUSU:**

Acesse a tela Configurações » Avançado » Dicionário de Dados:

![Imagem 5: Acesse a tela Configurações » Avançado » Dicionário de Dados:](https://ajuda.sankhya.com.br/hc/article_attachments/28148276326423)

**![Imagem 6: Revisão e ajuste de usuários: Verifique todos os usuários cadastrados e altere aqueles cujos nomes excedam 10…](https://ajuda.sankhya.com.br/hc/article_attachments/28149605338775) Revisão e ajuste de usuários:**
Verifique todos os usuários cadastrados e altere aqueles cujos nomes excedam 10 caracteres, para que fiquem dentro do limite definido.

![Imagem 7: Ajuste na estrutura da tabela: Após realizar as correções nos usuários, solicite ao DBA da empresa que ajuste a coluna…](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) **Ajuste na estrutura da tabela:**
Após realizar as correções nos usuários, solicite ao DBA da empresa que ajuste a coluna **NOMEUSU** da tabela **TSIUSU**, garantindo que seu tamanho esteja conforme o padrão permitido de 10 caracteres.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/28149605334295) CAUSA:**

O erro ocorre porque a coluna **NOMEUSU** da tabela **TSIUSU** contém valores com mais caracteres do que o permitido pelo padrão, que é de 10 caracteres. Consequentemente, ao tentar inserir um nome de usuário na coluna **NOMEUSUALTER**, que contenha mais do que 10 caracteres, resulta o erro.
