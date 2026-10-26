---
id: "38000543130007"
titulo: "ISS em Notas de Entrada e Saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38000543130007-ISS-em-Notas-de-Entrada-e-Sa%C3%ADda"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-08-12T16:15:50Z"
rotulos: ["ISS", "Configuração", "Alíquota de ISS", "Cidades", "Impostos", "NFS-e"]
---

# ISS em Notas de Entrada e Saída

## ISS em Entradas e Saídas

#### O que é ISS?

O **ISS (Imposto Sobre Serviços)** é um tributo de competência municipal ou do Distrito  Federal que incide sobre a prestação de serviços por empresas e profissionais, conforme uma lista taxativa estabelecida em legislação federal. Por ser municipal, cada cidade define suas próprias alíquotas (que variam de 2% a 5%), regras de recolhimento e procedimentos administrativos. A base de cálculo do imposto é o preço do serviço prestado.

#### Quais problemas empresariais são resolvidos pela configuração do ISS em um ERP?

- **Erro no cálculo do ISS** devido à ausência de automatização;
- **Emissão incorreta de Notas Fiscais de Serviço (NFS-e)**;
- **Descumprimento das exigências específicas de cada município**, ocasionando inconsistências fiscais;
- **Risco de penalidades e multas fiscais** por não conformidade;
- **Dificuldade em manter a regularidade fiscal da empresa** diante da complexidade do tributo;
- **Gestão tributária descentralizada e ineficiente**, especialmente em empresas que prestam serviços em diferentes municípios.

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo do ISS.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo do ISS.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Empresa”**
   Menu: Comercial » Preferências

- Na aba **“Documentos Fiscais Eletrônicos”**, subaba “**NFS-e”**, em **“Geral”**, configure os campos:

  - **“ISS”**: informe a opção **“Tributado”**.
- Em **“CNAE Empresa”**, configure os campos: 

  - **“CNAE”**: indique o CNAE correspondente à atividade da empresa;
  - **“Local Tributação (ISS Retido)”**: selecione a opção que determina em qual cidade o imposto será devido, no caso de imposto retido;
  - **“Local Tributação (ISS normal)”**: selecione a opção que determina em qual cidade o imposto será devido, no caso de imposto normal.

2. Acesse a tela **“Parceiros”**
   Menu: Configurações » Cadastros

- Na aba **“Fiscal”**, verifique o campo:

  - **“Retém ISS":** determina qual alíquota será utilizada no cálculo deste imposto. Se estiver selecionada, será utilizada a alíquota da cidade do Parceiro e irá deduzir o valor do imposto; se desmarcada, utilizará a alíquota da cidade da empresa e não deduzirá;
- O cálculo do **ISS** na Nota de Compra utiliza a alíquota da sua empresa se a opção "Retém ISS" estiver marcada, ou a alíquota do parceiro se estiver desmarcada. Para usar a alíquota da Cidade da Prestação do Serviço, deve-se informar essa cidade no campo "Cidade" no rodapé da nota antes de inserir o serviço.

3. Acesse a tela **“Serviço”**
   Menu: Configurações » Cadastros » Produtos

- Na aba **“Impostos”**, configure os campos:

  - **“Tem ISS”**: selecione a opção **“Tributado”**;
  - **“Cód. Trib. Município NFS-e”**: informe o código de tributação estipulado pelo município;
  - **“CNAE”**: indique o CNAE correspondente à atividade da empresa.

4. Acesse a tela **“Tipos de Operação - TOP”**
   Menu: Comercial » Arquivo » Cadastros

- Selecione a TOP de compra de serviços;
- Na aba **“Impostos”**, configure:

  - **“Tem ISS”**: marcado;
  - **“Cálculo de ICMS, IPI e ISS”**: selecione a opção **“Calcula e Digita”**.

5. Acesse a tela **“Alíquotas de ISS”**
   Menu: Contratos e Serviços » Arquivos » Cadastros

- Insira um cadastro clicando em **“+ Novo registro”**;
- No cabeçalho, preencha os campos “**Cidade”**, “**Serviço”** e “**Empresa”**.
- Na aba **Geral**, configure os campos:

  - **“Percentual ISS”**: indique a alíquota conforme definido pelo município.
  - **“Cód. Tributação ISS”**: selecione a opção correspondente à operação.
  - **“Perc. de dedução na base do ISS”**: preencha se houver deduções.
  - **“Tipo de dedução de base do ISS”**: preencha se o campo acima for diferente de zero.
  - **“Cód. Trib. Município”:** informe o código de tributação estipulado pelo município.
  - **“Tipo de Serviço”**: selecione a opção que melhor condiz com o serviço prestado.

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Tarefa:** Acesse o Portal de Compras e gere um pedido de compra com a TOP de compra de serviço.

1. Acesse a tela **“Portal de Compras”**

**Menu:** Comercial » Consulta » Portal de Compras

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **“Nota de Compra”**;
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Empresa;**
  - **Tipo Operação:** COMPRA - SERVIÇOS, por exemplo.

**Itens**

- Utilize na negociação o serviço configurado;
- Salve as informações.
- No Rodapé, na aba **“Impostos”**, verifique o campo **“Valor do ISS”**
- Acione o botão “**...**” (**Outras opções…**);
- Clique na opção **“Resumo de Impostos”** e verifique o ISS.

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
