---
id: "42468035034647"
titulo: "Como lançar faltas na folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42468035034647-Como-lan%C3%A7ar-faltas-na-folha"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Faltas e Atrasos"
atualizado_em: "2026-10-02T15:32:01Z"
rotulos: ["FPEVEFALTAD", "LANCAFALTMESANT", "Art. 473 da CLT", "Lançar Falta", "Perde descanso semanal remunerado", "Lançamento de Faltas na Folha de Pagamento"]
---

# Como lançar faltas na folha

**Módulo:**Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.rh.Faltas

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A rotina de lançamento de faltas permite registrar, na tela **Faltas**, **faltas injustificadas do colaborador para que o desconto seja considerado na folha de pagamento.**

Considera-se falta injustificada aquela não prevista em lei, diferentemente da falta justificada (Art. 473 da CLT ou outra legislação aplicável), que exige documentação comprobatória e não gera desconto.

Quando a falta também resultar em suspensão disciplinar, utilize a jornada [**Lançamento de Faltas com Suspensão Disciplinar na Folha de Pagamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468830204567).

### 2. Pré-requisitos

- Permissão de acesso à tela **Faltas** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- **Tipo de ocorrência** cadastrado na tela **Ocorrências** (Pessoal+ > Rotinas Folha), com a propriedade **Falta habilitada** — sem esse cadastro, o lançamento não é refletido no histórico de ocorrências do colaborador.
- **Evento de folha cadastrado** (Cadastro de Eventos) para o desconto da falta, e configurado no parâmetro **Cód. Evento para Faltas/Dias (Desconto Férias) – FPEVEFALTAD** — sem o evento cadastrado, o sistema não calcula o desconto.
- Cadastro do colaborador ativo e dentro do período de contrato (entre admissão e demissão) na data da falta.
- Campo **Dia de apuração do ponto,** na tela [Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311) (aba Geral), configurado para definir a referência utilizada no lançamento da falta.

### 3. Jornada de Uso

[GIF animado: Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/42469664364823)

| **⚠️** **Atenção**  O lançamento apenas registra a falta. O desconto será considerado quando a folha de pagamento da referência for processada. |
| --- |

1. Acesse a tela **Faltas** (Pessoal+ > Rotinas Folha);
2. Informe a **Empresa** e o **Tipo de Filtro** e clique em **Aplicar** para localizar o colaborador. Se preferir, utilize o campo de pesquisa (ícone de lupa);
3. Clique sobre o card do colaborador para abrir o pop-up de lançamento;
4. Na Relação de Faltas, clique em + **Lançar Falta**;
5. Em **Tipo de Registro**, marque **Falta**;
6. Selecione o **Evento** que será utilizado para o desconto em folha;
7. Informe a **Referência**, correspondente ao mês em que a falta será considerada;
8. Preencha **Data de Início** e **Data de fim do período** com as datas da falta, dentro do mesmo mês de referência;

   | **⚠️** **Atenção**  Ao informar um período de faltas, registre apenas os dias efetivamente não trabalhados. Caso o período contenha dias de descanso semanal remunerado (DSR), realize lançamentos separados, considerando apenas os dias de trabalho. Por exemplo, para um colaborador que trabalha de segunda a sexta-feira e tem DSR aos sábados e domingos, registre a falta de segunda a sexta, sem incluir o fim de semana. |
   | --- |
9. Caso a falta também gere perda do descanso semanal remunerado (DSR), marque **Perde descanso semanal remunerado**;
10. Clique em **Lançar Falta**.

    O lançamento passa a ser exibido na **Relação de Faltas**.

    Para excluir uma falta lançada, posicione o cursor sobre o registro na **Relação de Faltas**, clique em **Excluir Falta** e confirme a operação.

    ![Imagem 2: Para excluir uma falta lançada, posicione o cursor sobre o registro na Relação de Faltas , clique em Excluir Falta e…](https://ajuda.sankhya.com.br/hc/article_attachments/42470286642583)

### 4. Pontos de Atenção

- Datas de início e fim precisam estar no mesmo mês de referência; períodos que cruzam meses são rejeitados.
- Não é possível lançar duas vezes uma falta na mesma data para o mesmo colaborador e tipo de registro.
- Com o parâmetro **Permite lançar faltas com folha/ponto fechados - LANCAFALTMESANT** desativado, o sistema bloqueia o lançamento se já existir folha mensal calculada na referência — a mesma regra vale para excluir uma falta já lançada.
- As faltas injustificadas podem reduzir a quantidade de dias de férias do colaborador, conforme o Art. 130 da CLT. Para mais informações, consulte o artigo [**Perda de Dias de Férias por Faltas Injustificadas (Evento 228 - Art. 130)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42490629375511).
- Se o colaborador for desligado após ter faltas lançadas, confira se a **Regra** **de** **Cálculo** (Pessoal+ > Cadastros), aba TRCT, subaba Eventos, tem os eventos de "faltas" e "DSR sobre faltas" configurados no campo 50 — sem isso, o TRCT (rescisão) não deduz as faltas corretamente no saldo de dias. Ver [**TRCT: Como Ajustar o Campo 50 para Considerar Faltas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/35913759653783-TRCT-Como-Ajustar-o-Campo-50-para-Considerar-Faltas).

### 5. Dicas de Usabilidade

- Use o campo de busca (lupa) no alto da tela para localizar rapidamente o colaborador.
- Confira o parâmetro **FPEVEFALTAD** antes de lançamentos em massa.
- Antes de processar a folha, revise os lançamentos registrados para evitar descontos indevidos.

## Perguntas Frequentes (FAQ)

**1. Faltas justificadas devem ser lançadas nesta tela?**

Não. Faltas justificadas (Art. 473 CLT) não geram desconto e não passam por esta tela.

**2. Posso lançar uma falta com folha ou ponto já fechados?**

Sim, desde que o parâmetro **Permite lançar faltas com folha/ponto fechados (LANCAFALTMESANT)** esteja ativado.

**3. Qual o evento padrão usado no desconto?**

O evento 102, configurável em FPEVEFALTAD.

**4. Posso lançar uma falta de vários dias de uma vez?**

Sim, desde que início e fim estejam no mesmo mês de referência.

**5. Como excluir uma falta lançada incorretamente?**

Posicione o cursor sobre a linha na Relação de Faltas e clique em Excluir Falta.

**6. E se a falta gerar suspensão disciplinar?**

Utilize a jornada [**Lançamento de Faltas com Suspensão Disciplinar na Folha de Pagamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468830204567), que orienta o lançamento conjunto da falta e da suspensão disciplinar.

**7. Posso lançar um único período que inclua dias de DSR?**

Não. Na rotina **Faltas**, devem ser informados apenas os dias em que houve falta ao trabalho. Se o período incluir dias de descanso semanal remunerado (DSR), esses dias também serão considerados como faltas pelo sistema. Nesses casos, realize lançamentos separados, contemplando apenas os dias efetivamente não trabalhados.

## Artigos Relacionados

- [Cadastro de Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494-Cadastro-de-Ocorr%C3%AAncias#CadastrodeOcorr%C3%AAncias)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Lançamento de Faltas com Suspensão Disciplinar na Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468830204567)
- [Restituição de Faltas na Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42487033706519)
- [Perda de Dias de Férias por Faltas Injustificadas (Evento 228 - Art. 130)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42490629375511)
