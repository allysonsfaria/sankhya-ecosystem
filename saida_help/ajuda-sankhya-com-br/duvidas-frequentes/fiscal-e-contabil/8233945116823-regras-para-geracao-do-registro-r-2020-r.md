---
id: "8233945116823"
titulo: "Regras para geração do registro R-2020 - REINF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8233945116823-Regras-para-gera%C3%A7%C3%A3o-do-registro-R-2020-REINF"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:12:21Z"
rotulos: ["Configuração", "Fiscal", "Alíquota de ISS", "Impostos", "NFS-e", "INSS deve ser calculado com alíquota de 35% ou 11%.", "Nota deve ser lançada como Serviço e com TOP tipo \"VENDA\".", "Marque as configurações corretas em Preferências da Empresa e atualize os livros de acordo com o modelo de documento.", "Reinf"]
---

# Regras para geração do registro R-2020 - REINF

Para a geração do registro R2020, o sistema busca as **notas** de serviços prestados, emitidas nos portais do sistema.

Veja abaixo os critérios de validação, para que as notas sejam levadas ao REINF, no registro R2020:

**1:** Deve existir o cálculo do **INSS**, em pelo menos um dos dois locais da nota:

**1.1:** Grade de itens > Botão Outras Opções > Consultar/Alterar dados do imposto do item.

![Imagem 1: 1.1: Grade de itens > Botão Outras Opções > Consultar/Alterar dados do imposto do item.](https://ajuda.sankhya.com.br/hc/article_attachments/16591365868439)

**1.1.1:** O INSS calculado aqui, pode ser lançado de **duas** formas:

**1°** Com o campo **"Tipo Retenção"** igual a **"Retido"**;
**2°** Com o campo Tipo Retenção igual a **"Não aplicado"**, porém, nessa situação o parâmetro **GERIMPINCREINF** deve estar ativado na base;

**1.1.2:** A **alíquota** utilizada para o cálculo do INSS deve ser **3,5%** ou **11%**.

**1.2:** Grade de itens > Botão Outras Opções > Outros Impostos.

![Imagem 2: 1.2: Grade de itens > Botão Outras Opções > Outros Impostos.](https://ajuda.sankhya.com.br/hc/article_attachments/16591365870743)

**1.2.1:** O **INSS** calculado aqui, pode ser lançado de **duas** formas:

**1°** Com o campo Tipo Retenção igual a **"Retido"**;
**2°** Com o campo Tipo Retenção igual a **"Incluso"**, porém, nessa situação o parâmetro **"GERIMPINCREINF"** deve estar ativado na base;

**1.2.2:** A **alíquota** utilizada para o cálculo do INSS deve ser **3,5%** ou **11%**.

**2:** Nas preferências da Empresa (Comercial), o campo **"Ativo"** deve estar marcado;

**3:** A nota deve ter sido lançada com um **Serviço** e não um **Produto**;

**4:** O **serviço** deve ter alguma opção marcada, no campo "**Classificação Cessão M.d.Obra**";

**5:** A nota deve ter sido lançada com uma TOP do tipo "**VENDA**";

**6:** Se o modelo de documento da TOP for diferente de **67**, o campo de atualização de **Livros de ISS** deve estar marcado como **"Saída"**.

**6.1:** Ou se o modelo de documento da nota for igual a **67**, o campo de atualização de **Livros de ICMS** deve estar como "**Ambos**" ou "**Saída**" e, o campo "**Status CT-e**" (cabeçalho da nota) deve estar como "**Aprovado**".

**6.2:** Ou se o Estado da empresa geradora do REINF for **DF-Distrito Federal** e o modelo de documento da TOP é **55**: a TOP deve estar marcada com o campo de **"Atualização de Livros de ISS"** igual a "**Não Atualiza**", ou, o campo de atualização de **Livros de ICMS** deve estar como "**Ambos**" ou "**Entrada**".

**7:** A nota deve estar **confirmada**;

**Observação:** o objeto responsável por buscar todos os documentos que são apresentados em tela, se trata de uma VIEW de banco de dados, denominada **VRI\_EVT\_R2020\_NFS\_INFOTPSERV**.

Nas **preferências** da empresa, na aba **"REINF"**, existem marcações que atuam na geração do registro.
