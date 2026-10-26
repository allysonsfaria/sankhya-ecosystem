---
id: "4411683161239"
titulo: "ORA-01031: privilégios insuficientes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4411683161239-ORA-01031-privil%C3%A9gios-insuficientes"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:20:59Z"
rotulos: ["Configuração", "Oracle", "não apagar", "#validadoWellingtonBraga", "Solução para Erro de Privilégios Insuficientes no Oracle", "Erro", "Artigo atualizado KCS", "Plataforma - KCS", "Banco de Dados", "DBA", "Privilégios"]
---

# ORA-01031: privilégios insuficientes

**MENSAGEM**

ORA-01031: privilégios insuficientes.

Mensagem apresentada quando a tentativa de acessar um objeto de banco de dados oracle em que o usuário do banco de dados não tem permissão para tal. Geralmente o erro acontece após a restauração de uma base de testes e é exibido ao tentar executar alguma atualização do sistema, compilar objetos ou executar querys, que por exemplo, buscam dados na view v$session. Isso ocorre porque privilégios de sistema, permissões de catálogo e quotas não são exportados automaticamente pelo oracle durante o processo de restauração.

### SOLUÇÃO

**Para seguir com a solução, solicite o auxílio de um profissional de banco de dados (DBA) ou de infraestrutura da empresa.**

Conecte-se ao banco de dados com o usuário sys as sysdba e execute os grants padrão. Veja abaixo o exemplo dos comandos para um usuário teste:

| GRANT RESOURCE, CONNECT TO TESTE / ALTER USER TESTE QUOTA UNLIMITED ON SANKHYA / ALTER USER TESTE QUOTA UNLIMITED ON SANKIND / GRANT SELECT ON DBA\_TABLES TO TESTE / GRANT CREATE SESSION TO TESTE / GRANT SELECT ON DBA\_TAB\_COLUMNS TO TESTE / GRANT SELECT ON DBA\_CONSTRAINTS TO TESTE / GRANT SELECT ON DBA\_TRIGGERS TO TESTE / GRANT SELECT ON DBA\_INDEXES TO TESTE / GRANT SELECT ON DBA\_VIEWS TO TESTE / GRANT SELECT ON DBA\_IND\_COLUMNS TO TESTE / GRANT SELECT ON DBA\_OBJECTS TO TESTE / GRANT SELECT ON V\_$SESSION TO TESTE / |
| --- |

Observação: No exemplo a cima é necessário alterar o "TESTE" para o usuário do banco de dados que está retornando o erro.

Após executar os comandos, valide novamente a execução das rotinas no ambiente de teste.

Importante **⚠️**

Caso seja cliente SaaS (Sankhya Cloud):

Erros de **privilégios insuficientes (ORA-01031 / insufficient privileges)** são ocorrências mais complexas e exigem uma análise técnica diretamente no banco de dados. O envio das informações abaixo ajuda a agilizar a atuação do DBA e reduz significativamente o tempo de investigação.
 
Abrir um chamado e encaminhar:
 
Usuário utilizado para acesso ao banco:(Ex: CUSTOMER\_DDL ou \_DML | NOMEDAEMPRESA\_DDL ou \_DML )
IP/Hostname: (Ex: 10.110.999.1)
Ambiente:(produção ou teste?)
Comando que deu erro:
 
**⚠️ Print completo da tela:** se possível, envie uma captura mais aberta, contendo toda a mensagem de erro e o contexto da operação.
