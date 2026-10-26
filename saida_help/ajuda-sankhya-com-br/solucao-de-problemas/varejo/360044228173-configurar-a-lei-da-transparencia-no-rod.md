---
id: "360044228173"
titulo: "Configurar a lei da transparência no rodapé do cupom fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044228173-Configurar-a-lei-da-transpar%C3%AAncia-no-rodap%C3%A9-do-cupom-fiscal"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:59:53Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Parceiro", "Impostos", "TOP", "Preferências", "Configurar lei da transparência", "Defina Classificação ICMS correta", "Ative \"Lei da Transparência\" nos cupons"]
---

# Configurar a lei da transparência no rodapé do cupom fiscal

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16200420637847) SITUAÇÃO:**

As informações da Lei da Transparência, não estão sendo apresentadas no rodapé dos cupons fiscais. 

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16200420640535) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16200458384279) Acesse: Configurações » Cadastros » Produtos » Produtos

Aba: **Impostos**

Campos:

**"% Carga Média Trib. Estadual":** TGFPRO.PERCCMTEST

**"% Carga Média Trib. Federal":** TGFPRO.PERCCMTFED

**"% Carga Média Trib. Nacional":** TGFPRO.PERCCMTNAC

![Imagem 4: "% Carga Média Trib. Nacional": TGFPRO.PERCCMTNAC](https://ajuda.sankhya.com.br/hc/article_attachments/14536550172695)

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16200458387479) OBSERVAÇÃO:**

Preencha a % Carga Média Trib. Estadual: e % Carga Média Trib. Federal:, ou preencha a % Carga Média Trib. Nacional:. Não pode preencher ambos.

![Imagem 6: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16200458389271) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

No cadastro de TOP de cupom fiscal, na aba **Impostos** a **"Classificação ICMS"** deve ser: Consumidor Final não contribuinte;

![Imagem 7: No cadastro de TOP de cupom fiscal, na aba Impostos a "Classificação ICMS" deve ser: Consumidor Final não contribuinte;](https://ajuda.sankhya.com.br/hc/article_attachments/14536551911831)

![Imagem 8: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16200458391063) Acesse: Configurações » Cadastros » Parceiros

No cadastro de parceiro, na aba **Fiscal** a **"Classificação ICMS"**deve ser: **"Consumidor Final não contribuinte"**;

![Imagem 9: No cadastro de parceiro, na aba Fiscal a "Classificação ICMS" deve ser: "Consumidor Final não contribuinte" ;](https://ajuda.sankhya.com.br/hc/article_attachments/14536595156631)

![Imagem 10: Acesse: Fast Service » Menu » Avançado » Preferencias » Todas as Preferencias](https://ajuda.sankhya.com.br/hc/article_attachments/16200420657431) Acesse: Fast Service » Menu » Avançado » Preferencias » Todas as Preferencias

Aba **Parâmetros Iniciais**:

**"Imprimir nas observações do cupom":** marque a opção '**Lei da Transparência**'.

![Imagem 11: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16200420659607) Acesse: Configurações » Avançado » Preferências

Parâmetro: "**LEI12741FONTE -Fonte do cálculo da Carga Média Tributária"**

Para cumprimento desta norma configure o parâmetro Fonte do cálculo da Carga Média Tributária (LEI12741FONTE), que estará ativado desde que exista qualquer caractere em seu campo texto.

É aconselhável que o usuário digite neste campo o nome da fonte na qual conseguiu as porcentagens médias. Para apresentação dos totais de tributação ao consumidor final, essa informação sairá impressa junto com o percentual e o valor calculado destas tributações.

Após a configuração mostrada, todo cupom fiscal emitido terá no rodapé dele a porcentagem de Carga Média Tributária para os produtos configurados.

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16200458397975) CAUSA:**

Quando não configurado o parâmetro e dados sobre os percentuais de carga tributária nos produtos, as informações da Lei da Transparência não é apresentada no cupom.
