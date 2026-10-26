---
id: "43546792733719"
titulo: "Como identificar e corrigir divergências no CST de IPI ao consultar impostos do item?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546792733719-Como-identificar-e-corrigir-diverg%C3%AAncias-no-CST-de-IPI-ao-consultar-impostos-do-item"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-10-09T21:23:11Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Como identificar e corrigir divergências no CST de IPI ao consultar impostos do item?

A divergência no CST de IPI durante a consulta de impostos do item pode gerar inconsistências fiscais e rejeições na emissão de notas fiscais eletrônicas. Esse cenário ocorre, principalmente, quando o CST de IPI apresentado na tela de consulta de impostos do item não corresponde ao esperado para a operação, seja por configuração incorreta nos cadastros ou por parametrizações inadequadas nas telas envolvidas no cálculo do imposto.

Para garantir a correta apuração e escrituração do IPI, é fundamental que o CST de IPI esteja devidamente configurado nos cadastros de produtos, parceiros e tipos de operação (TOP), além de observar as parametrizações específicas que influenciam o cálculo e a exibição do imposto. A seguir, veja como identificar e corrigir essas divergências.

### Principais causas da divergência

A divergência no CST de IPI pode ocorrer por diferentes motivos, como:

- **Configuração incorreta do CST de IPI** no cadastro do produto (Configurações Cadastros Produtos), especialmente nos campos **"Cód. Sit. Trib. IPI Saída"** e **"Cód. Sit. Trib. IPI Entrada"**.
- **Ausência ou erro na configuração do CST de IPI** no cadastro do parceiro (Configurações Cadastros Parceiros), aba Fiscal.
- **Parâmetros da TOP** (Configurações Cadastros Tipos de Operação - TOP) definidos de forma inadequada, como o campo **"Cálculo de ICMS, IPI, ISS, IBS, CBS e IS"** configurado para **"Não calcula e digita"**, o que pode resultar em CST de IPI em branco ou divergente.
- O parâmetro **PADCSTIPITOPNCD** é apresentado desativado por padrão. Ao ativá-lo, quando a TOP estiver configurada com o campo **Cálculo de ICMS, IPI e ISS** definido como **Não calcula e digita**, e o sistema não conseguir determinar o CST de IPI por meio das configurações existentes, serão utilizados os dados de **CST de IPI informados na TOP como padrão**.
  - **Observação:** para que o parâmetro funcione corretamente, é necessário que o campo **Tem IPI na compra?**, disponível na tela **Cadastro de Produtos**, aba **Impostos**, seção **IPI**, esteja ativado.

Além disso, divergências podem ser percebidas ao importar XMLs de notas fiscais, quando o CST de IPI do XML não corresponde ao configurado no sistema, ou em operações de devolução, quando o CST de IPI da nota de origem não é corretamente replicado.

### Como identificar e corrigir a divergência

Para identificar e corrigir a divergência no CST de IPI, siga o passo a passo:

**(1)** Acesse a tela **"Produtos"** (Configurações Cadastros Produtos), aba **"Impostos"**, e confira se os campos **"Tem IPI na venda"**, **"Tem IPI na compra"**, **"Cód. Sit. Trib. IPI Saída"** e **"Cód. Sit. Trib. IPI Entrada"** estão preenchidos corretamente conforme orientação fiscal.

**(2)** Verifique o cadastro do parceiro na tela **"Parceiros"** (Configurações Cadastros Parceiros), aba **"Fiscal"**, e ajuste o campo **"Cód. Sit. Trib. IPI Saída"** conforme necessário.

**(3)** Na tela **"Tipos de Operação - TOP"** (Configurações Cadastros Tipos de Operação - TOP), aba **"Impostos"**, confira se o campo **"Cálculo de ICMS, IPI, ISS, IBS, CBS e IS"** está configurado para **"Calcula e não digita"** ou **"Calcula e digita"**, conforme o processo desejado. Evite deixar como **"Não calcula e digita"** se deseja que o sistema calcule e sugira o CST de IPI automaticamente.

**(4)** Se necessário, ative o parâmetro **"Padrão CST.IPI pela TOP com Não Calcula e Digita? - PADCSTIPITOPNCD"** para que o sistema utilize o CST de IPI padrão da TOP quando não encontrar configuração adequada.

**(5)** Ao consultar ou alterar os dados do imposto do item (Central de Vendas/Compras Grade Itens Outras Opções Consultar/Alterar Dados do Imposto do Item), confira se o CST de IPI apresentado corresponde ao esperado. Caso necessário, ajuste manualmente, desde que a TOP permita edição.

Após os ajustes, gere novamente a nota fiscal e valide se o CST de IPI está correto tanto na tela quanto no XML gerado.

### Boas práticas para evitar divergências

Para evitar recorrência de divergências no CST de IPI:

- Mantenha sempre atualizados os cadastros de produtos, parceiros e TOPs, conforme orientação do contador.
- Realize conferências periódicas nas notas fiscais emitidas, especialmente em operações de devolução e importação de XMLs.
- Evite utilizar a configuração **"Não calcula e digita"** em TOPs de venda, salvo quando for realmente necessário digitar manualmente todos os impostos.
- Consulte a área fiscal para definir corretamente os CSTs de IPI aplicáveis a cada operação.

Seguindo essas orientações, é possível garantir a correta apuração do IPI e evitar rejeições fiscais por divergência de CST.
