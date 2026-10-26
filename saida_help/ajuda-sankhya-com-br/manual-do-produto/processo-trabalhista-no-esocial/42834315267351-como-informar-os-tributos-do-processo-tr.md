---
id: "42834315267351"
titulo: "Como informar os tributos do processo trabalhista (S-2501)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42834315267351-Como-informar-os-tributos-do-processo-trabalhista-S-2501"
trilha: "Manual do Produto > Pessoas+ > Processos Trabalhistas > Processo Trabalhista no eSocial"
atualizado_em: "2026-10-02T17:46:26Z"
rotulos: ["Processo Trabalhista", "br.com.sankhya.ProcessoTrabalhista", "Evento S-2501", "Informações de Tributos Decorrentes"]
---

# Como informar os tributos do processo trabalhista (S-2501)

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Processo Trabalhista > Informações de Tributos Decorrentes
**Versão disponível:** A partir da 4.21
**ID da Tela:** br.com.sankhya.ProcessoTrabalhista

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O menu **Informações de Tributos Decorrentes** é apresentado após a confirmação do cadastro do Processo Trabalhista e permite registrar os períodos e as bases de cálculo de **Contribuição Previdenciária e Imposto de Renda** decorrentes do processo trabalhista e ainda não declarados ao eSocial.

As informações cadastradas nessa etapa são utilizadas para a geração do evento **S-2501 – Informações dos Tributos Decorrentes de Processo Trabalhista**.

O cadastro deve ser realizado somente quando houver informações tributárias decorrentes do processo.

### 2. Pré-requisitos

- Processo trabalhista previamente cadastrado e confirmado.
- Existência de valores de Contribuição Previdenciária ou Imposto de Renda a recolher decorrentes do processo.
- Informações dos períodos, bases de cálculo e códigos de receita definidos no processo.

### 3. Jornada de Uso

[GIF animado: Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/42888596055575)

