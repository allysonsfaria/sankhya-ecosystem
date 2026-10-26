---
id: "44011141574935"
titulo: "Como integrar o Sankhya ERP com o Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011141574935-Como-integrar-o-Sankhya-ERP-com-o-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:57:15Z"
rotulos: ["sync_hc", "magis5", "sync_hash_c84173d62f4d", "magis5_204048109114"]
---

# Como integrar o Sankhya ERP com o Magis5 Hub?

## Entenda como realizar integração da sua conta Magis5 Hub com o Sankhya ERP.

O ERP Sankhya é a solução ideal para empresas que buscam um sistema completo, que une maturidade em gestão, tecnologia avançada e mobilidade.

---

No Magis5, é possível integrar apenas um **ERP/Gateway** por vez, independentemente da quantidade de **CNPJs**.

No entanto, caso seja necessário identificar no Sankhya o marketplace de origem de cada pedido, será preciso configurar uma integração de **ERP/Gateway**, específica para cada combinação de marketplace e CNPJ.

**Exemplo:** Se possui dois CNPJs, será necessário integrar dois **Sankhya Gateways**, um para cada CNPJ.

Feito login no Magis5 Hub clique em **"Configurações"**e depois em **"Integrações"** e por fim em "**ERPs & Faturador".

![sankhya](https://ajuda.sankhya.com.br/hc/article_attachments/44011154414231)**

Na aba **"ERPs & Faturador"** clique em **"novo"** no canto superior da tela.

![Imagem 2: Na aba "ERPs & Faturador" clique em "novo" no canto superior da tela.](https://ajuda.sankhya.com.br/hc/article_attachments/44011141769495)

Selecione o ERP **"Sankhya (Gateway)"** no campo **ERP** e preencha os campos conforme orientações abaixo:

![Imagem 3: Selecione o ERP "Sankhya (Gateway)" no campo ERP e preencha os campos conforme orientações abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44011183465111)

**Campos de preenchimento Obrigatórios:

- Descrição:** informe um nome que identifique seu ERP no painel do Magis5.

**- Token de Acesso:** a criação do token deve ser feita utilizando o usuário **"magis"** (conforme escrito), e não o usuário **"magis5"**, dentro do ERP Sankhya.

![Imagem 4: - Token de Acesso: a criação do token deve ser feita utilizando o usuário "magis" (conforme escrito), e não o usuário…](https://ajuda.sankhya.com.br/hc/article_attachments/44011168057879)

**- ERP Principal:** marque essa opção somente se esse ERP for o sistema responsável pelo controle de estoque.

> ⚠️ **Atenção:** Para integrações com o Sankhya, é obrigatório indicar um ERP principal. Nesse ERP devem ser preenchidas as **configurações de consulta de estoque**.

### Configurações de Criação de Pedido

Os seguintes campos **também são obrigatórios** e devem ser preenchidos **exatamente conforme configurados** no Sankhya:

**- Tipo de Operação**: Código do tipo de operação utilizada.

**- Centro de Resultado**: Código do centro de resultado.

**- Parceiro Transportadora**: Código da transportadora cadastrada.

**- Empresa**: Código da empresa que será utilizada para gerar a ordem de venda e faturamento.

**Campos de preenchimento Opcionais:**

**- Natureza:** código da natureza de venda.

**- Origem da venda:** código da origem da venda.

**- Vendedor:** código do vendedor.

### Configurações do Preço de Custo Imagem 5: Configurações do Preço de Custo

O preço de custo importado para o **Magis5 Hub** é obtido a partir do **ERP Sankhya**, considerando o valor referente à **última data de atualização registrada no sistema**.

Para mais detalhes sobre o preço de custo, [**[clique aqui]**](https://ajuda.sankhya.com.br/como-gerenciar-a-dinamicidade-de-preco-de-custo-utilizando-o-erp-sankhya?hsLang=pt-br).

⚠️ **Atenção:** essa configuração deve ser realizada **apenas quando o Sankhya for o ERP Principal**.

![Imagem 6: ⚠️ Atenção: essa configuração deve ser realizada apenas quando o Sankhya for o ERP Principal .](https://ajuda.sankhya.com.br/hc/article_attachments/44011133523351)

### Configurações de Consulta de Estoque

Para adicionar mais de um depósito, acesse a integração do Gateway principal e clique em **"Adicionar Filtro de Empresa".** Em seguida, informe o **ID da Empresa** e o **ID da Localização**, dados disponíveis no ERP Sankhya.

![Imagem 7: Para adicionar mais de um depósito, acesse a integração do Gateway principal e clique em "Adicionar Filtro de Empresa".…](https://ajuda.sankhya.com.br/hc/article_attachments/44011183900055)

**⚠️ Será necessário realizar essa configuração de consulta de estoque apenas no ERP Sankhya Principal.**

A configuração da consulta de estoque não é obrigatória. Caso o opte por não realizar essa configuração, o Magis5 Hub irá considerar automaticamente o estoque de todas as **localizações** existentes no Sankhya.

Para evitar esse comportamento, deve-se cadastrar apenas as **localizações** que deseja considerar, sempre vinculadas ao respectivo **ID da Empresa.**

### Como fazer o preenchimento da aba "Depósitos" e "Dados adicionais"  Imagem 8: Como fazer o preenchimento da aba "Depósitos" e "Dados adicionais"

O preenchimento dos campos indicados não é necessário para a integração com o ERP Sankhya.

Após seguir todos os passos indicados acima, clique em **"Salvar"**. A integração do seu ERP **Sankhya (Gateway)** será concluída com sucesso.

---

### Configuração do código da loja do ERP para os marketplaces

É necessário, também, configurar o **código da loja do ERP** nas configurações de cada marketplace dentro do Magis5 Hub.

Para realizar essa configuração clique vá em **"Configurações"** depois em **"Integrações"** e por fim **"Marketplaces".

![Captura de tela 2026-02-03 110434](https://ajuda.sankhya.com.br/hc/article_attachments/44011184101143)**

Clique para editar o canal de venda que precisa ser configurado.

![Imagem 10: Clique para editar o canal de venda que precisa ser configurado. No campo "Código da sua loja no ERP" , insira o valor…](https://ajuda.sankhya.com.br/hc/article_attachments/44011201043735)

No campo **"Código da sua loja no ERP"**, insira o valor definido como **"Tipo de Negociação"** dentro do ERP Sankhya.

![Imagem 11: Clique para editar o canal de venda que precisa ser configurado. No campo "Código da sua loja no ERP" , insira o valor…](https://ajuda.sankhya.com.br/hc/article_attachments/44011155266967)

Na aba **"Notas Fiscais"**, as **três primeiras flags** devem estar **obrigatoriamente ativadas**, enquanto as demais podem ser configuradas conforme as necessidades de cada marketplace.

![Imagem 12: Clique para editar o canal de venda que precisa ser configurado. No campo "Código da sua loja no ERP" , insira o valor…](https://ajuda.sankhya.com.br/hc/article_attachments/44011217960599)

Estas são as **particularidades** a serem ajustadas nas integrações de marketplaces com o ERP Sankhya. Após concluir os ajustes específicos de cada marketplace, clique em **"Salvar"** no canto superior da tela.

![Imagem 13: Estas são as particularidades a serem ajustadas nas integrações de marketplaces com o ERP Sankhya. Após concluir os…](https://ajuda.sankhya.com.br/hc/article_attachments/44011155482135)
