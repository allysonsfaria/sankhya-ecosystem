---
id: "39340252616855"
titulo: "Erro no Cálculo de Décimo Terceiro para Contrato Suspenso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39340252616855-Erro-no-C%C3%A1lculo-de-D%C3%A9cimo-Terceiro-para-Contrato-Suspenso"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-10T15:12:01Z"
rotulos: ["Configuração", "Contrato", "eSocial", "Folha de Pagamento", "FGTS", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no Cálculo de Décimo Terceiro para Contrato Suspenso

**MENSAGEM**

O sistema está calculando décimo terceiro salário para funcionário com contrato suspenso.

**SITUAÇÃO**

Ao processar o cálculo de décimo terceiro salário, o sistema está considerando funcionários que possuem **"contrato suspenso"**, gerando valores indevidos para colaboradores que não deveriam receber este benefício durante o período de suspensão.

**SOLUÇÃO**

Para corrigir o cálculo indevido do décimo terceiro salário, ajuste as configurações da ocorrência de afastamento:

**(1)** Acesse a tela **"Código de Afastamento"** (Pessoal+ » Cadastros » Código de Afastamento).

![Imagem 1: (1) Acesse a tela "Código de Afastamento" (Pessoal+ » Cadastros » Código de Afastamento).](https://ajuda.sankhya.com.br/hc/article_attachments/41081432731799)

**(2)** Localize a ocorrência de afastamento  (**Pessoal+ » Rotinas Folha » Ocorrências )** que foi lançada para o funcionário com contrato suspenso.

**(3)** Identifique as descrições informadas nos campos **"Descrição FGTS"** e **"Descrição RAIS"**.

![Imagem 2: (3) Identifique as descrições informadas nos campos "Descrição FGTS" e "Descrição RAIS" .](https://ajuda.sankhya.com.br/hc/article_attachments/41081432732695)

**(4)** Desmarque a opção **"Direito ao Décimo Terceiro"** para a ocorrência correspondente, na tela "Código de Afastamento"

![Imagem 3: (4) Desmarque a opção "Direito ao Décimo Terceiro" para a ocorrência correspondente, na tela "Código de Afastamento"](https://ajuda.sankhya.com.br/hc/article_attachments/41081432733719)

**(5)** Salve as alterações e recalcule o décimo terceiro salário para validar que o valor não será mais gerado para o funcionário.

**CAUSA**

O erro ocorre porque a ocorrência de afastamento criada para o funcionário estava configurada com a opção **"Direito ao Décimo Terceiro"** marcada. Quando essa configuração está habilitada, o sistema interpreta que o colaborador mantém o direito ao benefício mesmo durante a suspensão do contrato, gerando o cálculo indevido do décimo terceiro salário.
