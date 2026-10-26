---
id: "360043059873"
titulo: "Uso Denegado: Irregularidade fiscal do destinatário.(NT2013/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043059873-Uso-Denegado-Irregularidade-fiscal-do-destinat%C3%A1rio-NT2013-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:27Z"
rotulos: ["ERRONF", "Fiscal", "Parceiro", "NF-e", "SEFAZ", "302", "Uso Denegado: Irregularidade Fiscal do Destinatário", "Erro"]
---

# Uso Denegado: Irregularidade fiscal do destinatário.(NT2013/005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16458233616023) MENSAGEM:**

[302-Rejeição]: Uso Denegado: Irregularidade fiscal do destinatário.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16458233618199) SOLUÇÃO:**

Quando for emitida uma NFe, a Sefaz retornará a rejeição “302 – Uso Denegado: Irregularidade fiscal do destinatário” se o destinatário estiver com algum tipo de irregularidade cadastral.

Nessa situação o emitente do documento pode verificar se a Inscrição Estadual do destinatário está em uma das situações listadas abaixo. É possível realizar a consulta de sua situação cadastral através do site do SINTEGRA ou no Cadastro Centralizado de Contribuinte.

- Sintegra: <http://www.sintegra.gov.br/>
- CCC: <https://dfe-portal.svrs.rs.gov.br/NFE/CCC>

Nas consultas é exibido os termos “Habilitado” ou “Não Habilitado”. O resultado “Não Habilitado” indica que a Inscrição Estadual está em uma das quatro situações listadas no cadastro da Secretaria de Fazenda.

O emitente de uma NFe denegada pelo código de retorno 302 nada pode fazer para corrigir a situação. O código de retorno diz respeito a uma irregularidade na Inscrição Estadual do **destinatário**.

Somente o **representante legal do destinatário** deverá, junto a Sefaz normalizar sua Inscrição Estadual.

**(1)** Segue abaixo passo a passo para verificação:

Acesse: Configurações » Cadastros » **Parceiros**, aba "**Identificação"**

Campos:

- **"CNPJ/CPF".**
- **"Insc. Estadual / Identidade".**

![Imagem 3: "Insc. Estadual / Identidade".](https://ajuda.sankhya.com.br/hc/article_attachments/14472834610327)

Considerando os dados de acordo com o registrado no cadastro do parceiro, o emitente pode orientar o seu cliente a entrar em contato com a Sefaz para regularizar a sua situação.

**![Imagem 4: IMPORTANTE :](https://ajuda.sankhya.com.br/hc/article_attachments/16458233622807) IMPORTANTE:**

Até que a situação do destinatário seja regularizada, não será possível a emissão de notas para esse parceiro.

**![Imagem 5: CAUSA: Quando for emitida uma NF-e caso seja identificada pela SEFAZ que o destinatário possui irregularidades…](https://ajuda.sankhya.com.br/hc/article_attachments/16458233623703) CAUSA:**

Quando for emitida uma NF-e caso seja identificada pela SEFAZ que o destinatário possui irregularidades fiscais/cadastrais.

Situações da Inscrição Estadual que ocasionam a denegação de uso da NF-e:

- I.E. Suspensa;
- I.E. Cancelada;
- I.E. Baixada;
- I.E. Em Processo de Baixa.

![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17857503505943) **OBSERVAÇÃO:**

([NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=)) - Nota Técnica.
