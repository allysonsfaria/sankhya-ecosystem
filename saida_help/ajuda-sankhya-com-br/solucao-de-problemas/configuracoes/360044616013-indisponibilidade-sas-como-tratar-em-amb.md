---
id: "360044616013"
titulo: "Indisponibilidade SAS - Como tratar em ambiente Windows "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616013-Indisponibilidade-SAS-Como-tratar-em-ambiente-Windows"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:33Z"
rotulos: ["Configuração", "Log", "Serviços", "parou de funcionar", "Tratando a Indisponibilidade do SAS no Windows", "Erro", "Windows", "SAS"]
---

# Indisponibilidade SAS - Como tratar em ambiente Windows 

SAS (Serviço de acesso ao sistema) é um serviço de gerenciamento de licenças do sistema. Com base nesse serviço é possível acesso a telas/serviços contratados pelo cliente.

**Principais análises relacionadas a indisponibilidade SAS em ambiente Windows:**

![Imagem 1: Abra o 'Serviços' do Windows:](https://ajuda.sankhya.com.br/hc/article_attachments/18001988417943) Abra o 'Serviços' do Windows:

- Opção 1: Pesquise na barra de tarefas: services.msc
- Opção 2: Gerenciador de Tarefas >> Arquivo >> Nova Tarefa: services.msc

![Imagem 2: Com os Serviços do Windows aberto verifique se o serviço SAS está iniciado:](https://ajuda.sankhya.com.br/hc/article_attachments/18001988427415) Com os Serviços do Windows aberto verifique se o serviço **SAS** está iniciado:

No cenário abaixo, onde a coluna 'Status' encontra-se diferente de 'Em Execução', identifica-se que o SAS está parado:

![Imagem 3: Para iniciar o serviço clique na opção 'Iniciar o serviço' ou clique com o botão direito do mouse e escolha iniciar:](https://ajuda.sankhya.com.br/hc/article_attachments/18001998738839) Para iniciar o serviço clique na opção 'Iniciar o serviço' ou clique com o botão direito do mouse e escolha iniciar:

![Imagem 4: Aguarde enquanto a inicialização acontece:](https://ajuda.sankhya.com.br/hc/article_attachments/18001988442519) Aguarde enquanto a inicialização acontece:

![Imagem 5: Cerifique-se que o 'Status' foi atualizado para 'Em execução':](https://ajuda.sankhya.com.br/hc/article_attachments/18001998760087) Cerifique-se que o 'Status' foi atualizado para 'Em execução':

![Imagem 6: Cerifique-se que o 'Status' foi atualizado para 'Em execução':](https://ajuda.sankhya.com.br/hc/article_attachments/360060105474)

-----------------------------------------------------------------------------------------------------

**Verificando informações no log do SAS:**

![Imagem 7: Localize o local de instalação do SAS:](https://ajuda.sankhya.com.br/hc/article_attachments/18001988417943) Localize o local de instalação do SAS:

Será exibido o caminho de instalação do SAS:

![Imagem 8: Localize o diretório acima, até encontrar a pasta do SAS, dentro da pasta existirá a pasta log:](https://ajuda.sankhya.com.br/hc/article_attachments/18001988427415) Localize o diretório acima, até encontrar a pasta do SAS, dentro da pasta existirá a pasta log:

![Imagem 9: Acesse a pasta 'log':](https://ajuda.sankhya.com.br/hc/article_attachments/18001998738839) Acesse a pasta 'log':

**Observação:** poderão existir vários logs, o log está com essa definição:

- server é o log do servidor SAS por exemplo: server”ano””mês””dia”-”hora””minuto”.log
- Realize a análise do log mais recente, ou seja, o que você acabou de iniciar o serviço;

Analisando o log do SAS abrindo o arquivo com o notepad ou notepad++  “server”ano””mês””dia”-”hora””minuto”.log”, será aberto o arquivo de log por exemplo:

Atente-se a informação:

Significa que a conexão do SAS com o banco de dados está pronta “ready”.Nesse caso está tudo certo, caso não apresente a informação “ready”, verifique se o banco de dados está iniciado.
