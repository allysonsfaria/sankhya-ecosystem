---
id: "360045107993"
titulo: "Rastreamento de Saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107993-Rastreamento-de-Sa%C3%ADda"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:54:26Z"
rotulos: ["Rastreamento de Estoques", "Rastreamento de Saída", "Rastreamento de Saída manual", "Configuração", "Fiscal", "NF-e", "XML", "Impostos", "Estoque", "Configurações para Rastreamento de Saída"]
---

# Rastreamento de Saída

Para a geração dos dados de substituição tributária na tag ICMS 60 da NF-e, o sistema identifica as notas de entrada de cada produto, no momento da emissão de notas de saída, criando um vínculo entre elas, o que caracteriza o Rastreamento de Estoques. Para isso, são necessárias as seguintes configurações:

**Nota:** a tela **"Ativação de Empresa e Produtos"** foi criada apenas no módulo MGE Configurações, esta ainda não foi migrada para o Sankhya Om, ou seja, para utilizar o processo no SankhyaOm é preciso configurá-la (ativar) no MGE.

Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), [aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abapropriedades), campo **"Rastreamento de Estoques"**:

![Imagem 1: Nas Preferências da Empresa , aba Propriedades , campo "Rastreamento de Estoques" :](https://ajuda.sankhya.com.br/hc/article_attachments/360084345574)

Nas opções dispostas do campo teremos:

- **Não rastrear:** A empresa não utilizará o rastreamento de estoque;
- **Rastrear Doc. Fiscais e Não Fiscais:** No rastreamento, o sistema irá considerar documentos fiscais, assim como não fiscais;
- **Rastrear Doc. Fiscais:** Por esta opção, somente as TOP's configuradas com os campos **"Atualização do Livro ICMS"** (Tela **"Tipos de Operação - TOP"**, aba **"Livro Fiscal"**) com as opções **"Livro Entrada"** ou **"Livro Saída"** selecionadas, e o campo **"Atualização do Estoque"** (Tela Tipos de Operação - TOP, aba Estoque) com as opções **"Entrar"** ou **"Baixar"** selecionadas  irão fazer parte do rastreamento;

**Observação:** referente à opção Rastrear Doc. Fiscais e Não Fiscais, o sistema irá realizar o rastreamento dos Documentos Não Fiscais que estiverem com o campo Atualização Livro ICMS selecionado com a opção Não atualiza. Além disso, faz-se necessário que os parâmetros a seguir estejam configurados:

- **"Documentos Não-Fiscais atualizam Rastreamento/ST - DOCNFISCRASTST"**;
- No parâmetro **"Lista de TOP Entrada no rastr. de Doc. Não Fiscais - TOPENTNFISRAST"** informe as TOP's de Entrada Não-Fiscais;
- No parâmetro **"Lista de TOP Sáida no Rastr. de Doc. Não Fiscais - TOPSAINFISRAST"** informe as TOP's de Saída Não-Fiscais.

Ainda sobre estes teremos que nos atentar, pois:

Caso o parâmetro DOCNFISCRASTST estiver desligado, o sistema não irá considerar documentos não fiscais;
Se o parâmetro citado anteriormente, justamente com os parâmetros TOPENTNFISRAST e TOPSAINFISRAST estiverem vazios, todas as movimentações não fiscais serão consideradas.

Depois de realizadas estas configuradas, você poderá consultar as notas de rastreamento por meio da tela [Gerência de Rastreamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052261594).

No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Rastreamento Por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abarastreamentoporempresa), o campo **"Tipo de Rastreamento"** possui as seguintes opções:

- Sem rastreamento
- Rastrear
- Última compra
- Rastrear com Controle
- Rastrear com Local
- Rastrear com Controle e Local

![Imagem 2: Rastrear com Controle e Local](https://ajuda.sankhya.com.br/hc/article_attachments/15659029605527)

Na grade de Itens nas Centrais, tem-se os campos:

- Base de Cálc. da ST de oper. ant.;
- Vlr. do ICMS da ST da oper. ant.;
- Vlr ICMS destacado da oper. própria de oper. ant.

![Imagem 3: Vlr ICMS destacado da oper. própria de oper. ant.](https://ajuda.sankhya.com.br/hc/article_attachments/15659042276503)

Quando a nota é confirmada, o sistema irá rastrear as notas de saída para identificar cada produto das notas de entrada que estão lastreando a saída, gravando os dados dos cálculos tanto na nota de entrada/saída quanto nas tabelas de rastreamento do sistema.

Com os dados do rastreamento calculados, o sistema irá gerar no XML da nota uma TAG com o nome ICMS60 para cada item, destacando o valor da substituição tributária:

<ICMS>

 <ICMS60>

         <orig>0</orig>

         <CST>60</CST>

         <vBCSTRet>9.00</vBCSTRet>

         <vICMSSTRet>0.90</vICMSSTRet>

 </ICMS60>

</ICMS>

Desta forma será possível a obtenção do valor do ICMS ST retido anteriormente quando da emissão de notas de saída com CST 060, isto é, saídas com imposto retido anteriormente por substituição tributária.

Possibilitará a geração correta da tag ICMS60 da NF-e e atender a exigência de destacar estes valores no documento fiscal de saída de uma forma mais precisa que a utilização de valores médios.

**Observação:** o sistema realizará o cálculo do vICMSSTRet de acordo com a operação (vICMSSTRet - vICMSSubstituto), se o parâmetro **"Operaes classificadas com o CST 060 - ICMS cobrado anteriormente por substituio - ICMSSTRETLIQ060"** estiver ligado e se o vICMSSubstituto for menor/igual que o vICMSSTRet. Destacamos ainda, que está configuração é válida apenas para a emissão de NF-e e não irá influenciar nos valores da apuração.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107993-Rastreamento-de-Sa%C3%ADda#top)
