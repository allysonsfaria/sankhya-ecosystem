---
id: "39309113368599"
titulo: "Cálculo da Folha de Pagamento: visão geral"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599-C%C3%A1lculo-da-Folha-de-Pagamento-vis%C3%A3o-geral"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Cálculo da Folha"
atualizado_em: "2026-09-27T17:36:35Z"
rotulos: ["Configuração", "Eventos", "Impostos", "eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Folha de Pagamento", "Gerenciador de Folhas", "Pessoal+", "Cálculos da folha de pagamento", "INSS FGTS IRRF PIS"]
---

# Cálculo da Folha de Pagamento: visão geral

## Descrição e Usabilidade

O cálculo da folha de pagamento é a etapa onde o sistema apura os valores que o colaborador deve receber (proventos) e os descontos aplicáveis, como INSS, IRRF e benefícios.

No módulo Pessoas+, esse processo é feito de forma automatizada, com base nos cadastros, eventos e regras configuradas no sistema.

Essa rotina deve ser utilizada sempre que a empresa precisar:

- Calcular salários mensais;
- Gerar férias, rescisões ou 13º salário;
- Apurar encargos trabalhistas;
- Preparar informações para envio ao eSocial.

**Base legal**

O cálculo da folha segue regras da legislação trabalhista e tributária brasileira, como:

- CLT (Consolidação das Leis do Trabalho);
- INSS (Previdência Social);
- IRRF (Imposto de Renda Retido na Fonte);
- FGTS (Fundo de Garantia);
- eSocial (obrigação acessória do governo).

O sistema realiza esses cálculos conforme as incidências configuradas nos eventos, garantindo que os valores estejam corretos para apuração e envio ao governo.

### 1. Descrição da Funcionalidade

A rotina de **Cálculos** permite:

- Calcular folhas individuais ou coletivas.
- Apurar encargos (INSS, FGTS, IRRF, PIS).
- Validar configurações antes do cálculo.
- Conferir valores detalhados por funcionário.
- Gerar dados para integração contábil, financeira e eSocial.

O sistema também realiza validações automáticas, como:

- Comparação entre incidências de cálculo e eSocial;
- Verificação das bases de cálculo;
- Identificação de divergências em eventos.

Caso existam inconsistências, o sistema alerta antes de prosseguir.

### 2. Pré-requisitos

#### Permissões necessárias

