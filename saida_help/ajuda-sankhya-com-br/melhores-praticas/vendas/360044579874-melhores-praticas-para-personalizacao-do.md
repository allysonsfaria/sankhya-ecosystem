---
id: "360044579874"
titulo: "Melhores práticas para personalização do DANFE na Impressão de NF-e [Ireport]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579874-Melhores-pr%C3%A1ticas-para-personaliza%C3%A7%C3%A3o-do-DANFE-na-Impress%C3%A3o-de-NF-e-Ireport"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T15:51:26Z"
rotulos: ["DUVIDANF", "#RevisadoGui", "Configuração", "Impressão", "Relatórios", "NF-e", "XML", "DANFE", "Configuração: Modelos padrão parâmetros influenciam", "DANFE: Simplificado acompanha mercadoria", "Personalização: Use iReport configure XML"]
---

# Melhores práticas para personalização do DANFE na Impressão de NF-e [Ireport]

O DANFE (Documento Auxiliar da Nota Fiscal Eletrônica) é a impressão de uma representação gráfica simplificada da Nota Fiscal Eletrônica utilizada para acompanhar o trânsito da mercadoria. O formato do DANFE segue normas estabelecidas pela SEFAZ, e a Sankhya fornece um modelo de DANFE que satisfaz estas normas. Ou seja, usando o modelo fornecido pela Sankha já é possível emitir DANFE normalmente.
Porém, alguns clientes podem querer omitir alguns campos do DANFE ou personalizar a exibição de alguns deles. Este procedimento deve ser sempre verificado no manual do contribuinte. Nesse artigo, mostraremos como configurar o ambiente e as ferramentas necessárias para a personalização do DANFE.

