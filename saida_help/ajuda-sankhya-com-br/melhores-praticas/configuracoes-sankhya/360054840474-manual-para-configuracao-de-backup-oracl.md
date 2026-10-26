---
id: "360054840474"
titulo: "Manual para configuração de Backup Oracle Linux."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360054840474-Manual-para-configura%C3%A7%C3%A3o-de-Backup-Oracle-Linux"
trilha: "Melhores Práticas > Configurações Sankhya"
atualizado_em: "2026-07-22T15:28:00Z"
rotulos: ["Configuração", "Oracle", "Linux", "Configuração de Backup Oracle Linux", "ERP Sankhya", "Backup"]
---

# Manual para configuração de Backup Oracle Linux.

| - Este manual foi criado para **fornecer as principais orientações na configuração da rotina de Backup do ERP Sankhya** para Banco de Dados Oracle - Linux. - Recomendados que essas orientações **sejam seguidas por um profissional de T.I/banco de dados de sua empresa**, na ausência desse vale ressaltar que em caso de dúvidas ou necessidade de apoio para validar essa configuração, um consultor de serviços de sua Unidade será acionado. |
| --- |

### Imagem 1: Download: Download:

- Execute o download do arquivo em anexo ao final desse artigo;

### Imagem 2: Acessar a ferramenta putty, e executar os comandos listados nos tópicos abaixo; Acessar a ferramenta putty, e executar os comandos listados nos tópicos abaixo;

### Imagem 3: Configuração do Backup (Criando a Pasta): Configuração do Backup (Criando a Pasta):

[root@teste ~]# **cd /**

[root@teste /]# **mkdir -p /backup/exports /backup/logs /backup/scripts**

[root@teste /]# **chown  oracle.dba  -R  /backup**

[root@teste /]# **ls -lia /backup**

total 24

4910401 drwxr-xr-x  5 oracle dba 4096 Fev  3 13:21 .

             2 drwxr-xr-x 26 oracle dba 4096 Fev  3 13:21 ..

4910402 drwxr-xr-x  2 oracle dba 4096 Fev  3 13:21 exports

4910403 drwxr-xr-x  2 oracle dba 4096 Fev  3 13:21 logs

4910404 drwxr-xr-x  2 oracle dba 4096 Fev  3 13:21 scripts

###

### Imagem 4: I mportando arquivos para a pasta: Importando arquivos para a pasta:

[root@teste /]# **su -l oracle**

[oracle@teste ~]$ **cd**

[oracle@teste install]$ **cp exp\* estatisticas\* limpa\* snk\* /backup/scripts/**

[oracle@teste install]$ **cd  /backup/scripts/**

[oracle@teste scripts]$**ls -lia**

total 32

2621445 drwxr-xr-x. 2 oracle dba 4096 Jan 22 16:49 .

2621442 drwxr-xr-x. 5 oracle dba 4096 Jan 22 16:49 ..

2621448 -rwxr-xr-x. 1 oracle dba   60 Jan 22 16:49 estatisticas.sh

2621449 -rw-r--r--. 1 oracle dba  332 Jan 22 16:49 estatisticas.sql

2621446 -rwxr-xr-x. 1 oracle dba  530 Jan 22 16:49 expfull.sh

2621447 -rwxr-xr-x. 1 oracle dba  503 Jan 22 16:49 exports.sh

2621451 -rwxr-xr-x. 1 oracle dba  117 Jan 22 16:49 limpa\_trc.sh

### Imagem 5: Automatizar rotina de backup via CRONTAB Automatizar rotina de backup via CRONTAB

[oracle@teste scripts]$ **exit**

[root@teste ~] **cp /home/oracle/oracle /var/spool/cron**

[root@teste ~] **chown oracle.dba /var/spool/cron/oracle**

[root@teste ~] **chmod 600 /var/spool/cron/oracle**

### Imagem 6: Conferir agendamento de backup Conferir agendamento de backup

[root@teste ~]#**su -l oracle**

[oracle@teste ~]$**crontab -l**

**00 11 5 \* \* /backup/scripts/./limpa\_trc.sh**

**30 12,18 \* \* \* /backup/scripts/./exports.sh**

**00 20 \* \* \* /backup/scripts/./expfull.sh**

**00 21 \* \* \* /backup/scripts/./estatisticas.sh**

### Imagem 7: Mudar o nome do arquivo de backup oracle: Mudar o nome do arquivo de backup oracle:

[oracle@teste ~]$**vi /backup/scripts/exports.sh**

Substituir o nome nomecliente pelo nome do cliente, para substituir tecle :

ESC **:** e digite **%s/nomecliente/novonome/g** <ENTER>

Para sair e salvar, Tecle ESC e em seguida tecle **:wq**

[oracle@teste ~]**i /backup/scripts/expfull.sh**

Substituir o nome nomecliente pelo nome do cliente, para substituir tecle :

ESC **:** e digite **%s/nomecliente/novonome/g** <ENTER>

Para sair e salvar, Tecle ESC e em seguida tecle **:wq**

### Imagem 8: Validação: Validação:

Para validar se realmente o backup está funcionando, programe no crontab um horário próximo, como por exemplo daqui 2 minutos, e verifique se foi executado.

[oracle@teste ~]$ **crontab -e**

**00 11 5 \* \* /backup/scripts/./limpa\_trc.sh**

**35** **17,18 \* \* \* /backup/scripts/./exports.sh**

**00 20 \* \* \* /backup/scripts/./expfull.sh**

**00 21 \* \* \* /backup/scripts/./estatisticas.sh**

[oracle@teste ~]$ **cd /backup/exports**

[oracle@teste ~]$  **ll** **(localizar backup com o horário de 17:35)**

![Imagem 9: (oracle@teste ~)$ ll (localizar backup com o horário de 17:35)](https://ajuda.sankhya.com.br/hc/article_attachments/360092783494)

- **Anexos:**
