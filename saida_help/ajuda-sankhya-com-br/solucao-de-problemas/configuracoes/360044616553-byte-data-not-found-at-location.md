---
id: "360044616553"
titulo: "Byte data not found at location"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616553-Byte-data-not-found-at-location"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-07T11:48:21Z"
rotulos: ["Configuração", "Impressão", "Relatórios", "Preferências", "CORE_E02510", "Resolução de Erro de Byte Data em Relatórios", "Byte Data", "Erro", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Byte data not found at location

**MENSAGEM**

Byte data not found at location: [caminho do arquivo] (ex: [CORE\_E02510]: Byte data not found at location:/home/mgeweb/modelos/logo-sk.gif)

**SITUAÇÃO**

Esta mensagem aparece ao tentar **"gerar relatórios"**, **"imprimir documentos fiscais"** (NF-e, NFS-e, NFC-e, CT-e), **"emitir pedidos"**, **"boletos no portal de vendas"** ou **"baixar arquivos"** do sistema. O erro indica que o sistema não conseguiu localizar um arquivo de imagem (geralmente o logotipo da empresa) no caminho especificado para a impressão ou visualização do documento.

**SOLUÇÃO**

Para resolver este erro, siga os passos abaixo:

**(1)** Acesse a tela **"Preferências"** (Configurações >> Avançado >> Preferências) e localize o parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**. Verifique o caminho configurado neste parâmetro e anote-o.

**(2)** Verifique também o parâmetro **"FREPBASEFOLDER"**, que define a pasta exibida na tela **"Repositório de Arquivos"** (se estiver vazio, o sistema usa uma pasta padrão do servidor). Ele não faz parte do caminho da logo, mas a pasta do **"SERVDIRMOD"** só aparece no Repositório de Arquivos se estiver dentro da pasta do **"FREPBASEFOLDER"**.

**(3)** Acesse a tela **"Repositório de Arquivos"** (Configurações >> Avançado >> Repositório de Arquivos) ou navegue até a pasta física indicada no **"SERVDIRMOD"** (se ela não aparecer no repositório, o acesso deve ser feito direto no servidor, pela equipe de TI). Confirme se o arquivo de logotipo mencionado na mensagem de erro existe exatamente no caminho exibido na mensagem.

**(4)** Caso o arquivo não exista no diretório, insira o arquivo de logotipo da sua empresa com o nome exato que está sendo solicitado na mensagem de erro (exemplo: logo-sk.gif, Logo.jpg, logonfsenacional.jpg).

**(5)** Certifique-se de que o nome do arquivo no repositório corresponde exatamente ao nome configurado no modelo de impressão (arquivo .jrxml), inclusive letras maiúsculas e minúsculas (em servidores Linux, "Logo.jpg" e "logo.jpg" são arquivos diferentes). Verifique também a extensão do arquivo (.jpg, .png, .gif).

**(6)** Compare o caminho exibido na mensagem com o caminho do **"SERVDIRMOD"**. Se o nome do arquivo aparecer "colado" ao nome da pasta (exemplo: /home/mgeweb/modeloslogo-sk.gif), inclua uma barra no final do **"SERVDIRMOD"** (exemplo: /home/mgeweb/modelos/). 
**Observação:** o logotipo informado no campo **"Arquivo Logomarca"** (Comercial >> Preferências >> Empresa, aba **"Documentos Fiscais Eletrônicos"**) não gera este erro. Se esse arquivo não for encontrado, o documento é impresso sem a logo.

**(7)** Para modelos de impressão customizados, verifique o código do arquivo .jrxml e certifique-se de que a tag <imageExpression> aponta corretamente para o caminho do arquivo no servidor.

**(8)** Após realizar os ajustes necessários, tente novamente gerar o relatório ou imprimir o documento para validar se o erro foi corrigido. Mais detalhes sobre o uso do repositório podem ser encontrados no [Manual de Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594).

**CAUSA**

Este erro ocorre quando a configuração de impressão não foi realizada corretamente. As causas mais comuns são:

- O arquivo de logotipo não está inserido no diretório/caminho informado no parâmetro **"SERVDIRMOD"**.
- O parâmetro **"SERVDIRMOD"** está vazio ou com caminho incorreto.
- O nome do arquivo de logotipo no repositório é diferente do nome configurado no modelo de impressão (.jrxml), inclusive maiúsculas e minúsculas.
- O arquivo foi colocado em uma pasta do **"Repositório de Arquivos"** diferente da informada no **"SERVDIRMOD"**.
- O caminho foi montado errado: falta a barra entre a pasta e o nome do arquivo (exemplo: /home/mgeweb/modeloslogo-sk.gif) ou há pasta repetida (exemplo: /impressao//impressao/).
- Os arquivos foram movidos ou excluídos do repositório após uma atualização do sistema.
- Falta de permissão de acesso do sistema ao diretório onde a imagem está armazenada.
