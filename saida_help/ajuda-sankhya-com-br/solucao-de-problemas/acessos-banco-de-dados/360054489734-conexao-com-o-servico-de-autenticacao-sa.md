---
id: "360054489734"
titulo: "Conexão com o serviço de autenticação (SAS) não estabelecida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360054489734-Conex%C3%A3o-com-o-servi%C3%A7o-de-autentica%C3%A7%C3%A3o-SAS-n%C3%A3o-estabelecida"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T15:28:04Z"
rotulos: ["Configuração", "Servidor", "Preferências", "CORE_E01960", "conexão servidor solução", "Erro", "SAS"]
---

# Conexão com o serviço de autenticação (SAS) não estabelecida

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18522976797591) MENSAGEM**:

Conexão com o serviço de autenticação (SAS) não estabelecida.

**![Imagem 2: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18522983405463) CAUSA**:

Ocorre quando ocorreu a interrupção entre o servidor do SAS e o servidor da Aplicação, geralmente ocasionado quando o SAS não está iniciado.

**![Imagem 3: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/18522983262231) SOLUÇÃO**:

- **SERVIDOR LOCAL:**

![Imagem 4: Acesse a tela 'Preferências' (Configurações» Avançado» Preferências) e verifique se o IP do Servidor onde está…](https://ajuda.sankhya.com.br/hc/article_attachments/18522983265815) Acesse a tela 'Preferências' (Configurações» Avançado» Preferências) e verifique se o IP do Servidor onde está instalado o SAS, parâmetro: **IPSERVACESS**-IP do servidor de acessos (SAS) está configurado corretamente.

**![Imagem 5: Se o servidor do SAS é WINDOWS , acesse os Serviços do Windows e verifique se o SAS está iniciado, se não estiver,…](https://ajuda.sankhya.com.br/hc/article_attachments/18522976813335) Se o servidor do SAS é WINDOWS**, acesse os Serviços do Windows e verifique se o SAS está iniciado, se não estiver, inicie o mesmo.

[GIF animado: Imagem 6: Se o servidor do SAS é WINDOWS , acesse os Serviços do Windows e verifique se o SAS está iniciado, se não estiver,…](https://ajuda.sankhya.com.br/hc/article_attachments/360094326153)

- **Para mais detalhes: [Indisponibilidade SAS - Como tratar em ambiente Windows ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616013)**

**![Imagem 7: Se o servidor do SAS é LINUX , acesse o prompt de comando do Linux, geralmente através do aplicativo putty, e execute o…](https://ajuda.sankhya.com.br/hc/article_attachments/18522983290135) Se o servidor do SAS é LINUX**, acesse o prompt de comando do Linux, geralmente através do aplicativo putty, e execute o comando para iniciar o SAS. Se logado com o usuário MGEWEB, identifique a pasta de instalação do SAS e execute conforme instruções abaixo.

[GIF animado: Imagem 8: Se o servidor do SAS é LINUX , acesse o prompt de comando do Linux, geralmente através do aplicativo putty, e execute o…](https://ajuda.sankhya.com.br/hc/article_attachments/360094327653)

- Para mais detalhes: [Indisponibilidade SAS - Como tratar em ambiente Linux ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043983954)

![Imagem 9: Após iniciar o SAS, tente um novo acesso ao sistema. Caso o erro persista, acione imediatamente a equipe de suporte…](https://ajuda.sankhya.com.br/hc/article_attachments/18522983307159) Após iniciar o SAS, tente um novo acesso ao sistema. Caso o erro persista, acione imediatamente a equipe de suporte através dos canais de comunicação disponíveis.

- **SERVIDOR CLOUD SANKHYA:**

![Imagem 10: Acessar o portal de Ajuda Sankhya: Clique Aqui!](https://ajuda.sankhya.com.br/hc/article_attachments/18522983265815) Acessar o portal de Ajuda Sankhya:  [Clique Aqui!](https://ajuda.sankhya.com.br/hc/pt-br)

![Imagem 11: Efetuar login através da opção "Entrar". Caso seja seu primeiro login, clique em "Esqueci minha senha" e realize a…](https://ajuda.sankhya.com.br/hc/article_attachments/18522976813335) Efetuar login através da opção "Entrar". Caso seja seu primeiro login, clique em "Esqueci minha senha" e realize a criação de sua senha de acesso.

![Imagem 12: Efetuar login através da opção "Entrar". Caso seja seu primeiro login, clique em "Esqueci minha senha" e realize a…](https://ajuda.sankhya.com.br/hc/article_attachments/4418139045143)

![Imagem 13: Clicar em “Abrir Chamado”:](https://ajuda.sankhya.com.br/hc/article_attachments/18522983290135) Clicar em “Abrir Chamado”:

![Imagem 14: Clicar em “Abrir Chamado”:](https://ajuda.sankhya.com.br/hc/article_attachments/18522983319191)

![Imagem 15: Preencher os “Campos Obrigatórios” (“Assunto”, “Descrição”, “Categoria”, "prioridade”, “Versão do Sistema” e “Versão do…](https://ajuda.sankhya.com.br/hc/article_attachments/18522983307159) Preencher os “Campos Obrigatórios” (“Assunto”, “Descrição”, “Categoria”, "prioridade”, “Versão do Sistema” e “Versão do Banco de Dados”);

![Imagem 16: Marcar o campo “Estou enfrentando indisponibilidade” , conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/18522983349655) Marcar o campo **“Estou enfrentando indisponibilidade”**, conforme imagem abaixo:

![Imagem 17: Marcar o campo “Estou enfrentando indisponibilidade” , conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/18522976887319)

![Imagem 18: Incluir mensagens de erro e anexos conforme desejar e clicar no botão “Enviar”:](https://ajuda.sankhya.com.br/hc/article_attachments/18522976904599) Incluir mensagens de erro e anexos conforme desejar e clicar no botão “Enviar”:

Após esse procedimento nossa equipe técnica será acionada imediatamente e você receberá um retorno o mais rápido possível.

- **SERVIDOR TERCEIROS (FMC Direto, CCM, Ativy etc)**

Acionar o parceiro responsável pelo ambiente e solicitar que a conexão com o SAS seja reestabelecida;
