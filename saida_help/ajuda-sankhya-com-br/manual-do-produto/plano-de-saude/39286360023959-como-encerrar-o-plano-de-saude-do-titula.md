---
id: "39286360023959"
titulo: "Como encerrar o plano de saúde do titular e dos dependentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959-Como-encerrar-o-plano-de-sa%C3%BAde-do-titular-e-dos-dependentes"
trilha: "Manual do Produto > Pessoas+ > Benefícios > Plano de Saúde"
atualizado_em: "2026-10-02T15:50:15Z"
rotulos: ["Dependentes", "DIRF", "ID: br.com.sankhya.cadastro.funcionarios", "Folha de Pagamento", "Configuração Funcionários", "Plano de Saúde", "Pessoal+", "Cadastro de Plano de Saúde", "Encerramento de Plano de Saúde - Titular e Dependente"]
---

# Como encerrar o plano de saúde do titular e dos dependentes

**Módulo:** Pessoal+
**Caminho de Acesso:**

- Configuração Funcionários > Aba Plano de Saúde
- Configuração Funcionários > Aba Dependentes > Sub-aba Plano de Saúde
- Lançamento de Movimentos

---

## Descrição e Usabilidade

O encerramento do Plano de Saúde é o processo responsável por **interromper o cálculo automático dos descontos** de convênio médico ou odontológico na folha de pagamento do funcionário e seus dependentes.

Esse procedimento é essencial para:

- Evitar descontos indevidos após cancelamento do benefício;
- Garantir consistência nos cálculos da folha;
- Manter o histórico do benefício sem necessidade de exclusão;
- Prevenir divergências financeiras com o colaborador.

O encerramento correto envolve não apenas informar a data final do plano, mas também validar impactos na folha e nos lançamentos automáticos.

### 1. Descrição da Funcionalidade

A funcionalidade permite:

- Encerrar o plano de saúde do titular e dependentes;
- Interromper descontos futuros na folha;
- Manter o histórico do benefício para consultas;
- Evitar lançamentos automáticos indevidos.

### 2. Pré-requisitos

Antes de encerrar o plano, verifique:

- Se **não existe folha calculada** na referência do encerramento;
- Se há **lançamentos fixos** vinculados ao plano de saúde;
- Se a data de encerramento está definida corretamente conforme o contrato do convênio;

### 3. Jornada de Uso

#### 3.1 Encerrar plano do titular

