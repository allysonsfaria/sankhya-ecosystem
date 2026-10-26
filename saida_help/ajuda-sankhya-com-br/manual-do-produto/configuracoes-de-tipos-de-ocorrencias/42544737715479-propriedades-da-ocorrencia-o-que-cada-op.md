---
id: "42544737715479"
titulo: "Propriedades da ocorrência: o que cada opção faz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42544737715479-Propriedades-da-ocorr%C3%AAncia-o-que-cada-op%C3%A7%C3%A3o-faz"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Configurações de Tipos de Ocorrências"
atualizado_em: "2026-10-02T15:27:42Z"
rotulos: ["Indenização de Estabilidade", "Propriedades da Ocorrência", "Reduz Dias Trabalhados", "Quita Férias por Afastamentos – Art. 133 CLT", "Quita Férias em Licença Remunerada", "Abate no Aviso Prévio", "Configurações das Propriedades da Ocorrência para Folha de Pagamento", "Tem Direito de Adiantamento", "Deduz dias de Aviso-Prévio – Lei 12.506/2011"]
---

# Propriedades da ocorrência: o que cada opção faz

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Ocorrências > Cadastro
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

As **Propriedades da Ocorrência** definem como cada tipo de ocorrência será tratado pelo Pessoas+ durante os processos de folha de pagamento, férias, controle de ponto, Portal RH e demais rotinas.

A configuração correta dessas propriedades garante que o sistema execute automaticamente os comportamentos esperados quando a ocorrência for lançada para um colaborador.

### 2. Pré-requisitos

- Permissão para cadastrar ou editar **Ocorrências**.

### 3. Jornada de Uso

![Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/42553471370775)

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha);
2. Depois de preencher a seção **Geral** do [cadastro da ocorrência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494), configure as **Propriedades da Ocorrência**, conforme a finalidade desejada:

   🔹**Folha de Pagamento**

   | Propriedade | Funcionalidade |
   | --- | --- |
   | **Reduz Dias Trabalhados** | Define se a ocorrência reduz os dias trabalhados para fins de cálculo da folha. Alguns afastamentos previstos em lei possuem tratamento próprio e são considerados automaticamente pelo sistema.  **Marcada**: o sistema considera os dias do afastamento para reduzir os dias trabalhados do colaborador na apuração do cálculo mensal, impactando proporcionalmente o salário base e as bases de INSS, FGTS e IRRF.  **Desmarcada**: os dias da ocorrência não são deduzidos dos dias trabalhados, mesmo que a ocorrência já esteja lançada para o colaborador. |
   | **Falta** | Identifica a ocorrência como falta injustificada, permitindo seus reflexos na folha, férias e 13º salário. |
   | **Tem Direito de Adiantamento** | Mantém o direito ao adiantamento salarial ou benefícios quando aplicável. |

   **🔹Férias**

   | Propriedade | Funcionalidade |
   | --- | --- |
   | **Quita Férias por Afastamentos – Art. 133 CLT** | Utiliza a ocorrência na rotina de quitação automática do período aquisitivo prevista no Art. 133 da CLT.  **Marcada:** o sistema aplica liquidação de férias de acordo com o Artigo 133 da CLT (ex: afastamento por acidente, maternidade).  **Desmarcada:** não aplica a regra específica. |
   | **Quita Férias em Licença Remunerada** | Permite que a licença remunerada seja considerada nas regras de férias da empresa.  **Marcada:** os dias dessa licença remunerada reduzem automaticamente os dias de férias disponíveis do colaborador.  Exemplo: licença-prêmio que reduz férias proporcionais.  **Desmarcada:** não afeta direitos de férias. |

   **🔹Estabilidade**

   | Propriedade | Funcionalidade |
   | --- | --- |
   | **Indenização de Estabilidade** | Indica que a ocorrência gera estabilidade ao colaborador.  **Marcada:** o sistema calcula e provisiona indenizações relacionadas à estabilidade do emprego (ex: gravidez, acidente, doença).  Requer a configuração da **quantidade de meses** após o retorno do colaborador e do parâmetro FPCODHISESTABIL, para que em caso de desligamento, o cálculo da rescisão os meses de estabilidade a partir da data fim da ocorrência.  **Desmarcada:** nenhuma provisão de estabilidade é gerada. |
   | **Baixa na Provisão** | Utilizada para reduzir ou encerrar provisões de estabilidade (ex: gravidez, acidente, doença).  **Marcada:**reduz ou elimina provisões de estabilidade previamente constituídas.  **Desmarcada:** não afeta provisões. |

   **🔹Aviso-Prévio**

   | Propriedade | Funcionalidade |
   | --- | --- |
   | **Abate no Aviso Prévio** | Permite descontar dias da ocorrência na contagem do aviso-prévio a cumprir.  Aplica-se para faltas, afastamentos e outras ocorrências que justificam redução do aviso. |
   | **Deduz dias de Aviso-Prévio – Lei 12.506/2011** | Aplica as deduções previstas pela Lei nº 12.506/2011.  **Marcada:** aplica aumentos progressivos: 30 dias + 3 dias por ano de serviço (máx 60 dias).  📚Para mais detalhes, acesse [Reflexo afastamento na contagem do Aviso Prévio](https://ajuda.sankhya.com.br/hc/pt-br/articles/29904519221783).  **Desmarcada:**não aplica deduções conforme essa lei. |

   **🔹Portal RH**

   | Propriedade | Funcionalidade |
   | --- | --- |
   | **Aparece no Portal RH** | Disponibiliza a ocorrência para solicitação pelos colaboradores através do [Portal RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108433). |
   | **Necessita de anexo no Portal RH** | Impede a conclusão da solicitação enquanto o documento obrigatório não for anexado.  Exemplo: atestado médico, comprovante de comparecimento. |

   **🔹Controle de Ponto**

   | Propriedade | Funcionalidade |
   | --- | --- |
   | **Gera Ocorrência AFDT** | Gera movimentações relacionadas ao controle de frequência.  **AFDT** é o controle diário de presença/ausência.  Requer o preenchimento do **Tipo de Registro**. |
   | **Absenteísmo** | Inclui a ocorrência nos indicadores de absenteísmo da empresa.  **Marcada:** a ocorrência é contabilizada nas estatísticas de absenteísmo corporativo.  **Desmarcada:** não afeta indicadores de absenteísmo. |

   **🔹Outras Configurações**

   | Propriedade | Funcionalidade |
   | --- | --- |
   | **Ocorrência de reajuste salarial sindical** | Identifica automaticamente ocorrências utilizadas em reajustes salariais decorrentes de acordos ou convenções coletivas. |
3. Clique em **Confirmar alterações**.

### 4. Pontos de Atenção

- Configure apenas propriedades compatíveis com a finalidade da ocorrência.
- Algumas propriedades dependem de parâmetros adicionais para produzir efeito.
- Alterações podem impactar processamentos futuros.
- **Reduz Dias Trabalhados não é a única regra que desconta dias da folha.** Os tipos Acidente de trabalho, Doença acima de 15 dias, Licença maternidade, Serviço militar, Sem remuneração e Aposentadoria por Invalidez **sempre** são considerados afastamento no cálculo da folha, independentemente dessa marcação. Ela só decide o comportamento dos **demais** tipos (ex.: licenças diversas, atestados, faltas em horas).
- Se os [dias de falta com suspensão disciplinar](https://ajuda.sankhya.com.br/hc/pt-br/articles/42468830204567) não forem descontados na folha, verifique se a ocorrência está com a opção **Reduz Dias Trabalhados** marcada. Após alterar a configuração, é necessário **recalcular a folha da competência** para atualizar o cálculo.
- Ao marcar **Indenização de Estabilidade**, o campo **Quantos Meses de Estabilidade?** é exibido — e o código do tipo precisa estar configurado no parâmetro FPCODHISESTABIL para a rescisão considerar corretamente esses meses.

### 5. Dicas de Usabilidade

- Revise todas as propriedades antes de disponibilizar uma nova ocorrência.
- Utilize nomenclaturas padronizadas para facilitar futuras manutenções.

## Perguntas Frequentes (FAQ)

**1. Posso marcar várias propriedades na mesma ocorrência?**

Sim, desde que sejam compatíveis com sua finalidade.

**2. Alterar uma propriedade afeta lançamentos existentes?**

Os efeitos serão percebidos nos próximos processamentos realizados pelo sistema.

**3. Quais propriedades exigem configurações adicionais?**

Principalmente **Indenização de Estabilidade** e **Quita Férias por Afastamentos – Art. 133 CLT**.

**4.** **Como configurar uma ocorrência de suspensão disciplinar para que os dias sejam descontados da folha?**

Na ocorrência utilizada para a suspensão disciplinar, marque a opção **Reduz Dias Trabalhados**. Essa configuração faz com que os dias da ocorrência sejam considerados como dias não trabalhados no cálculo da folha.

Após alterar a configuração, é necessário **recalcular a folha da competência** para atualizar o cálculo.

## Artigos Relacionados

- [Cadastro de Ocorrências para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
- [Cadastro de Ocorrências com Estabilidade para Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055)
- [Quitação de Férias em caso de Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/31144991936151)
