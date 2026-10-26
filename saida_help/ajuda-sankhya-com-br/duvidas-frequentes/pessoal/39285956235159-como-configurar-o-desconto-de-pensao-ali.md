---
id: "39285956235159"
titulo: "Como configurar o desconto de pensão alimentícia no 13º salário?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39285956235159-Como-configurar-o-desconto-de-pens%C3%A3o-aliment%C3%ADcia-no-13%C2%BA-sal%C3%A1rio"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:36Z"
rotulos: ["Configuração", "Eventos", "Folha", "eSocial", "Configuração Funcionários", "13º Salário", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como configurar o desconto de pensão alimentícia no 13º salário?

O desconto de pensão alimentícia no 13º salário requer configurações específicas no sistema, diferentes daquelas utilizadas na folha mensal. Isso ocorre porque as incidências e regras de cálculo do 13º salário possuem particularidades que exigem eventos próprios.

Este artigo orienta sobre as principais situações relacionadas ao desconto de pensão no 13º salário e como configurá-las corretamente no sistema.

### Criação de evento específico para o 13º salário

Para que o desconto de pensão seja aplicado corretamente no 13º salário, é necessário criar um **"Evento Específico"** para esta finalidade, pois não é possível utilizar o mesmo evento do desconto mensal.

A solução consiste em duplicar o evento de pensão da folha mensal e adaptá-lo para o 13º salário, alterando as seguintes configurações:

- Ajuste o campo **"Tipo de Folha"** para **"13º Salário"**.
- Revise as incidências do evento para que estejam adequadas ao 13º salário.
- Verifique as fórmulas de cálculo para garantir que reflitam as regras específicas do 13º.

Após criar o novo evento, recalcule a folha do 13º salário para que a pensão passe a compor o cálculo corretamente.

### Pensão sobre salário mínimo no 13º

Para casos de pensão calculada sobre o salário mínimo, é necessário que o **"Evento 526"** (Pensionista sobre Salário Mínimo) esteja cadastrado na tela **"Configuração do Funcionário"** (Pessoal Cadastros Funcionários).

Siga os passos abaixo para configurar:

1. **(1)** Acesse a tela **"Configuração do Funcionário"** (Pessoal Cadastros Funcionários).
2. **(2)** Localize o funcionário que possui pensão sobre salário mínimo.
3. **(3)** Inclua o **"Evento 526"** na configuração do funcionário.
4. **(4)** Salve as alterações e recalcule a folha do 13º salário.

Esta configuração é essencial para que as informações sejam enviadas corretamente ao e Social e o cálculo seja processado adequadamente.

### Movimento fixo de pensão e fechamento de referência

Quando o movimento de pensão é fixo, é necessário que a referência anterior esteja fechada para que o evento seja levado automaticamente para a próxima referência.

Por exemplo: se a referência 12/2025 estiver aberta, o movimento fixo de pensão não será levado automaticamente para a folha de 01/2026. Neste caso, existem duas alternativas:

- Feche a referência anterior (12/2025) para que o sistema leve o movimento automaticamente.
- Lance manualmente o movimento fixo de pensão na nova referência.

Esta regra se aplica tanto para a folha mensal quanto para o 13º salário, garantindo a continuidade dos descontos de pensão alimentícia.

### Observações importantes

O sistema não possui eventos e fórmulas padrão para todos os cenários de pensão alimentícia. As configurações devem ser personalizadas de acordo com as determinações judiciais específicas de cada caso.

Caso seja necessário criar eventos customizados, essa personalização pode ser realizada pelo próprio cliente ou pela unidade de suporte, desde que as configurações sejam devidamente ajustadas para retornar o resultado esperado.
