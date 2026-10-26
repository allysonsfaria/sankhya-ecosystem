---
id: "29778847759383"
titulo: "Guia completo para a migração definitiva SaaS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29778847759383-Guia-completo-para-a-migra%C3%A7%C3%A3o-definitiva-SaaS"
trilha: "Modalidade SaaS > SaaS"
atualizado_em: "2026-10-15T17:33:50Z"
rotulos: ["Configuração", "Produção", "Backup e Dados Homologação e Testes Migração para SaaS", "Homologação", "Saas", "Backup", "Migração"]
---

# Guia completo para a migração definitiva SaaS

![Imagem 1: Backup / Criação de Ambiente de Homologação e Testes:](https://ajuda.sankhya.com.br/hc/article_attachments/29778816250263) Backup / Criação de Ambiente de Homologação e Testes:

![Imagem 2: Backup / Criação de Ambiente de Homologação e Testes:](https://ajuda.sankhya.com.br/hc/article_attachments/29778816253207)

**(1)** **Recolha os dados necessários:**

**(2)**Solicite ao seu datacenter ou responsável de TI os seguintes itens:

- Backup do banco de dados no formato datapump;
- Backup da pasta aplicação (toda a pasta do Sankhya OM);
- Log de exportação do backup no formato .log.
- Resultados das consultas abaixo para a base de produção:

**-- Quantidade de objetos inválidos:**
select COUNT(\*) from USER\_objects where STATUS='INVALID';

**-- Lista de objetos inválidos:**
select object\_name from USER\_objects where STATUS='INVALID';

**-- Quantidade de tabelas:**
select COUNT(\*) from user\_objects where object\_type='TABLE';

**-- Quantidade total de constraints:**
select count(\*) from USER\_CONSTRAINTS ;

**-- Quantidade total de constraints desabilitadas:**
select \* from USER\_CONSTRAINTS where STATUS='DISABLE';

**-- Quantidade de índices:**
select COUNT(\*) from USER\_INDEXES;

**-- Triggers desabilitadas:**
select TRIGGER\_NAME,STATUS from USER\_TRIGGERS where status <> 'ENABLED';

**-- Caminho do repositório da aplicação:**

select TEXTO from tsipar where chave like '%DIRMOD%';
select TEXTO from tsipar where chave like '%FREPBASEFOLDER%';

(1)** Envie os dados**
Encaminhe todos os dados solicitados para o e-mail: [sankhyasaas@sankhya.com.br](https://sankhyasaas@sankhya.com.br)

**(1)** **Homologação do sistema**

Nossa equipe criará um ambiente de homologação para que realizem os testes necessários e validem se as telas e rotinas estão funcionando corretamente.

**(2)Ações importantes durante os testes:**
Verifique se não aparecem erros nas rotinas e telas, caso encontre algum erro, responda diretamente ao nosso e-mail, nosso suporte fará a tratativa.

**(1)** **Finalização da homologação e agendamento da migração definitiva**
Se não houver erros ou se todos os problemas forem corrigidos, a etapa de homologação será concluída e agendaremos a migração definitiva.

**Nota:** O ambiente atual pode ser utilizado normalmente. No futuro, solicitaremos um novo backup. Assim que o ambiente de homologação estiver pronto, entraremos em contato por e-mail.

![Imagem 3: Parada da operação durante o processo / Backup / Migração definitiva para o SaaS:](https://ajuda.sankhya.com.br/hc/article_attachments/29778847740311) Parada da operação durante o processo / Backup / Migração definitiva para o SaaS:

![Imagem 4: Parada da operação durante o processo / Backup / Migração definitiva para o SaaS:](https://ajuda.sankhya.com.br/hc/article_attachments/29778847744151)

**(1)** **Parada da Operação, Backup e Migração Definitiva:**

**(2)** Prepare os dados para a migração

**(3)**Solicite ao seu datacenter ou responsável de TI os seguintes itens:

- Backup do banco de dados no formato datapump;
- Backup da pasta aplicação (toda a pasta do Sankhya OM);
- Log de exportação do backup no formato .log;
- Resultados das consultas abaixo para a base de produção:

**-- Quantidade de objetos inválidos:**
select COUNT(\*) from USER\_objects where STATUS='INVALID';

**-- Lista de objetos inválidos:**
select object\_name from USER\_objects where STATUS='INVALID';

**-- Quantidade de tabelas:**
select COUNT(\*) from user\_objects where object\_type='TABLE';

**-- Quantidade total de constraints:**
select count(\*) from USER\_CONSTRAINTS ;

**-- Quantidade total de constraints desabilitadas:**
select \* from USER\_CONSTRAINTS where STATUS='DISABLE';

**-- Quantidade de índices:**
select COUNT(\*) from USER\_INDEXES;

**-- Triggers desabilitadas:**
select TRIGGER\_NAME,STATUS from USER\_TRIGGERS where status <> 'ENABLED';

**-- Caminho do repositório da aplicação:**
select TEXTO from tsipar where chave like '%DIRMOD%';
select TEXTO from tsipar where chave like '%FREPBASEFOLDER%';

**(1)** **Parada da operação**

Durante a migração definitiva, a operação precisará ser interrompida para assegurar a integridade do backup e dos dados.

**(1)** **Envie os dados**

Encaminhe todos os dados solicitados para o e-mail: [sankhyasaas@sankhya.com.br](https://sankhyasaas@sankhya.com.br).

**(1)** **Ambiente de produção**

Nossa equipe configurará o ambiente de produção e, assim que tudo estiver pronto, entraremos em contato por meio do e-mail fornecido.
