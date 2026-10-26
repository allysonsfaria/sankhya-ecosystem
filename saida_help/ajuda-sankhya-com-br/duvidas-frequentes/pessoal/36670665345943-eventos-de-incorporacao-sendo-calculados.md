---
id: "36670665345943"
titulo: "Eventos de Incorporação Sendo Calculados como Média — Identificação e Correção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36670665345943-Eventos-de-Incorpora%C3%A7%C3%A3o-Sendo-Calculados-como-M%C3%A9dia-Identifica%C3%A7%C3%A3o-e-Corre%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-27T18:35:21Z"
rotulos: ["Configuração", "Eventos", "Folha de Pagamento", "Lançamento de Movimento", "Férias", "13º Salário", "Incorpora ao salário", "Eventos de Incorporação", "Identificação e Correção", "FPEVEINCSAL", "Remuneração"]
---

# Eventos de Incorporação Sendo Calculados como Média — Identificação e Correção

Os eventos de incorporação estão sendo tratados como **média** no sistema, o que é incorreto, pois a legislação determina que esse tipo de gratificação **integra a remuneração das férias e do 13º salário** para qualquer funcionário que a recebe.

### Procedimento:

Para corrigir o comportamento e garantir que a incorporação seja aplicada corretamente, siga os passos:

#### 1. Configuração do evento

##### **(1)** Acesse a tela ''Eventos'' (Pessoal+ » Cadastros » Eventos).

**(2)** Localize o evento da gratificação.

**(3)** Na aba **''Avançado''**, configure o campo **''Incide sobre médias''** para **''Incorpora ao salário''**.

![Imagem 1: (3) Na aba ''Avançado'' , configure o campo ''Incide sobre médias'' para ''Incorpora ao salário'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36688547076375)

#### 2. Inclusão do evento no parâmetro FPEVEINCSAL

##### **(1)** Acesse a tela [''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

##### **(2)** Localize o parâmetro ''FPEVEINCSAL – Eventos Variáveis Incorporados ao Salário''.

**(3)** No campo **''Texto''** inclua o código do evento.

**(4)** Salve.

![Imagem 2: (4) Salve.](https://ajuda.sankhya.com.br/hc/article_attachments/36670699561111)

#### 3. Fechamento da referência anterior

##### **(1)** Certifique-se de que a referência anterior ao cálculo está devidamente fechada.

**(2)** O sistema somente aplica a incorporação se a folha anterior estiver encerrada.

#### 4. Verificar lançamento no Lançamento de Movimento

##### **(1)** Acesse a tela [''Lançamento de Movimento''](https://ajuda.sankhya.com.br/hc/pt-br/articles/13968004985495-Lan%C3%A7amento-de-Movimento) (Pessoal+ » Rotinas Folha » Lançamento de Movimento).

**(2)** Na aba **''Funcionário''**, verifique se o evento está lançado de forma correta. 

**(3)** Após o ajuste, o sistema passará a tratar o evento como incorporação salarial, deixando de calculá-lo como média nas férias e no 13º salário.

**CAUSA:**

O comportamento incorreto ocorre porque um ou mais requisitos necessários para a incorporação não estão devidamente configurados, fazendo com que o sistema interprete o evento como **média**.

As causas identificadas são:

**1. Configuração incorreta no evento:**

- O campo ''Incide sobre médias'' não está definido como ''Incorpora ao salário'' no cadastro do evento.

**2. Evento não incluído no parâmetro FPEVEINCSAL:**

- Sem constar neste parâmetro (**Eventos Variáveis Incorporados ao Salário**), o sistema não reconhece que o evento deve integrar a remuneração.

**3. Referência anterior não está fechada:**

- Com a folha anterior aberta, o sistema considera o evento como média para evitar prejuízo ao funcionário.

**4. Evento não lançado no Lançamento de Movimento:**

- Sem o lançamento do evento para o funcionário, o valor não é utilizado na incorporação.
