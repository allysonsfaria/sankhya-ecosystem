---
id: "44011052763927"
titulo: "&nbsp;Como definir o preço de custo que será utilizado do ERP Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011052763927--nbsp-Como-definir-o-pre%C3%A7o-de-custo-que-ser%C3%A1-utilizado-do-ERP-Sankhya"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:54:02Z"
rotulos: ["sync_hc", "magis5", "sync_hash_a910c3ef7ec5", "magis5_206308485641"]
---

# &nbsp;Como definir o preço de custo que será utilizado do ERP Sankhya

## Entenda, neste artigo, como escolher o campo de custo do ERP Sankhya que será utilizado como base para a precificação automática dos anúncios no Magis5 HUB

![Imagem 1: Entenda, neste artigo, como escolher o campo de custo do ERP Sankhya que será utilizado como base para a precificação…](https://ajuda.sankhya.com.br/hc/article_attachments/44011036494999)[![Imagem 2: Entenda, neste artigo, como escolher o campo de custo do ERP Sankhya que será utilizado como base para a precificação…](https://ajuda.sankhya.com.br/hc/article_attachments/44011048006935)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#produtos-e-an%C3%BAncios)[![Imagem 3: Entenda, neste artigo, como escolher o campo de custo do ERP Sankhya que será utilizado como base para a precificação…](https://ajuda.sankhya.com.br/hc/article_attachments/44011063971863)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#estoque)[![Imagem 4: Entenda, neste artigo, como escolher o campo de custo do ERP Sankhya que será utilizado como base para a precificação…](https://ajuda.sankhya.com.br/hc/article_attachments/44011053268503)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#pedidos)[![https://ajuda.magis5.com.br/magis5-hub#expedi%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/article_attachments/44011032283543)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#expedi%C3%A7%C3%A3o)[![Imagem 6: Entenda, neste artigo, como escolher o campo de custo do ERP Sankhya que será utilizado como base para a precificação…](https://ajuda.sankhya.com.br/hc/article_attachments/44011064306711)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#financeiro)[![Imagem 7: Entenda, neste artigo, como escolher o campo de custo do ERP Sankhya que será utilizado como base para a precificação…](https://ajuda.sankhya.com.br/hc/article_attachments/44011053611671)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#configura%C3%A7%C3%B5es)

---

O Magis5 HUB possui uma funcionalidade de precificação automática que ajusta os preços dos anúncios conforme cada marketplace, respeitando as margens de cada canal de venda. O cálculo é feito a partir do custo do produto informado pelo ERP, e esse valor não pode ser alterado diretamente no Magis5 HUB. ([Entenda mais sobre precificação clicando aqui](https://ajuda.sankhya.com.br/produtos/precifica%C3%A7%C3%A3o-autom%C3%A1tica/configura%C3%A7%C3%A3o-margens-e-custos).)

Atualmente, o ERP Sankhya disponibiliza os seguintes tipos de custo:

- **Custo Gerencial**
- **Custo Médio Gerencial**
- **Custo Médio Calculado**
- **Custo Médio com ICMS**
- **Custo de Reposição**
- **Custo Médio sem ICMS**
- **Custo Variável**

### Como definir o preço de custo no Magis5 utilizando o ERP Sankhya

Feito login no Magis5 HUB vá em **"Configurações"**, **"Integrações"** e por fim **"ERPs e Faturador"**

![Captura de tela 2026-01-29 150628](https://ajuda.sankhya.com.br/hc/article_attachments/44011064470551)

Na tela de **ERPs e Faturador** edite o Sankhya principal (o que contem o símbolo de estrela na frente)

![Imagem 9: Na tela de ERPs e Faturador edite o Sankhya principal (o que contem o símbolo de estrela na frente)](https://ajuda.sankhya.com.br/hc/article_attachments/44011064583575)

![Imagem 10: Na tela de ERPs e Faturador edite o Sankhya principal (o que contem o símbolo de estrela na frente)](https://ajuda.sankhya.com.br/hc/article_attachments/44011048805655)

Quando a opção **“ERP principal”** estiver selecionada, será exibida outra configuração chamada **“Preço de Custo Somente Nesta Empresa”.

![Imagem 11: Quando a opção “ERP principal” estiver selecionada, será exibida outra configuração chamada “Preço de Custo Somente…](https://ajuda.sankhya.com.br/hc/article_attachments/44011037310359)

💡Essa opção define se o custo utilizado será o último custo gerencial atualizado, válido para todas as empresas, ou se será específico para cada empresa (CNPJ).**

O Sankhya permite cadastrar várias empresas no mesmo ambiente, cada uma com um CNPJ diferente, e cada empresa pode ter **custos distintos para o mesmo produto**.

Ao ativar a opção **“Preço de Custo Somente Nesta Empresa”**, o sistema exibirá um **campo de seleção** com os tipos de custo retornados pelo Sankhya, [conforme listados acima.

![Captura de tela 2026-01-30 125125](https://ajuda.sankhya.com.br/hc/article_attachments/44011064853911)](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011052763927--nbsp-Como-definir-o-pre%C3%A7o-de-custo-que-ser%C3%A1-utilizado-do-ERP-Sankhya#custo)

O campo **Custo Gerencial** virá pré-selecionado como padrão, mas, se desejar, é possível escolher outro tipo de custo.
Após a seleção de um campo diferente do padrão, as próximas consultas de custo passarão a considerar o tipo de custo escolhido.

⚠️ Ao editar a integração do ERP Sankhya, o botão **“Importar produtos”**, quando utilizado após a alteração do tipo de custo, já importará os custos dos produtos considerando a opção selecionada.

![Imagem 13: ⚠️ Ao editar a integração do ERP Sankhya, o botão “Importar produtos” , quando utilizado após a alteração do tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/44011054237847)
