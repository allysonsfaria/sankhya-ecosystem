---
id: "17146058998039"
titulo: "Análise para que NFs de devoluções de compra, sejam geradas no Sped Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17146058998039-An%C3%A1lise-para-que-NFs-de-devolu%C3%A7%C3%B5es-de-compra-sejam-geradas-no-Sped-Contribui%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:53:45Z"
rotulos: ["Configuração", "NF-e", "Impostos", "CFOP", "Estoque", "Problema de Geração", "Causas de Não Geração", "Solução Proposta", "EFD Contribuições"]
---

# Análise para que NFs de devoluções de compra, sejam geradas no Sped Contribuições

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17147357768215) **SITUAÇÃO:**

Durante as gerações do EFD Contribuições, podemos nos deparar com notas de devoluções de compras que não estão sendo geradas no txt.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17146053939095)CAUSA:**

Configurações/informações nos documentos que precisam ser gerados.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17146069935511)SOLUÇÃO:**

Segue algumas informações analisadas pelo sistema na geração desse tipo de documento:

- Nota deve estar no livro fiscal (tela Cadastro Livro ICMS/IPI) com o campo Origem como "estoque"
- No livro fiscal, deve estar como uma "saída"
- A TOP deve ser do tipo "devolução de compra"
- No livro o CFOP deve estar com uma das seguintes opções: 5201,5202,5205,5206,5207,5210,5410,5413,5411,5660,5661,5662,6201,6202,6205,6206,6207,6210,6410,6411,6660,6661,6662,7201,7202,7205,7206,7207,7210,7211
- Na tabela de impostos dos itens da nota, o CST usado deve ser o 49 e deve ter linhas de PIS/COFINS, conforme orienta o guia prático do EFD Contribuições:![Imagem 4: Na tabela de impostos dos itens da nota, o CST usado deve ser o 49 e deve ter linhas de PIS/COFINS, conforme orienta o…](https://ajuda.sankhya.com.br/hc/article_attachments/17181259543959)
