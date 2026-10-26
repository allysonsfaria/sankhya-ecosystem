---
id: "39353562852119"
titulo: "Erro ao Calcular Pensão Alimentícia no 13º Salário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39353562852119-Erro-ao-Calcular-Pens%C3%A3o-Aliment%C3%ADcia-no-13%C2%BA-Sal%C3%A1rio"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-27T18:33:46Z"
rotulos: ["Eventos", "Fórmulas", "Folha", "Configuração Funcionários", "Pensão Alimentícia", "13º Salário", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro ao Calcular Pensão Alimentícia no 13º Salário

**Mensagem**

O desconto de pensão alimentícia não está sendo calculado corretamente na folha de 13º salário, apresentando valor divergente do esperado ou deixando de ser aplicado.

**Situação**

Ao processar o cálculo da folha de 13º salário, o sistema não aplica o desconto de pensão alimentícia ou calcula um valor incorreto, mesmo com o colaborador possuindo dependente cadastrado com pensão ativa.

**Solução**

Para corrigir o cálculo da pensão alimentícia sobre o 13º salário, realize as seguintes validações:

**(1)** Acesse a tela **"Configuração Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários) e localize o colaborador que apresenta a inconsistência.

Na aba **Dependentes**, localize o dependente cadastrado como **pensionista** e verifique se o campo **"Evento de Desconto do 13º"** está preenchido com o código correto do evento de desconto de pensão referente ao 13º salário.

Caso o campo esteja em branco ou possua um código incorreto, informe o evento adequado e salve as alterações.

![Imagem 1: Caso o campo esteja em branco ou possua um código incorreto, informe o evento adequado e salve as alterações.](https://ajuda.sankhya.com.br/hc/article_attachments/41273750138007)

**(2)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento utilizado para desconto da pensão do 13º salário.

Verifique os seguintes pontos:

- O campo **Identificação** deve estar preenchido com o código **168 – Evento de Pensão Alimentícia – 13º Salário**.
- O evento **não deve possuir Regra de Cálculo**, pois o cálculo da pensão é realizado por meio de fórmula.
- Confirme se existe uma **Fórmula vinculada** ao evento, pois será ela a responsável pelo cálculo da pensão.

Caso alguma configuração esteja incorreta, realize o ajuste necessário.

![Imagem 2: Caso alguma configuração esteja incorreta, realize o ajuste necessário.](https://ajuda.sankhya.com.br/hc/article_attachments/41273725551511)

**(3)** Acesse a tela **"Fórmulas"** (Pessoal+ » Cadastros » Fórmulas) e localize a fórmula vinculada ao evento de desconto da pensão do 13º salário.

Verifique qual metodologia está sendo utilizada:

### Cenário 1 – A fórmula utiliza uma base de pensão

Se a fórmula possuir referências como **&E1997** (ou outro evento de base de pensão), será necessário validar se os eventos do 13º salário estão compondo essa base corretamente.

Por exemplo:

- Localize o evento **2ª Parcela do 13º Salário** na tela **Eventos**.
- Acesse a aba **Bases de Cálculo**.
- Verifique se a base de pensão utilizada pela fórmula está cadastrada.

Caso não esteja, realize o cadastro.

Essa conferência deve ser realizada para todos os eventos que participam do cálculo da 2ª parcela do 13º salário e que devem integrar a base da pensão.

![Imagem 3: Essa conferência deve ser realizada para todos os eventos que participam do cálculo da 2ª parcela do 13º salário e que…](https://ajuda.sankhya.com.br/hc/article_attachments/41273725553303)

### Cenário 2 – A fórmula utiliza a variável do sistema FBASEPENS

Se a fórmula utilizar a variável **FBASEPENS**, acesse novamente a tela **"Configuração Funcionários"** e valide a aba **"Incidências da Pensão 13º"**.

Nessa aba, confirme se todos os eventos que devem compor a base de cálculo da pensão estão cadastrados corretamente.

Caso identifique inconsistências, realize os ajustes necessários.

![Imagem 4: Caso identifique inconsistências, realize os ajustes necessários.](https://ajuda.sankhya.com.br/hc/article_attachments/41273725553943)

**(4)** Após efetuar todas as correções, recalcule a folha de 13º salário e valide se o desconto da pensão alimentícia passou a ser calculado corretamente.

**Causa**

As principais causas para essa inconsistência são:

- Campo **"Evento de Desconto do 13º"** não preenchido ou configurado com código incorreto no cadastro do dependente pensionista.
- Campo **"Identificação"** do evento de desconto vazio ou configurado incorretamente (diferente de **168 – Evento de Pensão Alimentícia – 13º Salário**).
- Evento de desconto configurado incorretamente, sem fórmula vinculada ou com regra de cálculo indevida.
- Eventos que deveriam compor a base de cálculo da pensão não cadastrados na **Base de Pensão** utilizada pela fórmula.
- Eventos não configurados corretamente na aba **"Incidências da Pensão 13º"**, quando a fórmula utiliza a variável **FBASEPENS**.

**Informações adicionais**

Para mais detalhes sobre a configuração de pensão alimentícia no sistema, consulte os artigos relacionados ao tema.

[**Cadastro de Dependente com Pensão Alimentícia**](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Cadastro-de-Dependente-com-Pens%C3%A3o-Aliment%C3%ADcia)

[**Configuração de Fórmulas de Pensão por Dependente**](https://ajuda.sankhya.com.br/hc/pt-br/articles/29655219319575-Configura%C3%A7%C3%A3o-de-F%C3%B3rmulas-de-Pens%C3%A3o-por-Dependente)
