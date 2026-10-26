---
id: "24084376156695"
titulo: "Registro 1975 - Veja como são preenchidos os campos 02 e 05"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24084376156695-Registro-1975-Veja-como-s%C3%A3o-preenchidos-os-campos-02-e-05"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:47:46Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Crédito", "Impostos", "Registro 1975", "campos 02 e 05", "Crédito Presumido Nas Saídas Internas", "Alíquota incidente sobre as importações-base", "Alíquotas de CBS"]
---

# Registro 1975 - Veja como são preenchidos os campos 02 e 05

**Campo 02: ALIQ\_IMP\_BASE** (Alíquota incidente sobre as importações-base)
 
**Campo 05:  G3\_12** (Crédito Presumido Nas Saídas Internas)
 
Para **preenchimento desses campos**, o sistema percorre algumas **regras**, sendo elas:

**(1)** Que exista um Decreto devidamente preenchido na tela **"Cadastro Incentivos Fiscais/Financeiros"** e que na Sub-aba **"Produtos"** tenham os devidos produtos inseridos corretamente.

**(1)** Que a Data de Validade e Fim Validade estejam dentro do período de geração do Arquivo.

Para o **cálculo do PRODEPE também existem certas validações,** como

**(2)** A Nota deve estar no Cadastro do livro e ser uma Saída;
**(2)** Com UF Destino igual a 'PE';
**(2)** No Cadastro do Produto o campo **"Indicador Esp. Inc. PRODEPE/FUNCRESCE"**deve ser preenchido como **"Com incentivo";**
**(2)** Na tela **"Cadastro Incentivos Fiscais/Financeiros"**, sub-aba **Produtos**, o campo **"Alíquota Incidente s/ Importações-base"** não pode estar em branco, para o sistema analisar a Quantidade Negociada na ITE da Nota.

**Atenção:**
 
O cálculo do **custo** é feito analisando a Tabela de Custo de Cada Produto (TGFCUS), inicialmente avaliando o campo **"Custo para Importações-base",**a fim de identificar o que foi informado (Médio com ICMS , Médio sem ICMS, Gerencial, Reposição). Assim, a depender da informação inserida, o sistema pegará na Tabela de Custo o devido valor de acordo com o dado passado.
 
**Observação:** caso o sistema não encontre nenhuma informação, será levado o **valor** de **zero**. E caso o **custo** levado seja igual a **zero**, o **Campo 05 -  G3\_12** ( Crédito Presumido Nas Saídas Internas) também **será zero**. 
 
**Pontos importantes para o Cálculo do CUSTO:**  o controle usado na Tabela de Custos para o Produto em questão deve ser o mesmo utilizado no momento de lançamento da Nota, e o mesmo serve para o CODLOCAL. Caso o Produto não tenha Controle por Local na Tabela de Custos, no momento de lançamento da Nota não se pode informar Local para o Produto. 
 
**Exemplo:** produto X na Tabela de custos não usa controle por local, então ficará igual a ZERO ( 0 ), mas no momento de geração da Nota é informado Local 10 para o mesmo Produto X.  Nesse caso, não será levado o Cálculo do Custo por ocorrer essa divergência de informação do Local.
