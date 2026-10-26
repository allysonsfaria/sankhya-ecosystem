---
id: "37665306824471"
titulo: "Como definir tabelas de preço por perfil do parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37665306824471-Como-definir-tabelas-de-pre%C3%A7o-por-perfil-do-parceiro"
trilha: "Universidade Sankhya > Jornada de Precificação"
atualizado_em: "2026-07-22T14:11:38Z"
rotulos: ["Configuração", "Parceiro", "Preferências", "Comercial", "Tabelas de Preço"]
---

# Como definir tabelas de preço por perfil do parceiro

| Categoria |
| --- |
| [Qual é o objetivo de se definir a tabela de preços pelo perfil do parceiro?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665306824471-Como-definir-tabelas-de-pre%C3%A7o-por-perfil-do-parceiro#h_01KEY7NY8P1TZN4B3GB4FT8PW8) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665306824471-Como-definir-tabelas-de-pre%C3%A7o-por-perfil-do-parceiro#h_01KEY7NY8S7E7H3ZCDZZTVMGVD) |
| [Quais os riscos de não utilizar uma tabela de preço por perfil do parceiro?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665306824471-Como-definir-tabelas-de-pre%C3%A7o-por-perfil-do-parceiro#h_01KEY7NY91EWCBNZKSVEHDKHRC) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665306824471-Como-definir-tabelas-de-pre%C3%A7o-por-perfil-do-parceiro#h_01KFBQG80AXP79VVCTYSB31JCB) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665306824471-Como-definir-tabelas-de-pre%C3%A7o-por-perfil-do-parceiro#h_01KEY7S4QFHTHN3CZM3N9GYN5G) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665306824471-Como-definir-tabelas-de-pre%C3%A7o-por-perfil-do-parceiro#h_01KEY7PDSXH00CJH78M9N16090) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665306824471-Como-definir-tabelas-de-pre%C3%A7o-por-perfil-do-parceiro#h_01KEY7PDVTM41WNG42217DVV5C) |

## Definição de tabela de preço por perfil

#### Qual é o objetivo de se definir a tabela de preços pelo perfil do parceiro?

Definir a tabela de preços pelo perfil do parceiro serve para fazer com que o sistema aplique automaticamente a tabela certa para cada cliente, de acordo com seu perfil. Isso evita que a equipe precise escolher a tabela manualmente a cada venda. Por exemplo, você pode ter uma tabela para distribuidores, outra para varejistas e outra para consumidores finais. Assim, cada cliente vê o preço que realmente faz sentido para ele. Isso torna as negociações mais rápidas, os preços mais justos e o controle comercial mais eficiente.

#### Quais problemas este recurso resolve?

- Ausência de condições comerciais adaptadas a diferentes perfis de parceiros.
- Dificuldade em atender demandas específicas de segmentos variados do mercado.
- Relações comerciais pouco eficientes e com baixo nível de fidelização.
- Barreiras na conquista de novos clientes ou canais de venda.
- Negociações complexas e demoradas por falta de critérios padronizados.

#### Quais os riscos de não utilizar uma tabela de preço por perfil do parceiro?

Deixar de adotar uma tabela de preços segmentada por perfil pode comprometer a competitividade da empresa, uma vez que limita a personalização da oferta comercial. Isso pode gerar insatisfação entre os parceiros, especialmente os que esperam condições adequadas ao seu porte ou segmento, e dificultar a atração de novos clientes. Além disso, a ausência de uma estrutura clara de precificação aumenta a complexidade das negociações, consome tempo da equipe comercial e pode levar a decisões incoerentes, com impacto direto na margem de lucro e no alinhamento estratégico. A falta de padronização também enfraquece o relacionamento com o parceiro e prejudica a consistência das práticas comerciais.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052318696)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa Axis LTDA atende diversos tipos de clientes, incluindo pequenos varejistas, grandes distribuidores e supermercados. Cada grupo apresenta características distintas, como volume de compra, poder de negociação e expectativa de preços competitivos. Durante uma análise de mercado, a empresa acordou que a aplicação de uma tabela única de preços resultou em margens de lucro inconsistentes e dificuldades em atender às expectativas específicas de cada segmento de clientes. Os pequenos varejistas estavam insatisfeitos com os preços elevados em relação ao volume de compras, enquanto os grandes distribuidores exigiam condições comerciais mais agressivas. Para resolver essas questões, a empresa decidiu implementar tabelas de preços personalizadas com base no perfil dos parceiros.

**Tarefa**: Crie e configure, na sua base de testes, tabelas de preços segmentadas por perfil, conforme as orientações indicadas.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Tabelas de Preços** 
   Menu: Comercial » Arquivo » Tabelas de Preços

- Clique no botão “**+**” (**Cadastrar Cadastro de Tabela de Preço**).
- Informe um número de identificação no campo **Código**.
- Defina um nome para identificação no campo indicado (Ex. VAREJO).
- Clique em Salvar.

**Aba Histórico de atualizações**

- Informe o mesmo código definido acima no campo **Tabela de origem**
- Preencha os campos **Dt. Vigor** e **Dt. Alteração** com a data atual
- Clique em Salvar.

2. Acesse a tela **Preferências**
   Menu: Configurações » Avançado » Preferências

- Pesquise a chave **TIPTABPRECO** e tecle ENTER.
- Defina a opção **Perfil** no campo **Valor**.
- Clique em **Salvar**.

Após alterar o parâmetro acima, feche a tela de **Tabela de Preço** para que a alteração seja refletida e, em seguida, abra-a novamente.

3. Acesse a tela **Tabelas de Preços**
   Menu: Comercial » Arquivo » Tabelas de preços

- Ative o **Modo grade**.
- Localize a tabela de preço do perfil criada no passo 1.

**Aba Perfis**

- Informe os perfis de parceiro que obedecerão às regras desta tabela de preço.

**Aba Regras -** Sub aba de Histórico de Atualizações

Como se trata de uma tabela nova, com origem nela mesma, ainda não há histórico de preços para os produtos. Por isso, é necessário informar os valores que serão aplicados a cada item nesta tabela.

- Clique no botão “**+**” (**Cadastrar Exceção de Preço**).
- Informe o produto no campo indicado**.**
- Defina **Valor** no campo **Tipo**.
- Informe o preço do produto.
- Clique em **Salvar**.

4. Acesse a tela **Parceiros** 
   Menu: Configurações » Cadastros » Parceiros

**Aba Identificação**

- Vincule o perfil indicado à tabela criada, preenchendo o campo "**Perfil principal**". 
  Para que a tabela de preço criada seja aplicada, é necessário que o perfil informado no cadastro da tabela de preços esteja vinculado ao parceiro.
- Clique em **Salvar**.

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo novamente.
