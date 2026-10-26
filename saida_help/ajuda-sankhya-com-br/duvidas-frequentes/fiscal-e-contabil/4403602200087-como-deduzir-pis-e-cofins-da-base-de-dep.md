---
id: "4403602200087"
titulo: "Como deduzir PIS e COFINS da base de depreciação?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403602200087-Como-deduzir-PIS-e-COFINS-da-base-de-deprecia%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:23:46Z"
rotulos: ["Configuração", "COFINS", "PIS", "Impostos", "Estoque", "Preferências", "#validadoThiagoArantes", "Deduzir PIS e COFINS", "Imobilizado PIS COFINS", "Imobilizado Grupo PIS/COFINS"]
---

# Como deduzir PIS e COFINS da base de depreciação?

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16345243019415) SOLUÇÃO:**

![Imagem 2: Primeiro é ter uma TOP de imobilizado. No exemplo do teste foi uma nota de compra de Imobilizado.](https://ajuda.sankhya.com.br/hc/article_attachments/16345243021975) Primeiro é ter uma TOP de imobilizado. No exemplo do teste foi uma nota de compra de Imobilizado.

Na aba estoque > campo Atualização do Bem: COMPRA

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15645720171799)

![Imagem 4: Na Aba "Impostos" faça as seguintes marcações - TEM PIS e TEM COFINS](https://ajuda.sankhya.com.br/hc/article_attachments/16345243024151) Na Aba **"Impostos"** faça as seguintes marcações - TEM PIS e TEM COFINS

![Imagem 5: Na Aba "Impostos" faça as seguintes marcações - TEM PIS e TEM COFINS](https://ajuda.sankhya.com.br/hc/article_attachments/15081854752407)

![Imagem 6: No cadastro do produto sinalize o mesmo como Imobilizado.](https://ajuda.sankhya.com.br/hc/article_attachments/16345243026327) No cadastro do produto sinalize o mesmo como Imobilizado.

Aba **"Geral"**, campo **"Usado como"**: Imobilizado

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15645791649943)

![Imagem 8: Na aba Imposto (do cadastro de produtos), Campos "Grupo PIS" e "Grupo Cofins" configure com o grupo de PIS e COFINS com…](https://ajuda.sankhya.com.br/hc/article_attachments/16345243027479) Na aba Imposto (do cadastro de produtos), Campos **"Grupo PIS"** e **"Grupo Cofins"** configure com o grupo de PIS e COFINS com as regras que fará calcular o PIS e COFINS na entrada do bem.

**Nota:** nos cadastros de alíquota de PIS e alíquota de COFINS devem ter as regras que serão responsáveis por fazer esse cálculo na nota.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15645750026519)

**OBSERVAÇÃO:**

O grupo de PIS ou GRUPO de COFINS é a configuração mais genérica que existe e deve-se ser assim para ser possível usar essas regras em outro cadastro de produtos, o que vai diferenciar e tornar a regra específica são as exceções feitas no cadastro delas. Seja por Empresa, por parceiro, ou por TOP. Se coloca uma regra e informa um código de TOP, toda vez que existir aquela TOP o sistema vai considerar aquela exceção.

Após essas configurações, ao lançar a nota e salvar o bem, o sistema abrirá uma tela para gerar o bem (isso acontece e deve ser feito antes de confirmar a nota, no momento em que salva o item na nota a tela já abre).

![Imagem 10: Após essas configurações, ao lançar a nota e salvar o bem, o sistema abrirá uma tela para gerar o bem (isso acontece e…](https://ajuda.sankhya.com.br/hc/article_attachments/15081847518487)

![Imagem 11: A partir desse clique em gerar bens automaticamente no botão "Outras opções" , o sistema irá gerar os bens de acordo…](https://ajuda.sankhya.com.br/hc/article_attachments/16345243033239) A partir desse clique em gerar bens automaticamente no botão **"Outras opções"**, o sistema irá gerar os bens de acordo com o que está na nota, assim clique em salvar na parte e lado direito da tela.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15645750028439)

Ao Salvar, o sistema retornará para a tela de lançamento da nota para confirmar a a nota.

Após confirmar a nota, é possível conferir o calculo de PIS e COFINS acessando no item o botão outras opções> Clicando em Consultar/Alterar dados do imposto.

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/15645750030231)

Os dados demonstrados serão os mesmos valores representados na Aba **"Tributos Recuperáveis"** da Sub aba **"Bens do cadastro do bem"**, no cadastro de produtos.

![Imagem 14: Os dados demonstrados serão os mesmos valores representados na Aba "Tributos Recuperáveis" da Sub aba "Bens do cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/15081835074199)

![Imagem 15: Para Gerar a depreciação deduzindo valor de PIS e COFINS, vá até as preferências da empresa (Comercial/preferências),…](https://ajuda.sankhya.com.br/hc/article_attachments/16345227653655) Para Gerar a depreciação deduzindo valor de PIS e COFINS, vá até as preferências da empresa (Comercial/preferências), aba **"Regime de Apuração da Contrib. Social e Aprop. Crédito"**, linha de **"Regime de apuração Vigente"** e marque o campo "**Excluir PIS/COFINS da base de Depreciação".**

![Imagem 16: Para Gerar a depreciação deduzindo valor de PIS e COFINS, vá até as preferências da empresa (Comercial/preferências),…](https://ajuda.sankhya.com.br/hc/article_attachments/15081868806935)
