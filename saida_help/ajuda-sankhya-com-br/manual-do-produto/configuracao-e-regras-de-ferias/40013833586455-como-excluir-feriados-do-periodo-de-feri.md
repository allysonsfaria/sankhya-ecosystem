---
id: "40013833586455"
titulo: "Como excluir feriados do período de férias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40013833586455-Como-excluir-feriados-do-per%C3%ADodo-de-f%C3%A9rias"
trilha: "Manual do Produto > Pessoas+ > Férias > Configuração e Regras de Férias"
atualizado_em: "2026-10-02T15:40:59Z"
rotulos: ["Configuração", "CLT", "Folha de Pagamento", "Férias", "Regras de Cálculo", "Pessoal+", "br.com.sankhya.rh.regras.calculo", "Feriados não computados em férias"]
---

# Como excluir feriados do período de férias

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros > Regras de Cálculo > Aba Propriedades > Sub-aba Férias
**ID da Tela:** br.com.sankhya.rh.regras.calculo

---

## Descrição e Usabilidade

De acordo com o Artigo 134 da CLT, as férias devem ser concedidas em **período contínuo**, sendo contabilizadas em **dias corridos**. Além disso, os Artigos 66 da CLT e 70 da CLT tratam do descanso e dos feriados, mas não estabelecem a exclusão desses dias durante o período de férias.

No entanto, as empresas podem, por política interna, acordo ou convenção Coletiva, optar por **não computar feriados no período de férias**, ampliando o descanso do colaborador.

No Pessoal+, essa configuração permite:

- aplicar regras mais vantajosas ao colaborador;
- adequar o cálculo conforme acordos coletivos ou políticas internas;
- garantir flexibilidade no tratamento dos feriados durante as férias.

⚠️Essa prática não é obrigatória por lei, mas é permitida quando traz benefício ao colaborador e não viola normas legais ou coletivas vigentes.

### 1. Descrição da Funcionalidade

Essa funcionalidade permite **definir quais feriados não devem ser considerados no período de gozo das férias**, evitando que esses dias sejam descontados do período do colaborador.

Ao utilizar essa opção, o sistema:

- Desconsidera os feriados configurados na contagem dos dias de gozo das férias;
- **Prorroga automaticamente a data fim das férias**, conforme a quantidade de feriados desconsiderados;
- **Ajusta a data de retorno ao trabalho** do colaborador;
- Mantém o pagamento do feriado na **folha mensal**, conforme a competência e regras de pagamento da empresa.

### 2. Pré-requisitos

Antes de realizar a configuração:

- A regra de cálculo deve estar cadastrada;
- Os feriados devem estar cadastrados na tela **Feriados** (Pessoal+ > Cadastros);
- Não pode haver folha de férias já calculada para o período.

### 3. Jornada de Uso

[GIF animado: Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/40014237664535)

1. Acesse a tela **Regras de Cálculo** (Pessoal+ > Cadastros);
2. Localize a regra desejada e clique sobre o card;
3. Vá até a aba **Propriedades** > **Férias**;
4. Clique no botão **Incluir feriados não computados nas férias**;
5. No pop-up exibido, informe:
   - **Data não computada**;
   - Marque se a regra será **válida para os anos subsequentes;**
   - Clique em **Incluir data.**
6. O feriado será exibido na seção **Feriados não computados nas férias.**
7. Clique em **Finalizar Edição** para salvar.

### 4. Pontos de Atenção

- Apenas feriados com **data configurada** serão desconsiderados no cálculo.
- Feriados sem configuração continuarão sendo considerados normalmente.
- Não é possível alterar feriados quando já existir cálculo de férias para o período.

  Nessa situação, o botão ficará desabilitado e será exibida a mensagem:
  **"Feriado com folha de férias calculada, não será possível excluir"**

### 5. Dicas de Usabilidade

- Configure os feriados antes de calcular as férias.
- Utilize a opção de validade para anos subsequentes para evitar retrabalho.
- Revise a regra de cálculo sempre que houver mudanças em acordos ou políticas internas.
- Após configurar, faça um cálculo teste para validar a data de retorno do colaborador.

## Perguntas Frequentes (FAQ)

**1. Como definir que um feriado não seja considerado nas férias?**

Acesse a tela **Regras de Cálculo > Propriedades > Férias** e utilize a opção **Feriados não computados nas férias**, informando a data desejada.

**2. O que acontece se eu não configurar a data de inativação do feriado?**

O feriado continuará sendo considerado normalmente no cálculo das férias.

**3. Posso alterar um feriado após calcular as férias?**

Não. O sistema bloqueia a alteração quando já existe cálculo de férias para o período.

**4. A configuração vale para anos futuros?**

Sim, desde que o checkbox **Válido para os anos subsequentes** esteja marcado.

## Artigos relacionados

- Regras de Cálculo
- Cálculo de Férias
- Cadastro de Feriados
