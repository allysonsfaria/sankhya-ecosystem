---
id: "44011499572887"
titulo: "Como funciona a Tabela de Frete do Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011499572887-Como-funciona-a-Tabela-de-Frete-do-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:04:24Z"
rotulos: ["sync_hc", "magis5", "magis5_204055239607", "sync_hash_adab74562b11"]
---

# Como funciona a Tabela de Frete do Magis5 Hub?

## Configurando manualmente os valores de Frete para Marketplaces.

---

Alguns marketplaces não permitem a integração do valor do frete por API, o que impede a obtenção automática desses valores. Para contornar essa limitação, o Magis5 HUB oferece uma funcionalidade chamada **Tabela de Frete**, onde você pode configurar manualmente os valores de frete conforme as faixas de preço de venda.

### Passo a Passo para Configuração da Tabela de Frete

Feito login no Magis, vá até a aba **"Configurações"**, **"Integrações"** e por fim **"Marketplaces"**.

![Imagem 1: Passo a Passo para Configuração da Tabela de Frete](https://ajuda.sankhya.com.br/hc/article_attachments/44011484295447)

Ao selecionar o Marketplace na lista disponível, escolha aquele para o qual deseja configurar a **Tabela de Frete** e clique em **Editar** para acessar as configurações detalhadas.

![Imagem 2: Dentro das opções de edição do Marketplace, acesse a aba "Margens e Custos" e localize a seção "Tabela de Frete" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011489543703)

Dentro das opções de edição do Marketplace, acesse a aba **"Margens e Custos"** e localize a seção **"Tabela de Frete"**.

![Imagem 3: Dentro das opções de edição do Marketplace, acesse a aba "Margens e Custos" e localize a seção "Tabela de Frete" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011504942615)

### Configuração da Tabela de Frete:

- Na seção Tabela de Frete, você verá os campos para configurar as faixas de preço e o valor adicional que será aplicado.
- **Peso De (gramas) (Opcional):** Campo opcional para definir a faixa de peso inicial.
- **Peso Até (gramas) (Opcional):** Campo opcional para definir a faixa de peso final.
- **De (R$):** Especifique o valor mínimo da faixa de preço.
- **Para (R$):** Especifique o valor máximo da faixa de preço.
- **Valor Adicional (R$):** Informe o valor que será adicionado ao frete para as vendas dentro dessa faixa.

**Exemplo Prático:**

- Suponha que o **Marketplace X** cobre uma taxa de R$ 5,00 para produtos com valor até R$ 79,00.
- Para configurar isso, preencha os campos da seguinte forma:
  - **De (R$):** 0
  - **Para (R$):** 79
  - **Valor Adicional (R$):** 5
- Depois, clique em **Adicionar** para salvar essa faixa na Tabela de Frete.
- Repita o processo para outras faixas de preço, conforme necessário.

Aqui está um exemplo visual de como deve ser preenchido com base no exemplo dado:

![Imagem 4: Aqui está um exemplo visual de como deve ser preenchido com base no exemplo dado:](https://ajuda.sankhya.com.br/hc/article_attachments/44011457813527)

Certifique-se de revisar periodicamente as configurações para garantir que os valores de frete estejam corretos. Essa função é essencial para que os custos de envio sejam calculados adequadamente e repassados ao cliente final.

⚠️ **Importante:** essa funcionalidade está disponível apenas para clientes que utilizam a nossa precificação automática

### Como o Magis5 HUB Calcula o Frete?

O Magis5 HUB realiza o cálculo do frete de uma maneira específica, combinando o preço do produto com o valor do frete antes de aplicar as regras de preço. Veja como funciona:

**- Verificação do Peso:** O Magis5 primeiro verifica se o peso do produto está dentro da faixa permitida pela regra de frete configurada.
**Por exemplo:** Se a regra se aplica a produtos de 500g a 2kg, o peso do seu produto deve estar nesse intervalo.

⚠️ **Importante: Para o canal de venda Magazine Luiza, o cálculo de frete no Magis5 HUB não é valido por cubagem, mas sim com base no peso.**

**- Verificação do Preço com o Frete:** O Magis5 soma o valor do frete ao preço do produto para verificar se o total se encaixa na faixa de preço configurada. **Por exemplo:** se o produto custa R$ 59,00 e o frete é R$ 21,00, o sistema considera o total como R$ 80,00 (R$ 59,00 + R$ 21,00).

**- Aplicação da Regra**: Se o valor total **(produto + frete)** estiver dentro da faixa de preço configurada, a regra de frete será aplicada. Caso contrário, a regra não será aplicada, e o valor original do produto será mantido.

- O Magis5 soma o valor do frete ao preço do produto antes de verificar se o preço está dentro da faixa configurada.
- A regra de frete só é aplicada se o total (preço do produto + frete) se encaixar na faixa de preço configurada.

![Imagem 5: A regra de frete só é aplicada se o total (preço do produto + frete) se encaixar na faixa de preço configurada.](https://ajuda.sankhya.com.br/hc/article_attachments/44011489854359)

[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44011505191447)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