**![Imagem 1: Download do iReport](https://ajuda.sankhya.com.br/hc/article_attachments/15579406919319) Download do iReport**

O iReport é a ferramenta utilizada para editar arquivos do tipo .jrxml, que são os arquivos de modelo do DANFE. A Sankhya disponibiliza a versão homologada do iReport pré-configurada para funcionar com Oracle e SqlServer e as funções especiais de relatório fornecidas pela Sankhya. O endereço do download é:

<http://downloads.sankhya.com.br/>

O arquivo é encontrado na seção “Ferramentas”. Deve ser baixado o arquivo “iReport-4.0.1”. Uma vez que o arquivo foi baixado, basta descompactar o .zip e utilizar o iReport.

**![Imagem 2: Obter o modelo padrão do DANFE](https://ajuda.sankhya.com.br/hc/article_attachments/15579406928279) Obter o modelo padrão do DANFE**

Uma vez que o iReport está instalado corretamente, devemos obter o modelo do DANFE na tela de modelos padrão do SankhyaW. Essa tela é acessada pelo seguinte caminho no sistema:

Comercial » Arquivo » Cadastros » Modelo de Impressão (Nota/Pedido)

Acessando a tela, devemos acessar o menu “Baixar Modelos Padrões” e selecionar o modelo desejado. Existem 4 modelos para o DANFE, 1 modelos retrato e 1 modelo paisagem para cada versão do DANFE. A versão do DANFE corresponde à versão do manual do usuário da NF-e. Basicamente, empresas que utilizam a versão 4.01 da NF-e devem usar a versão 4 do DANFE. Todas as outras devem usar a versão 3. A figura abaixo mostra o acesso do menu na tela de modelo de impressão:

![Imagem 3: Acessando a tela, devemos acessar o menu “Baixar Modelos Padrões” e selecionar o modelo desejado. Existem 4 modelos…](https://ajuda.sankhya.com.br/hc/article_attachments/15579253222679)

**![Imagem 4: Obtendo o XML de uma nota](https://ajuda.sankhya.com.br/hc/article_attachments/15579406930583) Obtendo o XML de uma nota**

A versão 4.0 do DANFE utiliza diretamente o XML da NF-e como fonte de dados. Isso quer dizer que a maioria dos dados do DANFE são lidos diretamente do XML da nota fiscal, economizando operações de leitura do banco de dados. Assim, para testar o DANFE fora do SankhyaW, é preciso obter o XML de uma NF-e para ser usado como fonte de dados. Isso pode ser feito pela tela do “Portal de Vendas” no SankhyaW, cujo caminho é:

Comercial » Consulta » Portal de Vendas

na tela, basta selecionar uma NF-e e no menu “Outras opções” selecionar a opção “Nota Fiscal Eletrônica -> Gerar XML da Nfe em arquivo para conferência”, como mostrado na figura seguinte:

![Imagem 5: na tela, basta selecionar uma NF-e e no menu “Outras opções” selecionar a opção “Nota Fiscal Eletrônica -> Gerar XML da…](https://ajuda.sankhya.com.br/hc/article_attachments/15579287261975)

**![Imagem 6: Configurar a fonte de dados XML](https://ajuda.sankhya.com.br/hc/article_attachments/15579406933271) Configurar a fonte de dados XML**

O próximo passo é configurar uma fonte de dados XML. Dessa maneira, indicamos o arquivo XML da NF-e que usaremos como base da personalização. Essa configuração é ignorada pelo sistema, mas é necessária para visualizar a personalização pelo iReport. Para criar uma fonte de dados XML, devemos abrir o iReport e seguir os seguintes passos:

1. clicar no ícone “Report Datasources”, localizado na barra de ferramentas
2. No pop-up “Connections/Datasources” clicar no botão “New”
3. No wizard, selecionar a opção “XML file datasource”
4. Clicar em “Next”

A figura abaixo ilustra a execução destes passos:

![Imagem 7: A figura abaixo ilustra a execução destes passos:](https://ajuda.sankhya.com.br/hc/article_attachments/19253710422551)

Após clicar em “Next”, é mostrado o pop-up que recebe os parâmetros da fonte de dados propriamente dita. Para configurá-la devemos:

1. Fornecer um nome para a fonte de dados.
2. Navegar até o arquivo XML da NF-e que fornecerá os dados
3. Selecionar a opção “Use the report XPath expression when filling the report”.
4. Preencher os campos “Date pattern” e “Number Pattern” com os valores yyyy-MM-dd e #,##0.00, respectivamente.
5. Salvar a fonte de dados.

![Imagem 8: Salvar a fonte de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/19253701512983)

As funções de conexão são fornecidas pela Sankhya. Daí a necessidade de usar o iReport pré-configurado. Existem 3 versões de função de conexão:

- Funcoes.conectarOracle(ip, numeroPorta, servico, usuario, senha)
- Funcoes.conectarSqlServer( ip, numeroPorta, nomeBanco, usuario, senha)
- Funcoes.conectarSqlServer( ip, numeroPorta, instancia, nomeBanco, usuario, senha)

De forma que deve ser usada a versão adequada para cada caso. Uma vez que a conexão foi configurada, o parâmetro JDBC\_CONNECTION pode ser passado como conexão para uma função pdes. Vejamos um exemplo, suponhamos que a empresa emissora de NF-e mantenha um campo adicional na tabela do cabeçalho da nota dizendo se é uma venda “1 ESTRELA”, “2 ESTRELAS”, etc., e que esse campo deve aparecer na frente da natureza de operação. O nome do campo é AD\_ESTRELA.
Nesse caso, temos que inserir um campo de texto e editar o valor de sua expressão para obter o valor do banco de dados, já que essa informação não está no XML da nota. Vamos usar a função PDES para fazê-lo:

![Imagem 9: De forma que deve ser usada a versão adequada para cada caso. Uma vez que a conexão foi configurada, o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/19253701521175)

No exemplo acima, no passo 1 adicionamos um campo no layout do DANFE. No passo 2 abrimos o editor de expressões do campo e inserimos uma chamada à função PDES, passando o parâmetro JDBC\_CONNECTION como parâmetro de conexão.

**![Imagem 10: Personalizando os campos do relatório](https://ajuda.sankhya.com.br/hc/article_attachments/19253710447255) Personalizando os campos do relatório**

Uma vez que o ambiente esteja configurado basta arrastar os campos para o layout do relatório. Os campos do DANFE padrão se encontram disponíveis na listagem de campos do relatório. Existe ainda a possibilidade de acessar a estrutura do XML e disponibilizar qualquer nó XML que não se encontra na listagem padrão, como mostra a figura abaixo:

![Imagem 11: Uma vez que o ambiente esteja configurado basta arrastar os campos para o layout do relatório. Os campos do DANFE…](https://ajuda.sankhya.com.br/hc/article_attachments/19253710455447)

**![Imagem 12: Personalizando os campos do relatório](https://ajuda.sankhya.com.br/hc/article_attachments/19253710456983) Personalizando os campos do relatório**

Por fim, após personalizar o DANFE este deve ser cadastrado no sistema para ser usado no envio de NF-e da empresa. Este passo é bastante simples. Na tela de modelos de impressão de notas criamos um novo modelo e inserimos os arquivos editados no novo modelo. Na tela de preferências da empresa, acessamos a aba NF-e e informamos o número do relatório formatado no campo apropriado. Esse procedimento deve ser realizado para cada empresa que deseja emitir NF-e. O mesmo relatório pode ser utilizado por diversas empresas.

**Importante:**

O grupo da tag <infAdic> recebe a tag <infAdFisco> recebe o conteúdo das observações padrão informada no cabeçalho do documento. Que são previamente cadastrado em: (Comercial » Arquivo » Cadastros » Observações para Notas) e informação padrão informada nos itens de documento que tem origem na alíquota de ICMS: (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS).

Se a soma dos caracteres de todas as observações superarem os 2000 caracteres previstos na infAdFisco o sistema joga o restante dos dados na tag <infCpl>.

As informaçoes contida na tag <infCpl> são os conteúdos das observações da nota(TGFCAB.OBSERVACAO) e do item(TGFITE.OBSERVACAO), não tem relação com a observação padrão que é tratada na infAdFisco, fora essas observações, tudo que resultar da resolução do modelo de dados adicionais da NFe configurado na TOP também é gerado na tag <infCpl> que comporta ate 5000 caracteres.

**PARÂMETROS QUE INFLUENCIAM NA ROTINA:**

ENVOBSNFE - Envia Observação na NFe: Habilita ou não o envio da observação padrão para o DANFE (XML) da Nfe. Se a observação estiver na alíquota de ICMS este parâmetro deve estar habilitado pra gerar na impressão.

ENVOBSPADNFE - Envia Observação padrão na NFe: Habilita ou não o envio da observação da TGFCAB para o DANFE (XML) da NFe. Se criado uma Nota de Complemento, esta levara as informaçoes da Observação da nota de origem
