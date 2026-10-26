---
id: "42468830204567"
titulo: "Como lançar falta com suspensão disciplinar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42468830204567-Como-lan%C3%A7ar-falta-com-suspens%C3%A3o-disciplinar"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Faltas e Atrasos"
atualizado_em: "2026-10-20T12:12:59Z"
rotulos: ["Ocorrências", "Faltas", "ID: br.com.sankhya.rh.Faltas", "FPEVEFALTAD", "Suspensão Disciplinar", "Lançamento de Faltas com Suspensão Disciplinar na Folha de Pagamento"]
---

# Como lançar falta com suspensão disciplinar

**Módulo:**Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.rh.Faltas

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

Utilize esta rotina quando uma falta injustificada também resultar em suspensão disciplinar do colaborador. Ao concluir o lançamento, o sistema registra, em uma única operação, a suspensão disciplinar como ocorrência e o movimento de desconto da falta na folha de pagamento.

Para registrar apenas a falta injustificada, consulte o artigo [**Lançamento de Faltas na Folha de Pagamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468035034647).

| **⚠️** **Atenção**  Esta rotina não substitui os procedimentos administrativos da empresa para aplicação de medidas disciplinares. Ela apenas registra a suspensão disciplinar no sistema e o respectivo desconto da falta. |
| --- |

### 2. Pré-requisitos

- Permissão de acesso à tela **Faltas** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- **Tipo de ocorrência** (Histórico de suspensão disciplinar) cadastrado na tela **Ocorrências** (Pessoal+ > Rotinas Folha), com a propriedade **Falta habilitada** — sem esse cadastro, o lançamento não é refletido no histórico de ocorrências do colaborador.
- **Evento de folha cadastrado** (Cadastro de Eventos) para o desconto da falta, e configurado no parâmetro **Cód. Evento para Faltas/Dias (Desconto Férias) – FPEVEFALTAD** — sem o evento cadastrado, o sistema não calcula o desconto.
- Cadastro do colaborador ativo e dentro do período de contrato (entre admissão e demissão) na data da falta.
- Campo **Dia de apuração do ponto** configurado na tela [Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311) (aba Geral) — define a referência considerada para a falta.

### 3. Jornada de Uso

[GIF animado: Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/42470456053271)

1. Acesse a tela **Faltas** (Pessoal+ > Rotinas Folha);
2. Informe a **Empresa** e o **Tipo de Filtro** e clique em **Aplicar** para localizar o colaborador (ou use a busca pela lupa, no alto da tela);
3. Clique sobre o card do colaborador para abrir o pop-up de lançamento;
4. Na Relação de Faltas, clique em + **Lançar Falta**;
5. Em **Tipo de Registro**, selecione **Falta** e marque a opção **Suspensão Disciplinar**;
6. Preencha os campos obrigatórios da Suspensão Disciplinar: **Código**, **Histórico** e **Descrição**;
7. Selecione o **Evento** de desconto e informe a **Referência** da folha;
8. Preencha a **Data de início** e a **Data de fim** da suspensão;

   | **⚠️** **Atenção**  As datas informadas devem corresponder apenas aos dias efetivamente não trabalhados. Não inclua dias de descanso semanal remunerado (DSR) no período da falta, pois eles também serão considerados como faltas pelo sistema. |
   | --- |
9. Clique em **Lançar Falta**. O sistema registra simultaneamente a ocorrência de suspensão disciplinar e o movimento de desconto da falta.

### 4. Pontos de Atenção

- Código, Histórico e Descrição da Suspensão Disciplinar são obrigatórios quando a marcação é habilitada, sem eles o lançamento não é concluído.
- Também se aplicam a esta rotina as regras de referência da folha e de bloqueio quando existir folha calculada, conforme descrito no artigo [**Lançamento de Faltas na Folha de Pagamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468035034647).
- Verifique se não há sobreposição de datas com outras ocorrências do colaborador no mesmo período, consulte [**Cálculo de Dias de Afastamento a Maior na Folha de Pagamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37217719357719-C%C3%A1lculo-de-Dias-de-Afastamento-a-Maior-na-Folha-de-Pagamento) para o procedimento completo de verificação e correção.

### 5. Dicas de Usabilidade

- Utilize uma descrição objetiva para facilitar futuras consultas ao histórico do colaborador.
- Confirme o código de suspensão configurado na tela **Ocorrências** (Pessoal+ > Rotinas Folha) antes de lançamentos recorrentes desse tipo.

## Perguntas Frequentes (FAQ)

**1. Preciso lançar a suspensão em outra tela?**

Não. Suspensão e desconto são lançados juntos, na tela Faltas.

**2. O que acontece se eu não preencher o Código da Suspensão?**

O sistema não permite concluir o lançamento.

**3. Onde consulto a suspensão depois de lançada?**

No histórico de ocorrências do colaborador, na tela Ocorrências.

**4. Posso editar essa suspensão depois?**

Sim, pela rotina de Edição de Ocorrências, na tela Ocorrências — não pela tela Faltas.

**5.** **A suspensão disciplinar gera automaticamente o desconto da falta?**

Sim. Ao concluir o lançamento, o sistema registra tanto a ocorrência de suspensão disciplinar quanto o movimento de desconto correspondente na folha de pagamento.

## Artigos Relacionados

- [Lançamento de Faltas na Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468035034647)
- [Cadastro de Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Consulta de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40336545146519)
- [Edição de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40407377343127)
