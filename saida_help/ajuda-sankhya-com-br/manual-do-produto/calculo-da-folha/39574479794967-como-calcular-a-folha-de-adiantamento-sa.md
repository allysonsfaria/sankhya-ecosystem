---
id: "39574479794967"
titulo: "Como calcular a folha de adiantamento salarial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Cálculo da Folha"
atualizado_em: "2026-10-02T15:34:51Z"
rotulos: ["eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Folha de Pagamento", "Gerenciador de Folhas", "Configuração Funcionários", "Pessoal+", "Cálculo da Folha de Adiantamento Salarial", "Adiantamento Salarial"]
---

# Como calcular a folha de adiantamento salarial

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:** br.com.sankhya.rh.CalculoIndFolha

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KNM8VTC156V1T0RDKT6HSDZ3)

1. [Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KNM8QJSSCM63W5PDYC5H509H)
2. [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KNM8QJSXM70BFA46K6MEGKA4)
3. [Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KNM8QJT47HTJP549CCK4CXFD)
4. [Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KNM8QJVAZ8JGY2XAP5E7KYFB)
5. [Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KNM8QJVCV2JX3915BPYYXPN8)

[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KNM8QJVEYWZHTPXGADT4055F)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KNM8QJVJZ90JPXBAJ439P5GN)

---

## Descrição e Usabilidade

O cálculo da **folha de adiantamento salarial** é utilizado pelas empresas que realizam o pagamento antecipado de parte do salário do colaborador antes do fechamento da folha mensal.

Embora esse cálculo **não seja obrigatório por legislação**, ele é uma prática comum em empresas que adotam políticas internas de **vale salarial, quinzena ou adiantamento mensal**.

No Pessoal+, essa rotina pode ser realizada de **duas formas**:

**1. Por percentual no cadastro do colaborador**

- Utilizada quando a empresa define um percentual fixo sobre o salário (ex: 30%, 40%, 50%).

**2. Por valor lançado manualmente**

- Utilizada quando o adiantamento não segue percentual fixo.

### 1. Descrição da Funcionalidade

A rotina de adiantamento salarial permite:

- calcular antecipações salariais;
- gerar holerite de adiantamento;
- integrar com financeiro;
- integrar com contabilidade;
- liberar recibo ao PortalRH;
- controlar envio ao eSocial;
- recalcular ou excluir quando necessário.

Quando o percentual é configurado no cadastro do colaborador, o sistema identifica automaticamente, mês a mês, que existe uma folha pendente de adiantamento.

### 2. Pré-requisitos

**Permissões**

Acesso às telas:

- Configuração Funcionários;
- Cálculos;
- Gerenciador de Folhas;
- Lançamento de Movimento (quando usar valor).

**Configuração de percentual no cadastro do colaborador**

1. Acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros).
2. Localize o(s) colaborador(es).
3. Na aba **Contrato**, preencha o campo **% Adiantamento**.

   Exemplo: 40%

   ![Imagem 1: Exemplo: 40%](https://ajuda.sankhya.com.br/hc/article_attachments/39745010956183)

   💡 A fórmula do evento padrão Sankhya utiliza esse campo para calcular automaticamente.
4. Após salvar, o sistema passará a considerar mensalmente esse colaborador na folha de adiantamento.

**Configuração de valor no movimento do colaborador**

1. Acesse a tela **Lançamento de Movimento** (Pessoal+ > Rotinas Folha).
2. Filtre por **Empresa** e **Referência**.
3. Localize o colaborador e selecione o card correspondente.
4. Na aba **Lançamento**, indique:

   - Tipo de Movimento = Fixo;
   - Código do Evento de Adiantamento;
   - Valor.
5. Clique em **Finalizar Adição** para salvar e depois, em **Lançar Movimentos**.

   ![Imagem 2: Clique em Finalizar Adição para salvar e depois, em Lançar Movimentos .](https://ajuda.sankhya.com.br/hc/article_attachments/39745694470167)

**Antes de calcular:**

- Se já existir uma folha mensal calculada para a mesma competência, o cálculo do adiantamento fica bloqueado. Exclua o cálculo da folha mensal antes de calcular o adiantamento.
- Confirme que o evento de adiantamento está ativo e configurado para participar da folha de adiantamento (Pessoal+ > Cadastros > Eventos).

### 3. Jornada de Uso

**(1)** A tela de **Cálculos**(Pessoal+ > Rotinas Folha) pode ser acessada de duas maneiras:

1. Pela barra de pesquisa do Sankhya Om;

![Imagem 3: Pela barra de pesquisa do Sankhya Om;](https://ajuda.sankhya.com.br/hc/article_attachments/40299265242647)

2. Pelo **Gerenciador de DP** (Pessoal+ > Rotinas Folha), clicando sobre o menu **Cálculos**.

![Imagem 4: Pelo Gerenciador de DP (Pessoal+ > Rotinas Folha), clicando sobre o menu Cálculos .](https://ajuda.sankhya.com.br/hc/article_attachments/40299293193495)

**(2)**  O cálculo de folha adiantamento pode ser realizado de duas formas:

- [coletiva](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KR1E0V7JMDKCZPQ1K74YHP00);
- [individual](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967-Como-calcular-a-folha-de-adiantamento-salarial#h_01KMN9T6V9VMMTP3H52XTBVM5Y).

Clique sobre a opção desejada.

![Imagem 5: Clique sobre a opção desejada.](https://ajuda.sankhya.com.br/hc/article_attachments/40299265243671)

#### 🔹Realizar o cálculo coletivo

1. Para calcular todos os colaboradores de uma vez:
2. Clique em **Coletivo**.
3. Selecione **Adiantamento** e preencha as etapas abaixo:
   1. Etapa 1 – **Informações Gerais**
      1. Informe a **Referência** (mês/ano) e a **Data de Pagamento**.
      2. Ao marcar a opção **Apenas folhas não calculadas**, serão apresentadas nas próximas etapas somente os colaboradores que não tiveram folhas de pagamento calculadas na referência selecionada.
   2. Etapa 2 – **Empresas**
      1. Selecione a(s) **empresa**(s).
   3. Etapa 3 –**Departamentos**
      1. Selecione os **departamentos** (opcional).
   4. Etapa 4 – **Funcionários**
      1. Defina os **colaboradores**.

         Nesta etapa é possível realizar filtros de seleção para agilizar a escolha dos colaboradores.
   5. Etapa 5 – **Calcular**
      1. Clique em **Calcular**.
4. Acesse a tela [**Gerenciador de Folhas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247) (Pessoal+ > Rotinas Folha) para realizar:
   1. as devidas conferências;
   2. confirmação da folha;
   3. emissão dos recibos de pagamento;
   4. integrações contábil e financeira;
   5. liberação da folha para o eSocial.

#### 🔹Realizar o cálculo individual

1. Selecione os cards **Individual** e **Adiantamento** respectivamente.
2. Preencha as etapas:

   1. Etapa 1 – **Informações Gerais**

      - Referência;
      - Data de Pagamento;
      - Empresa;
      - Funcionário.

      Clique em **Próximo**.
   2. Etapa 2 – **Calcular**

      1. Escolha o modo:

         - **Calcular com log**
         - **Calcular sem log**
         - **Calcular com log de incorporações**

         💡 **Recomendação:** utilize **Calcular com log** para auditoria e conferência.

         O log apresenta:

         - fórmulas principais;
         - fórmulas auxiliares;
         - variáveis utilizadas;
         - funções executadas;
         - eventos acionados.
3. Clique em **Calcular**.
4. Após o cálculo, realize a [conferência da folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/39318926935191) revisando:

- valor do adiantamento;
- base salarial utilizada;
- descontos;
- líquido;
- eventos gerados.

  Se estiver correto, clique em **Confirmar Folha**.

  | ⚠️ Após a confirmação, no cálculo individual ainda é possível **Lançar Evento** na aba **Movimentações**:  1. clique em **Adicionar Movimento** e informe o **Evento** e o **Índice**; 2. clique em **Finalizar Adição** e verifique se o evento foi inserido; 3. clique em **Confirmar alterações** para o sistema efetuar o recálculo automático da folha. |
  | --- |

5. Após a confirmação, clique em **Documentos** para emitir ou enviar o **holerite de adiantamento**.

   O sistema apresentará o recibo para:

- impressão;
- envio por e-mail;
- conferência interna.

6. Acesse a tela [**Gerenciador de Folhas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247) (Pessoal+ > Rotinas Folha) para realizar:
   - integrações contábil e financeira;
   - liberação da folha para o eSocial.

### 4. Pontos de Atenção

- O cálculo de adiantamento é **opcional** e depende da política da empresa.
- O adiantamento salarial considera o **pagamento no mês para composição do IRRF**.
- O evento de adiantamento (padrão 650) e o evento de desconto do adiantamento na folha mensal precisam estar configurados para incidir na base **1904 – Base IRRF Folha Normal**. Isso garante que o valor seja considerado corretamente na recomposição das bases tributáveis do período, evitando bitributação.
- O regime da empresa (**Caixa** ou **Competência**), configurado em **Empresas** (Pessoal+ > Cadastros), interfere diretamente na recomposição do IRRF sobre o adiantamento.
- O cálculo padrão **não realiza desconto de INSS**.
- O percentual informado no cadastro impacta automaticamente as próximas competências.
- Sempre valide a data de pagamento antes do cálculo.
- Em cálculo coletivo, revise os colaboradores pelo botão **Ver Funcionários**.
- Após integrações financeiras e contábeis, revise as informações antes da liberação ao eSocial.
- Caso haja erro após liberação, bloqueie o envio, ajuste a folha e libere novamente.
- Para que a folha de adiantamento seja corretamente [gerada no evento S-1200 do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/37945375822103), é necessário que exista ao menos **um evento** calculado que **não esteja configurado apenas como É base? na tela Eventos**. Quando a folha possuir somente eventos classificados como base, o sistema poderá não gerar o S-1200 da competência.

### 5. Dicas de Usabilidade

- Utilize percentual fixo quando a política da empresa for padronizada.
- Prefira cálculo com log em conferências de suporte.
- Faça a conferência do líquido antes de confirmar.
- Utilize PortalRH para reduzir solicitações de holerite ao DP.
- Realize integrações somente após conferência final.

## Perguntas Frequentes (FAQ)

**1. O cálculo de adiantamento é obrigatório?**

Não. Ele é opcional e depende da política interna da empresa.

**2. Posso calcular por valor em vez de percentual?**

Sim. Nesse caso, utilize a tela **Lançamento de Movimento**.

**3. O cálculo pode ser realizado de forma coletiva?**

Sim. É possível calcular todos os colaboradores da empresa em uma única execução.

**4. O adiantamento salarial desconta INSS?**

Não no cálculo padrão. O adiantamento normalmente considera apenas antecipação salarial para composição posterior da folha mensal.

**5. O adiantamento impacta o IRRF?**

Sim. O pagamento do adiantamento é considerado na composição do IRRF da competência.

**6.** **Posso recalcular a folha após confirmar?**

Sim. Porém, antes disso, revise possíveis integrações contábeis, financeiras e liberações ao eSocial.

**7**. **Posso incluir eventos após a confirmação da folha?**

Sim. Na folha individual é possível incluir movimentações adicionais pela aba Movimentações.

**8.** **O percentual de adiantamento vale para os próximos meses?**

Sim. Enquanto o campo % Adiantamento permanecer preenchido no cadastro do colaborador, o sistema continuará utilizando esse percentual automaticamente.

**9. Posso calcular somente alguns departamentos?**

Sim. No cálculo coletivo é possível filtrar os colaboradores por departamento.

**10. Posso liberar o holerite no PortalRH?**

Sim. A liberação pode ser feita após a confirmação da folha.

**11. Preciso integrar com financeiro e contabilidade?**

Somente se a empresa possuir licença desses módulos.

**12.** **O adiantamento não está sendo descontado na folha mensal. O que verificar?**

Verifique se:

- o evento de desconto de adiantamento está corretamente configurado;
- apenas um evento possui a característica de desconto de adiantamento salarial;
- o evento participa da folha normal;
- a fórmula do evento está correta;
- a folha anterior foi fechada corretamente.

Também valide se o evento está marcado para cálculo na folha complementar e se o cálculo foi reprocessado após os ajustes.

**13. O sistema não está calculando adiantamento para colaboradores em férias. O que pode causar isso?**

Normalmente isso ocorre devido à fórmula do evento de adiantamento possuir validações que bloqueiam o cálculo quando existem dias de férias na referência.

Nesses casos, é necessário:

- revisar a fórmula do evento;
- validar as condições envolvendo dias trabalhados;
- ou criar um evento complementar específico para colaboradores pós-férias.

Também é importante verificar se o colaborador trabalhou pelo menos metade do mês.

**14. O valor do adiantamento está diferente do percentual esperado. O que devo conferir?**

Verifique:

- se o evento utiliza fórmula padrão ou personalizada;
- o tipo de mês da regra de cálculo (Comercial ou Real);
- configurações de resíduos;
- fórmulas que dividem fixamente por 30 dias.

Fórmulas personalizadas podem gerar diferenças quando o mês possui 31 dias ou quando existem afastamentos e férias.

**15. O IRRF do adiantamento não está sendo calculado. O que pode causar isso?**

As causas mais comuns são:

- utilização de eventos personalizados sem configuração adequada;
- fórmula de IRRF personalizada;
- evento de adiantamento sem incidência correta;
- evento padrão 650 inativo;
- sequência incorreta de eventos;
- valor mínimo de desconto configurado no evento de IRRF.

Em muitos cenários, a utilização do evento padrão resolve a inconsistência.

**16. O sistema está calculando adiantamento para colaborador afastado pelo INSS. Como corrigir?**

Verifique se:

- o afastamento foi lançado corretamente;
- a ocorrência utilizada corresponde ao tipo correto de afastamento;
- a situação do colaborador foi atualizada corretamente no cadastro.

Quando o afastamento não ultrapassa os primeiros 15 dias, o sistema pode entender que o colaborador ainda está em atividade normal.

**17. O colaborador afastado por licença maternidade não está recebendo adiantamento. O que verificar?**

Esse comportamento normalmente está relacionado a:

- fórmulas personalizadas;
- eventos desprotegidos;
- validações específicas por empresa dentro da fórmula.

Verifique se o evento padrão está ativo e atualizado.

**18. O adiantamento está utilizando salário antigo após reajuste salarial. Como corrigir?**

Verifique a aba Histórico da tela Configuração Funcionários.

Se existir histórico gravado antes do reajuste salarial para a mesma referência do cálculo, o sistema poderá considerar o salário anterior no cálculo do adiantamento.

**19. Posso utilizar eventos personalizados para adiantamento?**

Sim, porém é necessário garantir que:

- as incidências estejam corretas;
- as bases estejam configuradas;
- as fórmulas estejam atualizadas;
- os eventos participem corretamente das recomposições de IRRF.

Eventos personalizados desatualizados são uma das principais causas de inconsistência no cálculo.

**20. O sistema apresenta aviso de tabelas de faixa desatualizadas ao emitir o holerite. O que fazer?**

Verifique:

- se existem tabelas duplicadas;
- se os códigos das tabelas estão corretos;
- se as tabelas foram atualizadas adequadamente após upgrade do sistema.

Após ajuste das tabelas, recalcule a folha de adiantamento.

**22. Por que colaboradores admitidos no mesmo dia tiveram cálculos diferentes?**

Isso normalmente ocorre quando:

- os colaboradores pertencem a sindicatos diferentes;
- utilizam regras de cálculo diferentes;
- possuem tipos de mês distintos (Comercial ou Real).

As regras de cálculo impactam diretamente a proporcionalidade do adiantamento.

## Artigos Relacionados

- [Configuração de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Lançamento de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319)
- [Cálculos da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
