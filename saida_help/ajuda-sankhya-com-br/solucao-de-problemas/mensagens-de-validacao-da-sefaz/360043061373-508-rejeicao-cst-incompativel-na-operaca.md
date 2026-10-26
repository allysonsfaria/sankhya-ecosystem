---
id: "360043061373"
titulo: "508 Rejeição: CST incompatível na operação com Não Contribuinte - [nItem:999] (NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043061373-508-Rejei%C3%A7%C3%A3o-CST-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-N%C3%A3o-Contribuinte-nItem-999-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:18Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "Impostos", "CST incompatível na operação com Nao Contribuinte", "Indicador de IE do destinatário inválido", "Ajuste CST no cadastro do parceiro", "508 Rejeição", "Rejeição 508", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# 508 Rejeição: CST incompatível na operação com Não Contribuinte - [nItem:999] (NT2015/003)

**MENSAGEM**

Rejeição 508: CST incompatível com não contribuinte.

**SITUAÇÃO**

Esta rejeição ocorre quando o emissor tenta validar uma nota fiscal utilizando um Código de Situação Tributária (CST) que exige a condição de contribuinte do ICMS, porém o destinatário da nota está cadastrado como **"Não Contribuinte"** ou com o campo **"Indicador de IE"** incorreto na tela (Configurações >> Cadastros >> Parceiros).

**CAUSA**

O erro é gerado pela divergência entre a tributação aplicada (CST) e o perfil fiscal do parceiro destinatário. Algumas legislações estaduais impedem que determinados CSTs sejam utilizados em operações destinadas a pessoas que não possuem Inscrição Estadual (IE) ativa.

**SOLUÇÃO**

Para solucionar esta rejeição, siga os passos abaixo:

Acesse a tela (Configurações >> Cadastros >> Parceiros) e localize o parceiro destinatário da nota.

Verifique na aba **"Fiscal"** se o campo **"Classificação ICMS"** está preenchido corretamente como **"Não Contribuinte"** ou **"Isento"**, conforme o caso.

Caso o parceiro seja realmente contribuinte, ajuste a **"Inscrição Estadual"** e altere o indicador para **"Contribuinte ICMS"**.

Se o parceiro for um consumidor final não contribuinte, revise a configuração da alíquota e do CST utilizado na operação na tela (Comercial >> Arquivo >> Cadastros>> Alíquotas), garantindo que o CST utilizado seja compatível com operações para não contribuintes.

![Imagem 1: Após realizar as correções, salve o cadastro do parceiro e tente reenviar a nota fiscal pela tela (Comercial >>…](https://ajuda.sankhya.com.br/guide-media/01H532NS5KVBYNJ6CRSGDMZHCD) Após realizar as correções, salve o cadastro do parceiro e tente reenviar a nota fiscal pela tela (Comercial >> Consulta >> Central de Vendas).
