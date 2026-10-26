---
id: "4404870563351"
titulo: "A rotina de atualização do Sankhya-W não está instalada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404870563351-A-rotina-de-atualiza%C3%A7%C3%A3o-do-Sankhya-W-n%C3%A3o-est%C3%A1-instalada"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:22:53Z"
rotulos: ["Configuração", "Atualização", "WPM", "Sankhya-W", "Erro"]
---

# A rotina de atualização do Sankhya-W não está instalada

WPM é a sigla de Web Package Manager, que como o próprio nome sugere, é um atualizador de pacotes executado via web (browser).

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16369490899351) MENSAGEM**:

A rotina de atualização do Sankhya-W não está instalada
Não foi encontrado dentro do servidor de aplicações a instalação do Atualizador Automático do Sankhya-W.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16369490901271) SOLUÇÃO:**

#### Ambiente Windows:

Acesse o <http://downloads.sankhya.com.br> > Aplicações > WPM > Baixar .pkg

Localize a pasta **Sankhya-Om** Gerenciador de Pacotes > pkgs e coloque o arquivo baixado anteriormente:

![Imagem 3: Localize a pasta Sankhya-Om Gerenciador de Pacotes > pkgs e coloque o arquivo baixado anteriormente:](https://ajuda.sankhya.com.br/hc/article_attachments/4404875229591)

Retorne na pasta **Sankhya-Om** Gerenciador de Pacotes > bin e execute o sankhyaw-package-manager.exe

![Imagem 4: Retorne na pasta Sankhya-Om Gerenciador de Pacotes > bin e execute o sankhyaw-package-manager.exe](https://ajuda.sankhya.com.br/hc/article_attachments/4404875254167)

**Opção [1]**

**Opção [S/N]: S**

Selecione o servidor que será atualizado via WPM

Selecione o pacote de atualização

[1] sankhya-w\_atualizador-web-X.Xbxx.pkg

O processo de atualização do sistema foi executado com sucesso!

#### Ambiente Linux:

Acesse o servidor de aplicação onde está o **Sankhya-W** com usuário mgeweb:

Baixe o pacote em <http://downloads.sankhya.com.br> > Aplicações > WPM > Baixar .pkg e transfira para o servidor via WinSCP ou FileZilla para o diretório:

 /home/mgeweb/sankhyaW\_gerenciador\_de\_pacotes/pkgs

![Imagem 5: /home/mgeweb/sankhyaW_gerenciador_de_pacotes/pkgs](https://ajuda.sankhya.com.br/hc/article_attachments/15694886950423)

Ou pegando link ao fazer o download via Navegador Chrome (ctrl + J e botão direito 'Copiar endereço do link'):

![Imagem 6: Ou pegando link ao fazer o download via Navegador Chrome (ctrl + J e botão direito 'Copiar endereço do link'):](https://ajuda.sankhya.com.br/hc/article_attachments/4404870165015)

E dentro da pasta pkgs, dar o seguinte comando: (exemplo de link)

$ wget <https://downloads-sankhya-wpm.s3.amazonaws.com/sankhya-w_atualizador-web-9.0b54.pkg>

![Imagem 7: $ wget https://downloads-sankhya-wpm.s3.amazonaws.com/sankhya-w_atualizador-web-9.0b54.pkg](https://ajuda.sankhya.com.br/hc/article_attachments/4404870253591)

Agora com o pacote baixado e na pasta pkgs, acesse o Gerenciador de Pacotes:

$ pwd

 /home/mgeweb/sankhyaW\_gerenciador\_de\_pacotes/pkgs

$ cd ..

$ cd bin

$ ./sankhyaw-package-manager

![Imagem 8: $ ./sankhyaw-package-manager](https://ajuda.sankhya.com.br/hc/article_attachments/4404875254167)

Siga os mesmo passos do início do artigo.

O processo de atualização do sistema foi executado com sucesso!

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16369490902935) CAUSA:**

O WPM (Web Package Manager) não está instalado, foi deletado ou está corrompido, sendo necessário refazer a instalação.
