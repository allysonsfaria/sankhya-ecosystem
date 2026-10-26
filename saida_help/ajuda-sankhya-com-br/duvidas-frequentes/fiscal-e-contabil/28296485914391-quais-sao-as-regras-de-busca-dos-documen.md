---
id: "28296485914391"
titulo: "Quais são as regras de busca dos documentos gerados com a marcação 'Tributa PIS/COFINS Despesas Acessórias Separadamente no F100?'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28296485914391-Quais-s%C3%A3o-as-regras-de-busca-dos-documentos-gerados-com-a-marca%C3%A7%C3%A3o-Tributa-PIS-COFINS-Despesas-Acess%C3%B3rias-Separadamente-no-F100"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:37:58Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "TOP", "Documentos", "Estoque", "EFD Contribuições", "Tributa PIS/COFINS Despesas Acessórias Separadamente no F100"]
---

# Quais são as regras de busca dos documentos gerados com a marcação 'Tributa PIS/COFINS Despesas Acessórias Separadamente no F100?'

Confira neste artigo as regras de busca dos documentos que serão gerados mediante a ativação da marcação **"Tributa PIS/COFINS Despesas Acessórias Separadamente no F100?"** na tela de geração do EFD Contribuições.

O sistema realizará uma consulta na tela **"Cadastro Livro ICMS/IPI"** buscando pela empresa e período de geração do txt, validando as seguintes situações:

**(1)** Documentos que estejam como **"Saída"**;

**(1)** O campo Origem deve estar como **"estoque"**;

**(1)** O campo Destino deve estar como **"Parceiro"**;

**(1)** O modelo dos documentos deve ser **1 ou 55**;

Em seguida serão validadas as condições que os documentos devem ter em seu lançamento nas centrais:

**(1)** O tipo de movimento da TOP dos documentos deve ser **Pedido de venda ou Nota de venda;**

**(1)** A TOP do documento deve estar com os campo **"tem PIS" e "tem COFINS"** marcados;

**(1)**Os documentos devem possuir em seus impostos (outras opções da grade de itens >> consultar/alterar impostos do item) uma linha dos impostos PIS ou COFINS, com os campos **"Base reduzida" e "Valor" zerados**, e que seja uma das seguintes **incidências**:

**(2)**Frete
**(2)**Seguro
**(2)**Destaque
**(2)**Embalagem
**(2)**Juro
