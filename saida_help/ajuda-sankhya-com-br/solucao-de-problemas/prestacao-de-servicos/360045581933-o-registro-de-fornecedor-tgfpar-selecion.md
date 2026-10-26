---
id: "360045581933"
titulo: "O registro de fornecedor TGFPAR selecionado não está cadastro ou não está ativo ou não é analítico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045581933-O-registro-de-fornecedor-TGFPAR-selecionado-n%C3%A3o-est%C3%A1-cadastro-ou-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico"
trilha: "Solução de Problemas > Prestação de Serviços"
atualizado_em: "2026-07-22T15:33:13Z"
rotulos: ["Configuração", "Parceiro", "Contrato", "Financeiro", "SQL 50001", "Verifique contratos com campo \"ATIVO\" = 'NÃO'", "Ative o contrato ou cancele/suspenda produtos/serviços", "Mensagem: Fornecedor não cadastrado ou ativo", "Erro"]
---

# O registro de fornecedor TGFPAR selecionado não está cadastro ou não está ativo ou não é analítico

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16311269889431) MENSAGEM:**

[SQL 50001]: o registro de fornecedor TGFPAR selecionado não está cadastro ou não está ativo ou não é analítico.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16311277226135) SOLUÇÃO:**

Ao executar a rotina de 'Reajuste de Contratos Ativos', caso seja localizado algum contrato com o campo ATIVO=NÃO, porém com produtos/serviços que tenham ocorrências de ativação vigentes, será apresentada a mensagem.

![Imagem 3: Identifique na tela " Contratos " (Caminho de acesso: Contratos e Serviços » Arquivos) os que estão com o campo "ATIVO"…](https://ajuda.sankhya.com.br/hc/article_attachments/16311277228823) Identifique na tela **"[Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos)"** (Caminho de acesso: Contratos e Serviços » Arquivos) os que estão com o campo **"ATIVO"** = 'NÃO'.

![Imagem 4: Dentre esses, localize aqueles que ainda possuem produtos/serviços com ocorrência de ativação vigentes. Ou seja, que…](https://ajuda.sankhya.com.br/hc/article_attachments/16311269903767) Dentre esses, localize aqueles que ainda possuem produtos/serviços com ocorrência de ativação vigentes. Ou seja, que não possuem ocorrências de cancelamento ou suspensão vinculadas.

Localizado o(s) contrato(s) causador(es) da mensagem de validação, alinhe internamente qual o processo adequado:

**(2)** Ative o respectivo contrato ou lance as devidas ocorrências de cancelamento ou suspensão para seus produtos/serviços.

![Imagem 5: Feito isso, será possível executar a rotina de " Reajuste de Contratos Ativos ".](https://ajuda.sankhya.com.br/hc/article_attachments/16311277242519) Feito isso, será possível executar a rotina de **"[Reajuste de Contratos Ativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos)".**

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16311277247511) CAUSA:**

Ao executar a rotina de Reajuste de Contratos Ativos, caso seja localizado algum contrato com o campo ATIVO=NÃO, porém com produtos/serviços que tenham ocorrências de ativação vigentes, será apresentada a mensagem.
