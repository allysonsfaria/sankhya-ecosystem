---
id: "37728648375447"
titulo: "Como realizar adiantamento e empréstimos a fornecedores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37728648375447-Como-realizar-adiantamento-e-empr%C3%A9stimos-a-fornecedores"
trilha: "Universidade Sankhya > Jornada de Pagamentos"
atualizado_em: "2026-07-22T14:09:02Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "TOP", "Adiantamento", "Financeiro"]
---

# Como realizar adiantamento e empréstimos a fornecedores

| Categoria |
| --- |
| [O que é o controle de adiantamentos e qual sua importância?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37728648375447-Como-realizar-adiantamento-e-empr%C3%A9stimos-a-fornecedores#h_01KF3TJR3A6NN2THDCM07FRS7A) |
| [Quais problemas este procedimento resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37728648375447-Como-realizar-adiantamento-e-empr%C3%A9stimos-a-fornecedores#h_01KF3TJJX95MK3C3EWG20XD8XY) |
| [Vídeo](https://ajuda.sankhya.com.br/hc/pt-br/articles/37728648375447-Como-realizar-adiantamento-e-empr%C3%A9stimos-a-fornecedores#h_01KF3TJEBVHPWHVQMJRD9J6PVD) [Como realizar adiantamento e empréstimos](https://drive.google.com/file/d/1aajsKoKAGYerPm6Qi9HdubOdv8q1tue4/view?t=3) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37728648375447-Como-realizar-adiantamento-e-empr%C3%A9stimos-a-fornecedores#h_01KF3TJ6V1SCTCKNH1BTPPYBJK) |
| [Chegou a sua vez! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37728648375447-Como-realizar-adiantamento-e-empr%C3%A9stimos-a-fornecedores#h_01KF3TJ043X7HFT73PC3KEZSX9) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37728648375447-Como-realizar-adiantamento-e-empr%C3%A9stimos-a-fornecedores#h_01KF3TGP2EC459ANHETYQ4B4SW) |

## Controle de Adiantamentos/Empréstimos a fornecedores

#### O que é o controle de adiantamentos e qual sua importância?

É o processo de registrar valores pagos antecipadamente a fornecedores, em situações em que o pagamento ocorre antes da emissão da nota fiscal, como em contratos com sinal, reserva de materiais, prestação de serviços ou condições comerciais específicas. Esse controle assegura que os adiantamentos sejam monitorados corretamente até sua compensação, evitando pagamentos duplicados, saldos esquecidos e distorções nos relatórios financeiros. Além disso, proporciona visibilidade sobre valores já comprometidos, mas ainda não faturados, fortalecendo o planejamento de caixa e a organização financeira da empresa.

#### Quais problemas este procedimento resolve?

- **Evita pagamentos duplicados ou fora do controle:** Registra e acompanha o que já foi antecipado.
- **Dá visibilidade sobre saldos a compensar:** Mostra exatamente quanto ainda falta abater nas notas fiscais.
- **Melhora o planejamento financeiro:** Permite prever corretamente os valores já comprometidos.
- **Reduz riscos de erros e inconsistências:** Facilita a reconciliação e evita lançamentos manuais incorretos.
- **Organiza a relação com fornecedores:** Garante que adiantamentos estejam formalizados e rastreáveis.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052442519)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis** precisa garantir a continuidade no fornecimento de materiais essenciais e, para isso, acordou um pagamento antecipado com um fornecedor. Como a nota fiscal ainda não foi emitida, é necessário registrar esse adiantamento no ERP Sankhya, controlando o valor como saldo a compensar.
O objetivo é garantir que as informações financeiras, como parceiro, valor e condição de pagamento, fiquem devidamente vinculadas, evitando erros futuros na compensação e assegurando visibilidade no fluxo de caixa.

**Tarefa:** Você realizar o registro do adiantamento no sistema e validar se os títulos foram registrados corretamente no financeiro.

#### Chegou a sua vez! Realize as movimentações no ERP Sankhya

**Atenção:**

- Certifique-se de que o usuário possui acesso à rotina de Adiantamento/Empréstimo.

1. **Acesse a tela Adiantamento / Empréstimos**
   Menu: Configurações » Rotinas » Adiantamento / Empréstimos
2. **Iniciar um novo registro.**

- Clique no botão **"Novo"** para iniciar o lançamento de um novo adiantamento.

3. **Passo a passo para o lançamento.**
   **Preencha os dados da janela “Adiantamento/Empréstimo”:**

- **Empresa**: Selecione a empresa **Axis**, que está realizando o pagamento.
- **Data de Negociação da Despesa:** Informe a data de negociação.
- **Data de Vencimento da Despesa**: Indique a data de vencimento prevista.
- **Parceiro**: Escolha o fornecedor ou parceiro ao qual o adiantamento será feito.
- Clique em **Próximo**.

**Preencha os dados da janela “Parcelamento”:**

- **Valor**: Insira o valor total do adiantamento.
- **Núm. Parcelas**: Caso o pagamento seja parcelado, indique o número de parcelas.
- **Frequência**: Defina a periodicidade das parcelas (mensal, semanal, etc.).
- **Tx. de juros (%)**: Informe a taxa de juros, se aplicável.
- **Tipo de parcelamento**: Escolha o tipo de parcelamento.
- **Tipo de Juros**: Escolha a opção que melhor se adequa a sua necessidade se houver o cálculo de juros.
- Clique em **Próximo**.

**Preencha os dados da janela “Preferências”:**

- **TOP's de Receita e Despesa**: Escolha os tipos de operação (TOP) correspondentes, “1602 - Adiantamento a Fornecedor - Despesa” e “1652 - Adiantamento a Fornecedor - Receita”.
- **Tipos de Títulos** **de Receita e Despesa:** Exemplo, “Boleto”.
- **Natureza da Despesa**: "Adiantamento a Fornecedores"
- **Natureza da Receita:** "Adiantamento a Fornecedores"
- **Centros de Resultado**: Indique o centro de resultado relacionado ao adiantamento, exemplo, “Compras”.
- **Conta Bancária**: Configure a conta bancária para movimentação.
  **Finalize o preenchimento:**
- Clique em **"Concluir"** para finalizar o lançamento.

4. **Conferir os títulos gerados.**

- O sistema exibirá os títulos na grade para conferência.
- Verifique se todas as informações estão corretas.

5. **Confirmar o adiantamento.**

- Após a conferência, clique no botão **"Confirmar"** para efetivar a inclusão do adiantamento na movimentação financeira, será gerado um número único para esse adiantamento no campo **“Adiant./Emp”** essa numeração pode ser usada para consulta do registro na **Movimentação Financeira.**

6. **Validação final.**

- **Acesse a tela Movimentação Financeira**
  Menu: Financeiro» Rotinas » Movimentação Financeira
- Clique em **+ Filtros** para criação de um filtro personalizado para a busca do adiantamento.
- Selecione **Filtros personalizados** e **Criar filtro.**
- Informe o **Nome do filtro.**
- Busque o campo **"Nro. Compensação/Acerto",** essa informação será utilizada para busca dos títulos, preencha o operador com **“Igual (=)”** e marque a flag **“Valor variável”** clique em **Salvar.**
- Informe o número do adiantamento criado anteriormente e clique em **"Aplicar"** para carregar os títulos vinculados a ele.
- Certifique-se de que o adiantamento foi registrado corretamente e está visível no módulo de movimentação financeira para acompanhamento futuro.

#### Correção e Repetição

- Confirme se todos os dados do adiantamento foram preenchidos corretamente, especialmente: empresa, parceiro, valor, vencimento e conta bancária.
- Verifique também se os títulos gerados estão visíveis na movimentação financeira e vinculados ao número de adiantamento criado.
- Se houver divergências, revise as informações e refaça o lançamento.
- Para reforçar o aprendizado, registre um novo adiantamento com outro fornecedor, variando os valores e condições de pagamento para testar o comportamento do sistema.
