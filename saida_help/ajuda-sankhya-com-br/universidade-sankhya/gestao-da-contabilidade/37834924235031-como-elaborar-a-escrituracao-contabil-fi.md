---
id: "37834924235031"
titulo: "Como elaborar a Escrituração Contábil Fiscal (ECF)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37834924235031-Como-elaborar-a-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Fiscal-ECF"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-07-22T14:07:02Z"
rotulos: ["Configuração", "ECF", "SPED", "Fiscal", "Contabilidade", "Escrituração Contábil Fiscal", "Obrigações Acessórias"]
---

# Como elaborar a Escrituração Contábil Fiscal (ECF)

| Categoria |
| --- |
| [O que é a Escrituração Contábil Fiscal (ECF)?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834924235031-Como-elaborar-a-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Fiscal-ECF#h_01KFGT9YBB8PPAZYCQ06EE9JP8) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834924235031-Como-elaborar-a-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Fiscal-ECF#h_01KFGTA8NTF8A1TKWDN295VE5X) |
| [Demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834924235031-Como-elaborar-a-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Fiscal-ECF#h_01KFGTAGYAE5A558A5WA63A4S6) |
| [Cenário de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834924235031-Como-elaborar-a-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Fiscal-ECF#h_01KFGTAYMBWDYWN08GDFQ3FX4J) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834924235031-Como-elaborar-a-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Fiscal-ECF#h_01KFGTB6MX544JNAZZ26AR7SXF) |

## Escrituração Contábil Fiscal (ECF)

#### O que é a Escrituração Contábil Fiscal (ECF)?

A Escrituração Contábil Fiscal (ECF) é uma obrigação acessória digital que substitui o antigo Livro de Apuração do Lucro Real (LALUR) e tem como objetivo integrar e consolidar as informações contábeis e fiscais das empresas, permitindo o correto cálculo e a fiscalização dos tributos IRPJ e CSLL. Essa escrituração deve ser apresentada por empresas tributadas pelo lucro real, presumido, arbitrado ou outros regimes específicos, promovendo maior transparência, precisão nos dados e eficiência no processo de controle da Receita Federal.

#### Quais problemas este recurso resolve?

- Inconsistências entre informações contábeis e fiscais, ao exigir a integração e conciliação desses dados em um único ambiente digital.
- Risco de autuações fiscais, reduzido pela maior transparência e rastreabilidade das informações prestadas à Receita Federal.
- Erros no cálculo do IRPJ e CSLL, ao padronizar e automatizar o processo de apuração dos tributos.
- Falta de controle sobre ajustes fiscais, com a substituição do antigo LALUR e registro detalhado dos ajustes e adições/exclusões ao lucro contábil.
- Retrabalho e duplicidade de informações, já que a ECF centraliza dados anteriormente distribuídos em diferentes documentos.
- Baixa eficiência na fiscalização tributária, ao fornecer à Receita Federal dados mais completos, estruturados e analisáveis eletronicamente.
- Desalinhamento com obrigações acessórias do SPED, pois a ECF faz parte do ambiente SPED e favorece a conformidade com o sistema eletrônico do Fisco.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1125161708)

#### Cenário de aplicação

A empresa Axis LTDA., enquadrada no regime de Lucro Real, precisa entregar a Escrituração Contábil Fiscal (ECF) referente ao ano-calendário em curso. Como essa obrigação consolida as informações contábeis e fiscais para apuração do IRPJ e da CSLL, é fundamental que o ERP Sankhya esteja configurado corretamente, contemplando forma de tributação, parâmetros de apuração e blocos obrigatórios do SPED. Essa preparação garante a consistência dos dados transmitidos à Receita Federal, reduzindo riscos de inconsistência, autuações fiscais e retrabalho no processo de fechamento.

**Tarefa:** assista ao vídeo de demonstração prática e siga o passo a passo abaixo para configurar a ECF no sistema. Certifique-se de parametrizar corretamente a forma de tributação, os períodos de apuração, os blocos e registros obrigatórios, assegurando a geração do arquivo digital em conformidade com as normas do SPED e com o regime tributário da empresa.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Empresa**
   **Menu:** Contabilidade » Preferências » Empresa

- **Aba ECF - Escrituração Contábil Fiscal**
  **Sub aba Blocos**
- Para registrar o bloco manualmente clique em “**+**” (**Cadastrar Definição dos blocos a serem gerados EFB**).
- Informe a **Sequência** numérica correspondente.
- Preencha a **Descrição** do bloco.
- O campo **Gerar Bloco** quando habilitado, irá gerar o ECF com base nos registros configurados
- Salve as alterações.

Grade Registros

- Para vincular manualmente os registros aos blocos, selecione o registro do bloco na grade superior.
- Clique em “**+**” (**Cadastrar** **Definição Registro Bloco EFB**).
- Informe o Registro e sua respectiva Descrição.
- Marque a opção Gerar Registro.
- Salve as alterações..

**Sub aba** **Parâmetros de Tributação**

- Configure os campos abaixo de acordo com as informações solicitadas: 

  - **Forma de Tributação**: determine neste campo a forma de tributação da empresa.
  - **Indicador do Período de Apuração de IRPJ e da CSLL**: defina o período de apuração de IRPJ e CSLL.
  - **Escrituração:** determine a escrituração a ser utilizada pela empresa.
  - **Tipo de Pessoa Jurídica Imune ou Isenta:** defina qual das opções a empresa se enquadra.
  - **Apuração do IRPJ para Imunes ou Isentas:** defina neste campo como será a periodicidade da apuração do IRPJ para imunes ou isentas.
  - **Apuração do CSLL para Imunes ou Isentas:** defina neste campo como será a periodicidade da apuração do CSLL para imunes ou isentas.
  - **PJ Sujeita à Alíquota da CSLL de 9% ou 17% ou 20% em 31/12/2015:** Determine neste campo a alíquota da CSLL da PJ a ela sujeita.
  - **Critério de reconhecimento de receitas (L.Presumido)**: Determine neste campo qual será o fundamento de reconhecimento de receitas a ser utilizado. A configuração deste campo será utilizada para o preenchimento do campo IND\_REC\_RECEITA do registro 0010.
- Após definir os parâmetros, salve as alterações

2. Acesse a tela **Plano de Contas**

**Menu:** Contabilidade » Cadastros » Plano de Contas

- Selecione na hierarquia de contas, com um duplo clique, a conta analítica desejada.
- Acesse a aba **Conta Contábil Referencial** e preencha os campos **Tipo e Cód. Conta Ref.**, selecionando entre as opções disponíveis conforme a natureza do Grupo de Conta definida na aba **Geral**.
- No topo da tela, ao lado da empresa, o botão “**Relatório com Plano de Conta Referencial**” (ícone de documento) exibe o plano de contas cadastrado juntamente com as respectivas Contas Contábeis Referenciais.
- Salve as alterações.

3. Acesse a tela **Geração de Blocos para Integração - ECF**
   **Menu:** Contabilidade » Conexão » ECF » Geração de Blocos para Integração - ECF

- Selecione a **Empresa** para a qual se deseja gerar os blocos e o **Período** das informações.

**Aba Parâmetros**

- No campo **Natureza do Livro** informe o nome da Natureza do livro associado; sua finalidade e a que se destina o instrumento.
- Determine no campo **Indicador de sit. Início do período** a situação da empresa referente à geração do arquivo em relação ao início do período informado.
- No topo da tela, clique em **Gerar Arquivo**.
- No pop-up Processos acione o botão “**Baixar** **arquivo**” e salve o  em sua máquina.
