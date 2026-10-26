---
id: "9397894004375"
titulo: "Data de Validade não pode ser menor que data do sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9397894004375-Data-de-Validade-n%C3%A3o-pode-ser-menor-que-data-do-sistema"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-24T12:42:46Z"
rotulos: ["Configuração", "NF-e", "Importação", "Estoque", "CORE_E03154", "COM_E00200", "Parâmetro", "Restrição de Data de Validade", "Erro"]
---

# Data de Validade não pode ser menor que data do sistema

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18588557375127) MENSAGEM:**

[COM\_E00200]  Data de Validade não pode ser menor que data do sistema.

[CORE\_E03154] Data de Validade não pode ser menor que data do sistema

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588557387287) SITUAÇÃO:**

Ao dar entrada de NF-e pelo portal de importação de XML a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18588557395479) CAUSA:**

Dar entrada em uma nota com produtos vencidos sem ligar o parâmetro **PERPRODVENC-Permitir entrada de Produto vencido?**

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588588263703) SOLUÇÃO:**

Caso seja necessário dar entrada em uma nota com produtos vencidos é necessário acessar a tela **Preferências** (Configurações » Avançado » Preferências) e ligar o parâmetro **PERPRODVENC-Permitir entrada de Produto vencido?**

![Imagem 5: Caso seja necessário dar entrada em uma nota com produtos vencidos é necessário acessar a tela Preferências…](https://ajuda.sankhya.com.br/hc/article_attachments/9397653289367)
