---
id: "360044463153"
titulo: "Como ajustar o tamanho dos pacotes para Sincronização no DataSync?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044463153-Como-ajustar-o-tamanho-dos-pacotes-para-Sincroniza%C3%A7%C3%A3o-no-DataSync"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:57:28Z"
rotulos: ["Configuração", "Ajuste de Tamanho de Pacotes no DataSync", "Desempenho", "Rede", "Datasync", "Transferência de Arquivos"]
---

# Como ajustar o tamanho dos pacotes para Sincronização no DataSync?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17127091500695) SITUAÇÃO:**

Quando houver um quantidade maior do que o habitual para sincronização via DataSync, pode ocorrer dos dados não serem sincronizados ou demorar para sincronizar, gerando um 'engarrafamento' no trafego das informações.

**![Imagem 2: SOLUÇÃO: Para evitar este incidente, crie uma propriedade nas configurações do Datasync:](https://ajuda.sankhya.com.br/hc/article_attachments/17127091506199) SOLUÇÃO:**
Para evitar este incidente, crie uma propriedade nas configurações do Datasync:

![Imagem 3: Na pasta de instalação da aplicação DataSync, acesse:](https://ajuda.sankhya.com.br/hc/article_attachments/17127077646487) Na pasta de instalação da aplicação DataSync, acesse:

Exemplo considerando a instalação em ambiente Windows.:

- C:\DataSync\**conf**

![Imagem 4: Dentro da pasta conf localize o arquivo 'datasync.conf' e faça sua edição por meio do bloco de notas, inserindo a…](https://ajuda.sankhya.com.br/hc/article_attachments/17127091525399) Dentro da pasta conf localize o arquivo 'datasync.conf' e faça sua edição por meio do bloco de notas, inserindo a propriedade **filetransfer.packetsize**conforme exemplo abaixo:

**Antes da edição:**

#Fri Jan 09 10:08:14 BRST 2009
porta.webconsole=8080
intervalo.download.ftp=5

**Após a edição:**

#Fri Jan 09 10:08:14 BRST 2009
porta.webconsole=8080
intervalo.download.ftp=5
**filetransfer.packetsize=1024**

Configurando a propriedade filetransfer.packetsize com o valor 1024, a aplicação irá fragmentar o pacote respeitando o limite de 1024 kbyte, transferindo as partes individuais até concluir a toda a transferência do pacote.

**(1)** **Exemplos de configuração:**
filetransfer.packetsize=10240      (10\*1024=10240 ou seja 10 MB)
filetransfer.packetsize=20480      (20\*1024=20480 ou seja 20 MB)
filetransfer.packetsize=30720      (30\*1024=30720 ou seja 30 MB)
filetransfer.packetsize=51200      (50\*1024=51200 ou seja 50 MB)
filetransfer.packetsize=102400    (100\*1024=102400 ou seja 100 MB)

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17127091530647) OBSERVAÇÃO:**

Ao realizar qualquer alteração no arquivo 'datasync.conf', reinicie o serviço do DataSync.
