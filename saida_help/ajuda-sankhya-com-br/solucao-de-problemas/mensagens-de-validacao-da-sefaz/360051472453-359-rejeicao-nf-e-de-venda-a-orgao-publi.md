---
id: "360051472453"
titulo: "359 - Rejeição: NF-e de venda a Órgão Público sem informar a Nota de Empenho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051472453-359-Rejei%C3%A7%C3%A3o-NF-e-de-venda-a-%C3%93rg%C3%A3o-P%C3%BAblico-sem-informar-a-Nota-de-Empenho"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:30:42Z"
rotulos: ["Configuração", "Nota de Empenho", "NF-e", "SEFAZ", "Impostos", "Rejeição 359", "Venda a Órgão Público", "Órgão Público"]
---

# 359 - Rejeição: NF-e de venda a Órgão Público sem informar a Nota de Empenho

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/15936614611735) MENSAGEM**:

359 - Rejeição: NF-e de venda a Órgão Público sem informar a Nota de Empenho.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15936576368919) CAUSA:**

NF-e com desoneração de ICMS motivada por venda a Órgão Público (**<motDesICMS>8</motDesICMS>**), sem informar Nota de Empenho.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15936614615191) SOLUÇÃO:**

Ao emitir uma NF-e que possui o campo motDesICMS = 8 (Desoneração de ICMS motivada por venda a órgão público), devemos obrigatoriamente informar a nota de empenho.

![Imagem 4: Preencher, no cabeçalho da nota emitida, o campo " Nota de Empenho ":](https://ajuda.sankhya.com.br/hc/article_attachments/15936576370967) Preencher, no cabeçalho da nota emitida, o campo "**Nota de Empenho**":

![Imagem 5: Preencher, no cabeçalho da nota emitida, o campo " Nota de Empenho ":](https://ajuda.sankhya.com.br/hc/article_attachments/15936576199063)

- Caso não localize esse campo, acesse a tela 'Configurador de Layout da nota' e adicione o mesmo. Para mais detalhes: [Como inserir um campo no layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973-Como-inserir-um-campo-no-layout-da-nota-)

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15936614617879) Importante:**

| Caso a 'Nota de Empenho não deva ser informada, será necessário realizar os devidos ajustes no campo **"Cód.Mot.Desoneração ICMS"** da aba 'Geral' da regra de ICMS utilizada, inserindo um código diferente de [8], conforme as orientações do Contador (Tela: Comercial » Arquivo » Cadastros » Alíquotas » **Alíquotas de ICMS**). Feito isso, refaça o faturamento. |
| --- |

**![Imagem 7: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/15936576372503) OBSERVAÇÕES:**

![Imagem 8: Implementação opcional, a critério da UF.](https://ajuda.sankhya.com.br/hc/article_attachments/15936576375575) Implementação opcional, a critério da UF.

![Imagem 9: Manual de Orientação do Contribuinte.](https://ajuda.sankhya.com.br/hc/article_attachments/15936614621463) [Manual de Orientação do Contribuinte.](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)
