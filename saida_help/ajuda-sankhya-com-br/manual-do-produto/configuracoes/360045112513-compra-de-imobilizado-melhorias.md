---
id: "360045112513"
titulo: "Compra de Imobilizado - Melhorias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112513-Compra-de-Imobilizado-Melhorias"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:59:16Z"
rotulos: ["Configuração", "NF-e", "Compra", "CALCDEPMESANO", "SUBCREDICMSCIAP", "Compra de Imobilizado - Melhorias manual", "Imobilizado", "ICMS", "Impostos", "Melhorias na Compra de Imobilizado", "CIAP"]
---

# Compra de Imobilizado - Melhorias

Na entrada de bens pela [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) são gerados os cadastros dos bens relativos aos produtos utilizados como imobilizado (opções [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974-Central-de-Compras-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#bens), **"Compra de Bens"** e Bens, Compra de Bens, **"Outras Opções"**, **"Gerar bens automaticamente"** localizadas no botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974-Central-de-Compras-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) da Grade de itens).

O sistema registra diversas informações, como por exemplo, o valor de aquisição, base de depreciação e valores de crédito de ICMS do CIAP conforme os dados da nota. De acordo com as configurações do CIAP no produto e determinados parâmetros, os cálculos são efetuados para encontrar os valores anteriormente citados e informados no bem.

Na geração do bem, temos:

Se a [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizada no lançamento da NF-e e a CFOP do bem estiverem configuradas para calcular diferencial de alíquota (marcação **"Calcular diferença de ICMS"**, abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) e [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), respectivamente), será efetuado o cálculo da diferença da mesma forma que é realizado na apuração de ICMS. Além disso, será adicionado o valor do diferencial aos valores: Aquisição e Base de Depreciação. 

Quando o produto estiver configurado para atualizar CIAP (marcação **"Atualizar CIAP"**, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)) tem-se o seguinte comportamento:

- O cálculo do campo **"Valor do ICMS"** presente na aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-ababens), sub-aba **"CIAP"**, não irá considerar o frete extra nota;
- Os campos **"Valor crédito de ICMS sobre frete"**, **"Valor crédito ICMS por subst. tributária"** e **"Valor crédito de ICMS dif. alíquota"** também serão alimentados.

No cálculo da Base da Depreciação, o sistema irá subtrair os seguintes valores: Valor do ICMS do item, Valor S.T do item, Valor do Diferencial de Alíquota e Valor do ICMS do frete, pois quando ocorre o aproveitamento não se pode depreciar estes valores.

Vejamos alguns exemplos de cálculos:

**1-** Neste caso, o bem não atualiza CIAP.

R$ 1.000,00 **⇾** Valor do item na nota

R$ 120,00    **⇾** ICMS

R$ 10,00     **⇾** ICMS S.T.

R$ 60,00 **⇾** Diferencial de Alíquota

|  | ![Imagem 1: R$ 60,00 ⇾ Diferencial de Alíquota](https://ajuda.sankhya.com.br/hc/article_attachments/42310981004567) |  |
| --- | --- | --- |

**2-** Neste caso, o bem atualiza CIAP.

R$ 1.000,00 **⇾** Valor do item na nota

R$ 120,00    **⇾** ICMS

R$ 10,00     **⇾** ICMS S.T.

R$ 60,00 **⇾** Diferencial de Alíquota

|  | ![Imagem 2: R$ 60,00 ⇾ Diferencial de Alíquota](https://ajuda.sankhya.com.br/hc/article_attachments/42310994074135) |  |
| --- | --- | --- |

No Cálculo do Valor de Aquisição, temos:

Pode-se trabalhar com o parâmetro **"Subtrair Crédito de ICMS do CIAP do valor de aquisição - SUBCREDICMSCIAP"** que por padrão é apresentado desligado. Sendo que, pode ocorrer as seguintes situações:

- Quando o parâmetro SUBCREDICMSCIAP estiver desativado ou o parâmetro **"Considera só mes/ano para cálculo da depreciação - CALCDEPMESANO"** estiver ligado, nenhuma alteração irá ocorrer (os dois parâmetros não podem ficar ligados simultaneamente).
- Quando o parâmetro SUBCREDICMSCIAP estiver ligado e o produto estiver configurado para atualizar CIAP (marcação **"Atualizar CIAP"**, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos)), o sistema irá alterar o valor calculado do **"Valor de Aquisição"** (aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-ababens), sub-aba **"Geral"**) subtraindo os seguintes valores: Valor ICMS do item, Valor S.T do item, Valor do Diferencial de Alíquota e Valor do ICMS do frete.

Vejamos os exemplos dos cálculos:

Neste caso o bem não atualiza CIAP e o parâmetro SUBCREDICMSCIAP está desligado:

R$ 1.000,00 **⇾** Valor do item na nota

R$ 120,00    **⇾** ICMS

R$ 10,00     **⇾** ICMS S.T.

R$ 60,00 **⇾** Diferencial de Alíquota

|  | ![Imagem 3: R$ 60,00 ⇾ Diferencial de Alíquota](https://ajuda.sankhya.com.br/hc/article_attachments/42310981009047) |  |
| --- | --- | --- |

Nesta situação o bem atualiza CIAP e o parâmetro SUBCREDICMSCIAP está ligado:

R$ 1.000,00 **⇾** Valor do item na nota

R$ 120,00    **⇾** ICMS

R$ 10,00     **⇾** ICMS S.T.

R$ 60,00 **⇾** Diferencial de Alíquota

|  | ![Imagem 4: R$ 60,00 ⇾ Diferencial de Alíquota](https://ajuda.sankhya.com.br/hc/article_attachments/42310981009815) |  |
| --- | --- | --- |