[GIF animado: Imagem 1: 3.1 Encerrar plano do titular](https://ajuda.sankhya.com.br/hc/article_attachments/39286602115351)

1. Acesse a tela **Configuração Funcionários** (Pessoal+ > Cadastros).
2. Vá até a aba **Plano de Saúde**.
3. Localize o plano ativo.
4. Preencha o campo **Referência Final** com a data de encerramento.
5. Salve o cadastro.

#### 3.2 Encerrar plano dos dependentes

![Imagem 2: 3.2 Encerrar plano dos dependentes](https://ajuda.sankhya.com.br/hc/article_attachments/39286690199447)

1. Acesse a a tela **Configuração Funcionários** e localize o **colaborador titular**.
2. Clique na aba **Dependentes** e entre na sub-aba **Plano de Saúde**.
3. Localize o plano do dependente.
4. Preencha o campo **Referência Final**.
5. Salve as alterações.

#### 3.3 Excluir lançamento fixo (obrigatório)

![Imagem 3: 3.3 Excluir lançamento fixo (obrigatório)](https://ajuda.sankhya.com.br/hc/article_attachments/39287378992663)

1. Acesse a tela **Lançamento de Movimentos** (Pessoal+ > Rotinas Folha).
2. Informe os filtros: **Empresa**, **Referência** e **Funcionário**.
3. Clique em **Pesquisar**.
4. Acesse a aba **Visualização** e localize o evento de desconto do plano de saúde.
5. Exclua o lançamento fixo a partir da referência desejada.

📌 Isso impede que o desconto continue sendo lançado automaticamente nas próximas folhas.

#### 3.4 Reprocessar a folha (se necessário)

Caso já exista cálculo na referência:

1. Exclua o cálculo da folha;
2. Realize o encerramento do plano;
3. Recalcule a folha novamente.

### 4. Pontos de Atenção

- **Não é possível alterar ou excluir o plano se existir folha calculada na referência.**

  - Nesse caso, será necessário:

    - excluir o cálculo da folha;
    - realizar o ajuste;
    - recalcular a folha.

    Na prática, esse bloqueio é disparado pela presença, na referência, de um evento de desconto do próprio plano de saúde já calculado, identificado pela combinação de natureza de rubrica 9219 e código de incidência de IRRF 67 ou 9067. Ou seja, não é qualquer folha calculada na referência que impede o encerramento, e sim especificamente a existência desse evento de desconto de plano de saúde já processado. Por isso, ao seguir os passos acima (excluir o cálculo, ajustar e recalcular), o ponto principal a conferir é se esse evento de desconto deixou de constar na folha calculada da referência.
- Informar apenas a **Referência Final não é suficiente.**

  Se houver lançamento fixo, o desconto continuará sendo aplicado.
- As funções **FCONVENIODPD**, **FCONVENIO** e **FPLANOSAUDE** validam automaticamente a **Referência Final** da dependência cadastrada no plano de saúde.

  Caso o período de dependência já tenha sido encerrado, o dependente não será considerado nos cálculos da folha para competências posteriores à data final informada.

  Não é necessário realizar exclusões ou ajustes adicionais nas fórmulas dos eventos para que esse comportamento seja aplicado.
- O não encerramento correto pode gerar:

  - Descontos indevidos em folha;
  - Retrabalho no cálculo;
  - Divergências com o colaborador;
  - Ajustes manuais desnecessários.

### 5. Dicas de Usabilidade

- Sempre encerre o plano **antes do cálculo da folha**;
- Valide com o RH ou financeiro a data correta de encerramento;
- Revise se existem lançamentos fixos ativos;
- Utilize a Referência Final em vez de excluir o cadastro (mantém histórico);
- Após ajustes, sempre confira os valores na folha recalculada.

## Perguntas Frequentes (FAQ)

**1. O plano foi encerrado, mas o desconto continua na folha. O que pode ser?**

Provavelmente existe um **lançamento fixo ativo**. É necessário excluí-lo na tela **Lançamento de Movimentos**.

**2. Não consigo alterar ou excluir o plano de saúde. Por quê?**

Isso ocorre quando já existe **folha calculada na referência**. Será necessário:

- Excluir o cálculo da folha;
- Realizar o ajuste;
- Recalcular.

**3. Basta preencher a Referência Final para parar o desconto?**

Não necessariamente. Se houver lançamento fixo, o desconto continuará ocorrendo.

**4. O dependente continua sendo considerado no cálculo após informar a Referência Final da dependência?**

Não.

Após o encerramento da dependência, as funções **FCONVENIODPD**, **FCONVENIO** e **FPLANOSAUDE** deixam de considerar automaticamente esse dependente nas competências posteriores à **Referência Final**.

**5. Posso excluir o plano de saúde em vez de encerrar?**

Não é recomendado. O ideal é preencher a **Referência Final**, mantendo o histórico.

**6. O que acontece se eu não encerrar corretamente o plano?**

Pode gerar:

- Descontos indevidos;
- Divergência com o colaborador;
- Necessidade de ajustes manuais;
- Retrabalho no fechamento da folha.

**7. Em que momento devo fazer o encerramento do plano?**

Antes do cálculo da folha da competência. Isso evita necessidade de recálculo.

## Artigos Relacionados

- [Cadastro de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)
- [Lançamento de Movimentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319)
- [Reprocessamento de Plano de Saúde para Funcionários e Dependentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079)
- [Valores de Plano de Saúde na DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/28555465280663)
