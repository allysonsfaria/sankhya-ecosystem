---
id: "10621517874327"
titulo: "Falha Não foi possível gerar o relatório solicitado. Motivo: XXXXXXXX (Arquivo ou diretório inexistente)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10621517874327-Falha-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-relat%C3%B3rio-solicitado-Motivo-XXXXXXXX-Arquivo-ou-diret%C3%B3rio-inexistente"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:16:18Z"
rotulos: ["Configuração", "Relatórios", "Preferências", "Folha", "#folha", "Caminho do arquivo incorreto", "Verifique e corrija o caminho no parâmetro", "Falha ao gerar relatório", "Erro"]
---

# Falha Não foi possível gerar o relatório solicitado. Motivo: XXXXXXXX (Arquivo ou diretório inexistente)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19036219616919) MENSAGEM:**

Falha: Não foi possível gerar o relatório solicitado.
Motivo: Arquivo ou diretório inexistente.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19036219624471) SITUAÇÃO:**

Ao tentar fazer a impressão da documentação referente a rescisão do funcionário a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19036219629207) CAUSA:**

Ocorre quando o caminho informado no parâmetro não está correto.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19036219636119) SOLUÇÃO:**

Verifique o caminho que está informado no parâmetro **'Caminho da pasta padrao de relatorios folha - FPPASTAPADRAO'**. Para tal, acesse a tela **Preferências** (Caminho de acesso à tela: Configurações » Avançado » Preferências).

Feito isso, acesse os caminhos informados no parâmetro e verifique se de fato existem. Vale destacar que o caminho deve estar no padrão:
Ex:
Windows, exemplo: C:\**suapasta**\sankhya-om\jboss\bin\
Para Linux, exemplo: /home/**suapasta**/relatorios/
