---
id: "43675364630551"
titulo: "Valores incorretos em férias vencidas na rescisão: como identificar e corrigir"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675364630551-Valores-incorretos-em-f%C3%A9rias-vencidas-na-rescis%C3%A3o-como-identificar-e-corrigir"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-14T16:05:42Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Valores incorretos em férias vencidas na rescisão: como identificar e corrigir

Ao realizar o cálculo da rescisão no ERP Sankhya, é importante conferir se os valores de **Férias Vencidas** foram calculados corretamente.

Quando o valor apresentado estiver diferente do esperado, alguns pontos devem ser verificados, como:

- Parametrização das férias;
- Composição da remuneração do funcionário;
- Médias salariais e de valores variáveis;
- Faltas não justificadas que possam impactar a quantidade de dias de férias;
- Período aquisitivo das férias;
- Eventos configurados para compor a base de cálculo das férias.

O cálculo das férias vencidas considera a remuneração devida ao funcionário, incluindo as médias de valores variáveis quando aplicável, além do **terço constitucional**. Também devem ser consideradas as faltas que podem impactar a quantidade de dias de férias.

Por isso, quando houver divergência no valor calculado, é necessário verificar a composição da base e as parametrizações envolvidas, identificando se todos os eventos necessários estão sendo considerados no cálculo.

### Principais causas de valores incorretos

Fatores que podem gerar divergências no cálculo das férias vencidas

As principais causas para valores incorretos em férias vencidas na rescisão são:

**Configurações de eventos:** eventos personalizados podem não estar configurados para compor a base de cálculo das férias. Por isso, é importante avaliar os eventos envolvidos e conferir se suas parametrizações estão corretas. Para isso basta acessar o evento pela tela **Eventos** (**Pessoal+ > Cadastros > Eventos)** e validar a regra de calculo e as bases cadastradas.

**Ponto de atenção:** os eventos utilizados no cálculo de férias devem ser parametrizados especificamente para essa finalidade. O mesmo evento **não deve ser utilizado em outros tipos de folha**, como **folha mensal** e **13º salário**, pois essa configuração pode interferir nos cálculos.

 **Processamento de faltas:** o sistema irá considerar automaticamente as faltas no cálculo das férias, o que pode alterar o valor calculado. Por isso, é importante verificar se as faltas foram lançadas corretamente e se estão sendo consideradas no período correto.

Para conferir as faltas do colaborador, acesse a tela **Faltas** (**Pessoal+ > Rotinas Folha > Faltas)** e valide os lançamentos realizados.

**Médias salariais não consideradas:** a ausência de médias de valores variáveis, como horas extras, comissões e adicionais, pode impactar o valor final das férias vencidas. Essa situação pode ocorrer quando o evento não está configurado corretamente para compor as médias.

Para verificar a configuração do evento, siga os passos abaixo:

1. Acesse a tela **Eventos** (**Pessoal+ > Cadastros > Eventos)**.
2. Selecione o evento que deseja avaliar.
3. Acesse a aba **Avançado**.
4. Localize o campo **Incide sobre as médias**.
5. Verifique a opção selecionada e confirme se a configuração está adequada ao comportamento esperado para o evento.

Esse campo define como o evento será considerado no cálculo das médias. Por isso, sua configuração deve ser validada sempre que houver divergência nos valores de médias utilizados no cálculo das férias.

 **Erro na composição da remuneração:** quando um evento que deveria compor a remuneração não está configurado corretamente, o valor utilizado no cálculo das férias pode ficar diferente do esperado.

Para verificar essa configuração:

1. Acesse a tela **Eventos** (**Pessoal+ > Cadastros > Eventos)**.
2. Selecione o evento que deseja avaliar.
3. Acesse a aba **Avançado**.
4. Localize o campo **Incide sobre as médias**.
5. Verifique se o campo está configurado como **Incorpora ao salário**.

Quando aplicável, essa configuração permite que o evento seja considerado na composição da remuneração utilizada no cálculo das férias.

### Boas práticas para evitar divergências

Para evitar divergências nos valores de férias vencidas na rescisão, mantenha a parametrização dos eventos atualizada, principalmente para eventos personalizados. Também é importante realizar conferências periódicas nos cálculos de férias e rescisão, verificando as médias, faltas e demais valores considerados no cálculo.

Antes de finalizar a rescisão, recomenda-se ainda revisar os valores apresentados e confirmar se estão de acordo com o esperado.

Seguindo essas orientações, é possível identificar possíveis divergências com antecedência e garantir maior segurança no cálculo das férias vencidas.
