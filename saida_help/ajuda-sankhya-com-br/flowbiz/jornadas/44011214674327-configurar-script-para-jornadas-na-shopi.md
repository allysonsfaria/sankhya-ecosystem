---
id: "44011214674327"
titulo: "Configurar script para Jornadas na Shopify"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011214674327-Configurar-script-para-Jornadas-na-Shopify"
trilha: "Flowbiz > Jornadas"
atualizado_em: "2026-10-05T18:58:59Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_135", "sync_hash_03d2c4fb5fd3"]
---

# Configurar script para Jornadas na Shopify

Confira o passo a passo de como **realizar a integração do Tracker de Jornadas da Flowbiz com sua loja Shopify.**

## Primeira Etapa — Inserção do Script no Google Tag Manager (GTM)

**1.** Entre em contato com a equipe de Suporte Técnico da Flowbiz e solicite o script para inserção.

**1.1** Acesse o Google Tag Manager > **selecione o container utilizado em seu site.**

**1.2** Insira o script em todas as páginas

**1.3** Crie uma nova Tag HTML personalizada e insira o script baixado.

:::warning
**Importante:** configure o acionamento (trigger) para todas as páginas (All Pages), seguindo o padrão habitual das integrações Flowbiz.

:::

Caso tenha dúvidas, pode acessar nosso outro [tutorial de inserção de scripts dentro do Google Tag Manager](https://useflowbiz.movidesk.com/kb/pt-br/article/461005/como-inserir-o-script-de-integracao-via-google-tag-manager-gtm?ticketId=&q=).

## Segunda Etapa — Configuração na Shopify

Essa etapa é necessária para que o Tracker de Jornadas funcione corretamente dentro da sua loja.

**2.1** Preparar o script

Use o mesmo script que foi enviado anteriormente pela equipe da Flowbiz.

Antes de inserir o código, **remova as tags** de **abertura** e **fechamento** do script, ou seja:

Em seguida, adicione as três linhas abaixo no topo do código:

> window.analytics = analytics;
>
> window.browser = browser;
>
> window.init = init;

**Exemplo de como o código deve ficar:**

:::success
window.analytics = analytics;

window.browser = browser;

window.init = init;

(function(m, a, i, l, b, z, j, s) {

if (m[z]) return;

m[z] = {

id: b,

ready: 0

};

z = a.createElement(i);

j = a.getElementsByTagName(i)[0];

z.async = 1;

z.src = l;

j.parentNode.insertBefore(z, j);

})(window, document, 'script', '<https://d3eq1zq78ux3cv.cloudfront.net/static/scripts/integration.min.js>', 'xxxxxxxxxxxxxxxxxxxxxx', 'MailbizIntegration');

:::

:::warning
(substitua o “xxxxxxxxxxxxxxxxxxxxxx” pelo seu ID de integração)

:::

## 2.2 Inserir o script na Shopify

Acesse o **Admin da Shopify**.

Vá até **Configurações** → **Customer Events** (Eventos do cliente) → Clique em **Add Custom** Pixel → Adicionar Pixel Customizado → Nomeie o pixel como "**Flowbiz"**

**Em Permissões, marque as opções:**

✅ Marketing

✅ Analytics

**Em Venda de dados, selecione:**

“Data collected does not qualify as data sale”

(Os dados coletados NÃO serão utilizados para venda de dados.)

**Cole o código formatado no campo do pixel.**

Clique em **Salvar** no topo da página.

Após **salvar**, clique em Conectar Pixel.

---

:::warning
Para clientes com Checkout Yampi

:::

Mesmo que a loja utilize o Checkout Yampi, a configuração do Pixel na Shopify continua sendo necessária. O processo segue as mesmas etapas descritas anteriormente:

1. **Inserir o script via GTM** nas duas plataformas, Shopify e Yampi, utilizando o script base enviado pela equipe da Flowbiz.
2. **Configurar o Pixel customizado na Shopify** em Configurações → Customer events → Adicionar Pixel customizado, seguindo os mesmos passos da Segunda Etapa.

---

Em caso de dúvidas, chame o nosso time de suporte pelo chat da ferramenta. 😉
