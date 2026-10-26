---
id: "19967440314007"
titulo: "Não foi possível iniciar o processo de atualização. A instalação não será iniciada. O modo modular está ativo e este Wildfly não é compatível"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/19967440314007-N%C3%A3o-foi-poss%C3%ADvel-iniciar-o-processo-de-atualiza%C3%A7%C3%A3o-A-instala%C3%A7%C3%A3o-n%C3%A3o-ser%C3%A1-iniciada-O-modo-modular-est%C3%A1-ativo-e-este-Wildfly-n%C3%A3o-%C3%A9-compat%C3%ADvel"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T14:51:22Z"
rotulos: ["Configuração", "Atualização", "WPM", "WildFly não compatível", "Usar o Web Package Manager (WPM)", "WPM desatualizado ou não instalado", "WPM atualização Sankhya-W", "WildFly", "Erro"]
---

# Não foi possível iniciar o processo de atualização. A instalação não será iniciada. O modo modular está ativo e este Wildfly não é compatível

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19967450393111) **MENSAGEM:**

Não foi possível iniciar o processo de atualização.
A instalação não será iniciada. O modo modular está ativo e este Wildfly não é compatível. Atualize o WildFly para versão mais recente em nosso site <http://downloads.sankhya.com.br/>.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19967450430231) CAUSA:**

O WPM (Web Package Manager) está desatualizado, não está instalado, foi deletado ou está corrompido, sendo necessário refazer a instalação.

A rotina de atualização do Sankhya-W não está instalada
Não foi encontrado dentro do servidor de aplicações a instalação do Atualizador Automático do Sankhya-W.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19967440282775)SOLUÇÃO:**

WPM é a sigla de Web Package Manager, que como o próprio nome sugere, é um atualizador de pacotes executado via web (browser).

#### Ambiente Windows:

Acesse o [http://downloads.sankhya.com.br](http://downloads.sankhya.com.br/) > Aplicações > WPM > Baixar .pkg

Localize a pasta **Sankhya-Om** Gerenciador de Pacotes > pkgs e coloque o arquivo baixado anteriormente:

![Imagem 4: Localize a pasta Sankhya-Om Gerenciador de Pacotes > pkgs e coloque o arquivo baixado anteriormente:](https://ajuda.sankhya.com.br/hc/article_attachments/19967440290455)

Retorne na pasta **Sankhya-Om** Gerenciador de Pacotes > bin e execute o sankhyaw-package-manager.exe

![Imagem 5: Retorne na pasta Sankhya-Om Gerenciador de Pacotes > bin e execute o sankhyaw-package-manager.exe](https://ajuda.sankhya.com.br/hc/article_attachments/19967450411031)

**Opção [1]**

**Opção [S/N]: S**

Selecione o servidor que será atualizado via WPM

Selecione o pacote de atualização

[1] sankhya-w\_atualizador-web-X.Xbxx.pkg

O processo de atualização do sistema foi executado com sucesso!

#### Ambiente Linux:

Acesse o servidor de aplicação onde está o **Sankhya-W** com usuário mgeweb:

Baixe o pacote em [http://downloads.sankhya.com.br](http://downloads.sankhya.com.br/) > Aplicações > WPM > Baixar .pkg e transfira para o servidor via WinSCP ou FileZilla para o diretório:

 /home/mgeweb/sankhyaW\_gerenciador\_de\_pacotes/pkgs

![Imagem 6: /home/mgeweb/sankhyaW_gerenciador_de_pacotes/pkgs](https://ajuda.sankhya.com.br/hc/article_attachments/19967450413975)

Ou pegando link ao fazer o download via Navegador Chrome (ctrl + J e botão direito 'Copiar endereço do link'):

![Imagem 7: Ou pegando link ao fazer o download via Navegador Chrome (ctrl + J e botão direito 'Copiar endereço do link'):](https://ajuda.sankhya.com.br/hc/article_attachments/19967450417175)

E dentro da pasta pkgs, dar o seguinte comando: (exemplo de link)

$ wget <https://downloads-sankhya-wpm.s3.amazonaws.com/sankhya-w_atualizador-web-9.0b54.pkg>

![Imagem 8: $ wget https://downloads-sankhya-wpm.s3.amazonaws.com/sankhya-w_atualizador-web-9.0b54.pkg](https://ajuda.sankhya.com.br/hc/article_attachments/19967440300055)

Agora com o pacote baixado e na pasta pkgs, acesse o Gerenciador de Pacotes:

$ pwd

 /home/mgeweb/sankhyaW\_gerenciador\_de\_pacotes/pkgs

$ cd ..

$ cd bin

$ ./sankhyaw-package-manager

![Imagem 9: $ ./sankhyaw-package-manager](https://ajuda.sankhya.com.br/hc/article_attachments/19967450411031)

Siga os mesmo passos do início do artigo.

O processo de atualização do sistema foi executado com sucesso!
