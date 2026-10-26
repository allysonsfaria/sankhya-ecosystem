---
id: "7396959855127"
titulo: "Regras para geração do registro R-2010 - REINF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7396959855127-Regras-para-gera%C3%A7%C3%A3o-do-registro-R-2010-REINF"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:13:32Z"
rotulos: ["Configuração", "Impostos", "Estoque", "Financeiro", "#validadoMurilo", "NFS-e", "Verifique se o parceiro possui um CNPJ com 14 dígitos e que a nota ou financeiro estejam confirmados.", "INSS deve estar presente e corretamente configurado na nota.", "Configurações de Preferências e TOP devem estar ajustadas conforme o tipo de documento.", "Reinf"]
---

# Regras para geração do registro R-2010 - REINF

Temos para a geração do registro R2010, dois cenários:

(1)** Documento com origem Estoque;**

(1)** Documento com origem Financeiro;**

#### Primeiro cenário:

Documento com origem **Estoque**

**1:** Os valores de INSS devem constar na nota, em um dos dois locais a seguir:

**1.1:** Outros Impostos do ITEM (TGFIMN com campo sequencia diferente de zero):

####

![Imagem 1: 1.1: Outros Impostos do ITEM (TGFIMN com campo sequencia diferente de zero):](https://ajuda.sankhya.com.br/hc/article_attachments/16519468290327)

Nessa tela, deve-se ter uma linha com o imposto do tipo INSS (Tela Impostos), podendo ser do tipo retido ou incluso, porém se estiver como incluso, o parâmetro **"GERIMPINCREINF"** deve estar ativo na base; A alíquota utilizada deve ser de 3,5% ou 11%;

**1.2:** Consultar/Alterar dados dos impostos dos itens (TGFDIN):

![Imagem 2: 1.2: Consultar/Alterar dados dos impostos dos itens (TGFDIN):](https://ajuda.sankhya.com.br/hc/article_attachments/16519453061783)

Deve existir uma linha com o imposto INSS e nesta linha deve-se observar o campo "**Tipo Retenção**":

**1.2.1:** Se for do tipo **retido**, o sistema já considera como correto para geração;

**1.2.2:** Se for do tipo **não aplicado** se faz necessário que o parâmetro **"GERIMPINCREINF"** esteja ativado;

**1.2.3:** Se for do tipo **não retido,** se faz necessário que o parâmetro **"GERIMPNRETR2010"** esteja ativado;

**Observação:** A alíquota utilizada deve ser de **3,5%** ou **11%**;

**2:** Nas preferências da Empresa(Comercial) o campo "**Ativo"** deve estar marcado;

**3:** A nota deve ter sido lançada, com um **serviço**, e não um **produto**;

**4:** O serviço deve ter alguma opção marcada, no campo **"Classificação Cessão M.d.Obra":**

**5:** A nota deve ter sido lançada com uma TOP do tipo "**Compra**";

**6:** Se o modelo de documento da TOP for diferente de 67, o campo de atualização de Livros de ISS deve estar marcado como **"Entrada".**

**6.1:** OU Se o modelo de documento da nota for igual a 67, o campo de atualização de Livros de ICMS deve estar como "Ambos" ou "Entrada".

**6.2:** OU Se o Estado da empresa geradora do REINF for DF-Distrito Federal e o modelo de documento da TOP é 55: a TOP deve estar marcada com o campo de atualização de Livros de ISS igual a "Entrada", ou, o campo de atualização de Livros de ICMS deve estar como "Ambos" ou "Entrada".

**7:** A nota deve estar confirmada;

**8:** O parceiro da nota, deve ter como documento um CNPJ, com 14 dígitos (ignorando os pontos e traços);

#### Segundo cenário: Documento com origem Financeira

**1:** O Financeiro deve estar na tela Outros Impostos, da seguinte forma:

![Imagem 3: 1: O Financeiro deve estar na tela Outros Impostos, da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/16519453064215)

Nessa tela, deve-se ter uma linha com o imposto do tipo INSS (Tela Impostos), podendo ser do tipo retido ou incluso, porém se estiver como incluso, o parâmetro GERIMPINCREINF deve estar ativo na base;

**1.1:** A alíquota utilizada deve ser de **3,5%** ou **11%**;

**2:** Nas preferências da Empresa(Comercial) o campo ATIVO deve estar marcado;

**3:** O financeiro deve estar marcado com alguma opção para o campo **Classificação Cessão M.d.Obra**;

![Imagem 4: 3: O financeiro deve estar marcado com alguma opção para o campo Classificação Cessão M.d.Obra ;](https://ajuda.sankhya.com.br/hc/article_attachments/16519468295447)

**4:** A TOP utilizada para lançamento do financeiro, deve ser do tipo "Financeiro";

**5:** Se o modelo de documento da TOP for diferente de 67, o campo de atualização de Livros de ISS deve estar marcado como **"Entrada"**.

**5.1:** Ou Se o modelo de documento da nota for igual a 67, o campo de atualização de Livros de ICMS deve estar como **"Ambos"** ou **"Entrada".**

**5.2:** OU Se o Estado da empresa geradora do REINF for DF-Distrito Federal e o modelo de documento da TOP é 55: a TOP deve estar marcada com o campo de atualização de Livros de ISS igual a "Entrada", ou, o campo de atualização de Livros de ICMS deve estar como "Ambos" ou "Entrada".

**6:** O parceiro do financeiro, deve ter como documento um CNPJ, com 14 dígitos (ignorando os pontos e traços);

**Observação:** o objeto responsável por buscar todos os documentos que são apresentados em tela, se trata de uma VIEW de banco de dados, denominada **VRI\_EVT\_R2010\_NFS\_INFOTPSERV.**

Nas **"Preferências"** da empresa, na aba **"REINF"**, existem marcações que atuam na geração do registro.
