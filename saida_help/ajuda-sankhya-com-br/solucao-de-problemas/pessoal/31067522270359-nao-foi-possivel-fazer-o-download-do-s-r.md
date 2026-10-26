---
id: "31067522270359"
titulo: "Não foi possível fazer o download do(s) relatório(s). Motivo: Lista de arquivos vazia"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31067522270359-N%C3%A3o-foi-poss%C3%ADvel-fazer-o-download-do-s-relat%C3%B3rio-s-Motivo-Lista-de-arquivos-vazia"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:31Z"
rotulos: ["Configuração", "Relatórios", "Preferências", "Não foi possível", "Lista de arquivos vazia", "fazer o download do(s) relatório(s)", "Erro", "JAVA HOME"]
---

# Não foi possível fazer o download do(s) relatório(s). Motivo: Lista de arquivos vazia

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31285258240023) MENSAGEM:**

Não foi possível fazer o download do(s) relatório(s). Motivo: Lista de arquivos vazia! Verifique se o diretório possui arquivos e o filtro que define os arquivos a serem compactados.

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/31285258241687) SITUAÇÃO**

Ao tentar gerar o relatório de médias.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31285258242327) SOLUÇÃO:**

![Imagem 4: Acesse a tela "Preferências" (Configurações » Avançado » Preferências) e no parâmetro " FPPASTAPADRAO" informe o…](https://ajuda.sankhya.com.br/hc/article_attachments/31285258244247)  Acesse a tela **"Preferências"**(Configurações » Avançado » Preferências) e no parâmetro **"FPPASTAPADRAO"** informe o caminho da pasta **JAVA HOME.**

**(2)**Para capturar este caminho, acesse a tela **"Administração do Servidor"** (Configurações » Avançado » Administração do Servidor), busque pelo campo **"JAVA HOME"** e pegue o link até o nome java.

![Imagem 5: (2) Para capturar este caminho, acesse a tela "Administração do Servidor" (Configurações » Avançado » Administração do…](https://ajuda.sankhya.com.br/hc/article_attachments/31286159136151)

![Imagem 6: Depois tente novamente a emissão do Relatório.](https://ajuda.sankhya.com.br/hc/article_attachments/31285249059479) Depois tente novamente a emissão do Relatório.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31285258247575) CAUSA:**

O Caminho da pasta padrão de relatórios folha não está informando corretamente.
