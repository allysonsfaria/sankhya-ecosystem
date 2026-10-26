---
id: "360056865874"
titulo: "Melhores Práticas e Configurações para Geração do Registro 53 - Sintegra - MGE/Mitra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056865874-Melhores-Pr%C3%A1ticas-e-Configura%C3%A7%C3%B5es-para-Gera%C3%A7%C3%A3o-do-Registro-53-Sintegra-MGE-Mitra"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:27:02Z"
rotulos: ["#criadoRoger", "Configuração", "MGE", "Impostos", "Sintegra", "Estoque", "GNRE", "Financeiro", "Definir e associar GNRE no financeiro", "Ajustar campos em MGE Configurações e Financeiro", "Marcar opções e gerar registros no MGE Estoque e Livros"]
---

# Melhores Práticas e Configurações para Geração do Registro 53 - Sintegra - MGE/Mitra

**Caso de Uso:**

A empresa possui uma 'Nota Fiscal de Compra', na qual o fornecedor não somou o ST no total, neste caso é preciso gerar um documento 'GNRE' e também uma despesa no financeiro referente ao ST. Para isto deve-se configurar no sistema.

**Outros artigos relacionados:**

- [Melhores Práticas para Configuração e Cálculo do Garantido Integral (GNRE - Compra).](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580314)
- [Associar autenticação do DAE e GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014)

**Vejamos as configurações que envolvem o processo:**

![Imagem 1: Acesse o MGE Configurações , Menu>>Arquivos>>Endereços>>UFs Campo: Parceiro Secretaria da Receita Estadual = (Preencher…](https://ajuda.sankhya.com.br/hc/article_attachments/16250296934423) Acesse o MGE Configurações, Menu>>Arquivos>>Endereços>>UFs
Campo: **Parceiro Secretaria da Receita Estadual** = [Preencher este com o código do parceiro, devidamente já cadastrado]
![Imagem 2: Acesse o MGE Configurações , Menu>>Arquivos>>Endereços>>UFs Campo: Parceiro Secretaria da Receita Estadual = (Preencher…](https://ajuda.sankhya.com.br/hc/article_attachments/360096534054)

![Imagem 3: Acesse o MGE Configurações , Menu>>Arquivos>>Endereços>>UFs Campo: Parceiro Secretaria da Receita Estadual = (Preencher…](https://ajuda.sankhya.com.br/hc/article_attachments/16250296936983) Acesse o MGE Financeiro, Menu>>Avançado>>Preferencias>>Empresa
Aba: Fiscal
Campo: Gerar GNRE p/ ST [marcado]

![Imagem 4: Acesse o MGE Configurações , Menu>>Arquivos>>Endereços>>UFs Campo: Parceiro Secretaria da Receita Estadual = (Preencher…](https://ajuda.sankhya.com.br/hc/article_attachments/360098849453)

Aba: Inscrição Estadual de Contribuinte Substituto Tributário no Estado Destinatário
Campo: Gerar GNRE p/ ST [marcado]

Preencher  Código e Descrição da UF e Inscrição Estadual.

![Imagem 5: Preencher Código e Descrição da UF e Inscrição Estadual.](https://ajuda.sankhya.com.br/hc/article_attachments/360096535454)

![Imagem 6: MGE Configurações, Financeiro ou Estoque, acesse a tela de Parâmetros em Avançado>>Preferencias>>Todas as Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16250276435095) MGE Configurações, Financeiro ou Estoque, acesse a tela de Parâmetros em Avançado>>Preferencias>>Todas as Preferências

Parâmetro TIPTITGNREST (TIPO DE TÍTULO da GNRE p/ST) - Informar neste parâmetro o código do '\*Tipo de Título', que será usado para a GNRE.

![Imagem 7: Parâmetro TIPTITGNREST (TIPO DE TÍTULO da GNRE p/ST) - Informar neste parâmetro o código do '*Tipo de Título', que será…](https://ajuda.sankhya.com.br/hc/article_attachments/360096535694)

\*O cadastro de Tipo de Título é acessado em **MGE Financeiro>>Arquivos>>Cadastros>>Tipos de Titulo>>Tipos de Titulo**

![Imagem 8: Acesse o MGE Financeiro, Menu>>Rotinas>>Associar Autenticação do Documento de Arrecadação](https://ajuda.sankhya.com.br/hc/article_attachments/16250296945303) Acesse o MGE Financeiro, Menu>>Rotinas>>Associar Autenticação do Documento de Arrecadação

Nesta tela apresentará os títulos que possuem o 'Tipo de Título' igual ao valor do parâmetro TIPTITGNREST e que tenham o campo 'Histórico' vazio.

Na parte superior, pode ser utilizado o filtro rápido por Empresa e/ou Parceiro.
Ao 'Aplicar', os títulos serão apresentados, para que seja digitado no histórico as informações da GNRE. Após as atualizações do histórico, ao aplicar, os títulos não serão apresentados novamente.

![Imagem 9: Na parte superior, pode ser utilizado o filtro rápido por Empresa e/ou Parceiro. Ao 'Aplicar', os títulos serão…](https://ajuda.sankhya.com.br/hc/article_attachments/16250276441495) Acesse o MGE Estoque, Menu>>Arquivos>>Produtos
Aba: Impostos
Campo: Produto constante no apêndice I do RCTE/GO = [marcado]

![Imagem 10: Na parte superior, pode ser utilizado o filtro rápido por Empresa e/ou Parceiro. Ao 'Aplicar', os títulos serão…](https://ajuda.sankhya.com.br/hc/article_attachments/16250296950039) Acesse o MGE Estoque, Menu>>Arquivos>>Cadastros>>Tipos de Operação
Aba: Validações
Gerar GNRE p/ ST = [marcado]

**Nota**: Esta opção estará habilitada somente para 'Pedido de Compra' e de 'Venda', 'Nota de Compra' e de 'Venda'.

A geração do financeiro da nota pegará a 'Parcela' do 'Tipo de Negociação', que esteja com o 'Tipo de Título' igual ao parâmetro TIPTITGNREST. Se a 'Empresa' e a TOP estiverem marcadas para "Gerar GNRE p/ ST?", se a Nota possuir valor de ST, o sistema gerará um financeiro de despesa, para o 'Parceiro da Secretária da Receita Estadual' da UF de destino, e com o valor da ST.

Caso não seja possível, o sistema encontrar o 'Parceiro da Secretária da Receita Estadual', a parcela não será gerada.

![Imagem 11: Na parte superior, pode ser utilizado o filtro rápido por Empresa e/ou Parceiro. Ao 'Aplicar', os títulos serão…](https://ajuda.sankhya.com.br/hc/article_attachments/16250296954135) Acesse o MGE Livros, Menu>>Conexão>>Sintegra
Registros Opcionais>>Marcar a opção 55-GNRE

Funcionalidade:  Gerar o registro 55, para os títulos de despesas baixados, com a data da baixa dentro do período informado, com o 'Tipo de Título' igual ao do parâmetro TIPTITGNREST, que não seja uma provisão.

**Condição**: Não será gerado o registro 53 - Substituição Tributária "Sintegra" se: O campo "Produto constante no apêndice I do RCTE/GO" for igual a 'SIM'; a movimentação for de 'Entrada', onde a UF da empresa seja GO e a UF do Parceiro também seja GO; e o 'Valor de ST', não somar ao total da nota.
