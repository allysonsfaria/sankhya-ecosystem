---
id: "9162561382423"
titulo: "Arquivo/Diretório não foi encontrado no repositório, ou não foi possível lê-lo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9162561382423-Arquivo-Diret%C3%B3rio-n%C3%A3o-foi-encontrado-no-reposit%C3%B3rio-ou-n%C3%A3o-foi-poss%C3%ADvel-l%C3%AA-lo"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:10:03Z"
rotulos: ["Configuração", "Impressão", "Financeiro", "CORE_E01220", "Arquivo não encontrado", "Adicione modelo de cheque", "Verifique configuração do parâmetro", "Erro"]
---

# Arquivo/Diretório não foi encontrado no repositório, ou não foi possível lê-lo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18796821781271) MENSAGEM:**

[CORE\_E01220] Arquivo/Diretório não foi encontrado no repositório, ou não foi possível lê-lo.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18796829399575) SITUAÇÃO:**

Ao tentar realizar a impressão de Cheques a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18796829413783) CAUSA:**

Quando o caminho do repositório está diferente entre o modelo e a tela Repositório de Arquivos.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18796829430295) SOLUÇÃO:**

Verifique a configuração do parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER".**

Se o parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"** estiver em branco (sem nenhum caminho), ao abrir a tela "Repositório de Arquivos", serão apresentados os arquivos da pasta ".sw\_file\_repository" que estão localizados dentro da pasta do usuário no C:\.

![Imagem 5: Diante disso, é necessário verificar dentro do servidor se existe essa pasta (sw_file_repository), lembrando que dentro…](https://ajuda.sankhya.com.br/hc/article_attachments/9162534971671)

Diante disso, é necessário verificar dentro do servidor se existe essa pasta (sw\_file\_repository), lembrando que dentro dela tem que ter a pasta/modelo abaixo:

Repo://cheque/SICREDI/modelo\_cheque - SICREDI.txt

![Imagem 6: Diante disso, é necessário verificar dentro do servidor se existe essa pasta (sw_file_repository), lembrando que dentro…](https://ajuda.sankhya.com.br/hc/article_attachments/9162536399255)

![Imagem 7: Assim, é necessário salvar ou colocar novamente esse modelo de cheque dentro dessa pasta. Ou ainda pegar a pasta raiz e…](https://ajuda.sankhya.com.br/hc/article_attachments/18796821817495)

Assim, é necessário salvar ou colocar novamente esse modelo de cheque dentro dessa pasta.
Ou ainda pegar a pasta raiz e colocar naquele parâmetro, para que assim que abrir a tela de repositório de arquivo seja possível visualizar a pasta cheque.