1. Acesse o **Painel de Configurações** (Pessoal+ > Configurações > Painel de Configurações).
2. Vá até a seção **Configuração de Permissões**.
3. Selecione a tela **Cálculos**, em seguida, o grupo de acessos e usuários desejados e certifique-se de que a permissão **para realizar todos os tipos de cálculo** esteja habilitada para permitir o uso da tela.

   [GIF animado: Imagem 1: Selecione a tela Cálculos , em seguida, o grupo de acessos e usuários desejados e certifique-se de que a permissão para…](https://ajuda.sankhya.com.br/hc/article_attachments/39707858954519)

   Também é necessário ativar as permissões para realizar as seguintes funcionalidades diretamente na tela **Cálculos**:

   - **Lançar movimentos**;
   - **Editar eventos**;
   - **Recalcular / Excluir** folhas;
   - **Integrar com o financeiro**.

     1. No **Painel de Configurações** (Pessoal+ > Configurações > Painel de Configurações), seção **Configuração de Permissões**.
     2. Selecione o card **Folha**, em seguida, o grupo de usuários desejado e certifique-se de que as permissões acima estejam habilitadas.

        [GIF animado: Imagem 2: Selecione o card Folha , em seguida, o grupo de usuários desejado e certifique-se de que as permissões acima estejam…](https://ajuda.sankhya.com.br/hc/article_attachments/39708562092567)

#### Configurações prévias

(3)**Eventos**

Certifique na tela **Eventos** (Pessoal+ > Cadastros > Eventos) que os eventos que você precisa estão configurados para os tipos de folha que serão calculadas:

- eventos cadastrados corretamente;
- incidências (INSS, FGTS, IRRF, eSocial) configuradas;
- **eventos marcados** como parte de regras automáticas de cálculo para outros tipos de pagamento (mensal, férias);
- se o evento **possui reflexos**, como DSR, e se estes também estão corretamente configurados.

(3)**Lançamento de movimento**

Acesse a rotina de **Lançamento de movimento** (Pessoal+ > Rotinas Folha > Lançamento de Movimento) e crie os lançamentos (horas extras, faltas, adicionais) necessários.

📚 Para mais detalhes, consulte o artigo: [Lançamento de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319).

### 3. Jornada do Cálculo da Folha

A seguir está o fluxo completo recomendado:

#### **(1)** Acessar a rotina de cálculos

A tela de **Cálculos** (Pessoal+ > Rotinas Folha) pode ser acessada de duas maneiras:

1. Pela barra de pesquisa do Sankhya Om;

   ![Imagem 3: Pela barra de pesquisa do Sankhya Om;](https://ajuda.sankhya.com.br/hc/article_attachments/39310406964759)
2. Pelo **Gerenciador de DP** (Pessoal+ > Rotinas Folha), clicando sobre o menu **Cálculos**.

   ![Imagem 4: Pelo Gerenciador de DP (Pessoal+ > Rotinas Folha), clicando sobre o menu Cálculos .](https://ajuda.sankhya.com.br/hc/article_attachments/39310484206615)

#### **(2)** Realizar o cálculo da folha

Escolha o tipo de cálculo:

- [Mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/39311261533335)
- [Adiantamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39574479794967)
- [Dissídio](https://ajuda.sankhya.com.br/hc/pt-br/articles/40279701222935)
- Férias
- Rescisão
- 13º salário
- Pensionista
- Intermitente
- [Avulsa](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295)
- [Rescisão complementar](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727)
- [Autônomo](https://ajuda.sankhya.com.br/hc/pt-br/articles/43529821213335)

O cálculo pode ser:

- Coletivo (vários colaboradores);
- Individual.

#### **(3)** Tratar divergências (se houver)

Antes do cálculo, o sistema pode apresentar inconsistências como:

- Eventos com incidência incorreta;
- Diferença entre base de cálculo e eSocial.

  ![Imagem 5: Diferença entre base de cálculo e eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/39310552684567)

Você pode:

- **Corrigir** imediatamente;
- **Continuar com o cálculo** e ajustar depois;
- Ou clicar no botão Exportar para Planilha em excel para visualizar todas as divergências para correção.

Após tratar as divergências poderá seguir o cálculo com segurança.

#### **(4)** Conferir a folha de pagamento

![Imagem 6: (4) Conferir a folha de pagamento](https://ajuda.sankhya.com.br/hc/article_attachments/39582001382167)

Após o cálculo, é obrigatório conferir:

- Proventos (salários, adicionais, horas extras);
- Descontos (INSS, IRRF, benefícios);
- Bases de cálculo;
- Encargos (FGTS, INSS, PIS);
- Avisos e inconsistências.

A conferência pode ser feita:

- Na própria tela [**Cálculos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/39318926935191) (cálculo individual);
- Ou no **Gerenciador de Folhas** (cálculo coletivo).

#### **(5)** Confirmar a folha

Após a conferência, clique em **Confirmar Folha**.

![Imagem 7: Após a conferência, clique em Confirmar Folha .](https://ajuda.sankhya.com.br/hc/article_attachments/39582036382359)

Isso garante que os valores estão validados e prontos para os próximos processos.

#### **(6)** Emitir holerite

Após a confirmação:

1. Acesse **Documentos > Holerite...**.

   [GIF animado: Imagem 8: Acesse Documentos > Holerite... .](https://ajuda.sankhya.com.br/hc/article_attachments/39582164036631)

   O sistema apresentará o recibo para:

   - conferência interna;
   - impressão;
   - envio por e-mail.

| ℹ️ **Nota:** a emissão dos holerites pode ser influenciada por parâmetros específicos de cada tipo de folha (mensal, férias, 13º salário, rescisão, entre outros). Para conhecer seus impactos na geração do documento, consulte o artigo [**Parâmetros do Pessoal+**](https://ajuda.sankhya.com.br/hc/pt-br/articles/38767444361239). |
| --- |

#### **(7)**  Liberação para Portal RH

Se a empresa utilizar o [Portal RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108433), acesse a tela **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha) para disponibilizar o holerite aos colaboradores.

[GIF animado: Imagem 9: Se a empresa utilizar o Portal RH , acesse a tela Gerenciador de Folhas (Pessoal+ > Rotinas Folha) para disponibilizar…](https://ajuda.sankhya.com.br/hc/article_attachments/39597340253591)

1. Selecione os filtros pertinentes e clique no botão **Liberação para PortalRH**.
2. No pop-up apresentado, escolha o **Tipo de Folha** calculada e a **Referência**.
3. Clique no card da **empresa**, para selecioná-la.
4. Clique em **Funcionários** e marque a liberação clicando no card do colaborador ou usando a opção **Marcar todos**.
5. Clique em **Liberar dados para PortalRH**.
6. Antes de conferir a(s) folha(s), poderá bloquear a visualização do(s) holerite(s) no Portal RH, basta seguir os passos acima e clicar em **Bloquear Liberação**.

   💡 O bloqueio é útil quando a folha foi liberada antes da conferência final.

#### **(8)** Realizar integrações

Após a confirmação da folha, podem ser feitas as integrações abaixo:

- [**Integrar com Financeiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610374)
- [**Integrar com Contabilidade**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7080867168151)

#### **(9)** Liberação para eSocial

[GIF animado: Imagem 10: (9) Liberação para eSocial](https://ajuda.sankhya.com.br/hc/article_attachments/39598065832215)

1. Antes do envio dos eventos, deve liberar os dados da folha calculada para o eSocial.
2. No **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha), clique no botão **Liberação para o eSocial.**
3. Selecione:

   - empresa;
   - referência;
   - funcionários.
4. Clique em **Liberar dados para eSocial**.

   Os cards das folhas liberadas para o eSocial receberão o ícone correspondente.

   ![Imagem 11: Os cards das folhas liberadas para o eSocial receberão o ícone correspondente.](https://ajuda.sankhya.com.br/hc/article_attachments/42148497730455)
5. Caso necessário, utilize **Bloquear liberação** para impedir o envio até a correção dos dados.

   O sistema pode alertar sobre:

   - Eventos não enviados no S-1010;
   - Inconsistências de cadastro.

#### **(10)** Geração e envio dos eventos ao eSocial

Depois da liberação da folha, faça a geração e o envio dos eventos pela **Central do eSocial** (Pessoal+ > Rotinas Folha):

- **S-1200 – Remuneração do trabalhador**

  - Envia os valores da folha (salário, horas extras, adicionais).
- **S-1210 – Pagamentos de rendimentos do trabalho**

  - nforma quando e como o funcionário foi pago;
  - Base para imposto de renda.
- **S-2299 – Desligamento**

  - Enviado quando há rescisão;
  - Contém verbas rescisórias.
- **S-2399 – Término de TSVE**

  - Para trabalhadores sem vínculo (ex: autônomos).
- **S-1299 – Fechamento dos eventos periódicos**

  - "Fecha a folha" no eSocial;
  - Depois dele, não é possível enviar novos eventos da competência (sem reabrir).
- **S-1298 – Reabertura dos eventos periódicos**

  - Usado quando precisa corrigir a folha após o fechamento.
- **S-3000 – Exclusão de eventos**

  - Remove eventos enviados incorretamente.

#### **(11)** Fechamento da folha

Após o envio dos eventos ao eSocial, é necessário realizar o fechameto da folha calculada para consolidar os dados e liberar as guias de impostos. Esse fechamento deve ser feito até o dia 15 do mês seguinte.

[GIF animado: Imagem 12: Após o envio dos eventos ao eSocial, é necessário realizar o fechameto da folha calculada para consolidar os dados e…](https://ajuda.sankhya.com.br/hc/article_attachments/39598096603927)

1. Acesse o **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha).
2. Clique no botão **Fechamento**.
3. No pop-up apresentado, selecione a **empresa** e clique em **Confirma Fechamento**.

### 4. Pontos de Atenção

- Sempre conferir a folha antes de confirmar.
- Divergências em eventos podem gerar erro no eSocial.
- Alterações após confirmação podem ser bloqueadas por parâmetro.
- Bases de cálculo devem estar alinhadas com as incidências.
- Eventos não enviados ao eSocial podem impedir o envio da folha.

### 5. Dicas de Usabilidade

- Faça o cálculo individual para validar casos específicos.
- Utilize o LOG para entender como os valores foram calculados.
- Verifique os avisos antes de integrar ou enviar ao eSocial.
- Padronize a conferência antes da confirmação da folha.
- Revise eventos sempre que houver erro recorrente.

## Perguntas Frequentes (FAQ)

**1. Posso calcular a folha sem corrigir divergências?**

Sim, mas o ideal é corrigir antes para evitar erros no cálculo e no eSocial.

**2. Qual a diferença entre cálculo coletivo e individual?**

O coletivo calcula vários funcionários de uma vez. O individual é usado para conferência ou casos específicos.

**3. Preciso conferir a folha antes de confirmar?**

Sim, a conferência é essencial para garantir que os valores estão corretos.

**4. O que acontece se eu não enviar eventos ao eSocial?**

O sistema pode bloquear ou apresentar alertas no envio da folha.

**5. Posso recalcular a folha depois de confirmar?**

Depende do parâmetro da empresa. Em alguns casos, será necessário excluir e recalcular.

Um cenário comum: se você alterar eventos de um colaborador que já teve o **adiantamento do 13º salário** calculado, é necessário recalcular individualmente essa parcela (Cálculos > Individual > 13º Salário) antes de confirmar novamente a folha. Pular esse recálculo gera erro no cálculo.

**6. Por que uma empresa não aparece na lista do Cálculo Coletivo da Folha?**

Isso acontece quando a empresa não tem colaboradores cadastrados ou está com a situação marcada como inativa no cadastro. Se uma empresa foi encerrada e não deve mais aparecer na lista de cálculo coletivo, acesse o cadastro dela e marque a situação como inativa.
