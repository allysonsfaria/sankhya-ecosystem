---
id: "360043142534"
titulo: "Não foram encontradas configurações para cálculo do imposto 'PIS'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043142534-N%C3%A3o-foram-encontradas-configura%C3%A7%C3%B5es-para-c%C3%A1lculo-do-imposto-PIS"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:13Z"
rotulos: ["ERRONF", "#RevisadoJR", "CORE_E04491", "Produtos", "Configuração", "Empresa", "PIS", "Impostos", "TOP", "Configuração PIS ausente", "Verifique Empresa TOP Produtos Alíquotas", "Falta de regra PIS configurada"]
---

# Não foram encontradas configurações para cálculo do imposto 'PIS'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16146194521111) MENSAGEM:**

[CORE\_E04491]  Não foram encontradas configurações para cálculo do imposto 'PIS'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16146201839511) SITUAÇÃO:**

Ao tentar faturar/confirmar nota que possui incidência de PIS, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16146194525847) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16146201842583) Acesse: Comercial » Preferências » Empresa

- Aba: **"Propriedades"**, campo **"Calcula PIS?"**: marcado

![Imagem 5: Aba: "Propriedades" , campo "Calcula PIS?" : marcado](https://ajuda.sankhya.com.br/hc/article_attachments/14692327489559)

![Imagem 6: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16146194534551) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Aba: **"Impostos"**, campo **"Tem PIS"**: marcado

![Imagem 7: Aba: "Impostos" , campo "Tem PIS" : marcado](https://ajuda.sankhya.com.br/hc/article_attachments/14692391594391)

![Imagem 8: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16146201847959) Acesse: Configurações » Cadastros » Produtos » Produtos

- Aba: **"Impostos"**, campo **"Grupo PIS"**:

![Imagem 9: Aba: "Impostos" , campo "Grupo PIS" :](https://ajuda.sankhya.com.br/hc/article_attachments/14692446553367)

![Imagem 10: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/article_attachments/16146201848471) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS

Realize um filtro com as informações referente ao seu lançamento, considerando os campos abaixo:

- Deve existir uma configuração nessa tela, com o mesmo **GRUPO** informado no cadastro do **produto**, com os campos TIPO (Entrada/Saída) e EMPRESA correspondentes.
- Se os campos PARCEIRO/TOP encontrarem-se como 0, significa que essa alíquota será utilizada para todos os parceiros/TOP'S referente aquele TIPO/GRUPO.
- Necessário compreender que se tratando de nota fiscal eletrônica, mesmo que não exista incidência desse imposto, as configurações citadas acima deverão existir, mesmo que para uma alíquota = 0 (zero).

![Imagem 11: Após os ajustes, efetue a confirmação da nota novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16146201851543) Após os ajustes, efetue a confirmação da nota novamente.

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16146201852951) CAUSA:**

Geralmente ocorre em relação ao cadastro da Empresa, Produto e TOP ou não possuir uma Regra de Alíquotas de PIS devidamente configurada.
