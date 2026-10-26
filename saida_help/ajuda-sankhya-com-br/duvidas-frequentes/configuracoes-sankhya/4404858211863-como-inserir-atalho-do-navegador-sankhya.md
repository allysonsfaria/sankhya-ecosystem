---
id: "4404858211863"
titulo: "Como inserir atalho do Navegador Sankhya na área de trabalho Ubuntu/Mint (Linux)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404858211863-Como-inserir-atalho-do-Navegador-Sankhya-na-%C3%A1rea-de-trabalho-Ubuntu-Mint-Linux"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:22:55Z"
rotulos: ["Configuração", "Navegador", "Linux", "Criando Atalho do Navegador Sankhya no Linux", "Navegador Sankhya", "Ubuntu", "Mint", "Atalho"]
---

# Como inserir atalho do Navegador Sankhya na área de trabalho Ubuntu/Mint (Linux)

Em algumas versões do Ubuntu ou Mint, a criação de atalhos era algo bastante simples (botão do lado direito do mouse). Nas ultimas versões este processo ficou um pouco mais complicado, por esse motivo segue alguns passos para facilitar nesta criação do atalho.

![Imagem 1: Crie uma pasta 'Sankhya' no diretório /home/usuario/ ($HOME)](https://ajuda.sankhya.com.br/hc/article_attachments/16369512177687) Crie uma pasta 'Sankhya' no diretório /home/usuario/ ($HOME)

$ cd $HOME

$ mkdir Sankhya

**![Imagem 2: OBSERVAÇÃO: O nome 'usuario' foi usado como exemplo sendo necessário alterar para o nome de usuário da maquina.](https://ajuda.sankhya.com.br/hc/article_attachments/16369541664663) OBSERVAÇÃO:** O nome 'usuario' foi usado como exemplo sendo necessário alterar para o nome de usuário da maquina.

![Imagem 3: Acesse o http://downloads.sankhya.com.br/ e baixe a versão do Navegador Sankhya de acordo com seu Linux e extraia…](https://ajuda.sankhya.com.br/hc/article_attachments/16369512180887) Acesse o <http://downloads.sankhya.com.br/> e baixe a versão do Navegador Sankhya de acordo com seu Linux e extraia dentro da pasta criada no item 1 (Sankhya)

![Imagem 4: Acesse o http://downloads.sankhya.com.br/ e baixe a versão do Navegador Sankhya de acordo com seu Linux e extraia…](https://ajuda.sankhya.com.br/hc/article_attachments/15694920760343)

![Imagem 5: E recomendável criar um link simbólico para não ser necessário atualizar o diretório do atalho em novas atualizações do…](https://ajuda.sankhya.com.br/hc/article_attachments/16369541671063) E recomendável criar um link simbólico para não ser necessário atualizar o diretório do atalho em novas atualizações do navegador, acesse a pasta que extraída no item 2, botão direito 'Abrir no terminal':

![Imagem 6: E recomendável criar um link simbólico para não ser necessário atualizar o diretório do atalho em novas atualizações do…](https://ajuda.sankhya.com.br/hc/article_attachments/4404848610583)

Execute o comando:

**ln -s $HOME/Sankhya/NavegadorSankhya\_1.3b324\_linuxx64/Navegador\_Sankhya-1.3b324/ $HOME/Sankhya/NavegadorSankhya**

**![Imagem 7: OBSERVAÇÃO: edite o comando de acordo com a versão utilizada.](https://ajuda.sankhya.com.br/hc/article_attachments/16369541664663) OBSERVAÇÃO:** edite o comando de acordo com a versão utilizada.

![Imagem 8: OBSERVAÇÃO: edite o comando de acordo com a versão utilizada.](https://ajuda.sankhya.com.br/hc/article_attachments/4404857272599)

Após criado ficará da seguinte forma:

![Imagem 9: Após criado ficará da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/15694934272407)

![Imagem 10: Crie o arquivo 'navegador-sankhya.desktop' ou use o modelo anexo, abra o editor de texto e insira as seguintes…](https://ajuda.sankhya.com.br/hc/article_attachments/16369512186135) Crie o arquivo 'navegador-sankhya.desktop' ou use o modelo anexo, abra o editor de texto e insira as seguintes informações:

[Desktop Entry]
Version=1.0
Type=Application
Name=Navegador Sankhya
GenericName=Navegador Sankhya
Comment=Ferramenta para acesso web ao SankhyaOm
Exec=bash -c "cd $HOME/Sankhya/NavegadorSankhya && ./execNavegadorSankhya"
Terminal=false
Icon=$HOME/Sankhya/NavegadorSankhya/resources/icon.png
Categories=WebBrowser;
StartupNotify=true
Actions=Window;

Salve o arquivo e feche.

**![Imagem 11: OBSERVAÇÃO: Em algumas distribuições Linux Mint não reconhece o formato .png, disponibilizamos em anexo uma imagem em…](https://ajuda.sankhya.com.br/hc/article_attachments/16369541664663) OBSERVAÇÃO:** Em algumas distribuições Linux Mint não reconhece o formato .png, disponibilizamos em anexo uma imagem em formato .xpm, basta colocar na pasta $HOME/Sankhya/NavegadorSankhya/resources/

![Imagem 12: Copie o arquivo 'navegador-sankhya.desktop' para o diretório /usr/share/applications, botão direito 'Abrir no…](https://ajuda.sankhya.com.br/hc/article_attachments/16369512188183) Copie o arquivo 'navegador-sankhya.desktop' para o diretório /usr/share/applications, botão direito 'Abrir no terminal':
**sudo cp $HOME/Sankhya/navegador-sankhya.desktop /usr/share/applications/navegador-sankhya.desktop**

Informar a senha para root

![Imagem 13: Informar a senha para root](https://ajuda.sankhya.com.br/hc/article_attachments/4404849467543)

![Imagem 14: Neste momento se tudo certo, pesquise nos aplicativos e localize o Navegador Sankhya:](https://ajuda.sankhya.com.br/hc/article_attachments/16369512190359) Neste momento se tudo certo, pesquise nos aplicativos e localize o Navegador Sankhya:

![Imagem 15: Neste momento se tudo certo, pesquise nos aplicativos e localize o Navegador Sankhya:](https://ajuda.sankhya.com.br/hc/article_attachments/4404857923607)

Ubuntu: Copie e cole na Área de trabalho o arquivo criado 'navegador-sankhya.desktop

Mint: Pesquisar por Navegador Sankhya, botão direito '+ adicionar à área de trabalho'
