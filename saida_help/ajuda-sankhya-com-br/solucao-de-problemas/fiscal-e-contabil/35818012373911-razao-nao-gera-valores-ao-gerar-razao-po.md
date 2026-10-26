---
id: "35818012373911"
titulo: "Razão não gera Valores ao gerar Razão por empresa de origem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35818012373911-Raz%C3%A3o-n%C3%A3o-gera-Valores-ao-gerar-Raz%C3%A3o-por-empresa-de-origem"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:24:35Z"
rotulos: ["não gera", "Configuração", "Relatórios", "Empresa", "Contábil", "Preferências", "Lançamentos", "Razão", "Valores", "por", "Gravar empresa de origem nos lançamentos", "ao gerar", "empresa de origem", "Quebrar razão por empresa de origem", "TCBSALEMP", "CTBUTISALEMPORG"]
---

# Razão não gera Valores ao gerar Razão por empresa de origem

No módulo Contábil do sistema, é possível detalhar relatórios para identificar os saldos por Empresa de Origem dos lançamentos.
Para isso, na tela '**'Empresa''** (Contabilidade» Preferências) na aba **''Lançamentos''**, conta com duas marcações essenciais:

- **Quebrar razão por empresa de origem:** permite que os relatórios contábeis apresentem os lançamentos separados conforme a empresa de origem, facilitando a análise individualizada de cada entidade.
- **Gravar empresa de origem nos lançamentos:** assegura que cada lançamento contábil registre a informação da empresa que o gerou, garantindo a segregação correta dos saldos e a precisão dos relatórios contábeis.

Quando essas opções estão habilitadas, relatórios como o Balancete de Verificação passam a ser apresentados de forma segmentada, exibindo separadamente os saldos de cada Empresa de Origem. Dessa maneira, é possível visualizar com maior precisão quais empresas foram responsáveis por gerar cada saldo.

#### Importância da Tabela TCBSALEMP

Quando a marcação **“Quebrar razão por empresa de origem”** é utilizada, o sistema passa a buscar os saldos na tabela **''TCBSALEMP'**'.

**(1)** Cenário comum de problema:

- Caso a tabela TCBSALEMP não esteja populada, o relatório '**'Razão por Empresa de Origem'**' não exibirá informações.
- Isso ocorre porque não existem saldos consolidados registrados para cada empresa de origem, impossibilitando a apresentação dos dados no relatório.

#### Habilitando o Parâmetro CTBUTISALEMPORG

Antes de utilizar a recomposição de saldos por Empresa de Origem, é necessário habilitar o parâmetro **''CTBUTISALEMPORG''**.

**(1)** Siga os passos para habilitação:

**(1)** Acesse a tela **''Preferências'',** localize o parâmetro CTBUTISALEMPORG e habilite-o.

Com esse parâmetro ativo, o sistema passa a considerar a empresa de origem durante a recomposição de saldos e na geração dos relatórios contábeis, garantindo que as informações sejam apresentadas de forma segregada por empresa.

![Imagem 1: Com esse parâmetro ativo, o sistema passa a considerar a empresa de origem durante a recomposição de saldos e na…](https://ajuda.sankhya.com.br/hc/article_attachments/35818033674775)

#### Recomposição de Saldos por Empresa de Origem

Quando a tabela TCBSALEMP não estiver populada, o relatório Razão por Empresa de Origem ficará sem dados. Para resolver, é necessário executar a Recomposição de Saldos por Empresa de Origem, que irá preencher os saldos consolidados por empresa na tabela TCBSALEMP.

**(1)** Siga os passos abaixo:

**(1)** Acesse a tela ''**Empresa''** (Contabilidade» Preferências) clique no botão ''**Outras Opções''**, e selecione a opção **''Recompor Saldos por Empresa Origem'';**

**(2)** Ao selecionar Recompor Saldos por Empresa de Origem, será exibido um pop-up solicitando a **data de referência de partida:**

- Informe a data a partir da qual o sistema deve recalcular os saldos;

  Exemplo: para recompor a partir de 1º de janeiro de 2023, insira 01/01/2023.
- Confirme a operação no pop-up (botão OK / Confirmar). O sistema iniciará o recálculo dos saldos a partir da data informada;
- Ao término do processamento, verifique se a tabela TCBSALEMP foi corretamente populada para as empresas e períodos selecionados;
- Gere novamente o relatório Razão por Empresa de Origem para validar que os saldos passaram a ser exibidos corretamente.

![Imagem 2: Gere novamente o relatório Razão por Empresa de Origem para validar que os saldos passaram a ser exibidos corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/36309091177623)![Imagem 3: Gere novamente o relatório Razão por Empresa de Origem para validar que os saldos passaram a ser exibidos corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/35818012366743)
