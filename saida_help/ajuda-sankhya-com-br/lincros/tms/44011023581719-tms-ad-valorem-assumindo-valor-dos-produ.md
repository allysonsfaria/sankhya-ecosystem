---
id: "44011023581719"
titulo: "[TMS] Ad Valorem assumindo valor dos produtos e não da Nota Fiscal."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011023581719--TMS-Ad-Valorem-assumindo-valor-dos-produtos-e-n%C3%A3o-da-Nota-Fiscal"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T18:53:26Z"
rotulos: ["sync_hc", "lincros", "lincros_13439823", "sync_hash_7dd506fc791d"]
---

# [TMS] Ad Valorem assumindo valor dos produtos e não da Nota Fiscal.

**Menu**: Documentos eletrônicos > NF-es
**Objetivo**: Entender por que o pré-conhecimento de uma NF-e está levando em conta o valor dos produtos e não o valor da NF-e.

## Considerações:

- Ter uma NF-e importada no TMS onde a sua modalidade é diferente de 9 (Sem frete) para que então, seja criado um pré-conhecimento para a NF-e no momento da sua importação.

Em uma Auditoria de frete é comum fazer o uso do componente de frete Ad Valorem, onde, naturalmente esse componente deve usar como base de cálculo o valor da NF-e, porém pode acontecer em alguma situações onde ao invés de usar o valor da NF-e ser usado o valor dos produtos. Para exemplificar vamos usar um exemplo pratico para mais fácil visualização. No exemplo abaixo temos um pé-conhecimento onde o componente Ad Valorem recebe um valor de 1,50 % resultando em R$ 646,15, porém esse calculo foi feito em cima do valor dos produtos e não da mercadoria.

Exemplificando, no pré-conhecimento:

![Imagem 1: Exemplificando, no pré-conhecimento:](https://ajuda.sankhya.com.br/hc/article_attachments/44011023796375)

Na NF-e o valor dos produtos é de R$ 43.076,42:

![Imagem 2: Na NF-e o valor dos produtos é de R$ 43.076,42:](https://ajuda.sankhya.com.br/hc/article_attachments/44011044390423)

Com isso temos o cálculo de R$ 43.076,42 X 1,50% do componente Ad Valorem = R$ 646,15.

Esse comportamento se deve a NF-e estar configurada para fazer a substituição tributária, podemos validar isso dentro da NF-e na aba Fiscal/Contábil:

![Imagem 3: Esse comportamento se deve a NF-e estar configurada para fazer a substituição tributária, podemos validar isso dentro…](https://ajuda.sankhya.com.br/hc/article_attachments/44011033597975)

Essa configuração é feito quando dentro do XML da NF-e a tag <vST> receber um valor maior que zero, exemplificando essa configuração do XML podemos observar ela no print abaixo:

![Imagem 4: Essa configuração é feito quando dentro do XML da NF-e a tag <vST> receber um valor maior que zero, exemplificando essa…](https://ajuda.sankhya.com.br/hc/article_attachments/44011033730839)

Essa modificação de "Sim" para "Não" pode ser feita dentro da NF-e selecionando ao invés "Sim" selecionar "Não" conforme o print abaixo:

![Imagem 5: Essa modificação de "Sim" para "Não" pode ser feita dentro da NF-e selecionando ao invés "Sim" selecionar "Não"…](https://ajuda.sankhya.com.br/hc/article_attachments/44011024413335)

Após alterar para "Não" e salvar a NF-e e recalcular o pré-conhecimento o componente Ad Valorem passou a levar em consideração o valor da NF-e para o calculo do Ad Valorem, conforme print abaixo:

![Imagem 6: Após alterar para "Não" e salvar a NF-e e recalcular o pré-conhecimento o componente Ad Valorem passou a levar em…](https://ajuda.sankhya.com.br/hc/article_attachments/44011050065943)

Existe um outro cenário a onde pode ser da vontade da transportadora ou do embarcador de realizar o calculo de ad valorem não sobre o valor da NF-e mas sim dos produtos dessa NF-e, para isso, o TMS da Lincros possui um parâmetro de empresa denominado 'calcularIST' que quando ativado e caso a NF-e estiver fazendo a substituição tributária (substituição tributária = Sim) o TMS realizará o cálculo do ad valorem sobre os valores de produto da NF-e.

Caso seja necessário que esse comportamento ocorra apenas para uma transportadora ou determinadas transportadoras é necessário manter o parâmetro citado acima desativado, manter a substituição tributaria marcada como Sim na NF-e e no cadastrado da transportadora empresa Cadastros gerais > Transportadoras > Transportadora (empresa) > Cadastro marcar a flag "Permitir calcular IST":

![Imagem 7: Existe um outro cenário a onde pode ser da vontade da transportadora ou do embarcador de realizar o calculo de ad…](https://ajuda.sankhya.com.br/hc/article_attachments/44011029604759)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
