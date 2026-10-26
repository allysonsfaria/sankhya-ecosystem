---
id: "43674838199191"
titulo: "Por que eventos personalizados não são considerados na base de desconto do vale transporte?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43674838199191-Por-que-eventos-personalizados-n%C3%A3o-s%C3%A3o-considerados-na-base-de-desconto-do-vale-transporte"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-09-28T13:07:04Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Por que eventos personalizados não são considerados na base de desconto do vale transporte?

No ERP Sankhya, o desconto do vale transporte é calculado com base em eventos padrão do sistema, seguindo a legislação vigente e as regras de parametrização da folha de pagamento. Quando um evento personalizado é criado, ele não é automaticamente considerado como base para o desconto do vale transporte, pois não faz parte da estrutura padrão de cálculo do sistema.

Isso significa que, ao criar um evento personalizado para fins específicos — como bonificações, ajustes internos ou lançamentos demonstrativos —, esse evento não será utilizado na composição da base de cálculo do desconto do vale transporte, a menos que seja feita uma personalização específica na fórmula do evento de desconto ou nas regras de cálculo da folha.

### Como funciona a composição da base do desconto do vale transporte

O desconto do vale transporte é limitado a 6% do salário base do colaborador, considerando apenas os eventos padrão definidos para compor essa base. Eventos personalizados, por padrão, não são incluídos nesse cálculo. Para que um evento personalizado seja considerado, é necessário ajustar a fórmula do evento de desconto do vale transporte, incluindo explicitamente o novo evento na base de cálculo.

Caso não haja essa personalização, o sistema ignora o evento personalizado ao calcular o desconto, mantendo a integridade das regras legais e evitando descontos indevidos ou divergentes.

### Orientações para uso correto de eventos personalizados na folha

Utilize eventos personalizados para lançamentos que não impactam diretamente a folha de pagamento, como controles internos, análises gerenciais ou composições de custo para relatórios de BI. Para esses casos, recomenda-se criar o evento como demonstrativo e realizar o lançamento pela tela **"Lançamento de Movimento"** Pessoal+ » Rotinas Folha » Lançamento de Movimento garantindo que o valor não interfira nos cálculos oficiais da folha.

Se houver necessidade de que o evento personalizado componha a base de desconto do vale transporte, realize uma personalização na fórmula do evento de desconto, incluindo o código do evento personalizado na regra de cálculo.

### Recomendações para evitar erros e garantir conformidade legal

Sempre revise as bases de cálculo e incidências dos eventos ao criar ou alterar eventos personalizados. Certifique-se de que apenas eventos apropriados estejam compondo a base do desconto do vale transporte, evitando assim inconsistências na folha e possíveis questionamentos legais.

Para lançamentos que não devem impactar a folha, utilize eventos do tipo demonstrativo e mantenha-os fora das fórmulas de cálculo dos descontos obrigatórios. Dessa forma, o controle gerencial é mantido sem comprometer a conformidade dos cálculos legais.
