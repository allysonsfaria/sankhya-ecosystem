---
id: "44238369720727"
titulo: "PROD_E00447: Para um Processo Produtivo de Desmonte ser válido, o Produto (PA) XX e Controle (PA) deve existir no Processo de Produção Relacionado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44238369720727-PROD-E00447-Para-um-Processo-Produtivo-de-Desmonte-ser-v%C3%A1lido-o-Produto-PA-XX-e-Controle-PA-deve-existir-no-Processo-de-Produ%C3%A7%C3%A3o-Relacionado"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-10-15T15:02:05Z"
---

# PROD_E00447: Para um Processo Produtivo de Desmonte ser válido, o Produto (PA) XX e Controle (PA) deve existir no Processo de Produção Relacionado.

**Mensagem**

[PROD\_E00447]: Para um Processo Produtivo de Desmonte ser válido, o Produto (PA) XX e Controle (PA) deve existir no Processo de Produção Relacionado.

**Situação**

Ao realizar um versionamento ou inclusão de produtos, na tela **"Composição do Produto"** (Produção » Cadastros » Composição do Produto), é apresentado a mensagem acima.

**Solução**

**(1)** Verifique se o **produto que está sendo incluído ou versionado no processo de desmonte** possui uma composição cadastrada no **processo produtivo relacionado (processo de produção)**.

**(2)** Caso a composição do produto não esteja vinculada ao processo produtivo relacionado, será necessário avaliar a situação:

- **Produto não cadastrado no processo de produção:** Verifique se a ausência da composição é indevida. Caso seja necessário, realize a inclusão do produto no processo produtivo correspondente.
- **Produto cadastrado indevidamente no processo de desmonte:** Acesse a tela **"Processo Produtivo - NOVA"** (Produção » Cadastros » Processo Produtivo - Nova) e realize o versionamento do processo. Em seguida, retorne à tela **"Composição do Produto"** e exclua a nova versão gerada da composição do produto, evitando que ela seja utilizada nas versões posteriores do processo de desmonte.

**Causa**

A mensagem é apresentada quando o **produto vinculado ao processo de desmonte não está cadastrado no processo produtivo relacionado**.
