---
id: "1500001377522"
titulo: "O arquivo modelo 'ABC' deve estar na pasta definida pelo parâmetro SERVDIRMOD, que neste caso é '/home/mgeweb/xxxyyy/'\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001377522-O-arquivo-modelo-ABC-deve-estar-na-pasta-definida-pelo-par%C3%A2metro-SERVDIRMOD-que-neste-caso-%C3%A9-home-mgeweb-xxxyyy"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:58Z"
rotulos: ["Configuração", "NF-e", "TOP", "não apagar", "#validadoHugo", "#PublicadoHyago", "Solução para Erro de Configuração do Modelo de Nota Fiscal", "Erro", "Documentos Eletrônicos"]
---

# O arquivo modelo 'ABC' deve estar na pasta definida pelo parâmetro SERVDIRMOD, que neste caso é '/home/mgeweb/xxxyyy/'"

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16285586337047) MENSAGEM**:

Ao tentar confirmar ou aprovar a nota apresenta mensagem "O arquivo modelo 'ABC' deve estar na pasta definida pelo parâmetro SERVDIRMOD, que neste caso é '/home/mgeweb/xxxyyy/".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16285586343703) SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16285538760599) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

![Imagem 4: Verifique o campo "Modelo para Dados Adicionais de NF-e" se o modelo informado está correto.](https://ajuda.sankhya.com.br/hc/article_attachments/16285586350487) Verifique o campo **"Modelo para Dados Adicionais de NF-e"** se o modelo informado está correto.

- Se precisar dos dados adicionais da nota:

A configuração deste modelo é na tela **"Modelos de Nota Fiscal/Duplicatas/Boleto(s)"**  e o sistema buscará no diretório configurado no parâmetro **"SERVDIRMOD"** o arquivo configurado no modelo.

- Se não precisar dos dados adicionais da nota:

![Imagem 5: No campo Modelo para Dados Adicionais de NF-e retire a configuração e deixe o campo 'em branco'.](https://ajuda.sankhya.com.br/hc/article_attachments/16285586353175) No campo Modelo para Dados Adicionais de NF-e retire a configuração e deixe o campo 'em branco'.

![Imagem 6: Após realizar a correção das configurações tente novamente aprovar a nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16285538774935) Após realizar a correção das configurações tente novamente aprovar a nota.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16285586363415) CAUSA:**

Mensagem de alerta ocorre quando configurado na TOP Modelos de Nota Fiscal/Duplicatas/Boleto(s) e este modelo TXT não existe no diretório do servidor onde esta instalado o sistema.
