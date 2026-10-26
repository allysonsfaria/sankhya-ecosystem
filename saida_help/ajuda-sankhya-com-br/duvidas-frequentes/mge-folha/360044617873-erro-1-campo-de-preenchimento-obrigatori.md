---
id: "360044617873"
titulo: "Erro 1 - Campo de preenchimento obrigatório: Município."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617873-Erro-1-Campo-de-preenchimento-obrigat%C3%B3rio-Munic%C3%ADpio"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:41Z"
rotulos: ["#criadoRoger", "#RevisadoLorrana", "Configuração", "Funcionários", "Cidades", "eSocial", "Central do eSocial", "Código de Município ausente", "Erro: Município não preenchido", "Preencher campo \"Naturalidade\" e \"Mun. Domicílio Fiscal\"", "Erro"]
---

# Erro 1 - Campo de preenchimento obrigatório: Município.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16949135206423) MENSAGEM:**

Erro 1 - Campo de preenchimento obrigatório: Município.
Elemento: /eSocial/evtAdmissao/trabalhador/nascimento/codMunic
[null]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16949135207959) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: MGEPessoal » Arquivos » Funcionários Aba: "Pessoais" Campo " Naturalidade" : identifique a Cidade de Nascimento](https://ajuda.sankhya.com.br/hc/article_attachments/16949094442135) Acesse: MGEPessoal » Arquivos » Funcionários
Aba: **"Pessoais"**
Campo **"Naturalidade"**: identifique a Cidade de Nascimento

![Imagem 4: Acesse: MGEConfiguraçoes: MGEConf » Arquivos » Endereços » Cidades Campo "Mun. Domicilio Fiscal" : preencha conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/16949135211543) Acesse: MGEConfiguraçoes: MGEConf » Arquivos » Endereços » Cidades
Campo **"Mun. Domicilio Fiscal"**: preencha conforme dados do [IBGE](https://cidades.ibge.gov.br/)

![Imagem 5: Acesse: MGEPessoal » Avançado » Central do E-social.](https://ajuda.sankhya.com.br/hc/article_attachments/16949094448279) Acesse: MGEPessoal » Avançado » Central do E-social.

Gere e transmita novamente as obrigações.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16949094450071) CAUSA:**

Ocorre quando o Código de Município Domicílio Fiscal do cadastro da Cidade de Nascimento não está devidamente preenchido

**![Imagem 7: OBSERVAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16949135221527) OBSERVAÇÃO:**

Evento: S-2200 - [Manual Orientação do ESocial](https://portal.esocial.gov.br/manuais/mos-v-2-4-02-publicada-cg.pdf)
