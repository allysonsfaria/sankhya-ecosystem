---
id: "38956082590487"
titulo: "NFS-e: Segregação de PIS/COFINS Retido e Apuração Própria (NT 007/2026)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38956082590487-NFS-e-Segrega%C3%A7%C3%A3o-de-PIS-COFINS-Retido-e-Apura%C3%A7%C3%A3o-Pr%C3%B3pria-NT-007-2026"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > NFS-e"
atualizado_em: "2026-09-15T17:55:02Z"
rotulos: ["Configuração", "Impostos", "NFS-e", "Alíquota de PIS", "Alíquota COFINS", "aliquotas de cofins", "pis", "cofins", "segregação", "aliquotas de pis", "cofis retido", "NT 007/2026"]
---

# NFS-e: Segregação de PIS/COFINS Retido e Apuração Própria (NT 007/2026)

Para atender às exigências da Nota Técnica 007/2026, o sistema Sankhya foi atualizado para realizar a separação automática dos valores de PIS e COFINS no momento da transmissão da NFS-e.

A estrutura do documento fiscal exige que o Fisco receba de forma segregada o que é imposto de **Apuração Própria** (devido pelo prestador do serviço, "já incluso" na operação) e o que é imposto **Retido na Fonte**. O sistema mapeia essa diferença com base nas configurações da sua tela de [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos).

Veja como configurar e conferir cada um dos cenários:

#### 1. Configuração e conferência do PIS/COFINS retido

Para que o sistema informe à prefeitura (ou ao Portal Nacional) que os impostos configurados tratam-se de "impostos retidos", é necessário configurar o comportamento de subtração.

**Como configurar:**

1. Acesse o caminho: Configurações > Cadastros > [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos).
2. Ao configurar um tipo de imposto PIS ou COFINS, o campo de comportamento na nota deve estar marcado com a opção **"Subtrair"**. É essa marcação que sinaliza ao sistema o caráter de retenção daquele tributo.

**Como conferir na emissão da nota:** no momento do faturamento ([Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) / [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)), você pode validar se a retenção foi aplicada corretamente:

1. Selecione a nota e o item desejado.
2. Clique no botão [**Outras Opções...**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) da Central de Vendas e acesse [**Outros Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#outrosimpostos)**,** um pop-up será aberto onde serão apresentados os impostos previamente configurados na tela [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos).
3. O imposto listado (PIS ou COFINS) estará apontado no tipo de imposto com o status **Retido**.

#### 2. Configuração e conferência do PIS/COFINS de apuração própria

Os impostos de Apuração Própria são os valores devidos pelo prestador do serviço que já compõem a operação de forma direta. O sistema os agrupa em uma tag específica do XML/JSON chamada `pisCofinsApuracaoPropria`.

**Como configurar:** estes valores são calculados com base nas configurações regulares efetuadas no cadastro de suas respectivas alíquotas (Comercial > Arquivo > Cadastros > Alíquotas > [Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS) / [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS)).

**Como conferir na emissão da nota:** durante a digitação da nota na Central, você pode checar os valores que serão enviados como apuração própria:

1. Selecione a nota e o item do serviço.
2. Clique no botão **Outras Opções...** e acesse [**Consultar/Alterar Dados do Imposto do Item**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974-Central-de-Compras-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#consultaralterardadosdoimpostodoitem).

Os valores calculados e apresentados neste pop-up são os que o sistema considerará automaticamente para preencher os campos **"Pis Apuração Própria"** e **"Cofins Apuração Própria"** na comunicação com o Gateway de notas da prefeitura.
