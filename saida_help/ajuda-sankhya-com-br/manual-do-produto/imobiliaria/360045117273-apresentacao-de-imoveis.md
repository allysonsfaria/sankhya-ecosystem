---
id: "360045117273"
titulo: "Apresentação de Imóveis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis"
trilha: "Manual do Produto > Imobiliária > Imobiliária"
atualizado_em: "2026-07-29T14:08:41Z"
rotulos: ["Locação", "br.com.sankhya.tim.rotinas.apresentacao", "Vendas", "Visualização de mapa", "Seleção de imóveis", "Parâmetros configuráveis", "Imobiliária", "Prospecção", "Imóveis", "FAC"]
---

# Apresentação de Imóveis

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311358313879) Módulo: Imobiliária > Rotinas > Prospecção
![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311358315799) Versão disponível: a partir da 3.31
```

---

Por meio dessa tela, será possível selecionar os imóveis que atendam as necessidades do Prospect de forma rápida e objetiva. Essa rotina apresenta uma grande variedade de filtros para que a pesquisa se torne ágil, ampla e confiável.

| [FAC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#FAC) |  | [Marcações e botões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#marca%C3%A7%C3%B5esebot%C3%B5es) |
| --- | --- | --- |
| [Visualizar resultado no mapa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#visualizarresultadonomapa) |  | [Outros botões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#outrosbot%C3%B5es) |
| [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#par%C3%A2metrosqueinfluenciamnestarotina) |  |  |

## FAC

No topo dessa tela, tem-se o seguinte campo e botão relacionado à [FAC - Ficha de Atendimento ao Cliente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609334):

O campo **"FAC"** vinculará o atendimento em curso. Assim, será nesse atendimento que  serão vinculados os imóveis que o cliente manifestou interesse, assim como os registros das visitas e futuras propostas realizadas aos imóveis selecionados.

Ao acionar o botão **"Nova FAC"**, e em seguida o campo FAC, será aberto o seguinte pop-up para a inserção de um atendimento diretamente pela tela de [Apresentação de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273), sendo que, apenas as informações principais serão solicitadas:

[GIF animado: Imagem 3: Ao acionar o botão "Nova FAC" , e em seguida o campo FAC , será aberto o seguinte pop-up para a inserção de um…](https://ajuda.sankhya.com.br/hc/article_attachments/360061937353)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#top)

## Marcações e botões

O botão ![Imagem 4: O botão "Imprimir Termo de Entrega de Chaves" permite realizar a impressão da ficha de visita vinculada ao parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/360061017114) **"Imprimir Termo de Entrega de Chaves"** permite realizar a impressão da ficha de visita vinculada ao parâmetro **"Relatório Termo Saída Chaves - TIMNURFETERMO"**. Essa mesma ficha poderá ser impressa também pela tela FAC - Ficha de Atendimento ao Cliente.

Quando você selecionar a marcação **"Só desta FAC"**, será exibido apenas os imóveis que já foram vinculados ao atendimento informado no campo FAC.

Ao efetuar a marcação **"Locação"**, serão apresentados apenas os imóveis disponíveis para locação e, a marcação **"Venda"** exibirá somente os imóveis disponíveis para venda.

Por meio do botão **"Buscar"**, realize a busca dos imóveis de acordo com os filtros especificados.

Se você utilizar o botão **"Limpar"**, serão retornados os filtros da tela à seus valores padrão.

[GIF animado: Imagem 5: Se você utilizar o botão "Limpar" , serão retornados os filtros da tela à seus valores padrão.](https://ajuda.sankhya.com.br/hc/article_attachments/360061017134)

**Nota:** em cada item de imóveis da lista retornada, a descrição poderá ser personalizada utilizando a função **"TIM\_DESCRICAO\_IMOVELAP"** do Banco de Dados, que aceita como argumento o código do imóvel e retorna o texto da descrição.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#top)

## Visualizar resultado no mapa

Ao selecionar a marcação **"Visualizar resultado no mapa"**, o resultado da pesquisa será exibido em um mapa, com os imóveis resultantes da pesquisa representados por marcadores.

Quando você escolher um resultado, os imóveis próximos serão apresentados como bandeiras, sendo que estas irão variar entre a cor verde (valor de venda abaixo da avaliação) e vermelho (valor de venda acima da avaliação).

[GIF animado: Imagem 6: Quando você escolher um resultado, os imóveis próximos serão apresentados como bandeiras, sendo que estas irão variar…](https://ajuda.sankhya.com.br/hc/article_attachments/360061937373)

Nos detalhes do imóvel teremos as fotos vinculadas a ele, bem como, os dados de contato com o proprietário, a situação das chaves e quais foram os captadores.

**Observação:** em cada imóvel marcado no mapa, a descrição aberta ao clicar no marcador, poderá ser personalizada utilizando a função **"GET\_INFO\_IMOVEL\_MAPA"** do Banco de Dados, que aceita como argumento o código do imóvel e retorna o texto da descrição.

Ao acionar o marcador, os seguintes botões :

![Imagem 7: Adic. Interesse: Por meio desse botão, vincula-se o imóvel selecionado ao atendimento atual, esse vínculo permite que,…](https://ajuda.sankhya.com.br/hc/article_attachments/360061017154) **Adic. Interesse:** Por meio desse botão, vincula-se o imóvel selecionado ao atendimento atual, esse vínculo permite que, posteriormente, sejam feitas visitas e/ou propostas para o imóvel.

![Imagem 8: Adicionar Visita: Acionando esse botão, será solicitada uma visita para aquele imóvel, naquele atendimento; este…](https://ajuda.sankhya.com.br/hc/article_attachments/360061017174) **Adicionar Visita:** Acionando esse botão, será solicitada uma visita para aquele imóvel, naquele atendimento; este recurso executará a mesma ação da opção **"Solicitar Visita"** na [FAC - Ficha de Atendimento ao Cliente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609334), aba **"Imóveis da FAC"**, botão **"Ações..."**.

![Imagem 9: Cadastro de Imóveis: Esse botão, quando acionado, abrirá o Cadastro de Imóveis com o imóvel selecionado.](https://ajuda.sankhya.com.br/hc/article_attachments/360061937393) **Cadastro de Imóveis:** Esse botão, quando acionado, abrirá o [Cadastro de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608914) com o imóvel selecionado.

![Imagem 10: Ver mais: Quando você utilizar esse botão, será possível visualizar mais informações sobre o imóvel.](https://ajuda.sankhya.com.br/hc/article_attachments/360061017214) **Ver mais:** Quando você  utilizar esse botão, será possível visualizar mais informações sobre o imóvel.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#top)

## Outros botões

Ao selecionar um imóvel, será exibida uma tela com os detalhes do Imóvel e esta possui os seguintes botões no topo:

![Imagem 11: Inserir SAC: Esse botão abrirá a tela Inserir SAC , preenchendo os campos pertinentes ao atendimento no ato de inclusão…](https://ajuda.sankhya.com.br/hc/article_attachments/360061017234) **Inserir SAC:** Esse botão abrirá a tela [Inserir SAC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608894), preenchendo os campos pertinentes ao atendimento no ato de inclusão do registro.

![Imagem 12: SACs do Imóvel: Quando você utilizar esse botão, um pop-up com as SACs recentes lançadas para o imóvel selecionado.…](https://ajuda.sankhya.com.br/hc/article_attachments/360061017254) **SACs do Imóvel:** Quando você utilizar esse botão, um pop-up com as SACs recentes lançadas para o imóvel selecionado. Esse recurso será utilizado durante o atendimento, para uma consulta ao seu histórico, sendo possível visualizar os acompanhamentos inseridos pelos diversos setores da empresa que foram vinculados exclusivamente ao imóvel.

![Imagem 13: SAC Rápido: Ao acionar esse botão, será possível inserir uma SAC rápida , diretamente da tela de Apresentação de…](https://ajuda.sankhya.com.br/hc/article_attachments/360061017274) **SAC Rápido:** Ao acionar esse botão, será possível inserir uma SAC rápida, diretamente da tela de Apresentação de Imóveis. Esse recurso executa a mesma ação de **"Sac Rápido"** da FAC - Ficha de Atendimento ao Cliente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#top)

## Parâmetros que influenciam nesta rotina

Após a seleção, os imóveis que atendam ao filtro de busca, serão apresentados, por padrão, ordenados pela data de inclusão. Caso a administradora queira alterar esta ordenação, você poderá fazê-la por meio do parâmetro **"Ordenação do resultado na Apresentação de imóveis. - TIMORDERBYAP"**.

O parâmetro **"Oculta imovel Baixado Ap de Imoveis? - TIMOCULTBAAP"** definirá se os imóveis com **"Estágio"** igual a **"Baixado"** serão exibidos ou não na Apresentação de Imóveis.

Habilitando o parâmetro **"Controla Produto Apresentação de Imoveis? - TIMCTRLPROD"**, será necessário informar no [Cadastro dos Corretores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116973), se eles atuam em Venda, Locação ou em ambos e, a partir desta marcação, o sistema exibirá na [Apresentação de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273) apenas aqueles disponíveis para a área de atuação a qual o corretor encontra-se vinculado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117273-Apresenta%C3%A7%C3%A3o-de-Im%C3%B3veis#top)
