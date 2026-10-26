---
id: "43675341461143"
titulo: "Como evitar divergências no cálculo da folha de pagamento entre meses com 31 dias e a configuração de mês comercial?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675341461143-Como-evitar-diverg%C3%AAncias-no-c%C3%A1lculo-da-folha-de-pagamento-entre-meses-com-31-dias-e-a-configura%C3%A7%C3%A3o-de-m%C3%AAs-comercial"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-09-28T12:23:41Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como evitar divergências no cálculo da folha de pagamento entre meses com 31 dias e a configuração de mês comercial?

A divergência entre o cálculo da folha de pagamento considerando 31 dias (mês real) e 30 dias (mês comercial) é uma dúvida frequente entre usuários do ERP Sankhya. Essa diferença pode impactar diretamente o valor do salário, férias, rescisões e outros eventos trabalhistas, especialmente quando a configuração da empresa está definida para utilizar o mês comercial, mas o sistema, por algum motivo, utiliza o mês real em determinados cálculos.

O correto entendimento e parametrização das regras de cálculo são fundamentais para garantir a conformidade legal e evitar pagamentos incorretos. A seguir, detalhamos as melhores práticas para configurar e validar o cálculo correto, além de exemplos práticos para cada situação.

### Como parametrizar corretamente o tipo de mês na folha de pagamento

Para garantir que o sistema utilize sempre 30 dias no cálculo da folha mensal, acesse a tela **"Regras de Cálculo"** (Pessoal+ Cadastros Regras de Cálculo), aba **"Propriedades"**. No campo **"Tipo de Mês"**, selecione a opção **"Comercial (30 dias)"**. Assim, independentemente do mês (inclusive meses com 31 dias), o sistema calculará o salário mensal considerando 30 dias.

![Imagem 1: Para garantir que o sistema utilize sempre 30 dias no cálculo da folha mensal, acesse a tela "Regras de Cálculo"…](https://ajuda.sankhya.com.br/hc/article_attachments/43812192459799)

Caso a opção **"Mês Real (28, 29, 30 e 31)"** esteja selecionada, o sistema utilizará a quantidade real de dias do mês vigente, o que pode gerar diferenças no valor do salário em meses com 31 dias.

### Diferença de cálculo em eventos proporcionais e obrigatoriedade legal

Para eventos proporcionais, como admissões, rescisões, afastamentos e férias, a legislação trabalhista determina que o cálculo deve ser feito com base nos dias reais do mês. Por exemplo, em uma rescisão ocorrida em fevereiro, o correto é dividir o salário por 28 dias (ou 29 em ano bissexto), conforme a Súmula 264 do TST e o art. 64 da CLT.

Mesmo que a regra geral da empresa seja mês comercial, é fundamental marcar as opções:

- **"Calcula resíduo de admissões em meses que não possuem 30 dias"**
- **"Calcula resíduo de rescisão em meses que não possuam 30 dias"**
- **"Calcula resíduo de afastamento em meses que não possuem 30 dias"**
- **"Calcula resíduo de férias em meses que não possuem 30 dias"**

Essas marcações garantem que, para eventos proporcionais, o sistema utilize os dias reais do mês, evitando divergências e atendendo à legislação.

### Como validar e corrigir divergências no cálculo da folha

Suponha que a folha mensal de janeiro (31 dias) esteja calculando o salário base utilizando 31 dias, mesmo com a configuração de mês comercial. Isso pode ocorrer se houver marcações indevidas nas opções de cálculo de resíduos. Para corrigir:

Acesse a tela **"Regras de Cálculo"** (Pessoal+ Cadastros Regras de Cálculo), aba **"Propriedades"**.

 Desmarque a opção **"Calcula resíduo de férias em meses que não possuem 30 dias"** se o cálculo for para folha mensal sem eventos proporcionais.

 Recalcule a folha de pagamento. O sistema passará a considerar 30 dias para o salário mensal, conforme a configuração de mês comercial.

Para eventos proporcionais, mantenha as opções de cálculo de resíduos marcadas, garantindo o uso dos dias reais do mês.

**Importante:** Nunca utilize a opção **"Considera 30 dias em Fevereiro"** para rescisões, pois isso contraria a legislação trabalhista.

Dessa forma, a folha mensal será sempre calculada com 30 dias, e eventos proporcionais seguirão os dias reais do mês, evitando divergências e garantindo conformidade legal.
