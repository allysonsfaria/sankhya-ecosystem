---
id: "39994756964887"
titulo: "Sistema Lento ou Travado na Tela de Login"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39994756964887-Sistema-Lento-ou-Travado-na-Tela-de-Login"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-09-14T11:51:03Z"
rotulos: ["Configuração", "Servidor", "Log", "Linux", "Sistema lento", "Sistema travado", "Sistema travado na tela de login", "Remover Deploys com Falha", "Reiniciar o sistema", "Identificar e Limpar Logs", "Acúmulo de arquivos de log", "Desempenho", "Windows"]
---

# Sistema Lento ou Travado na Tela de Login

Este artigo descreve os procedimentos para **diagnosticar e resolver problemas de inoperância ou lentidão do sistema,** cenários que **podem ser causados pelo consumo excessivo de espaço em disco no servidor**.

### Sintomas

O ambiente pode apresentar um ou mais dos seguintes comportamentos:

- O sistema não carrega a tela de login ou trava nela, impedindo o acesso;
- O sistema apresenta lentidão extrema em diversas operações;
- Usuários relatam que o processo de login, quando funciona, demora um tempo excessivo (por exemplo, mais de 10 minutos);
- É identificado um consumo rápido e inesperado do espaço de armazenamento no servidor.

### Procedimento para Linux

**(1)** Reinicie o serviço ou servidor

Como primeira ação, realize a reinicialização dos serviços ou do servidor para tentar restabelecer a operação.

**(2)** Valide o uso de memória (Linux)

Execute o comando abaixo para verificar o consumo de memória RAM:

```
free -h
```

**(3)** Valide o uso de disco

Verifique o espaço em disco disponível:

```
df -h
```

Identifique especialmente a partição **/** ou diretórios críticos como **/home**.

Para analisar o consumo dentro de diretórios:

```
du -sh *
```

**(4)** Verifique diretórios com maior consumo

Foque principalmente em:

- Diretórios de logs
- Diretórios de aplicação
- Ambientes de teste/homologação (maior risco de acúmulo)

**(5)** Valide e remova deploys com falha

Acesse o diretório de deployments da aplicação, por exemplo:

```
.../wildfly_producao/standalone/deployments
```

Verifique e remova arquivos com status de falha (**.failed**).

**(6)** Identifique e limpar logs (etapa crítica)

Analise o volume de arquivos de log e remova os que não são mais necessários.

**(7)** Validação final

Após a limpeza:

- Teste o login no sistema;
- Valide a performance geral;
- Confirme normalização do uso de disco.

###

### Procedimento para Windows

**(1)** Acesse **''Este Computador''** e verifique o espaço disponível no disco (geralmente unidade C:).

**(2)** Identifique possíveis diretórios com alto consumo de armazenamento, principalmente pastas de logs da aplicação.

**(3)** Para validar o uso de memória, abra o **''Gerenciador de Tarefas''** (Ctrl + Shift + Esc) e verifique o consumo na aba **“Desempenho”**.

**(4)** Caso necessário, realize a limpeza de arquivos desnecessários para liberar espaço em disco.

####

##### CAUSA:

O erro acontece devido ao acúmulo de arquivos de log, especificamente em uma base de dados de teste. Esse acúmulo compromete o espaço em disco, a performance do sistema e a capacidade de conexão da aplicação.
