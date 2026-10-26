---
id: "44013484182807"
titulo: "[TMS] - Como Configurar Arredondamento de Peso em Tabelas de Frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013484182807--TMS-Como-Configurar-Arredondamento-de-Peso-em-Tabelas-de-Frete"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:58:53Z"
rotulos: ["sync_hc", "lincros", "lincros_13432380", "sync_hash_f2667c2b0288"]
---

# [TMS] - Como Configurar Arredondamento de Peso em Tabelas de Frete

**1 - Problema Relatado pelo Cliente:**
O cliente relatou que a transportadora sempre realiza o arredondamento do peso para cima, o que impacta na cobrança e Auditoria de Fretes. Como exemplo, um peso de 27,0167 kg é considerado como 28 kg na cobrança. O cliente deseja aplicar essa lógica de arredondamento automático no sistema, e esse artigo mostra como o cliente pode configurar um arredondamento de peso tanto para cima quanto para baixo.

## 2 - Passo a Passo para Resolver o Problema:

Para configurar o arredondamento do peso de forma que ele sempre seja arredondado para cima ou para baixo, você pode utilizar três componentes na Tabela de Fretes do TMS. Veja abaixo como essa configuração funciona:

1. ## Acessar a tabela de fretes e navegar em "Generalidade":

   - Navegue até Cadastros gerais > Transportadoras > Negociações > Tabelas de frete
   - Acesse a aba "Generalidade" e adicione os componentes que serão mencionados abaixo em sequencia.
2. ## Habilitação dos componentes:

   - Caso algum dos componentes mencionados abaixo não esteja disponível na sua interface, será necessário solicitar a habilitação deles via chamado com o Suporte da Lincros.
3. ## Ativando o componente "Formato do Peso":

   - O componente **formatoPeso** precisa estar configurado com o valor `POR_QUILO_FRACAO`.
   - Esse formato permite que o sistema reconheça frações de quilo e as trate conforme a configuração de arredondamento.
   - ![Imagem 1: Esse formato permite que o sistema reconheça frações de quilo e as trate conforme a configuração de arredondamento.](https://ajuda.sankhya.com.br/hc/article_attachments/44013484330519)
4. ## Configurando o arredondamento do peso:

   - Em seguida, adicione o componente **formatoArredondamento**.
   - Neste campo, é necessário definir se o peso será arredondado para cima ou para baixo.
   - Para o caso apresentado, o valor correto a ser configurado é arredondar `PARA CIMA`.
   - ![Imagem 2: Para o caso apresentado, o valor correto a ser configurado é arredondar PARA CIMA .](https://ajuda.sankhya.com.br/hc/article_attachments/44013471650199)
5. ## Definindo a máscara de exibição do peso:

   - Por fim, inclua e configure o componente **mascaraArredondamento** com a máscara `####,##`.
   - Essa configuração garante a exibição adequada do valor do peso, mantendo duas casas decimais após a vírgula.
   - ![Imagem 3: Essa configuração garante a exibição adequada do valor do peso, mantendo duas casas decimais após a vírgula.](https://ajuda.sankhya.com.br/hc/article_attachments/44013484506647)
6. ## Exemplo de um arredondamento para cima, em uma tabela de frete:

   - ![Imagem 4: Exemplo de um arredondamento para cima, em uma tabela de frete:](https://ajuda.sankhya.com.br/hc/article_attachments/44013484624919)

**3 - Resumo do Artigo:**
Este artigo orienta como configurar o sistema para que o peso de uma Nota Fiscal, Pré-conhecimento ou CT-e seja sempre arredondado para cima no cálculo do frete. A configuração é feita por meio dos componentes `formatoPeso`, `formatoArredondamento` e `mascaraArredondamento`. Caso os componentes não estejam visíveis, deve ser aberto um chamado com o time de Suporte da Lincros para habilitá-los.