1. Acesse o processo trabalhista previamente cadastrado e confirmado.
2. Clique no menu **Informações de Tributos Decorrentes**.
3. Clique em **Incluir nova informação de tributos**.
4. Preencha as seções abaixo, conforme o processo trabalhista.

   #### Referência de Pagamento

   Informe os dados referentes ao pagamento dos valores decorrentes do processo:

   - **Referência de pagamento:** informe a referência quando a empresa estiver autorizada, por decisão judicial ou acordo, a parcelar os valores da condenação e houver mais de uma referência de pagamento.
   - **Observação:** descreva informações relacionadas ao pagamento da parcela prevista no acordo ou sentença.
   - **Inclusão realizada via Portal do eSocial?**: marque essa opção quando o registro tiver sido enviado ao eSocial diretamente pelo Portal do eSocial.
   - **Nº de Recibo eSocial (S-2501)**: informe o número do recibo quando o evento S-2501 já tiver sido enviado pelo Portal do eSocial.

     | **⚠️** **Atenção**  Quando o S-2501 tiver sido enviado pelo Portal do eSocial, informe o número do recibo e gere o evento S-2501 na Central do eSocial para a referência de pagamento. Nesse caso, não é necessário realizar um novo envio do evento. |
     | --- |

   Clique em **Finalizar Adição** para salvar as informações.

   - **Informações do Imposto de Renda por Código de Receita**

     [GIF animado: Imagem 2: Informações do Imposto de Renda por Código de Receita](https://ajuda.sankhya.com.br/hc/article_attachments/42888782988823)

     Para informar valores de Imposto de Renda, clique em **Incluir Valor Receita IR**.

     Para facilitar o preencimento das seções, você pode expandir somente a seção que precisa informar dados.

     - **Imposto de Renda por Código de Receita**

       Selecione o **Código de Receita relativo a Imposto de Renda Retido na Fonte** e informe o **Valor relativo ao imposto para o CR**, considerando:

       - **Rendimento mensal**;
       - **13º salário**.
     - **Informações Complementares vinculadas ao Código de Receita**

       Quando aplicável, informe:

       - Rendimento tributável mensal do Imposto de Renda;
       - Rendimento tributável do IR de 13º - Tributação exclusiva;
       - Rendimento isento, portador moléstia grave c/ laudo;
       - Rendimento isento, portador moléstia grave c/ laudo - 13º salário;
       - Parcela isenta de aposentadora - Benef. com 65 anos ou mais;
       - Parcela isenta de aposentadoria - Benef. com 65 anos ou mais - 13º salário;
       - Juros de mora por atraso de pagamento de salário;
       - Juros de mora por atraso de pagamento de salário - 13º salário;
       - Previdência Oficial;
       - Previdência Oficial - 13º salário;
       - Outros rendimentos isentos ou não tributáveis;

         | **⚠️** **Atenção**  O campo **Outros rendimentos isentos ou não tributáveis** não é habilitado quando o **Código de Receita relativo a Imposto de Renda Retido na Fonte** for **188651 (IRRF - RRA)**. |
         | --- |
       - Descrição de rendimentos isentos ou não tributáveis.

         Deve ser preenchida obrigatoriamente quando o campo **Outros rendimentos isentos ou não tributáveis** estiver preenchido com um valor maior que zero.
     - **Rendimentos isentos exclusivos do Código de Receita IRRF-CCP/NINTER**

       Esta seção é habilitada para preenchimento quando o **Código de Receita relativo a Imposto de Renda Retido na Fonte** estiver com a opção **056152 (IRRF - CCP/NINTER)** selecionada.

       Informe, quando aplicável, os valores relativos a:

       - diárias;
       - ajuda de custo;
       - indenização e rescisão de contrato;
       - PDV;
       - acidentes de trabalho;
       - abono pecuniário;
       - auxílio-moradia.
     - **Informações complementares relativas a RRA**

       Esta seção é desabilitada quando o **Código de Receita relativo a Imposto de Renda Retido na Fonte** estiver com o código **593656 (IRRF - Decisão da Justiça do Trabalho)** selecionado.

       Quando habilitada, preencha:

       - **Descrição dos Rendimentos Recebidos Acumuladamente**;
       - **Quantidade de meses relativos ao RRA**;
       - **Valor das custas judiciais**.

       O campo **Valor total das despesas com advogados** é preenchido automaticamente com a soma dos valores informados no campo **Valor da despesa** da seção **Identificação dos Advogados**, caso exista uma ou mais discriminações de valores por advogado cadastrado.
     - **Identificação dos Advogados**

       Informe os dados do(s) advogado/escritório(s) contratado(s) pelo reclamante.

       Para habilitar essa seção, os dados da seção **Informações complementares relativas a RRA** devem estar preenchidos e válidos.
     - **Dedução do rendimento tributável relativa a dependentes**

       Informe os dados do(s) dependente(s) e o **Valor da Dedução**.

       O valor informado deve ser menor ou igual ao valor da dedução por dependente definido na legislação do Imposto de Renda vigente.
     - **Informação dos beneficiários da pensão alimentícia**

       Informe os dados do(s) dependente(s) e o **Valor da Pensão** com o valor líquido da pensão já calculado.
     - Após preencher as informações, salve o registro.

       Para alterar ou excluir um valor cadastrado, utilize os botões **Editar Valor Receita IR** ou **Excluir Valor Receita IR**.
   - **Processos Administrativos/Judiciais**

     | **⚠️** **Atenção**  Não será habilitada para preenchimento quando o **Código de Receita relativo a Imposto de Renda Retido na Fonte** estiver com a opção **593656 (IRRF - RRA Decisão da Justiça do Trabalho)** selecionada. |
     | --- |

     A seção permite informar processos contra a administração pública que tenham influência no cálculo das contribuições devidas ao:

     1. Regime Geral da Previdência Social (RGPS);
     2. Fundo de Garantia de Tempo de Serviço (FGTS);
     3. Imposto de Renda (IRRF) e/ou demais tributos.

     [GIF animado: Imagem 3: Imposto de Renda (IRRF) e/ou demais tributos.](https://ajuda.sankhya.com.br/hc/article_attachments/42888956006679)

     Para cadastrar um processo:

     - Clique em **Incluir Processos IRRF 593656**.
     - Selecione o processo relacionado a não retenção de tributos ou aos depósitos judiciais.
     - Informe os respectivos valores.
     - Salve as informações.

   #### Identificação do Período e Base de Cálculo dos Tributos

   [GIF animado: Imagem 4: Identificação do Período e Base de Cálculo dos Tributos](https://ajuda.sankhya.com.br/hc/article_attachments/42889120041751)

   Para cadastrar os períodos e as bases de cálculo:

   - Clique em Incluir **Período/Base Cálculo**.
   - Preencha as informações do período e das bases de cálculo.
     - **Referência da informação:** será obrigatória quando o valor da **Base de Cálculo Contribuição Previdenciária - Remuneração** e/ou **Base de Cálculo Contribuição Previdenciária -13º Salário** for maior que zero.
   - Preencha as **Informações das Contribuições Sociais por Código de Receita**;

     As informações referentes às contribuições sociais e de IRRF correspondentes a cada base de cálculo devem ser realizadas de acordo com o determinado no processo.

     - Clique em Incluir **Código e Valor**.
     - Escolha o **Código de Receita** correspondente.
     - Informe o valor apurado para cada base de cálculo, utilizando a alíquota disponibilizada na **Tabela 29 do eSocial**.
     - Salve a informação.

       Para alterar ou excluir um registro, utilize os botões **Editar CP por Código Receita** ou **Excluir CP por Código Receita**.
     - Após preencher as informações do período, clique em **Incluir**.

       Os períodos cadastrados podem ser alterados ou excluídos pelos botões **Editar período/base de cálculo de tributos** ou **Excluir período/base de cálculo de tributos**.
5. Clique em **Finalizar edição**.

   Repita o procedimento para cada período necessário.
6. Após finalizar o cadastro das informações, libere os tributos para envio ao eSocial:

   [GIF animado: Imagem 5: Após finalizar o cadastro das informações, libere os tributos para envio ao eSocial:](https://ajuda.sankhya.com.br/hc/article_attachments/42889268635543)

   - Clique em **Ativa seleção de Processos Trabalhista**.
   - Selecione o(s) registro(s) desejado(s).
   - Clique em **Liberar tributos selecionados**.
   - Confirme a liberação.

   A liberação permite o tratamento das informações para envio do evento **S-2501** ao eSocial.

   Para excluir um cadastro neste menu, selecione o registro e clique em **Remover tributos selecionados**.

### 4. Pontos de Atenção

- Cadastre as **Informações de Tributos Decorrentes** somente quando houver valores de Contribuição Previdenciária ou Imposto de Renda a recolher decorrentes do processo.
- É possível cadastrar mais de um período de base de cálculo.
- A **Referência da informação** é obrigatória quando houver valor nas bases de Contribuição Previdenciária - Remuneração ou 13º salário.
- Quando houver parcelamento dos valores da condenação, cadastre cada referência de pagamento correspondente.
- O preenchimento de determinadas seções depende do **Código de Receita** selecionado.
- As informações de RRA, dependentes, pensão alimentícia e despesas com advogados devem ser preenchidas quando aplicáveis ao processo.
- O **S-2501 deve ser gerado após o S-2500**.
- Após o envio do S-2501, alterações ou exclusões das informações poderão exigir novo tratamento do evento no eSocial.

### 5. Dicas de Usabilidade

- Separe as informações por período antes de iniciar o cadastro.
- Tenha em mãos os códigos de receita e os valores apurados antes de iniciar o preenchimento.
- Confira os valores das bases de cálculo antes de liberar os tributos.
- Quando houver parcelamento, organize as referências de pagamento antes de realizar o cadastro.
- Revise as informações de RRA, despesas com advogados, dependentes e pensão alimentícia antes de finalizar.

## Perguntas Frequentes (FAQ)

**1. Preciso preencher os tributos em todos os processos trabalhistas?**

Não. Essa etapa só deve ser preenchida quando houver valores de Contribuição Previdenciária ou Imposto de Renda a recolher decorrentes do processo.

**2. Posso cadastrar mais de um período de base de cálculo?**

Sim. É possível incluir vários períodos de base de cálculo, que ficam disponíveis para edição ou exclusão.

**3. Quando o S-2501 é gerado?**

O evento S-2501 é tratado a partir das informações de tributos cadastradas e liberadas no processo trabalhista. A geração ocorre após o S-2500.

**4. Posso informar um processo parcelado?**

Sim. Quando houver parcelamento dos valores da condenação, cadastre cada referência de pagamento correspondente às parcelas previstas no acordo ou decisão.

**5. O que faço se o S-2501 foi enviado pelo Portal do eSocial?**

Marque **Inclusão realizada via Portal do eSocial?**, informe o **Nº de Recibo eSocial (S-2501)** e siga o procedimento de geração indicado na Central do eSocial.

## Artigos Relacionados

- [Cadastro de Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42632245838871)
- [Inclusão de Dependentes do Trabalhador no Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42862840302615)
- [Informações do Contrato de Trabalho no Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42634479723671)
- [Consulta e Exclusão de Processos Trabalhistas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42844767586071)
