---
id: "39352477406743"
titulo: "Como configurar eventos na base de cálculo da margem consignável para empréstimo consignado em rescisão?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39352477406743-Como-configurar-eventos-na-base-de-c%C3%A1lculo-da-margem-consign%C3%A1vel-para-empr%C3%A9stimo-consignado-em-rescis%C3%A3o"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:49Z"
rotulos: ["Configuração", "Eventos", "Financeiro", "Rescisão", "Artigo criado KCS", "Sankhya RH - KCS", "Empréstimo Consignado"]
---

# Como configurar eventos na base de cálculo da margem consignável para empréstimo consignado em rescisão?

No cálculo de rescisão contratual com empréstimo consignado, o sistema utiliza a **"Base Margem Crédito Trabalhador"** para determinar o limite de 35% sobre o qual o desconto pode ser aplicado. É fundamental que todos os eventos que compõem a remuneração do colaborador estejam corretamente vinculados a esta base de cálculo.

A configuração inadequada dos eventos pode resultar em cálculos incorretos, considerando apenas parte da remuneração (como horas extras e DSR) e desconsiderando outros valores importantes como saldo de salário, 13º salário e demais verbas rescisórias.

### Eventos que devem compor a base de cálculo

A **"Base Margem Crédito Trabalhador"** deve incluir todos os eventos de natureza remuneratória que fazem parte da rescisão. Os eventos mais comuns que precisam estar configurados nesta base são:

**Eventos de proventos:**

- Saldo de salário
- Horas extras (50%, 60%, 100% e demais percentuais)
- DSR sobre horas extras
- 13º salário proporcional e indenizado
- Férias proporcionais e vencidas
- 1/3 constitucional sobre férias
- Adicional noturno
- Adicional de insalubridade
- Adicional de periculosidade
- Comissões

Eventos desprotegidos ou personalizados criados pela empresa também precisam ser incluídos manualmente na base, caso representem valores remuneratórios.

### Como incluir eventos na base de cálculo

Para garantir que o cálculo da margem consignável considere todos os eventos necessários, siga os passos abaixo:

**(1)** Acesse a tela **"Eventos >Bases de Cálculo"** (Pessoal+ » Cadastros » Eventos).

**(2)** Localize a base **"Base Margem Crédito Trabalhador"** ou **"Margem Consignável"** e inclua a base dentro do evento .

![Imagem 1: Verifique quais eventos já estão vinculados a esta base de cálculo. Inclua manualmente os eventos que estão faltando,…](https://ajuda.sankhya.com.br/hc/article_attachments/41356881823639)

**(3)** Verifique quais eventos já estão vinculados a esta base de cálculo.

**(4)** Inclua manualmente os eventos que estão faltando, especialmente:

- Eventos de saldo de salário
- Eventos de 13º salário (proporcional e indenizado)
- Eventos de horas extras que não estejam incluídos
- Eventos de DSR sobre horas extras
- Eventos personalizados criados pela empresa

**(5)** Salve as alterações realizadas na base de cálculo.

**(6)** Recalcule a folha de rescisão para que o sistema considere os novos eventos incluídos na base.

**(7)** Verifique se o valor do desconto do empréstimo consignado está correto, respeitando o limite de 35% sobre o total da remuneração rescisória.

### Eventos desprotegidos e personalizados

Eventos desprotegidos são aqueles criados pela própria empresa e não fazem parte da configuração padrão do sistema. Estes eventos **precisam ser incluídos manualmente** na **"Base Margem Crédito Trabalhador"**, pois o sistema não os adiciona automaticamente.

Exemplos comuns de eventos desprotegidos que podem precisar ser incluídos:

- Evento 200 (Saldo de Salário personalizado)
- Eventos de gratificações específicas da empresa
- Eventos de bonificações
- Eventos de prêmios

Sempre que criar um novo evento remuneratório, verifique se ele deve compor a base de cálculo da margem consignável e inclua-o manualmente.

### Validação do cálculo correto

Após configurar corretamente os eventos na base de cálculo, o sistema deve:

- Calcular a margem consignável considerando **todos os proventos** da rescisão (saldo de salário, 13º, férias, horas extras, DSR, etc.)
- Aplicar o percentual de **35% sobre o total** destes valores
- Limitar o desconto do empréstimo consignado ao valor máximo permitido
- Gerar o evento de **"Parcela Não Descontada"** caso o valor da parcela ultrapasse o limite legal

Caso o cálculo ainda apresente inconsistências após a configuração, verifique se há alguma regra específica ou fórmula personalizada que possa estar interferindo no processamento da base de cálculo.

### Considerações sobre o 13º salário

Existe uma discussão sobre a inclusão do 13º salário na base de cálculo da margem consignável. De acordo com o manual do e-Consignado disponibilizado pelo governo, as naturezas de rubricas **6001, 6002, 9201 e 9203** (que incluem 13º salário) compõem a base da margem de crédito do trabalhador.

Portanto, o sistema está configurado para seguir esta orientação oficial. Caso sua empresa adote interpretação jurídica diferente, será necessário ajustar manualmente a configuração dos eventos relacionados ao 13º salário na base de cálculo.

Consulte sempre a legislação vigente e o departamento jurídico da empresa para garantir que a configuração esteja em conformidade com as normas aplicáveis.
