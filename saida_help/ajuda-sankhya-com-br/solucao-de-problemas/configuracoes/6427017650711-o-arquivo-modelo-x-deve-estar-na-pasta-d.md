---
id: "6427017650711"
titulo: "O arquivo modelo 'X' deve estar na pasta definida pelo parâmetro SERVDIRMOD, que neste caso é 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6427017650711-O-arquivo-modelo-X-deve-estar-na-pasta-definida-pelo-par%C3%A2metro-SERVDIRMOD-que-neste-caso-%C3%A9-Y"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:16:27Z"
rotulos: ["Configuração", "Impressão", "XML", "CORE_E02117", "Corrigindo Erro de Arquivo Modelo no Parâmetro SERVDIRMOD", "Erro", "Documentos Eletrônicos"]
---

# O arquivo modelo 'X' deve estar na pasta definida pelo parâmetro SERVDIRMOD, que neste caso é 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16457476891927) MENSAGEM:**

[CORE\_E02117] O arquivo modelo 'X' deve estar na pasta definida pelo parâmetro **"SERVDIRMOD"**, que neste caso é 'Y'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457475178647) SOLUÇÃO:**

Precisa verificar no parâmetro SERVDIRMOD o caminho informado, em seguida pegar exatamente o nome do arquivo na msg de erro, e inserir na pasta identificada.  Esse arquivo pode ser inserido pela tela de repositório de arquivos, ou inserir diretamente pelo servidor.

Ex: Parâmetro servdirmod:   /home/mgeweb/modelos (esse caminho é onde será informado o modelo do arquivo). Para acessar o repositório nessa pasta, o parâmetro FREPBASEFOLDER deve estar informado da seguinte forma: /home/mgeweb/ (Dessa forma quando acessar a tela de repositório de arquivos, vai apresentar a pasta modelos e nessa pasta pode fazer o upload do arquivo que falta).

| **SERVDIRMOD:** Pasta de modelos para impressão  **FREPBASEFOLDER:** Diretório base para o repositório de arquivos |
| --- |

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457476896919)CAUSA:**

O erro ocorre quando o arquivo não está inserido corretamente no caminho do parâmetro do servdirmod.
