---
id: "9136004992023"
titulo: "Erro ao processar relatório formatado do envio de email"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9136004992023-Erro-ao-processar-relat%C3%B3rio-formatado-do-envio-de-email"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:10:25Z"
rotulos: ["Configuração", "Relatórios Formatados", "NF-e", "TOP", "CORE_E05181", "Erro na Formatação de Relatório de E-mai", "Erro"]
---

# Erro ao processar relatório formatado do envio de email

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19033356687383) MENSAGEM:**

[CORE\_E05181]  Erro ao processar relatório formatado do envio de email.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033375130647) SITUAÇÃO:**

Ao tentar confirmar o lançamento de uma nota fiscal a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19033375137687) CAUSA:**

Quando a logo não está inserida corretamente no caminho definido no parâmetro **"Pasta de modelos para impressão -** **SERVDIRMOD"** .

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033356702615) SOLUÇÃO:**

Analise o caminho apresentado na mensagem e certifique-se de que a logo está inserida corretamente nele, confira também se esse caminho da logo está cadastrado no parâmetro **"Pasta de modelos para impressão -** **SERVDIRMOD"** .

**Importante:** Se o erro for apresentado utilizando uma determinada TOP, verifique se o arquivo em TXT inserido na aba e-mail da TOP é realmente necessário. Caso não seja, retire-o e tente confirmar o lançamento novamente.
