---
id: "360044469273"
titulo: "Cadastro de produtos pede para calcular substituição tributária, mas a 'Tributação' do cadastro de alíquotas de ICMS não foi configurado adequadamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044469273-Cadastro-de-produtos-pede-para-calcular-substitui%C3%A7%C3%A3o-tribut%C3%A1ria-mas-a-Tributa%C3%A7%C3%A3o-do-cadastro-de-al%C3%ADquotas-de-ICMS-n%C3%A3o-foi-configurado-adequadamente"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:57:15Z"
rotulos: ["Produtos", "CORE_E04481", "Configuração", "ICMS", "Impostos", "Substituição Tributária", "Alíquotas de ICMS", "Configuração incorreta do ICMS-ST", "Problema com ICMS-ST em produtos", "Configure corretamente \"AVISACODTRIBERR\""]
---

# Cadastro de produtos pede para calcular substituição tributária, mas a 'Tributação' do cadastro de alíquotas de ICMS não foi configurado adequadamente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17124800951447) MENSAGEM:**

[CORE\_E04481]  Cadastro de produtos pede para calcular substituição tributária, mas a 'Tributação' do cadastro de alíquotas de ICMS não foi configurado adequadamente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17124800953495) SOLUÇÃO:**

Esse aviso será apresentado quando o parâmetro abaixo for definido como ligado, na tela **"Preferências".** Lembrando que ele impede que o lançamento seja feito em discordância.

- **"AVISACODTRIBERR- Avisar qdo Prod.marcado subst.trib.e conf.s/subs?":** com o parâmetro ligado, o sistema emite mensagem de eventuais divergências no cálculo de ICMS-ST, caso haja discordância entre o cadastro de Produto e Alíquota de ST.

Ocorre quando a configuração do campo **"Tipo de substituição"** do cadastro de produtos tem a marcação para calcular ST e na exceção de ICMS do lançamento não tem as configurações para cálculo de ST.

Para revisa/ajustar a divergência reportada pelo aviso, revise as configurações conforme detalhado abaixo, solicitando ao Contador da empresa apoio para definição correta das respectivas informações fiscais:

![Imagem 3: Tela "Produtos" (Caminho de acesso: Configurações » Cadastros), aba "Impostos", campo "Tipo de Substituição":](https://ajuda.sankhya.com.br/hc/article_attachments/17124812977943) Tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros), aba **"Impostos",** campo **"Tipo de Substituição":**

- **Substituição na Compra e Venda:** quando o produto é configurado com esta opção, significa que a existência de "ST" irá depender das configurações de alíquotas de ICMS, ou seja, depende das UF's de origem e de destino envolvidas. Esta opção é a mais habitualmente empregada, sendo acionada, portanto, quando a abrangência da aplicação da ST não envolve todas as UF's para as quais a empresa vende ou quando existe mais de uma empresa em UF's diferentes e a definição de ST na compra for diferente para cada uma delas.
- **Venda com Substituição Tributária (ST na Venda):** Esta opção deve ser selecionada para produtos sujeitos à ST nas saídas da empresa. Por exemplo, nas indústrias para os seus produtos acabados, sujeitos à Substituição Tributária nas vendas.
- **Revenda com Substituição Tributária (ST na Compra):**esta opção informa que o produto possui ST na Compra e consequentemente nunca na venda. Deste modo, seleciona-se esta opção para produtos com abrangência da ST Nacional ou que alcance todos os estados para os quais a empresa vende ou pretende vender seus produtos. Quando esta opção estiver marcada, o sistema irá calcular o ICMS cobrado anteriormente por substituição nas saídas deste produto, não havendo o destaque do imposto para qualquer que seja o destino da mercadoria. Outro ponto a se destacar é que produtos que utilizem esta opção devem conter um tratamento diferente na apuração de custos, pois pode-se garantir que o custo do produto possui o ICMS embutido, visto que na venda não haverá o débito de ICMS.
- **Não tem:** os produtos que não estão sujeitos à substituição devem estar com esta opção selecionada. É importante salientar que mesmo quando existir a configuração de alíquotas de ICMS apontando que deverá haver o cálculo da ST, se o produto estiver com esta opção selecionada não haverá o cálculo da Substituição.

![Imagem 4: Tela "Alíquotas de ICMS" (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas), aba "Substituição Tributária"](https://ajuda.sankhya.com.br/hc/article_attachments/17124812980119) Tela **"Alíquotas de ICMS"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas), aba **"Substituição Tributária"**

Caso para o item 1 seja definido que a incidência de ST deverá ocorrer, localize a exceção de ICMS que está sendo buscada e realize as configurações na aba **"Substituição Tributária"**, conforme informações fornecidas pela Contabilidade.

Para mais detalhes de como localizar a exceção de ICMS buscada, verifique o artigo [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360024578573)

![Imagem 5: Após os ajustes, refaça o lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/17124800963735) Após os ajustes, refaça o lançamento.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17124812986007) CAUSA:**

Ocorre quando a configuração do campo Tipo de substituição, do cadastro de produtos, tem a marcação para calcular ST e na exceção de ICMS do lançamento não tem as configurações para cálculo de ST.
