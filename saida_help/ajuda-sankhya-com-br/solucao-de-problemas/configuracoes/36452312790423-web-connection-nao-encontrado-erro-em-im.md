---
id: "36452312790423"
titulo: "Web Connection não encontrado - Erro em impressões ou no login de usuário com acesso apenas por computadores liberados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36452312790423-Web-Connection-n%C3%A3o-encontrado-Erro-em-impress%C3%B5es-ou-no-login-de-usu%C3%A1rio-com-acesso-apenas-por-computadores-liberados"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-15T20:10:15Z"
rotulos: ["Login", "Configuração", "Impressão", "Web Connection", "Navegador", "Web Connection não encontrado", "Erro em impressões", "login de usuário com acesso apenas por computadores liberados", "Erro em impressões ou no login de usuário com acesso apenas por computadores liberados", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Web Connection não encontrado - Erro em impressões ou no login de usuário com acesso apenas por computadores liberados

**MENSAGEM**

Web Connection não encontrado

![Imagem 1: Web Connection não encontrado](https://ajuda.sankhya.com.br/hc/article_attachments/36452312727703)

**SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta utilizar funcionalidades que dependem do Web Connection, como impressão de documentos ou quando usuários com configuração de **acesso apenas por computadores liberados** tentam fazer login no sistema através de navegadores externos.

**SOLUÇÃO**

- **Instalação do Web Connection:**

**(1)** Acesse o site [**''Downloads Sankhya''**.](https://downloads.sankhya.com.br/)

**(2)** Clique em **"Navegadores"** e em seguida em **"Web Connection"**.

**(3)** Instale a versão adequada de acordo com a arquitetura da máquina através do [downloads sankhya](https://downloads.sankhya.com.br/downloads?app=WebConnection&c=1)

![Imagem 2: (3) Instale a versão adequada de acordo com a arquitetura da máquina através do downloads sankhya](https://ajuda.sankhya.com.br/hc/article_attachments/37694432202007)

**(4)** Clique no botão de **downloads** (seta para baixo no canto superior direito do navegador) e no botão para **abrir o arquivo instalado** (quadrado com seta para cima).

![Imagem 3: (4) Clique no botão de downloads (seta para baixo no canto superior direito do navegador) e no botão para abrir o…](https://ajuda.sankhya.com.br/hc/article_attachments/37696755128983)

**(5)** No pop-up de segurança, clique em **"Mais informações"**.

![Imagem 4: (5) No pop-up de segurança, clique em "Mais informações" .](https://ajuda.sankhya.com.br/hc/article_attachments/37694182553367)

**(6)** Clique em **"Executar mesmo assim".**

![Imagem 5: (6) Clique em "Executar mesmo assim".](https://ajuda.sankhya.com.br/hc/article_attachments/37694185137047)

**(7)** Anote o **caminho de instalação** mostrado no pop-up (será necessário para a próxima etapa).

![Imagem 6: (7) Anote o caminho de instalação mostrado no pop-up (será necessário para a próxima etapa).](https://ajuda.sankhya.com.br/hc/article_attachments/37694182554647)

- ##### Execução do Web Connection:

##### **(1)** Verifique se o Web Connection está executando. Clique em "Mostrar ícones ocultos" (seta para cima) na barra de tarefas e verifique se o ícone do WebConnection está visível.

![Imagem 7: (1) Verifique se o Web Connection está executando. Clique em "Mostrar ícones ocultos" (seta para cima) na barra de…](https://ajuda.sankhya.com.br/hc/article_attachments/37694185142935)

**(2)** Caso não esteja executando, acesse o **"Explorador de arquivos"** e navegue até o caminho anotado na instalação (geralmente: Disco Local (C:) Usuários NOME\_USUÁRIO).

![Imagem 8: (2) Caso não esteja executando, acesse o "Explorador de arquivos" e navegue até o caminho anotado na instalação…](https://ajuda.sankhya.com.br/hc/article_attachments/37694182555415)![Imagem 9: (2) Caso não esteja executando, acesse o "Explorador de arquivos" e navegue até o caminho anotado na instalação…](https://ajuda.sankhya.com.br/hc/article_attachments/37694182558231)

**(3)** Acesse a pasta **"Sankhya web"** **"Sankhya\_web\_connectionx64"** **"executar"** **"web\_connection.exe"**:

- Entre em **"Sankhya web".**

  ![Imagem 10: Entre em "Sankhya web".](https://ajuda.sankhya.com.br/hc/article_attachments/37694185144727)
- Acesse **"Sankhya\_web\_connectionx64"** e **"executar".**

  ![Imagem 11: Acesse "Sankhya_web_connectionx64" e "executar".](https://ajuda.sankhya.com.br/hc/article_attachments/37694185145751)
- Clique em **"web\_connection.exe".**

  ![Imagem 12: Clique em "web_connection.exe".](https://ajuda.sankhya.com.br/hc/article_attachments/37694182560279)

**OBSERVAÇÃO:** Se aparecer o erro **"Porta configurada para WebConnection em uso"**, reconfigure a porta ou feche o aplicativo utilizando a porta: 9096. Web connection será fechado.

- Nesse caso, se o navegador Sankhya estiver aberto e nele estiverem usando o WebConnection embarcado, é provável que seja ele que está usando a porta. Basta fechar o navegador Sankhya e tentar executar o Web Connection novamente.
- Se não for o navegador sankhya, pode ser outro aplicativo. Nesse caso, procure o TI da empresa para verificar qual aplicativo e se é possível trocar a porta ou fechar o aplicativo.

- **Configuração final do WebConnection:**

**(1)** Faça login com o usuário **"SUP"** ou outro usuário sem restrição de acesso por computadores liberados.

**(2)** Abra a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas) e tente imprimir uma nota.

![Imagem 13: (2) Abra a tela "Portal de Vendas" (Comercial » Consulta » Portal de Vendas) e tente imprimir uma nota.](https://ajuda.sankhya.com.br/hc/article_attachments/37694182568855)

**(3)** No pop-up que abrir, clique em **"Configurar automaticamente".**

![Imagem 14: (3) No pop-up que abrir, clique em "Configurar automaticamente".](https://ajuda.sankhya.com.br/hc/article_attachments/37694182569367)

**(4)** Clique em **"Avançadas"** no próximo pop-up.

![Imagem 15: (4) Clique em "Avançadas" no próximo pop-up.](https://ajuda.sankhya.com.br/hc/article_attachments/37694185159319)

**(5)** Clique em **"Ir para localhost (não seguro)"**.

![Imagem 16: (5) Clique em "Ir para localhost (não seguro)" .](https://ajuda.sankhya.com.br/hc/article_attachments/37694182571543)

**(6)** Confirme a configuração quando aparecer a mensagem de sucesso.

![Imagem 17: (6) Confirme a configuração quando aparecer a mensagem de sucesso.](https://ajuda.sankhya.com.br/hc/article_attachments/37694185160855)

**(7)** Teste a impressão novamente para verificar se as impressoras aparecem.

![Imagem 18: (7) Teste a impressão novamente para verificar se as impressoras aparecem.](https://ajuda.sankhya.com.br/hc/article_attachments/37694182572823)

(8)** Para o Chrome:** Libere a permissão de acesso à rede local.

![Imagem 19: (8) Para o Chrome: Libere a permissão de acesso à rede local.](https://ajuda.sankhya.com.br/hc/article_attachments/37694185161879)![Imagem 20: (8) Para o Chrome: Libere a permissão de acesso à rede local.](https://ajuda.sankhya.com.br/hc/article_attachments/37694182573591)

**(9)** Deslogue do usuário usado para configuração e teste o login com o usuário que possui restrição de acesso.

**OBSERVAÇÃO:**

- As versões mais recentes do Chrome e Edge não aceitam conexões via HTTP, portanto o WebConnection não consegue se conectar nessas condições.
- Como solução definitiva recomendamos verificar com o datacenter ou com a equipe de TI da empresa a possibilidade de migrar a base para HTTPS.
- Como solução paliativa, pode usar o navegador sankhya. Assim, é possível utilizar o WebConnection por meio dele enquanto a migração para HTTPS não é realizada.

**CAUSA**

O erro ocorre devido às seguintes situações:

- **Web Connection não instalado** na máquina do usuário.
- **Configuração incompleta** do Web Connection após a instalação.
- **Incompatibilidade do navegador** - versões mais recentes do Chrome não aceitam conexões via HTTP, sendo necessário usar HTTPS.
