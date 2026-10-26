---
id: "25415945938839"
titulo: "Erro na geração XML de NF-e em navegadores externos (Google Chrome, Edge, entre outros)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25415945938839-Erro-na-gera%C3%A7%C3%A3o-XML-de-NF-e-em-navegadores-externos-Google-Chrome-Edge-entre-outros"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-08-17T13:44:43Z"
rotulos: ["Configuração", "Segurança", "NF-e", "Portal de Vendas", "XML", "Erro na geração XML de NF-e no Navegador Google Chrome", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Google Chrome"]
---

# Erro na geração XML de NF-e em navegadores externos (Google Chrome, Edge, entre outros)

**Mensagem**
Ao tentar gerar, visualizar ou baixar o arquivo XML de uma nota fiscal emitida através do navegador Google Chrome, o arquivo não é gerado, o download não é iniciado ou ocorre o download automático sem a exibição esperada. Ao utilizar o Navegador Sankhya, a funcionalidade opera normalmente.

**Situação**
Esta situação ocorre quando o usuário acessa o sistema Sankhya (como no **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas)) e tenta gerar ou processar o XML de NF-e/NFS-e utilizando o navegador Google Chrome. O navegador pode bloquear a ação de geração ou forçar o download automático do arquivo para a pasta local, impedindo o processamento correto dentro do sistema.

**Solução**
Para resolver este problema, configure as permissões de segurança do Google Chrome especificamente para o endereço da sua base Sankhya:

**(1)** Abra o Google Chrome e acesse as **"Configurações"** (clique nos três pontos no canto superior direito).

**(2)** No menu lateral, clique em **"Privacidade e Segurança"** e depois em **"Configurações de Site"**.

**(3)** Role a página até encontrar **"Pop-ups e redirecionamentos"** e clique em **"Adicionar"** no campo **"Permitir"**, inserindo o endereço completo da sua base (exemplo: suaempresa.sde.sankhya.com.br/mge).

**(4)** Clique no botão de **"Play"** ou nas configurações do site adicionado e localize o campo **"Conteúdo não seguro"**, selecionando a opção **"Permitir"**.

**(5)** Certifique-se de que a opção **"Downloads automáticos"** esteja definida como **"Permitir"** para o endereço do sistema.

**(6)** Feche e abra o navegador para aplicar as alterações e tente gerar o XML novamente.

**(7)** Confira no gif abaixo o passo a passo:
![Imagem 1: (1) Abra o Google Chrome e acesse as "Configurações" (clique nos três pontos no canto superior direito). (2) No menu…](https://ajuda.sankhya.com.br/hc/article_attachments/25415945932439)

### Configuração do WebConnection

Em alguns casos, é necessário utilizar o **"WebConnection"**. Certifique-se de que o aplicativo está instalado e ativo em segundo plano (bandeja do sistema). O Chrome pode marcar a conexão com o **"WebConnection"** como "Não segura" por ser uma aplicação externa; este é um comportamento esperado.

**Observações importantes:**

- Caso utilize o sistema em múltiplos ambientes, adicione cada um individualmente nas permissões.
- Após atualizações do Chrome, pode ser necessário revisar essas configurações.
- Se o problema persistir, verifique se sua base utiliza protocolo http. A solução definitiva, neste caso, é a migração para https.

**Causa**

O problema ocorre devido às políticas de segurança do Google Chrome, que atualmente possuem regras mais rígidas para bloqueio de downloads automáticos, pop-ups, redirecionamentos e conteúdos considerados não seguros (HTTP).

Como o sistema utiliza essas funcionalidades durante o processamento dos arquivos XML, o navegador pode interpretar a ação como um possível risco e, consequentemente, bloquear a execução automaticamente.
