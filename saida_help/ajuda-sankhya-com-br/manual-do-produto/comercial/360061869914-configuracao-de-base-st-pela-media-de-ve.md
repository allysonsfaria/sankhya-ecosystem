---
id: "360061869914"
titulo: "Configuração de base ST pela média de venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:34:52Z"
rotulos: ["Produtos", "Configuração", "ICMS", "Impostos", "TOP", "Venda", "br.com.sankhya.mgecom.base.st.media.venda", "Configuração de Base ST: Rotina Média Venda", "Rotina", "Média", "Comercial"]
---

# Configuração de base ST pela média de venda

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312190185495) Módulo: Comercial > Rotinas            ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42312177009687) Versão disponível: A partir da 4.5
```

---

Através dessa tela, você configura uma rotina para obtenção do preço médio de venda (Venda = Valor total - Vlr Desc) por um determinado período, sendo este a ser utilizado em operação configurável como preço de referência (produto), para aplicar as regras de obtenção da Base de Cálculo do ICMS-ST em operações aqui configuradas.

Para verificar de forma mais fácil sobre as funcionalidades dessa tela, acesse os links abaixo:

[Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#painelprincipal)                                                                           [Aba Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#abaempresas)

[Aba Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#abaparceiros)                                                                              [Aba TOP's](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#abatop's)

[Aba Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#abaprodutos)                                                                              [Botões Processar e Reprocessar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#bot%C3%B5esprocessarereprocessar)

![Imagem 3: Aba Produtos Botões Processar e Reprocessar](https://ajuda.sankhya.com.br/hc/article_attachments/1500003465642)

## Painel Principal

Ao iniciar um cadastro nessa tela, você deverá preencher alguns campos, sendo eles:

O campo **"Nro. Único"** pode ser de preenchimento automático ou manual. Você pode fazer essa escolha através do botão **"Configuração da Tela"**, opção **"Numeração"**.

Informe a **"Dt. Alteração"** da configuração, bem como se ela está apta ou não para utilização, por meio da marcação **"Ativo"**.

A marcação **"Executa processamento automático"**, quando realizada, define que o processamento será realizado automaticamente pelo sistema.

**Observação:** Esse processamento será executado pelo job às 00:10 do dia 01 de qualquer mês e ano.

No campo **"Lista de produtos a serem desconsiderados"** você informa os produtos (separados por vírgula) que deseja desconsiderar para fazer o cálculo do valor médio de venda.

Para as marcações **"Subst. na compra e na venda (Cálculo na Compra e na Venda)"**, **"Venda com subst. tributária (Cálculo de Subst. na Venda)"**, **"Revenda com subst. tributária (Cálculo de Subst. na Compra)"**, serão observadas a regra de prioridade existente ao lançar um item em uma nota, ou seja, verificando as configurações do campo **"Tipo de substituição"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), das abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos) e [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa).

**Importante:** Também será verificado para as marcações acima, se o parâmetro **"Usa imposto de produtos por empresa ? - EMPPRODIMPOST"** está ligado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#top)

## Aba Empresas

Nessa aba, selecione a(s) Empresa(s) que farão parte do cálculo da média.

**Observação:** Para incluir uma empresa nessa aba, ela deve estar com a marcação **"Usa valor médio de venda nas transferências entre empresas do mesmo grupo"** ([Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageral)) habilitada.

![Imagem 4: Observação: Para incluir uma empresa nessa aba, ela deve estar com a marcação "Usa valor médio de venda nas…](https://ajuda.sankhya.com.br/hc/article_attachments/360104528713)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#top)

## Aba Parceiros

Aqui, informe os Parceiros Destinatários que serão considerados para o cálculo do valor médio de venda na obtenção da base de cálculo ICMS-ST.

![Imagem 5: Aqui, informe os Parceiros Destinatários que serão considerados para o cálculo do valor médio de venda na obtenção da…](https://ajuda.sankhya.com.br/hc/article_attachments/360104530693)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#top)

## Aba TOP's

Selecione nessa aba, os Tipos de Operação - TOP que serão considerados para a busca dos movimentos de venda dos produtos. Aqui serão exibidas apenas as TOP's com Tipo de Movimento igual à **"V-Venda"**.

![Imagem 6: Selecione nessa aba, os Tipos de Operação - TOP que serão considerados para a busca dos movimentos de venda dos…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003484902)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#top)

## Aba Produtos

Nessa aba serão exibidos todos os produtos que estão ativos e que passam pelos filtros do campo Lista de produtos a serem desconsiderados e das marcações Subst. na compra e na venda (Cálculo na Compra e na Venda), Venda com subst. tributária (Cálculo de Subst. na Venda) e Revenda com subst. tributária (Cálculo de Subst. na Compra) do [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#painelprincipal).

![Imagem 7: Nessa aba serão exibidos todos os produtos que estão ativos e que passam pelos filtros do campo Lista de produtos a…](https://ajuda.sankhya.com.br/hc/article_attachments/360104528813)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#top)

## Botões Processar e Reprocessar

No topo dessa tela existem alguns botões importantes. Dentre eles, temos:

O botão ![Imagem 8: O botão "Processar" , quando acionado, realizará todo o cálculo solicitado. Ao executar essa ação, você será informado…](https://ajuda.sankhya.com.br/hc/article_attachments/16082110695063) **"Processar"**, quando acionado, realizará todo o cálculo solicitado. Ao executar essa ação, você será informado que essa operação pode demorar; assim, você decide se deseja confirmar a execução do processamento.

**Nota:** Para esse processamento, é necessário que você informe a data de referência que o cálculo deve ser feito, sendo que, somente é possível informar o mês atual ou anteriores.

**Observação:** Caso já exista um processamento, serão deletados todos os dados e processados novamente.

Quando você acionar o botão ![Imagem 9: Quando você acionar o botão "Reprocessar" , fará com que seja refeito o cálculo, caso tenha sido alterada alguma…](https://ajuda.sankhya.com.br/hc/article_attachments/16082115705111) **"Reprocessar"**, fará com que seja refeito o cálculo, caso tenha sido alterada alguma configuração dessa tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869914-Configura%C3%A7%C3%A3o-de-base-ST-pela-m%C3%A9dia-de-venda#top)

Acesse também:

[Média de preços de venda por Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003268941-M%C3%A9dia-de-pre%C3%A7os-de-venda-por-Produto)
