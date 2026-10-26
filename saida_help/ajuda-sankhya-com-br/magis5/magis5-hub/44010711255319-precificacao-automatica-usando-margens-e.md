---
id: "44010711255319"
titulo: "Precificação automática usando Margens e Custos no Magis5 Hub"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010711255319-Precifica%C3%A7%C3%A3o-autom%C3%A1tica-usando-Margens-e-Custos-no-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:43:58Z"
rotulos: ["sync_hc", "magis5", "magis5_204048155921", "sync_hash_670d9a263777"]
---

# Precificação automática usando Margens e Custos no Magis5 Hub

## Entenda neste artigo como formar os preços de venda dos anúncios de forma automática.

---

A Magis5 **ajusta automaticamente** o preço de produtos entre R$ **79,01 e R$ 79,99 para R$ 78,99**, evitando que entrem na **política de frete grátis do Mercado Livre.**

Assim, você protege sua margem de lucro e mantém a competitividade dos seus anúncios de forma automática.

Para vendedores, precificar corretamente seus anúncios pode ser um grande desafio, pois envolve diversos custos, como taxas do marketplace, embalagem, expedição e preço de custo do produto.

Para facilitar esse processo, o **Magis5 Hub** oferece a funcionalidade **"Precificação Automática"**, que calcula automaticamente as taxas padrão dos marketplaces com base no preço de custo registrado no ERP do vendedor, nos custos operacionais e na margem de lucro configurada.

A precificação automática pode ser configurada de duas formas:

- **Produto**: a configuração é aplicada a todos os anúncios do produto.
- **Anúncio**: a configuração é aplicada apenas ao anúncio específico.

O sistema segue a seguinte regra: se houver uma configuração específica no anúncio, ela será utilizada; caso contrário, o sistema aplicará a configuração do produto.

Além disso, é possível configurar **taxas específicas para cada marketplace**, considerando valores fixos ou percentuais aplicáveis a anúncios de diferentes faixas de preço.

Para verificar como configurar, [clique aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/44010711255319-Precifica%C3%A7%C3%A3o-autom%C3%A1tica-usando-Margens-e-Custos-no-Magis5-Hub#por-marketplace) para acessar o tutorial

### Como configurar "Margens e Custos" por produto no Magis5 HUB

Feito login no Magis5 HUB vá até **"Produtos"**, **"Gestão de produtos"** e por fim**"Produtos simples e compostos".**

![Captura de tela 2026-03-06 123757](https://ajuda.sankhya.com.br/hc/article_attachments/44010683786007)

Os seus produtos aparecerão na tela. Localize o produto desejado ou refine a busca utilizando os filtros disponíveis. Em seguida, clique em **"Editar"** para aplicar a precificação automática ao produto selecionado.

![Captura de tela 2026-03-06 124335](https://ajuda.sankhya.com.br/hc/article_attachments/44010711540503)

Ao editar o produto, acesse a aba **"Margens e custos"**. É nessa aba que você fará todas as configurações necessárias para que a **precificação automática** funcione corretamente nos anúncios desse produto.

![Captura de tela 2026-03-06 124830](https://ajuda.sankhya.com.br/hc/article_attachments/44010679860631)

- **Custo de operação:** neste campo, você pode cadastrar gastos fixos, como embalagens, informando o valor em reais (R$).
- **Porcentagem de lucro líquido:** aqui você define a margem de lucro que deseja obter com o produto, em porcentagem (%).
- **Comissão do produto por marketplace:** algumas comissões variam conforme o tipo de produto — por exemplo, um celular pode ter uma taxa diferente de uma blusa. O **Magis5 Hub** permite que você defina a porcentagem de comissão considerando o tipo de produto e o marketplace específico. Essa configuração é **opcional**; se você preferir usar as taxas padrão, basta deixar os campos em branco, e o sistema as aplicará automaticamente.

Com base no **preço de custo** cadastrado em seu ERP, o **Magis5 HUB** calcula automaticamente o **preço de venda**, levando em conta a porcentagem de lucro cadastrada, bem como as regras, comissões e taxas de cada marketplace. Assim, ao publicar anúncios, **não será necessário preencher o campo de preço**.

Se você preferir usar o método padrão, onde pode determinar um valor fixo para cada anúncio, basta deixar os campos da precificação automática em branco **(ou atualizar para zero)** e cadastrar o preço de venda diretamente na [publicação dos anúncios](https://ajuda.sankhya.com.br/an%C3%BAncios/como-publicar-an%C3%BAncios) ou em **"Anúncios publicados"**.

![Captura de tela 2026-03-06 125413](https://ajuda.sankhya.com.br/hc/article_attachments/44010711765527)

### Como configurar a precificação por Marketplace

Para começar, vá até **"Configurações"**, **"Integrações"** e depois clique em **"Marketplaces"**.

![Captura de tela 2026-03-06 125650](https://ajuda.sankhya.com.br/hc/article_attachments/44010670378519)

Em **"Marketplaces"** selecione o canal de venda que deseja, clique em **"Editar"** e preencha as informações em "**Margens e custos"**

![Captura de tela 2026-03-06 131006](https://ajuda.sankhya.com.br/hc/article_attachments/44010692618135)

- **Valor adicional no valor final do produto em %:** adiciona um percentual extra ao preço final calculado na precificação.
- **Valor adicional no valor final do produto em R$:** adiciona um valor fixo ao preço final calculado na precificação.
- **Base de cálculo para precificação automática:** define se a precificação será calculada a partir do preço de custo ou do preço de venda do produto.

💡 Utilize a nossa [**calculadora de precificação**](https://magis5.com.br/calculadora-precificacao-automatica-magis5/) para testar valores antes de preencher a aba **Margens e Custos** e conferir qual será o **valor final do seu anúncio**.

Também é possível configurar a **precificação automática** considerando o **peso final do produto** (incluindo a embalagem), já que alguns marketplaces aplicam taxas baseadas no peso. Por exemplo, em determinados marketplaces, o valor do frete varia de acordo com o peso e o valor do anúncio.

Para configurar corretamente, defina o **peso e o valor do anúncio** correspondente para cada faixa de peso. Se desejar adicionar mais faixas, clique em **"Adicionar"** e insira um número maior que o último peso cadastrado — por exemplo, se a primeira faixa vai de 1 g a 500 g, a próxima pode começar em 501 g.

![Imagem 7: Para configurar corretamente, defina o peso e o valor do anúncio correspondente para cada faixa de peso. Se desejar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010680160919)

### Taxa de frete e taxas fixas

No **Mercado Livre**, o cálculo do frete e das taxas fixas é feito automaticamente pelo **Magis5 Hub** ao consultar o anúncio. Se o anúncio estiver com **frete grátis**, o sistema reconhece isso automaticamente. O Mercado Livre cobra uma taxa fixa de R$ 6,00 para anúncios com valor final abaixo de R$ 79,00, e o Magis5 HUB realiza esse cálculo de forma automática.

Nos marketplaces **Olist, Americanas e Magalu**, as informações sobre frete e taxas fixas não são obtidas automaticamente, pois esses marketplaces não disponibilizam esses dados pela integração. Nesse caso, a configuração deve ser feita manualmente na seção **"Custo Operacional"** do anúncio, especialmente se ele estiver configurado como **frete grátis**.
