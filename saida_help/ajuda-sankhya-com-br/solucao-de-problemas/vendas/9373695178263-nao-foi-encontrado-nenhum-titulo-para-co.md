---
id: "9373695178263"
titulo: "Não foi encontrado nenhum título para compensar para a nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9373695178263-N%C3%A3o-foi-encontrado-nenhum-t%C3%ADtulo-para-compensar-para-a-nota"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-24T01:41:34Z"
rotulos: ["Configuração", "Parceiro", "Crédito", "Preferências", "Financeiro", "CORE_E03747", "Verifique parâmetro AVISARCREDCLI", "Verifique parâmetro AVISARCREDCLI", "Verifique parâmetro AVISARCREDCLI", "Verifique parâmetro AVISARCREDCLI", "Verifique parâmetro AVISARCREDCLI", "Verifique parâmetro AVISARCREDCLI", "Verifique parâmetro AVISARCREDCLI", "Verifique parâmetro AVISARCREDCLI", "Verifique parâmetro AVISARCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Configure parâmetro TIPTITCREDCLI", "Cheque título de compensação.", "Cheque título de compensação.", "Cheque título de compensação.", "Cheque título de compensação.", "Cheque título de compensação.", "Cheque título de compensação.", "Cheque título de compensação.", "Cheque título de compensação.", "Cheque título de compensação."]
---

# Não foi encontrado nenhum título para compensar para a nota

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15816220284055) MENSAGEM:**

[CORE\_E03747]  Não foi encontrado nenhum título para compensar para a nota.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15816220284823) SOLUÇÃO:**

Caso trabalhe com a compensação de crédito de clientes é preciso verificar se o parâmetro **AVISARCREDCLI** está habilitado, para isso, basta acessar a tela **Preferências** (Configurações » Avançado » Preferências) e informar o parâmetro citado.

![Imagem 3: Caso trabalhe com a compensação de crédito de clientes é preciso verificar se o parâmetro AVISARCREDCLI está…](https://ajuda.sankhya.com.br/hc/article_attachments/9373443590551)

Caso esteja é necessário que o tipo de título utilizado no lançamento esteja devidamente cadastrado no parâmetro **TIPTITCREDCLI,** para isso, basta acessar a tela **Preferências** (Configurações » Avançado » Preferências) e informar o parâmetro citado.

![Imagem 4: Caso esteja é necessário que o tipo de título utilizado no lançamento esteja devidamente cadastrado no parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/9373595710615)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15816212405527) CAUSA:**

Lançar nota para parceiro que possui crédito a compensar e não configurar corretamente o parâmetro **TIPTITCREDCLI e o parâmetro AVISARCREDCLI está marcado.**
