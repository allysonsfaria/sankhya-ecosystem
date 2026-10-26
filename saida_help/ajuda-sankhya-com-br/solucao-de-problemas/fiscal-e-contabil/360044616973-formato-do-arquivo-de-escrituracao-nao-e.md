---
id: "360044616973"
titulo: "Formato do arquivo de escrituração não é valido. Data inválida - usar formato \"ddmmaaaa\". (0000 DT_FIN)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616973-Formato-do-arquivo-de-escritura%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-valido-Data-inv%C3%A1lida-usar-formato-ddmmaaaa-0000-DT-FIN"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:35Z"
rotulos: ["Fiscal", "XML", "Validação", "EFD", "Utilizar validador correto", "Formato de arquivo inválido", "Incompatibilidade de validador", "Erro"]
---

# Formato do arquivo de escrituração não é valido. Data inválida - usar formato "ddmmaaaa". (0000 DT_FIN)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17004328557335) MENSAGEM:**

Formato do arquivo de escrituração não é valido.

Data inválida - usar formato "ddmmaaaa". (0000 DT\_FIN).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17004328567319)SOLUÇÃO:**

Essa mensagem é retornada quando o validador utilizado para esse processo não é compatível com o arquivo gerado.

**Exemplos:**

- Utilizando um 'Validador EFD ICMS-IPI' para validar um arquivo EFD CONTRIBUIÇÕES.
- Utilizando um 'Validador EFD Contribuições' para validar um arquivo EFD ICMS/IPI.

![Imagem 3: Realize o download do validador compatível com o arquivo gerado e refaça a validação. Em caso de dúvidas acione o…](https://ajuda.sankhya.com.br/hc/article_attachments/17004328573847) Realize o download do validador compatível com o arquivo gerado e refaça a validação. Em caso de dúvidas acione o contador de sua empresa.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17004349000599) CAUSA:**

Essa mensagem é retornada quando o validador utilizado para o processo não é compatível com o arquivo gerado.
