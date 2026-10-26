---
id: "360044351353"
titulo: "Como definir o tempo de inatividade no sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044351353-Como-definir-o-tempo-de-inatividade-no-sistema"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-09-03T13:26:03Z"
rotulos: ["#PUBLIFER", "#ValidadoHelp", "Configuração", "Segurança", "Configurando Tempo de Inatividade", "SankhyaOm", "Sessão"]
---

# Como definir o tempo de inatividade no sistema

**(1)** O **SankhyaOm** dispõe de um recurso de Time Out que consiste na definição de um período limite em que se a conexão do banco permanecer sem movimentação, esta conexão será encerrada automaticamente (logout), liberando para que um novo usuário possa acessar o sistema.

O time out é definido através do parâmetro **"Tempo máximo sessão inativa (em minutos) - SESSIONTIMEOUT":**

![Imagem 1: O time out é definido através do parâmetro "Tempo máximo sessão inativa (em minutos) - SESSIONTIMEOUT":](https://ajuda.sankhya.com.br/hc/article_attachments/14660171629975)

**![Imagem 2: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16832197478935) OBSERVAÇÃO:**

**(1)** O período definido no parâmetro é em minutos, e poderá haver uma diferença de até 5 minutos para iniciar o processo, ou seja, se o valor do parâmetro for 1, o logout poderá acontecer entre 1 e 6 minutos.

**(1)** Quando atingido o tempo máximo de inatividade do sistema configurado no parâmetro, será apresentada no topo da aplicação uma contagem regressiva de 15 segundos, que ao final realiza a saída do sistema automaticamente. Durante esta contagem, pode-se clicar no link **"Não cancele minha sessão, ainda estou aqui!",** evitando assim o processo de logout.

**(1)** Existe uma margem de erro de até 1 min para o tempo configurado.

![Imagem 3: Nota: Se o valor do parâmetro for "0" (zero), a sessão nunca irá expirar.](https://ajuda.sankhya.com.br/hc/article_attachments/16832138198167) **Nota:** Se o valor do parâmetro for "0" (zero), a sessão nunca irá expirar.

(1)** Time Out por usuário:**

Além do parâmetro global, pode-se especificar o timeout por usuário através do campo **"Tempo de Aplicativo inativo para finalizar",** localizado na aba **"Segurança",** do [Cadastro de Usuários:](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025239834-Usu%C3%A1rios)

![Imagem 4: Além do parâmetro global, pode-se especificar o timeout por usuário através do campo "Tempo de Aplicativo inativo para…](https://ajuda.sankhya.com.br/hc/article_attachments/14660226300311)

O sistema verifica se o usuário logado possui o campo informado, e se possuir, o mesmo é considerado ao invés do parâmetro de chave SESSIONTIMEOUT. O correto uso desse parâmetro, em conjunto com o campo no Cadastro de Usuários, é informar um tempo maior no SESSIONTIMEOUT e um tempo menor no cadastro de usuário. Desta maneira, o aviso questionando se o usuário ainda está utilizando o sistema será apresentado antes do tempo do parâmetro global. O contrário disso, a sessão do usuário irá expirar sem dar o aviso ao mesmo.
