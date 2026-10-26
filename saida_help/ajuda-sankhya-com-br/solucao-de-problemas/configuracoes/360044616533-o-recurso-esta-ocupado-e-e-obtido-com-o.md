---
id: "360044616533"
titulo: "O recurso está ocupado e é obtido com o NOWAIT especificado ou o timeout expirou"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616533-O-recurso-est%C3%A1-ocupado-e-%C3%A9-obtido-com-o-NOWAIT-especificado-ou-o-timeout-expirou"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:54Z"
rotulos: ["Configuração", "Atualização", "ORA-00054", "Erro de Recurso Ocupado ao Atualizar Sistema", "Erro", "SankhyaW"]
---

# O recurso está ocupado e é obtido com o NOWAIT especificado ou o timeout expirou

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16310441756951) MENSAGEM:**

[ORA-00054]: o recurso está ocupado e é obtido com o NOWAIT especificado ou o timeout expirou.

![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16310441761175) **SITUAÇÃO:**

Ao tentar atualizar o Banco de Dados ou pacote do **SankhyaW**, ocorre a mensagem.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16310441762711) **SOLUÇÃO:**

![Imagem 4: No momento da atualização é necessário que não tenha usuários no sistema.](https://ajuda.sankhya.com.br/hc/article_attachments/17378746280727)  No momento da atualização é necessário que não tenha usuários no sistema.

![Imagem 5: Recomenda-se programar um horário de atualização fora do expediente de trabalho ou no intervalo de almoço, por exemplo.](https://ajuda.sankhya.com.br/hc/article_attachments/17378746289943) Recomenda-se programar um horário de atualização fora do expediente de trabalho ou no intervalo de almoço, por exemplo.

![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16310441765015) **CAUSA:**

Ocorre quando ao iniciar o processo de atualização do sistema (pkg), via WPM ou atualização do Banco de Dados, algum recurso da aplicação esteja em uso.
