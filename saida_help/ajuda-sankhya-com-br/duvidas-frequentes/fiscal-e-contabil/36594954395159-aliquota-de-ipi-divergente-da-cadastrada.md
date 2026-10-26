---
id: "36594954395159"
titulo: "Alíquota de IPI divergente da cadastrada no produto ao lançar uma nota. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36594954395159-Al%C3%ADquota-de-IPI-divergente-da-cadastrada-no-produto-ao-lan%C3%A7ar-uma-nota-Como-resolver"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:22:42Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Impostos", "NCM", "Código NCM", "NCM do produto", "Alíquota de IPI", "Lançar nota"]
---

# Alíquota de IPI divergente da cadastrada no produto ao lançar uma nota. Como resolver?

**SITUAÇÃO:**

Ao lançar uma nota fiscal, o sistema pode calcular o IPI utilizando uma alíquota diferente daquela vinculada diretamente no cadastro do produto.

No cadastro de [**''Alíquotas de IPI''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI), a aba ''**NCM''**, que permite configurar alíquotas de forma abrangente para todos os produtos que compartilham o mesmo **código NCM**.

- Quando essa aba está preenchida em uma determinada alíquota, e o **NCM do produto** lançado na nota estiver listado nela, o sistema **prioriza essa configuração** na determinação da alíquota de IPI.

Isso significa que:

- Mesmo que o produto tenha uma alíquota individual cadastrada;
- Se existir uma **alíquota** com **NCM configurado** que contenha o NCM do produto, a **alíquota da aba NCM será utilizada,** prevalecendo sobre a alíquota vinculada ao produto.

Essa funcionalidade permite uma configuração mais eficiente, evitando a necessidade de vincular alíquotas produto a produto.

**SOLUÇÃO:**

Para entender ou ajustar o cálculo do IPI:

**(1)** Acesse a tela **''Alíquota de IPI''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de IPI).

**(2)** Verifique na aba **''NCM''**, se consta o **NCM do produto**.

- Se o **NCM do produto** estiver listado na aba ''NCM'', o sistema está funcionando corretamente, a alíquota definida por ''NCM'' **prevalece sobre a alíquota vinculada diretamente ao produto**.

![Imagem 1: Se o NCM do produto estiver listado na aba ''NCM'' , o sistema está funcionando corretamente, a alíquota definida por…](https://ajuda.sankhya.com.br/hc/article_attachments/36602381616791)

**(3)** Agora, para **ajustar** o cálculo do IPI, **remova** o ''NCM'' da aba ''NCM da alíquota'' que está sendo priorizada **ou** **ajuste** o vínculo de ''NCM'' para que corresponda á alíquota desejada.

**(4)** Se preferir que cada **produto utilize somente a alíquota vinculada no seu cadastro**, **não utilize** a aba ''NCM'' nas ''Alíquotas de IPI''.
