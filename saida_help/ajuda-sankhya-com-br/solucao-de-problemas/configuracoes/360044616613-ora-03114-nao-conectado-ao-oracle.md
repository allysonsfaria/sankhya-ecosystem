---
id: "360044616613"
titulo: "ORA-03114: Não conectado ao ORACLE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616613-ORA-03114-N%C3%A3o-conectado-ao-ORACLE"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:48Z"
rotulos: ["Configuração", "MGE", "Oracle", "Correção do Erro de Conexão ao Oracle", "Erro", "Banco de Dados"]
---

# ORA-03114: Não conectado ao ORACLE

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18585041325463) MENSAGEM:**

"General SQL error.
ORA-03114: Não conectado ao ORACLE
Alias: DBNSiade."

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18585024410647) SITUAÇÃO:**

Ao tentar acessar o sistema MGE, ocorre  a mensagem.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18585041404823) CAUSA:**

Ocorre quando as configurações de instalação do client do Oracle estão inadequadas, conforme discorremos acima ou quando a senha do banco de dados esta incorreta. A senha padrão é 'tecsis', se o cliente altera essa senha, se faz necessário ter o arquivo '**license.dat**' na pasta onde esta os executáveis do MGE.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18585024414231) SOLUÇÃO:**

Para correção seguir os passos abaixo:

![Imagem 5: Configuração incorreta do Client do Oracle: Para se certificar de que as configurações estejam corretas, acesse o "Net…](https://ajuda.sankhya.com.br/hc/article_attachments/18585041370263) Configuração incorreta do Client do Oracle:
Para se certificar de que as configurações estejam corretas, acesse o "Net Manager" (na pasta do Client do menu Iniciar, em "Ferramentas de Configuração e Migração"), e localize o nome de serviço de rede configurado: "Configuração do Oracle Net > Local > Nomeação de Serviço.
No nome de serviço, clique na opção "Testar Serviço",

Preencha os dados de usuário e senha para testar novamente. Caso o teste seja bem sucedido, observe as próximas possibilidades.

![Imagem 6: Configuração incorreta do nome de serviço no BDE: No BDE, o campo SERVER NAME que fica em Databases, e que está…](https://ajuda.sankhya.com.br/hc/article_attachments/18585024425367) Configuração incorreta do nome de serviço no BDE:
No BDE, o campo SERVER NAME que fica em Databases, e que está utilizando para acessar o sistema, deverá estar configurado o nome de rede local que é apresentado em "Nomeação de Serviço", indicado no "Net Manager" que vimos no item anterior.

![Imagem 7: Duas ou mais configurações de client na path do Windows - Variavéis de Ambiente Deverá existir apenas uma configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/18585024430871)Duas ou mais configurações de client na path do Windows - Variavéis de Ambiente
Deverá existir apenas uma configuração de client do Oracle na path do Windows. Ela deve indicar a pasta bin, do client do Oracle que está sendo indicado na barra de título do "Net Manager".

![Imagem 8: Falta de permissão na pasta do client do Oracle: O usuário do sistema operacional que acessa o MGE Mitra deve ter…](https://ajuda.sankhya.com.br/hc/article_attachments/18585041385239)Falta de permissão na pasta do client do Oracle:
O usuário do sistema operacional que acessa o MGE Mitra deve ter permissões de gravação na pasta de instalação do client do Oracle.

![Imagem 9: Também é premissa para acesso ao sistema que o UAC do Windows (User Account Control) esteja desabilitado.](https://ajuda.sankhya.com.br/hc/article_attachments/18585024445847)Também é premissa para acesso ao sistema que o UAC do Windows (User Account Control) esteja desabilitado.

![Imagem 10: Solicite que a área de TI ou Administrador de Banco de Dados, revise a senha do banco, seguindo as seguintes…](https://ajuda.sankhya.com.br/hc/article_attachments/18585041392663) Solicite que a área de TI ou Administrador de Banco de Dados, revise a senha do banco, seguindo as seguintes considerações para a senha:

- Máximo de 10 caracteres;
- Uso apenas de caracteres minúsculos;
- Não pode ser utilizado o número 0;
- São aceitos apenas alguns caracteres especiais: !, \*, $, | e &
Depois de usar uma senha dentro do padrão, sera preciso gerar novo arquivo 'license.dat', e inserir este arquivo dentro da pasta do executável do MGE

Caso utilize o Sankhya W. Se refazer a conexão com o banco de dados pelo gerenciador de pacotes
E atualizar a senha no arquivo de configuração do SAS também. (SAS.CFG)

**Abaixo o Link para baixar o Aplicativo:**
