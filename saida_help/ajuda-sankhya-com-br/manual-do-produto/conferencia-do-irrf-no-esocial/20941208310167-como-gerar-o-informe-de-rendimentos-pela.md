---
id: "20941208310167"
titulo: "Como gerar o Informe de Rendimentos pela folha ou pelo eSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial"
trilha: "Manual do Produto > Pessoas+ > Encargos e Obrigações Legais > Nova DIRF e Informe de Rendimentos > Conferência do IRRF no eSocial"
atualizado_em: "2026-10-01T18:04:15Z"
rotulos: ["Impostos", "Declaração", "DIRF", "eSocial", "Folha de Pagamento", "br.com.sankhya.rh.GeracaoGuias", "Geração  de Guias", "Pessoal+", "Informe de Rendimentos", "Instrução Normativa RFB n.º 2.060/2021"]
---

# Como gerar o Informe de Rendimentos pela folha ou pelo eSocial

**Módulo:** Pessoal+
**Versão Mínima:**5.76.0 
**SAN eSocial:** 3.41 
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Geração de Guias
**ID da Tela:** br.com.sankhya.rh.GeracaoGuias

---

### Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#h_01KEJHKYYGM5YWS98TP86S0AF8)
[1. Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#h_01KEHHEN852B34DK3P1A507270)
[2. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#h_01KEHHGHRW2B5R424TB1D8269E)
   [Gerar o Informe](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#h_01KR3VH745TNHTQQRQQH0S19ZK)
   [Qual forma usar](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#qual-forma-usar)
 [3. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#h_01KEHNMN6QYYQCG0TZ0MPH1EF2)
 [4. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#h_01KEHNMN6WDR35643HV50GGNQK)
[Perguntas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#h_01KEHNMN6Z0WGXED0EBMY26XGP)
[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167-Como-gerar-o-Informe-de-Rendimentos-pela-folha-ou-pelo-eSocial#h_01M3W2ZSVAPCBW53V7HDRV9NJ5)

---

### Descrição e Usabilidade

A partir do **ano-base 2025**, o Informe de Rendimentos pode ser gerado com os valores da **Folha de pagamento (cálculo)** ou com os totalizadores do **eSocial (S-5002)**. A escolha é feita no campo **Forma de Geração**, na tela **Geração de Guias**.

**O Informe de Rendimentos** (Comprovante de Rendimentos Pagos e de Imposto sobre a Renda Retido na Fonte) é um documento anual obrigatório que reúne todas as informações sobre os rendimentos pagos a trabalhadores ao longo de um ano-calendário, assim como os valores de tributos retidos na fonte. Ele é utilizado para fins de **declaração do Imposto de Renda da Pessoa Física (IRPF)** e deve atender ao modelo e aos requisitos definidos pelo governo federal.

Este comprovante deve ser entregue ao trabalhador até o **último dia útil do mês de fevereiro** do ano seguinte ao pagamento dos rendimentos, ou no momento da **rescisão de contrato de trabalho**, caso esta ocorra antes dessa data.

As duas formas usam o mesmo modelo de PDF. O que muda é a origem dos valores:

- **Folha de pagamento (cálculo)**

  O Informe é gerado a partir dos valores efetivamente pagos pela empresa, com base na **data de pagamento** registrada na folha. Todos os rendimentos tributáveis, deduções e tributos retidos são consolidados diretamente dos resultados de cálculo da folha de pagamento.
- **eSocial (S-5002)**

  O Informe é gerado a partir dos **retornos do eSocial**, considerando o envio do evento **S-1210** (informações de pagamento) e o retorno do evento **S-5002** (informações de rendimentos e tributos).

### 1. Antes de começar

Confira estes pontos antes de gerar. Eles evitam informes vazios ou com valores incorretos.

- **Permissões necessárias**
  - Acesso liberado para a tela **Geração de Guias** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
  - Acesso às empresas que vai selecionar.
- **Configurações prévias**

  Antes de gerar o Informe de Rendimentos, verifique as seguintes configurações:

  **1. Empresa Matriz:**

  No cadastro da [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913) (Configurações > Cadastros), aba [**Geral**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abageral), a **Empresa Matriz** deve ser indicada, pois ela tem a função de gerar também os dados das filiais.

  **2. Dados do declarante**

  As informações do responsável pelas informações devem estar preenchidas na aba [**Informações para DIRF**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas#abainforma%C3%A7%C3%B5esparadirf) da tela **Empresas** (Pessoal+ > Cadastros).
- **Para qualquer forma de geração**

  - O ano-base é 2025 ou posterior.
  - O funcionário tem CPF cadastrado.
  - Para enviar o informe por e-mail, o funcionário tem e-mail cadastrado.
- **Para gerar pela Folha de pagamento**
  - As folhas do ano-base estão calculadas e têm data de pagamento dentro do ano. O sistema usa o regime de caixa: vale a data de pagamento, não a competência.
  - Os eventos (rubricas) estão marcados para uso no eSocial e têm a incidência de IRRF correta. Eventos sem incidência de IRRF não entram no informe.
  - A categoria eSocial do funcionário está correta. Ela define a natureza do rendimento e o código de receita.
- **Para gerar pelo eSocial (S-5002)**
  - Os eventos S-1210 do ano-base foram transmitidos.
  - Os retornos S-5002 foram recebidos e importados no sistema. Sem S-5002, o funcionário não aparece na lista.
  - Se houve pagamento de processo trabalhista no ano, o S-2501 do processo foi enviado e teve retorno do eSocial.

### 2. Jornada de Uso

| **⚠️** **Atenção**  O Informe de Rendimentos referente ao **ano-calendário 2025** é gerado conforme o novo procedimento de envio das informações da DIRF pelo eSocial e mantendo o que determina o **leiaute definido na** [**Instrução Normativa RFB n.º 2.060/2021**](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/122177). Para os **anos-calendários anteriores**, o sistema utiliza o leiaute DIRF disponibilizado para o envio das informações até o ano base 2024.  📚 Acesse [Informe de Rendimentos: como gerar para anos anteriores a 2025 (DIRF)](https://ajuda.sankhya.com.br/hc/pt-br/articles/37610344151703). |
| --- |

#### Gerar o Informe

Com as configurações realizadas, acesse a tela **Geração de Guias** e, primeiramente, clique sobre o card **DIRF** e, depois, em **Demonstrativo e Rendimentos** e siga as etapas abaixo:

[GIF animado: Imagem 1: Com as configurações realizadas, acesse a tela Geração de Guias e, primeiramente, clique sobre o card DIRF e, depois,…](https://ajuda.sankhya.com.br/hc/article_attachments/41345947990295)

**Etapa 1 – Informações Gerais**

1. Preencha o campo **Ano base (Ano calendário)** com o ano em que os rendimentos foram pagos.

   Aparecem apenas trabalhadores com pagamento nesse ano, pela **data de pagamento** da folha.

   Desligados aparecem normalmente se receberam algum valor no período.
2. Selecione a **Forma de Geração** do relatório:
   - **Folha de pagamento (cálculo):** utiliza os valores calculados na folha, considerando a data de pagamento no ano-base, como: salários, férias, 13º, pensões, previdência, plano de saúde e IRRF;
   - **eSocial (S-5002):** utiliza exclusivamente os retornos do eSocial, considerando apenas trabalhadores com pagamento enviado no evento S-1210 e retorno disponível do S-5002 dentro do ano-base informado.
3. Marque **Liberar informes para os funcionários** se quiser disponibilizar os informes no **Portal RH** e enviá-los por e-mail.
4. Clique na etapa **2 Empresas** ou no botão **Próximo** para avançar para a próxima etapa.

| 💡 **Dica**  **Houve alteração nas informações do ano-base? Use o botão Consolidar Informe**  Depois de informar o ano-base, o botão **Consolidar Informe** aparece no canto inferior direito. Ele reprocessa os dados do ano sem gerar o PDF. Use-o antes da emissão final quando houver alterações nas informações que compõem o Informe. |
| --- |

**Etapa 2 – Empresas**

1. Clique nos cards das **Empresas** responsáveis pelo Informe.

   A lista mostra só as matrizes; as filiais entram automaticamente.
2. Avance para a próxima etapa.

![Imagem 2: Avance para a próxima etapa.](https://ajuda.sankhya.com.br/hc/article_attachments/37564073129751)

**Etapa 3 – Funcionários**

1. Selecione os colaboradores que irão compor o Informe:

   - individualmente, clicando nos respectivos cards ou
   - utilizando a opção **Marcar todos**.
2. Para facilitar essa seleção, utilize os **Filtros** padrões ou personalizados (por meio da opção **Gerenciar filtros**).
3. Avance para a etapa final.

[GIF animado: Imagem 3: Avance para a etapa final.](https://ajuda.sankhya.com.br/hc/article_attachments/37564096952343)

**Etapa 4 – Gerar**

1. Clique no botão **Gerar.**

   Os Informes estarão disponíveis para:

   - salvar no computador;
   - imprimir;
   - enviar por e-mail.

![Imagem 4: enviar por e-mail.](https://ajuda.sankhya.com.br/hc/article_attachments/37564096955287)

- Para envio por e-mail, clique em **Enviar comprovantes por e-mail** e confirme.

  | **⚠️** **Atenção**  O ícone de e-mail (envelope) só aparece se a marcação **Liberar informes para os funcionários** tiver sido habilitada na etapa 1 da geração. |
  | --- |

![Imagem 5: O ícone de e-mail (envelope) só aparece se a marcação Liberar informes para os funcionários tiver sido habilitada na…](https://ajuda.sankhya.com.br/hc/article_attachments/37564073132567)

| ℹ️ **Nota** Gerando pelo eSocial (S-5002): o que muda Na opção **eSocial (S-5002)**, o Informe é gerado com base nas informações enviadas ao eSocial e nos respectivos retornos do S-5002.   1. o evento **S-1210** (informações de pagamento) enviado dentro do ano-base; e 2. o retorno do evento **S-5002** (imposto de renda retido na fonte) disponível para o mesmo período.   Os valores são a soma dos retornos do S-5002 por CPF do beneficiário, de janeiro a dezembro do ano-base.   | **⚠️** **Atenção**  O Informe é gerado com base nos retornos do eSocial. Por isso, se houver eventos ainda sem retorno ou alterações na folha que ainda não foram refletidas no eSocial, os valores podem ser diferentes dos apresentados na geração pela folha. | | --- |   **Processos trabalhistas no Informe**  A partir da versão **5.129**, na forma **eSocial (S-5002)**, o Informe também considera os valores pagos em processos trabalhistas enviados ao eSocial (evento **S-2501**). Esses valores são somados aos demais rendimentos do funcionário, sem substituir nem duplicar.  Os valores são apresentados nos campos correspondentes do Informe, conforme sua natureza:   - **Valores do próprio ano** (decisão da Justiça do Trabalho ou acordo em comissão de conciliação): somados aos rendimentos tributáveis, ao INSS, à pensão alimentícia, ao IRRF e ao 13º salário. Diárias, ajuda de custo, indenizações, abono pecuniário e auxílio-moradia vão para os rendimentos isentos. - **Valores de anos anteriores**: aparecem em **Rendimentos Recebidos Acumuladamente (RRA)**, com o número do processo, a natureza, a quantidade de meses, as despesas com a ação judicial e o IRRF. - **Informações Complementares**: mostram os meses de pagamento do RRA e a pensão alimentícia de cada beneficiário, separada por tipo (mensal, 13º salário e rendimento isento).  | **⚠️** **Atenção**  Para que os valores de processos trabalhistas sejam considerados no Informe, o evento S-2501 precisa ter retorno do eSocial. Se o S-2501 for retificado, somente a versão mais recente será considerada. Se o evento for excluído, os valores do processo deixarão de ser considerados no Informe. | | --- | |
| --- | --- | --- |

#### Qual forma usar

- Use **eSocial (S-5002)** quando quiser gerar o Informe com base nos retornos das informações enviadas ao eSocial.
- Use **Folha de pagamento** quando os eventos do eSocial ainda não estiverem completos.

Em qualquer caso, use a mesma forma para todos os trabalhadores do ano-base.

|  | Folha de pagamento (cálculo) | eSocial (S-5002) |
| --- | --- | --- |
| Origem dos valores | Eventos das folhas calculadas e pagas no ano-base | Valores de IRRF devolvidos pelo governo no S-5002 |
| Quem aparece na lista | Funcionários com folha paga no ano-base | Funcionários com S-5002 recebido no ano-base |
| Como os valores são classificados | Pela incidência de IRRF de cada evento | Pelo código de receita e tipo de informação do S-5002 |
| Código de receita | Calculado pelo sistema a partir da categoria, país e situação do funcionário | O mesmo informado no S-5002 |
| Depende do eSocial | Não | Sim: S-1210 transmitido e S-5002 importado |
| Melhor uso | Conferir cálculos ou gerar antes dos retornos | Versão final, igual ao que o governo recebeu |
| Processos trabalhistas | Não considerados | Considerados, a partir da versão 5.129 |

**Os valores podem diferir entre as duas formas.** As causas mais comuns são: um S-1210 não transmitido, folha recalculada depois do envio ao eSocial ou incidência de IRRF configurada de forma diferente da enviada na tabela de rubricas (S-1010). Gere pelas duas formas e compare para achar a diferença.

### 3. Pontos de Atenção

- O Informe considera **a data de pagamento**, não a competência.
- É gerado **um Informe por empregador**.
- Quando o trabalhador possui mais de um contrato com o mesmo empregador, os valores são **agrupados**.
- Rendimentos com **exigibilidade suspensa** são apresentados separadamente, conforme a legislação.

### 4. Dicas de Usabilidade

- Gere o Informe após o fechamento da folha ou após a consolidação dos eventos do eSocial.
- Utilize a mesma forma de geração para todos os trabalhadores do ano-base.
- Em caso de divergência, revise os valores de pagamento e o retorno do eSocial.

### Perguntas Frequentes

**1. Um trabalhador ativo não aparece na lista. Por quê?**

O sistema mostra só quem recebeu pagamento no ano-base, pela data de pagamento. Na opção eSocial, ele também precisa ter S-1210 enviado e S-5002 retornado.

**2. O Informe considera a competência ou a data de pagamento?**

A data de pagamento. Uma folha de dezembro paga em janeiro entra no Informe do ano seguinte.

**3. O trabalhador tem dois contratos na mesma empresa. Sai um Informe para cada?**

Não. É gerado um Informe por empregador, e os valores dos contratos são somados.

**4. Alterei a folha depois de gerar. O Informe atualiza sozinho?**

Não. Clique em **Consolidar Informe** e gere novamente.

**5. Os valores estão diferentes do esperado. O que conferir?**

Revise os valores de pagamento da folha e o retorno do eSocial. Confira também a incidência de IRRF das rubricas.

**6. Qual nome aparece no Informe?**

A partir da versão 5.100, se o trabalhador tiver **Nome Social** cadastrado, ele é usado. Senão, vale o nome civil.

**7. E os rendimentos com exigibilidade suspensa?**

Eles aparecem separados, como manda a legislação.

**8. Os valores de processo trabalhista entram no Informe?**

Sim, a partir da versão 5.129, na forma eSocial (S-5002). Na forma Folha de pagamento, eles não são considerados.

**9. O que acontece se o S-2501 do processo trabalhista for retificado?**

Quando o S-2501 for retificado, o Informe considera somente a **versão mais recente** do evento. Se o S-2501 for excluído, os valores correspondentes ao processo deixam de ser considerados no Informe.

**10. O processo trabalhista foi enviado, mas o S-2501 ainda não teve retorno. Os valores aparecem no Informe?**

Não. Os valores do processo trabalhista são considerados no Informe após o **S-2501 ter retorno do eSocial**.

### Artigos Relacionados

- [Nova DIRF/eSocial 2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/37361211258647)
- [Relatório S-5002 (IRRF por trabalhador)](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567)
- [Correção de dados do IRRF no eSocial (S-1210) para anos anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223)
