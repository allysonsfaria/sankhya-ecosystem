---
id: "360043725634"
titulo: "Arquivo inválido. ID27 não encontrado no arquivo FST.MSG"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043725634-Arquivo-inv%C3%A1lido-ID27-n%C3%A3o-encontrado-no-arquivo-FST-MSG"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:59:55Z"
rotulos: ["Produtos", "Configuração", "Fast Service", "Atualização", "Arquivo inválido: ID27", "Causa: duplicação ou corrupção", "Solução: verificação de arquivos", "Erro"]
---

# Arquivo inválido. ID27 não encontrado no arquivo FST.MSG

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16422589911447) MENSAGEM:**

Arquivo inválido. ID27 não encontrado no arquivo FST.MSG.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16422606143255) SITUAÇÃO:**

Ao tentar instalar o Fast Service e acessar o sistema, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16422606149399) SOLUÇÃO:**

Considere o comportamento da aplicação e siga os passos conforme abaixo:

![Imagem 4: Verifique no computador se os arquivos "FST" e "FST.dll" existem em outras pastas.](https://ajuda.sankhya.com.br/hc/article_attachments/16422606156951) Verifique no computador se os arquivos "FST" e "FST.dll" existem em outras pastas.

Acesse o Windows Explorer, selecione: Este Computador e na barra de pesquisa no menu superior, pesquise por **"FST"**, isso fará uma busca em todo computador em todas as pastas, sub-pastas, para verificar se os arquivos estão em uma pasta diferente da pasta onde está instalado o Fast Service.

Caso exista,  apague as e deixe esses arquivos somente na pasta onde se encontra o executável do Fast. Em seguida, realize um teste de login.

Caso não resolva o problema realize o passo a seguir:

![Imagem 5: Realize a atualização dos arquivos que estão disponíveis no Portal Sankhya Página Inicial » Downloads » Arquivos »…](https://ajuda.sankhya.com.br/hc/article_attachments/16422606160919) Realize a atualização dos arquivos que estão disponíveis no Portal Sankhya Página Inicial » Downloads » Arquivos » [Fastservice Dlls (fst.dll Fst.msg)](https://place.sankhya.com.br/#/downloads/listararquivos/id/217)

Uma vez realizado o download e descompactado os arquivos, deixe-os somente na pasta do Fast Service. Depois realize um teste de login.

Caso não resolva problema realizar o passo a seguir:

![Imagem 6: Crie uma nova pasta do FastService no diretório C: (Exemplo: C:\FASTSERVICE) do computador e salve somente o executável…](https://ajuda.sankhya.com.br/hc/article_attachments/16422606165399) Crie uma nova pasta do FastService no diretório C: (Exemplo: C:\FASTSERVICE) do computador e salve somente o executável do Fast Service (FastService.exe), a licença(Licenca.snk), o autorized (Autorized.ecf), e as FST's(FST.msg, FST.dll). Crie um novo atalho na área de trabalho e realize um teste de login.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16422606170775) CAUSA:**

Ocorre quando os arquivos FST.msg, FST.dll estão presentes em mais de uma pasta no computador, ou estão desatualizados ou corrompidos e ao acessar o sistema, apresenta o erro.
