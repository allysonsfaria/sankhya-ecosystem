---
id: "39368488919319"
titulo: "Por que o evento IRRF Férias não aparece na folha de pagamento mensal?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39368488919319-Por-que-o-evento-IRRF-F%C3%A9rias-n%C3%A3o-aparece-na-folha-de-pagamento-mensal"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:12Z"
rotulos: ["Configuração", "Eventos", "Impostos", "eSocial", "Folha de Pagamento", "IRRF", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Por que o evento IRRF Férias não aparece na folha de pagamento mensal?

O evento **"9050 - IRRF Férias"** é configurado de forma padrão no sistema para não entrar na regra de cálculo da folha mensal. Isso ocorre porque este evento possui tributação exclusiva de acordo com a **tabela 21 - Códigos de Incidências Tributárias da Rubrica para o IRRF** do eSocial, sendo aplicado apenas na folha de férias.

![Imagem 1: O evento "9050 - IRRF Férias" é configurado de forma padrão no sistema para não entrar na regra de cálculo da folha…](https://ajuda.sankhya.com.br/hc/article_attachments/40805198601239)

Quando um colaborador entra em férias, o IRRF incidente sobre os valores de férias é calculado separadamente, por meio do evento **"9050 - IRRF Férias"**.

Esse evento não deve aparecer na folha de pagamento mensal, pois sua incidência é exclusiva do processamento da folha de férias.

### Configuração padrão do evento "9050 - IRRF Férias"

O evento em questão entra como regra de calculo em folhas de férias, rescisão e em folha complementar, essa configuração garante que o desconto de IRRF sobre férias seja processado corretamente apenas quando houver o cálculo específico de férias.

Para verificar a configuração do evento, acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento **"9050 - IRRF Férias""**. Observe que suas incidências e características estão vinculadas exclusivamente ao tipo de folha de férias.

![Imagem 2: Para verificar a configuração do evento, acesse a tela "Eventos" (Pessoal+ » Cadastros » Eventos) e localize o evento…](https://ajuda.sankhya.com.br/hc/article_attachments/40805221216407)

![Imagem 3: Para verificar a configuração do evento, acesse a tela "Eventos" (Pessoal+ » Cadastros » Eventos) e localize o evento…](https://ajuda.sankhya.com.br/hc/article_attachments/40805221217431)

###

### Eventos que incidem em IRRF mensal

Quando um evento é configurado para incidir exclusivamente em IRRF mensal, como por exemplo o evento **"50 - HORA EXTRA 50%"**, ele será considerado na recomposição da base de IRRF durante o cálculo da folha mensal, pois está configurado para incidência mensal.

![Imagem 4: Quando um evento é configurado para incidir exclusivamente em IRRF mensal, como por exemplo o evento "50 - HORA EXTRA…](https://ajuda.sankhya.com.br/hc/article_attachments/40805198608407)

![Imagem 5: Quando um evento é configurado para incidir exclusivamente em IRRF mensal, como por exemplo o evento "50 - HORA EXTRA…](https://ajuda.sankhya.com.br/hc/article_attachments/40805198609815)

Caso o mesmo evento seja utilizado simultaneamente na folha mensal, folha de 13º salário e/ou férias, pode ocorrer duplicidades de valores e, consequentemente, divergências nos valores apurados no eSocial.

Para evitar esse comportamento e garantir que o desconto de IRRF seja apurado de forma segregada entre cada tipo de folha, é necessário criar eventos específicos para cada cenário, ou seja, um evento para a folha mensal, outro para 13º salário e outro para férias, conforme a necessidade.

### Diferença entre IRRF mensal e IRRF férias

O **"9040 - IRRF Mensal"** é calculado sobre a base de rendimentos mensais do colaborador, considerando salário, horas extras, comissões e demais proventos que compõem a remuneração mensal.

![Imagem 6: O "9040 - IRRF Mensal" é calculado sobre a base de rendimentos mensais do colaborador, considerando salário, horas…](https://ajuda.sankhya.com.br/hc/article_attachments/40805198610583)

![Imagem 7: O "9040 - IRRF Mensal" é calculado sobre a base de rendimentos mensais do colaborador, considerando salário, horas…](https://ajuda.sankhya.com.br/hc/article_attachments/40805221221271)

Já o **"9050 - IRRF Férias"** é calculado exclusivamente sobre os valores pagos durante o período de férias, incluindo o terço constitucional. Por se tratar de uma tributação exclusiva na fonte, este cálculo não se mistura com o IRRF mensal.

![Imagem 8: Já o "9050 - IRRF Férias" é calculado exclusivamente sobre os valores pagos durante o período de férias, incluindo o…](https://ajuda.sankhya.com.br/hc/article_attachments/40805221222167)

![Imagem 9: Já o "9050 - IRRF Férias" é calculado exclusivamente sobre os valores pagos durante o período de férias, incluindo o…](https://ajuda.sankhya.com.br/hc/article_attachments/40805198612375)

Esta separação garante o correto cumprimento da legislação tributária e evita distorções no cálculo do imposto de renda retido na fonte.
