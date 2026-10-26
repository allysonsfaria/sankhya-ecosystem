---
id: "360044616293"
titulo: "Alíquota de \"COFINS\" não foi encontrada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616293-Al%C3%ADquota-de-COFINS-n%C3%A3o-foi-encontrada"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:11Z"
rotulos: ["#criadoRoger", "Produtos", "Alíquotas", "Configuração", "COFINS", "Impostos", "TOP", "Erro de Alíquota de COFINS"]
---

# Alíquota de "COFINS" não foi encontrada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16415523720215) MENSAGEM:**

'Erro durante a confirmação: 4649'
Local: Calculando COFINS
Alíquota de "COFINS" não foi encontrada.
Grupo: "YYYY", Tipo: "E", Empresa: "1", Parceiro: "AAAA", TOP: "X"
Verifique se nos cadastros de alíquota e de produto não existe espaço em branco no início ou no final do campo Grupo COFINS.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16415534920983) SITUAÇÃO:**

Ao tentar confirmar uma Nota de Compra/Venda é apresentada a mensagem.

**![Imagem 3: SOLUÇÃO: Para correção, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16415534922775) SOLUÇÃO:**
Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Comercial » Preferências » Empresa / Aba: Propriedades Campo:](https://ajuda.sankhya.com.br/hc/article_attachments/16415534925591) Acesse: Comercial » Preferências » Empresa / Aba: Propriedades
Campo:

- **"Calcula COFINS?"**

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP / Aba: Impostos Campo:](https://ajuda.sankhya.com.br/hc/article_attachments/16415534927383) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP/ Aba: Impostos
Campo:

- **"Tem COFINS"**

![Imagem 6: Acesse: Configurações » Cadastros » Produtos / Aba: Impostos](https://ajuda.sankhya.com.br/hc/article_attachments/16415534930839) Acesse: Configurações » Cadastros » Produtos / Aba: Impostos

Campo:

- **"Grupo COFINS"**

![Imagem 7: Efetue a configuração de acordo com a movimentação de Nota. Se para entrada, crie uma regra de PIS específica para…](https://ajuda.sankhya.com.br/hc/article_attachments/16415534934039) Efetue a configuração de acordo com a movimentação de Nota. Se para entrada, crie uma regra de PIS específica para Entrada com a respectiva alíquota e CST.

- Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS

**(1)** Recomenda-se criar especificamente regras de Entrada e regras de Saídas, pois o CST são diferentes para ambos.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16415523740823) CAUSA:**

Ocorre quando a nota está incidindo no cálculo de COFINS, geralmente em relação ao cadastro da Empresa, Produto e TOP. Também quando não possui uma Regra de Alíquotas de COFINS devidamente configurado.
