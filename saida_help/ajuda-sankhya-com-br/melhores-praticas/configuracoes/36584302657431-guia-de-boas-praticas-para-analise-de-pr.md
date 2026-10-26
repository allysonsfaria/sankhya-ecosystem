---
id: "36584302657431"
titulo: "Guia de Boas Práticas para Análise de Problemas com Jobs"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36584302657431-Guia-de-Boas-Pr%C3%A1ticas-para-An%C3%A1lise-de-Problemas-com-Jobs"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T14:22:45Z"
rotulos: ["Configuração", "Servidor", "Parâmetros", "Parâmetro", "SERVERHOSTSCHED", "Sankhya", "JOBs", "Resolução de Problemas"]
---

# Guia de Boas Práticas para Análise de Problemas com Jobs

**SITUAÇÃO:**

Este artigo tem por objetivo apresentar as situações mais comuns relacionadas à execução de **JOBs** no sistema Sankhya, além de orientar na identificação das causas e na correta resolução desses problemas.

Entre os cenários observados destacam-se com maior frequência:

- JOBs que não estão sendo executados.
- Ações agendadas que não geram o JOB correspondente no servidor.
- Falhas no envio de e-mails, acompanhadas da ausência de registros de tentativa na fila de processamento.

**SOLUÇÃO:**

As orientações abaixo reúnem as principais **verificações** e **ajustes** necessários para corrigir problemas comuns relacionados á **execução de JOBs** no sistema Sankhya:

#### 1. Valide os argumentos de inicialização do servidor

Alguns argumentos definidos no servidor WildFly podem impedir ou restringir a execução dos JOBs, como:

- `-Dsankhyaw.schedule.disable=true`

Impede a execução de todos os JOBs.

- `-Dsankhyaw.only.jobs=`

Restringe a execução aos JOBs especificados.

#### 2. Execute apenas os JOBs desejados:

Os argumentos devem ser configurados nos arquivos:

- `standalone.conf` (Linux)
- `standalone.conf.bat` (Windows)

Esses arquivos ficam, geralmente, no diretório:

`wildfly_producao/bin/` (Tanto para Windows quanto para Linux)

**Exemplo de uso**:

- Para permitir a execução de **apenas um JOB**:

`-Dsankhyaw.only.jobs=-22005`

- Para executar vários **JOBs específicos**:

`-Dsankhyaw.only.jobs=-22005,-22010,-22015`

Somente os JOBs listados serão executados.

**OBSERVAÇÃO:** após a alteração nos argumentos de inicialização, é obrigatória a reinicialização do servidor.

#### 3. Verifique o parâmetro SERVERHOSTSCHED:

Este parâmetro define onde os JOBs devem ser executados:

- **Vazio**

Os JOBs serão executados no servidor local.

- **Apenas IP**

Todos os JOBs serão direcionados ao servidor especificado.

- **"IP:NomeDoJob"**

Somente os JOBs listados serão executados no servidor informado.

#### 4. Verifique a tela "Controle de JOBs":

**(1)** Acesse a tela [**''Controle de JOBs''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594634-Controle-de-Jobs) (Configurações » Avançado » Controle de Jobs).

**(2)** Valide a **última data de execução** de cada JOB.

**(3)** Valide a existência de JOBs com **falhas registradas**, **longos intervalos sem execução** ou **status incorretos**.

#### 5. Revise os parâmetros complementares:

Alguns parâmetros influenciam diretamente rotinas de envio de mensagens, como:

- `QTDENVIOMSGJOB`

Define o número de mensagens processas por execução. (Padrão:50).

- `MSDINTAGENDADOR`

Define o intervalo, em minutos, para execução do job de envio de mensagens (Padrão:1 minuto).

#### 6. Ambientes de teste:

**(1)** Evite ativar todos os JOBs ao mesmo tempo.

**(2)** Utilize o argumento `-Dsankhyaw.only.jobs` para liberar somente os JOBs necessários às suas validações.

##### CAUSA:

As falhas na execução de JOBs geralmente ocorrem por **configurações incorretas no servidor** ou nos **parâmetros do sistema**. As causas mais comuns incluem:

- Argumentos de inicialização configurados incorretamente, como, `-Dsankhyaw.schedule.disable=true` bloqueando todos os JOBs e `-Dsankhyaw.only.jobs`, restringindo a execução sem intenção.
- Parâmetro **''SERVERHOSTSCHED''** configurado incorretamente, levando ao direcionamento dos JOBs para um servidor errado ou inexistente, falta de alinhamento entre o servidor configurado e o ambiente em uso, e configurações no formato “IP:NomeDoJob”, que limitam a execução apenas aos JOBs informados, geralmente sem que o usuário perceba.
- Parâmetros operacionais inconsistentes, como `QTDENVIOMSGJOB` e `MSDINTAGENDADOR`, afetando rotinas de envio de mensagens.
- Ambientes de teste configurados com todos os JOBs ativos, causando sobrecarga, processos indevidos e interferência nas validações.

Essas causas, isoladas ou em conjunto, podem prejudicar a execução dos JOBs e impactar rotinas que dependem deles.
