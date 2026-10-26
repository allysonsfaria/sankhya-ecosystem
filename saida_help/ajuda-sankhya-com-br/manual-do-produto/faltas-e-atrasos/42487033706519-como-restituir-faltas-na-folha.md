---
id: "42487033706519"
titulo: "Como restituir faltas na folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42487033706519-Como-restituir-faltas-na-folha"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Faltas e Atrasos"
atualizado_em: "2026-10-02T15:32:14Z"
rotulos: ["ID: br.com.sankhya.rh.Faltas", "FPEVEFALTAC", "Restituição de falta", "Restituição de Faltas na Folha de Pagamento"]
---

# Como restituir faltas na folha

**Módulo:**Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.rh.Faltas

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

Utilize esta rotina para restituir, na folha de pagamento, o desconto de uma falta lançada indevidamente. O sistema gera um novo lançamento de restituição, vinculado às mesmas datas da falta original, em uma folha diferente.

### 2. Pré-requisitos

- Permissão de acesso à tela **Faltas** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Existência de uma falta já lançada para o colaborador na data a ser restituída.
- **Evento de restituição cadastrado** (Cadastro de Eventos) e configurado no parâmetro **Cód. Evento para Restit. Faltas (Restit. Férias) – FPEVEFALTAC** (padrão: evento 105).

### 3. Jornada de Uso

[GIF animado: Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/42489711208215)

| **⚠️** **Atenção**  A restituição apenas registra o crédito da falta. O valor será considerado quando a folha da referência informada for processada. |
| --- |

1. Acesse a tela **Faltas** (Pessoal+ > Rotinas Folha);
2. Informe a **Empresa** e o **Tipo de Filtro** e clique em **Aplicar**;
3. Localize o card do colaborador que teve a falta lançada indevidamente. Se preferir, utilize o campo de pesquisa (ícone de lupa);
4. Clique sobre o card do colaborador para abrir o pop-up de lançamento;
5. Na Relação de Faltas, clique em + **Lançar Falta**.
6. Em **Tipo de Registro**, selecione **Restituição de falta**.
7. Selecione o **Evento** de restituição e informe a **Referência**, correspondente à folha em que o crédito será realizado.
8. Em **Data de início** e **Data de fim do período**, informe as datas em que ocorreu o desconto original.
9. Clique em **Lançar Restituição de falta**.

### 4. Pontos de Atenção

- A restituição só pode ser lançada se já existir falta registrada na mesma data — sem isso, o lançamento é bloqueado.
- Não é possível restituir a mesma data duas vezes.
- Após a restituição, a Relação de Faltas exibe os dois lançamentos (falta e restituição) nas mesmas datas, em folhas distintas — comportamento esperado, não duplicidade.
- A referência da restituição pode ser diferente da referência da falta original, desde que corresponda à folha em que o crédito será processado.

### 5. Dicas de Usabilidade

- Confira a Relação de Faltas do colaborador antes de lançar a restituição, para confirmar a data exata do desconto original.
- Confira se o parâmetro **FPEVEFALTAC** está corretamente configurado antes de realizar restituições em lote.

## Perguntas Frequentes (FAQ)

**1. Posso restituir uma falta sem lançamento anterior?**

Não. É preciso já existir uma falta lançada na mesma data.

**2. Qual o evento padrão da restituição?**

O evento 105, configurável em FPEVEFALTAC.

**3. A restituição substitui o lançamento original?**

Não. Os dois lançamentos permanecem visíveis na Relação de Faltas, em folhas distintas.

**4. Em que referência a restituição é lançada?**

No mês informado no campo Referência do lançamento de restituição — pode ser diferente do mês da falta original.

**5. A restituição exclui a falta lançada anteriormente?**

Não. O lançamento original permanece registrado para manter o histórico da movimentação. A restituição gera um novo lançamento que compensa o desconto realizado.

## Artigos Relacionados

- [Lançamento de Faltas na Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468035034647)
- [Lançamento de Faltas com Suspensão Disciplinar na Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468830204567)
- [Perda de Dias de Férias por Faltas Injustificadas (Evento 228 - Art. 130)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42490629375511)
