---
id: "38016530918039"
titulo: "Fechamento da comissão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38016530918039-Fechamento-da-comiss%C3%A3o"
trilha: "Universidade Sankhya > Jornada de Vendas > Jornada de Comissionamento"
atualizado_em: "2026-07-22T14:02:22Z"
rotulos: ["Configuração", "Movimentação Financeira", "Comissão", "Preferências", "Financeiro"]
---

# Fechamento da comissão

## Como realizar o fechamento da comissão - Integração com o financeiro

#### Qual objetivo de calcular a comissão?

Apresentar o fechamento da comissão com integração ao financeiro como uma etapa essencial para garantir a conexão entre o cálculo das comissões e os registros financeiros da empresa. Esse processo assegura que os valores apurados sejam lançados corretamente no sistema financeiro, permitindo pagamentos precisos, controle efetivo e conformidade com as diretrizes internas da organização.

#### Quais problemas este recurso resolve?

- Erros de pagamento por falta de vínculo entre cálculo e financeiro;
- Falta de controle sobre os valores provisionados e pagos em comissão;
- Desalinhamento entre as áreas de Vendas e Financeiro;
- Atrasos na liberação de pagamentos à equipe comercial;
- Falhas na contabilização das comissões no sistema.

#### Quais os riscos de não calcular a comissão?

Sem a integração do fechamento de comissão com o financeiro, a empresa pode enfrentar pagamentos incorretos ou divergentes, o que compromete a confiança da equipe de vendas. Além disso, a ausência desse controle prejudica a organização financeira, gera retrabalho e aumenta a exposição a erros manuais. A falta de registros claros também representa um risco contábil e fiscal, afetando diretamente a segurança e a credibilidade dos processos da organização.

#### Demonstração prática

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1056845377)

#### Cenário de aplicação

**Contexto:** A Axis Ltda estruturou seus processos de comissionamento e passou a integrar o fechamento das comissões diretamente ao sistema financeiro. A mudança trouxe mais agilidade na execução dos pagamentos e eliminou divergências entre os valores calculados e os valores pagos. Agora, as áreas Comercial e Financeira atuam de forma mais alinhada, garantindo controle, transparência e cumprimento dos prazos.

**Tarefa:** Siga as orientações indicadas para executar o fechamento de comissão.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Fechamento de Comissão”**
   **Menu:** Financeiro »  Rotinas  »  Fechamento de Comissão

**Filtros rápidos**

- Clique no botão “**Habilitar Filtros**”;
- Para o fechamento individualizado, informe o **comissionado** no campo indicado;
- Informe a data do fechamento no campo **“Data Neg.”**;
- No campo **“Período (Baixa/Neg./Exec.)”**, informe o período de referência para o fechamento;
- No campo **“Gerar comissão para”**, selecione **“Financeiro”**;
- Clique no botão “**Aplicar**”;
- Na grade de resultados, selecione os registros que serão integrados ao financeiro. Para isso, utilize os botões **"Remover selecionados"** e **"Remover NÃO selecionados"** para facilitar a escolha dos itens desejados;
- Clique em **“Gerar Financeiro”**.

**Preferências - Informe:**

- **Conta bancária** - Conta corrente correspondente ao débito da despesa que será gerada;
- **Tipo de título -** Tipo de título utilizado no pagamento posterior;
- **Natureza -** Natureza da operação;
- **Projeto -** Código do projeto, caso haja;
- **Dt.Venc.|Ref. -** Para a opção gerar integração(financeiro), é a data do vencimento para pagamento da comissão;
- **Banco -** Código do banco em que será efetuado o pagamento do título;
- **Tipo de operação -** Tipo de Operação, que deve gerar despesa no financeiro. Ex.: **DESPESAS DE FOLHA**;
- **Centro de resultado -** Código do Centro de Resultados para que seja direcionada a despesa;
- **Empresa**.

**Observações:**

- O programa gera para apenas uma empresa;
- Se a opção “**Considerar Valor do Desconto**” estiver marcada e houver um desconto no momento da baixa financeira, esse valor será proporcionalmente descontado da comissão devida. O sistema lançará automaticamente o desconto na comissão;
- Ao marcar a opção “**Considerar Taxa de Cartões**”, o sistema desconta da comissão do vendedor o valor proporcional à taxa informada no campo “**Taxa Administrativa**” da baixa financeira da nota;
- O campo “**Tratar Desconto/Taxa na Devolução**” será habilitado somente quando as opções “**Considerar Valor do Desconto**” ou “**Considerar Taxa de Cartões**” estiverem marcadas. Quando isso ocorre, o sistema também aplica o desconto e/ou a taxa de cartão nas comissões geradas a partir de notas de devolução.

2. **Para validar a integração ao financeiro**

- Acesse a tela **“Movimentação Financeira”**
  **Menu:** Financeiro »  Rotinas  »  Movimentação Financeira
- Para localizar o registro gerado, na parte superior da tela, utilize a barra de filtros:

  - Pendentes + Baixados: **Pendentes**;
  - Receitas + Despesas: **Despesas**.
- Crie um filtro para pesquisar por vendedor:

  - Clique em **“+ Filtros”**;
  - Em **“Filtros personalizados”**, clique em **“Criar filtro”**;
  - Nomeie o filtro, como por exemplo **“Vendedor”**;
  - Busque o campo **“Vendedor”** e opte por **“Igual (=)”**, em **“Operador”**;
  - Marque a opção **“Valor variável”** e **salve** o filtro.
- Agora, com os 3 filtros selecionados, realize a busca e valide as informações.

#### Correção e repetição

- Revise os registros para confirmar se os valores e percentuais estão corretos;
- Garanta que os lançamentos foram realizados de forma adequada e estão devidamente alinhados com os objetivos do processo;
- Caso haja erro no registro ou na alocação dos valores, refaça a atividade seguindo o passo a passo novamente.
