---
id: "33792842489623"
titulo: "Como cadastrar dependente para pensão alimentícia"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Dependentes do Colaborador"
atualizado_em: "2026-10-08T18:38:01Z"
rotulos: ["Dependentes", "eSocial", "Folha de Pagamento", "Configuração Funcionários", "Pensão Alimentícia", "Pessoal+", "Dependente Pensionista"]
---

# Como cadastrar dependente para pensão alimentícia

**Módulo:** Pessoal+
**Versão Mínima:** 5.47.0 
**Caminho de Acesso:** Pessoal+ > Cadastros > Configuração Funcionários > Aba Dependentes
**ID da Tela:** br.com.sankhya.cadastro.funcionarios

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#descri%C3%A7%C3%A3o-e-usabilidade)

[1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#1-descri%C3%A7%C3%A3o-da-funcionalidade)
[2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#2-pr%C3%A9-requisitos)
[3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#3-diagrama-de-fluxo)
[4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#4-jornada-de-uso)
[5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#5-pontos-de-aten%C3%A7%C3%A3o)
[6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#6-dicas-de-usabilidade)
[7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#7-casos-de-uso)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#faq-%E2%80%93-d%C3%BAvidas-frequentes)
[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Como-cadastrar-dependente-para-pens%C3%A3o-aliment%C3%ADcia#artigos-relacionados)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

Essa funcionalidade permite à empresa registrar, no sistema, os beneficiários (alimentandos) de pensão alimentícia vinculados aos colaboradores. A partir desse cadastro, os valores descontados são aplicados automaticamente na folha de pagamento, de forma integrada com o financeiro.

O sistema realiza a segregação dos valores conforme o tipo de rendimento (remuneração mensal, 13º salário, férias, PLR, RRA ou rendimentos isentos), garantindo que os dados sejam gerados corretamente no grupo [penAlim] dos eventos do eSocial.

Além de facilitar o controle interno e a rastreabilidade das informações, essa funcionalidade assegura o cumprimento das obrigações legais e fiscais da empresa, conforme previsto na legislação vigente.

### 2. Pré-requisitos

**Permissões necessárias**

- Acesso ao módulo de Folha de Pagamento e telas relacionadas por meio da rotina de **Acessos** (Configurações > Controle de Acessos).
- Permissão para editar funcionários e eventos.

**Parâmetros essenciais**

- Eventos de pensão alimentícia cadastrados na tela Eventos (Pessoal+ > Cadastros);
- Fórmulas configuradas na tela Fórmulas (Pessoal+ > Cadastros) para pensão por percentual.

**Configurações relacionadas**

- Cadastro do parceiro responsável pelo recebimento da pensão na tela Parceiros (Configurações > Cadastros).

### 3. Diagrama de Fluxo

![Imagem 1: 3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/33793013853335)

### 4. Jornada de Uso

#### 4.1. Cadastrar Evento de Pensão Alimentícia

Acesse a tela **Eventos** (Pessoal+ > Cadastros) e crie um **evento de desconto para pensão alimentícia**.

**Importante:** a criação do evento e da fórmula deve ser personalizada, pois as condições estabelecidas em decisões judiciais variam de um colaborador para outro. Por isso, cabe à empresa configurar os eventos e fórmulas conforme as particularidades de cada caso, garantindo que os descontos sejam aplicados corretamente na folha de pagamento.

- Na aba **Básico**, preencha o campo **Identificação do evento** com um dos códigos específicos relacionados à pensão alimentícia:
  - 166 - Evento de pensão alimentícia - Remuneração Mensal;
  - 167 - Evento de pensão alimentícia - Rescisão;
  - 168 - Evento de pensão alimentícia - 13º Salário;
  - 148 - Evento de pensão alimentícia - Férias;
  - 149 - Evento de pensão alimentícia - PLR;
  - 150 - Evento de pensão alimentícia - RRA.
- A **Unidade** deve ser configurada como **Quantidade**.
- Não preencha o campo **Evento como regra em cálculo de**.
- Se a pensão for por percentual, **Selecione a fórmula** correspondente.

  ![Imagem 2: Se a pensão for por percentual, Selecione a fórmula correspondente.](https://ajuda.sankhya.com.br/hc/article_attachments/33793797568023)
- Na aba **Avançado**, defina **Base DIRF** como **Pensão Judicial** ou **Pensão Judicial 13º**. Considere, ainda, que não há incidência de **INSS**. 

  A incidência de **IRRF** deve ser avaliada conforme o caso.

  ![Imagem 3: A incidência de IRRF deve ser avaliada conforme o caso.](https://ajuda.sankhya.com.br/hc/article_attachments/33793807106967)
- Na aba **eSocial**, selecione a opção **9213 - Pensão Alimentícia** no campo **Natureza da Rubrica**. 

  ![Imagem 4: Na aba eSocial , selecione a opção 9213 - Pensão Alimentícia no campo Natureza da Rubrica .](https://ajuda.sankhya.com.br/hc/article_attachments/33793840535703)

#### 4.2. Configurar Fórmula de Pensão Alimentícia

Na tela **Fórmulas** (Pessoal+ > Cadastros), configure uma fórmula específica para **calcular o percentual da pensão**, conforme a decisão judicial e os seguintes critérios:

- **Pensão por percentual do valor bruto ou líquido da folha de pagamento** cuja decisão judicial permita a dedução do IRRF retido da base de cálculo da pensão e a pensão deduza da base de cálculo do IRRF, utilize o modelo de sugestão de fórmula de pensão alimentícia 7 cálculos: [Configuração de Fórmulas de Pensão por Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/29655219319575).
- **Pensão em percentual sobre o salário mínimo**

Pode ser utilizada a seguinte fórmula

FTF(5, 1, @E\_INSALUBRIDADE, &Refere, QueFuncionario.TIPTAB)\*QUEMOVIMENTO.INDICE/100

- **Pensão em percentual sobre o salário líquido ou bruto** poderá utilizar a fórmula abaixo.

FBASEPENSDEP(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, 'M',QueMovimento.SEQUENCIA) \* QUEMOVIMENTO.INDICE/100

- **Pensão definida por valor fixo**, não é necessário criar fórmula.

Após a criação, vincule a fórmula ao evento no campo **Selecione a fórmula**, disponível na aba **Básico** do cadastro do evento.

#### 4.3. Cadastrar Dependente Pensionista

O cadastro do dependente pode ser feito pela requisição de Inclusão de Dependentes ou diretamente na tela Configuração Funcionários.

(1)** Requisições > Inclusão Dependentes**

- Acesse a tela **Requisições** (Pessoal+ > Rotinas Folha), opção **Inclusão de Dependente**, clique sobre o card do funcionário e depois no botão **Incluir Dependente**.

  [GIF animado: Imagem 5: Acesse a tela Requisições (Pessoal+ > Rotinas Folha), opção Inclusão de Dependente , clique sobre o card do funcionário…](https://ajuda.sankhya.com.br/hc/article_attachments/33797651230231)
- Preencha todos os dados obrigatórios de cada dependente. Marque a opção **Pensionista** e informe o tipo de pensão, o valor ou percentual, e o parceiro responsável que receberá a pensão.
- Salve e confirme o pedido. Essa requisição será enviada para aprovação do responsável, geralmente alguém do Departamento Pessoal.
- O DP será responsável por aprovar e configurar os eventos de descontos e as incidências que compõem as bases de cálculo, diretamente no cadastro do colaborador (tela Configuração Funcionários > Dependentes).

**(1)** **Tela Configuração Funcionários**

- Na tela **Configuração Funcionários** (Configurações > Cadastros > Pessoal), localize o funcionário e acesse a aba **Dependentes**. 

  ![Imagem 6: Na tela Configuração Funcionários (Configurações > Cadastros > Pessoal), localize o funcionário e acesse a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/33820350434583)
- Clique no botão **"+"** e, na sub-aba **Geral**, preencha os dados do dependente e marque **Pensionista**.
- Em **Dados da Pensão**, informe: o tipo de pensão, o valor ou percentual, o parceiro responsável (quem receberá) e inclua os eventos criados para desconto.

  ⚠️ Os campos de valor e percentual não devem ser preenchidos com zero **"0,00"**.

  ![Imagem 7: ⚠️ Os campos de valor e percentual não devem ser preenchidos com zero "0,00" .](https://ajuda.sankhya.com.br/hc/article_attachments/33820443696023)
- Complete as sub-abas de incidências (Mensal, 13º, Férias, Férias Indenizadas, PLR) indicando os eventos que compõem as bases de cálculo.
- Salve o cadastro.

#### 4.4. Envio do evento S-2200 ou S-2205 (eSocial)

Acesse a tela **Central do eSocial** (Pessoal+ > Rotinas Folha) para gerar e enviar o evento ao eSocial. 

- S-2200: utilize quando o dependente for incluído junto com a admissão do colaborador;
- S-2205: use quando o dependente for incluído após a admissão.

  ![Imagem 8: S-2205: use quando o dependente for incluído após a admissão.](https://ajuda.sankhya.com.br/hc/article_attachments/33816014999063)
- Após o envio, verifique o retorno de sucesso no sistema. Além disso, é importante acessar o Portal do eSocial e confirmar se o dependente foi efetivamente registrado por lá.

#### 4.5. Lançamento de Movimento

O sistema gera automaticamente o movimento de desconto na folha do funcionário com base no dependente cadastrado.

Acesse a tela **Lançamento de Movimento** (Pessoal+ > Rotinas Folha), confira, no card do colaborador, se consta o evento de pensão e valide se a **Sequência** do lançamento corresponde à **Sequência** do dependente. 

![Imagem 9: Acesse a tela Lançamento de Movimento (Pessoal+ > Rotinas Folha), confira, no card do colaborador, se consta o evento…](https://ajuda.sankhya.com.br/hc/article_attachments/33817262878359)

![Imagem 10: Acesse a tela Lançamento de Movimento (Pessoal+ > Rotinas Folha), confira, no card do colaborador, se consta o evento…](https://ajuda.sankhya.com.br/hc/article_attachments/33798638822807)

#### 4.6. Cálculo da Folha

- Execute o cálculo da folha em que o desconto deve ser aplicado, acessando a tela **Cálculos** (Pessoal+ > Rotinas Folha), como, por exemplo, a folha mensal.
- Verifique, na aba **Folha**, se o desconto da pensão foi calculado para cada dependente. 

  ![Imagem 11: Verifique, na aba Folha , se o desconto da pensão foi calculado para cada dependente.](https://ajuda.sankhya.com.br/hc/article_attachments/33820847511447)
- Valide se a **Sequência** do lançamento corresponde à **Sequência** do dependente e se o valor está proporcional à base (salário ou valor fixo). 

  ![Imagem 12: Exemplo prático : funcionário com salário R$ 2.000,00 - Um dependente - Pensão de 30% - Desconto gerado R$ 600,00](https://ajuda.sankhya.com.br/hc/article_attachments/33817598559383)
  **Exemplo prático**: funcionário com salário R$ 2.000,00 - Um dependente - Pensão de 30% - Desconto gerado R$ 600,00
- Confirme o cálculo da folha.

#### 4.7. Integração com o Financeiro

- Acesse a tela **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha), selecione a folha calculada e ative o modo de seleção para exibir os botões pertinentes em tela. 

  ![Imagem 13: Acesse a tela Gerenciador de Folhas (Pessoal+ > Rotinas Folha), selecione a folha calculada e ative o modo de seleção…](https://ajuda.sankhya.com.br/hc/article_attachments/33801178816663)
- Clique no botão **![Imagem 14: Clique no botão Integração Financeira por Eventos .](https://ajuda.sankhya.com.br/hc/article_attachments/33801178818071) Integração Financeira por Eventos**.
- Informe o evento, os dados complementares e marque a opção **Usar parceiro responsável pelo recebimento da pensão**. 

  ![Imagem 15: Informe o evento, os dados complementares e marque a opção Usar parceiro responsável pelo recebimento da pensão .](https://ajuda.sankhya.com.br/hc/article_attachments/33817619788439)
- Clique em **Visualizar Integração Financeira** para conferir os valores e confirme a integração financeira.

#### 4.8. Envio do evento S-1200 ou S-1210 ao eSocial

- Acesse a tela **Central do eSocial** (Pessoal+ > Rotinas Folha) para gerar e enviar os eventos ao eSocial.
  - S-1200: envia os valores de remuneração;
  - S-1210: envia os pagamentos realizados, incluindo pensão.

    ![Imagem 16: S-1210: envia os pagamentos realizados, incluindo pensão.](https://ajuda.sankhya.com.br/hc/article_attachments/33818308465687)
- Após o envio, verifique se o valor da pensão consta no S-1210 com o CPF do dependente.

  ![Imagem 17: Após o envio, verifique se o valor da pensão consta no S-1210 com o CPF do dependente.](https://ajuda.sankhya.com.br/hc/article_attachments/33821106236439)

#### 4.9 Encerramento do desconto de pensão alimentícia

Se o colaborador deixou de ter a obrigação judicial de pagar pensão alimentícia, é possível encerrar o desconto sem excluir o dependente, mantendo todo o histórico cadastral e financeiro.

1. Acesse a tela **Configuração Funcionários** (Configurações > Cadastros > Pessoal) e vá até a aba **Dependentes**.
2. Localize o dependente com pensão alimentícia ativa e, na sub-aba **Geral**, preencha o campo **Referência limite da pensão** com a **última referência** em que o desconto deve ocorrer (ex: 05/2025).

   A **referência informada** deve ser igual à **referência atual da empresa**.

   Após informar a data:

   - o sistema **impedirá novos descontos** em folhas futuras;
   - as informações da pensão ficarão **visíveis apenas para consulta**, evitando alterações indevidas.

   **Importante**

   - Não pode haver **cálculos em referências posteriores**, com exceção de férias ou adiantamento.
   - Caso haja cálculos posteriores, o sistema exibirá uma mensagem orientando a reabertura e exclusão dessas folhas.
   - Se a folha da referência informada já estiver fechada, será necessário reabri-la para editar ou apagar o campo.
3. Após preencher o campo, salve o cadastro do dependente e **execute o cálculo da folha** normalmente. 

   O sistema deixará de considerar os eventos de pensão a partir da próxima referência.

### 5. Pontos de Atenção

- Os campos **Identificação do evento** e **Natureza da Rubrica** **são gatilhos** para o correto envio do evento S-1210 ao eSocial.
- Quando **a inclusão de dependentes for realizada por requisições**, lembre-se de acessar o cadastro do colaborador **na tela Configuração Funcionários para configurar o desconto da pensão alimentícia** após a aprovação da solicitação.
- O preenchimento do **Parceiro responsável pelo recebimento da pensão é essencial** para que o valor da pensão seja corretamente calculado, integrado ao financeiro e para que o sistema gere automaticamente o grupo [penAlim] no evento S-1210.
- A **sequência deve ser a mesma do dependente no cadastro, lançamento do movimento e cálculo da folha** de pagamento para o correto envio ao eSocial.
- **Avalie a incidência de IRRF**, caso a caso; **não há incidência de INSS** sobre pensão.
- **Configure o desconto para cada tipo de folha em que a pensão deve incidir.**

  O desconto de pensão alimentícia não é automático para todos os tipos de folha só porque foi configurado uma vez. Na aba **Dados da Pensão** do dependente, preencha o campo de **Evento de Desconto** correspondente a cada tipo de folha em que o colaborador recebe valores: além do **Evento de Desconto - Mensal**, preencha também **Evento de Desconto - Férias** e **Evento de Desconto - 13º Salário** (e **Férias Indenizadas** ou **PLR**, quando aplicável). Deixar algum desses campos em branco faz a pensão não ser descontada naquele tipo de folha específico.
- **Configure também a base de cálculo e a fórmula de cada tipo de folha**.

  Além do evento de desconto, complete as abas **Incidências da Pensão Férias** e **Incidências da Pensão 13º**, informando os eventos/rubricas que devem compor a base de cálculo da pensão em cada um desses tipos de folha. Confirme também se a fórmula do evento de desconto está ajustada para o tipo de folha correspondente; a fórmula usada na folha mensal não deve ser reaproveitada em férias ou 13º sem adaptação.

  📚 Veja os três modelos de fórmula, por tipo de folha, em [Como configurar fórmulas de pensão por dependente?](https://ajuda.sankhya.com.br/hc/pt-br/articles/29655219319575).

  Por fim, confirme se o percentual ou valor configurado no cadastro do dependente reflete exatamente o que foi determinado judicialmente, já que essa é a referência usada em todos os tipos de folha.

### 6. Dicas de Usabilidade

- Utilize filtros nas abas de incidências do cadastro do dependente para localizar rapidamente os eventos necessários.
- Preencha os campos conforme a sentença judicial e realidade do funcionário.
- Revise os dados antes de confirmar a integração financeira para evitar divergências.

### 7. Casos de Uso

✅ **Exemplo Real:**
Cadastro de dependente pensionista com desconto percentual sobre o salário bruto, parceiro responsável informado e eventos de desconto configurados corretamente.

❌ **Erro Comum:**
Lançar os eventos de desconto diretamente na tela Lançamento de Movimento.

## FAQ – Dúvidas Frequentes

1. **É obrigatório informar o parceiro responsável pelo recebimento da pensão?**

   Sim, é um dos principais gatilhos para cálculo, integração financeira e envio ao eSocial.
2. **Preciso criar fórmula para todo tipo de pensão?**

   Não. Apenas para pensão calculada por percentual. Para valor fixo, não é necessário.
3. **Como cadastrar uma pensão com valor fixo?**

   Basta informar o valor no cadastro do dependente. Não é necessário fórmula.
4. **Como garantir que o desconto será enviado corretamente ao eSocial?**

   Certifique-se de preencher corretamente os campos "Identificação do evento" e "Natureza da Rubrica" nos eventos de pensão.
5. **Como saber se a pensão foi enviada ao eSocial?**

   No evento S-1210, verifique o grupo de Informações dos beneficiários da pensão alimentícia.
6. **O campo Percentual FGTS afeta o cálculo da pensão?**

   Não, é apenas informativo para rescisão e envio ao evento S-2999.
7. **A pensão alimentícia tem incidência de INSS?**

   Não. IRRF pode ter, dependendo do caso.
8. **O que fazer quando enviar o evento S-1210 e receber os retornos:**

- **"Erro 8 – Grupo ‘Informação dos beneficiários da pensão alimentícia’ deve ser preenchido.".**
  Esse erro ocorre quando o eSocial identifica que há desconto de pensão alimentícia, mas não encontra as informações completas para montar o grupo [penAlim].

  Verifique se o dependente está marcado como "Pensionista", se o Parceiro (responsável pelo recebimento) está preenchido e/ou se a sequência do dependente está correta no cadastro.
- **"Erro 1861 – CPF do dependente ‘XX’ inválido."**
  Esse erro pode ser causado pela presença de informações de um dependente que ainda não consta no Portal eSocial.

  Confira se houve o envio do dependente ao eSocial e caso não, realize o envio do evento S-2205 antes do envio do evento S-1210.

## Artigos Relacionados

- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767)
- [Configuração de Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287)
- [Como configurar fórmulas de pensão por dependente?](https://ajuda.sankhya.com.br/hc/pt-br/articles/29655219319575)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
