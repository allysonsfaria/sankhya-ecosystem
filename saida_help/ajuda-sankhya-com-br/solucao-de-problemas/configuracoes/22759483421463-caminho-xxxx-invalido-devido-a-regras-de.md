---
id: "22759483421463"
titulo: "Caminho XXXX inválido devido a regras de segurança! Favor procure o administrador do sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22759483421463-Caminho-XXXX-inv%C3%A1lido-devido-a-regras-de-seguran%C3%A7a-Favor-procure-o-administrador-do-sistema"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:48:47Z"
rotulos: ["Configuração", "SPED", "Segurança", "Parâmetro", "Erro"]
---

# Caminho XXXX inválido devido a regras de segurança! Favor procure o administrador do sistema

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/22765325082135) MENSAGEM:**

Caminho XXXX inválido devido a regras de segurança! Favor procure o administrador do sistema.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/22759483405591) SOLUÇÃO:**

**Novas regras para o diretório do parâmetro FREPBASEFOLDER**

Configuração do parâmetro e durante o uso do sistema, como nas telas de geração dos SPED’s.

![Imagem 3: Não pode ser usado os diretórios de forma direta, ou seja, salvar diretamente neles:](https://ajuda.sankhya.com.br/hc/article_attachments/22759491488279) Não pode ser usado os diretórios de forma direta, ou seja, salvar diretamente neles:

C:/

D:/

E:/

É necessário usar uma sub-pasta nos diretórios mencionados.

**EXEMPLO:**

![Imagem 4: EXEMPLO:](https://ajuda.sankhya.com.br/hc/article_attachments/22759491490199)

![Imagem 5: Não podemos utilizar diretórios que contenham:](https://ajuda.sankhya.com.br/hc/article_attachments/22759491491991) Não podemos utilizar diretórios que contenham:

bin

domain

modules

standalone/deployments

standalone/configuration

standalone/tmp

Windows

Gerenciador de Pacotes

Gerenciador\_de\_Pacotes

GerenciadordePacotes

Sankhyaconf

**EXEMPLO:**

Diretório mais uma das pastas proibidas “bin”

![Imagem 6: Diretório mais uma das pastas proibidas “bin”](https://ajuda.sankhya.com.br/hc/article_attachments/22759483413783)

![Imagem 7: Não podemos usar diretório que iniciem como:](https://ajuda.sankhya.com.br/hc/article_attachments/22759483417751) Não podemos usar diretório que iniciem como:

dev

lib

mnt

proc

run

srv

var

etc

opt

root

sys

Usr

**EXEMPLO:**

![Imagem 8: EXEMPLO:](https://ajuda.sankhya.com.br/hc/article_attachments/22759491497367)
