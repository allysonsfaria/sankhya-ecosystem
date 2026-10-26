---
id: "39377117510679"
titulo: "Erro CORE_E06695 - Não possui quantidade de itens pendentes para devolução."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39377117510679-Erro-CORE-E06695-N%C3%A3o-possui-quantidade-de-itens-pendentes-para-devolu%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-08-17T01:24:14Z"
rotulos: ["DUVIDANF", "NF-e", "Portal de Vendas", "Estoque", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# Erro CORE_E06695 - Não possui quantidade de itens pendentes para devolução.

**MENSAGEM**

[CORE\_E06695] Não possui quantidade de itens pendentes para devolução, verifique em **"Outras Opções"** no menu **"Documentos Relacionados"**.

**SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta emitir uma nota fiscal de devolução ou retorno de remessa através do **"Portal de Vendas"** (Comercial Consulta Portal de Vendas) ou **"Portal de Compras"** (Comercial Consulta Portal de Compras). O sistema impede a operação indicando que não existem itens pendentes para devolução no documento de origem selecionado.

**SOLUÇÃO**

A solução varia conforme o cenário identificado. Verifique qual situação se aplica ao seu caso:

**Cenário 1: Devolução já foi gerada anteriormente**

**(1)** Acesse o **"Portal de Vendas"** (Comercial Consulta Portal de Vendas) ou **"Portal de Compras"** (Comercial Consulta Portal de Compras), conforme o tipo de operação.
**(2)** Localize a nota fiscal de origem que está tentando devolver.
**(3)** Clique em **"Outras Opções"** e acesse o menu **"Documentos Relacionados"**.
**(4)** Verifique se a nota de devolução já foi gerada e está pendente de confirmação ou autorização.
**(5)** Caso a devolução esteja pendente, prossiga com o faturamento selecionando os itens corretos e confirme a operação.

**Cenário 2: Devolução anterior foi estornada e precisa ser desvinculada**

Quando uma nota de devolução foi emitida, mas posteriormente estornada (por não ter sido enviada dentro do prazo legal), o sistema mantém o vínculo entre a nota de origem e a devolução estornada, impedindo nova devolução.

**(1)** Identifique o número único (NUNOTA) da nota de origem e da devolução estornada.
**(2)** Solicite ao suporte técnico a retirada da vinculação entre a nota de origem e a devolução estornada através de ajuste via banco de dados.
**(3)** Após o ajuste, realize novamente o processo de emissão da nota de devolução.

**CAUSA**

O erro CORE\_E06695 ocorre quando o sistema identifica que:

- A devolução já foi gerada anteriormente para a nota de origem, estando pendente de confirmação ou autorização;
- Existe um vínculo ativo entre a nota de origem e uma devolução anterior (mesmo que estornada), impedindo nova devolução;
- Todos os itens da nota de origem já foram totalmente devolvidos, não restando quantidade pendente para nova devolução.

O sistema realiza essa validação para evitar devoluções duplicadas e garantir a integridade do controle de estoque e dos documentos fiscais.
