---
id: "360042718814"
titulo: "Existe MDF-e não encerrado há mais de 30 dias para o emitente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042718814-Existe-MDF-e-n%C3%A3o-encerrado-h%C3%A1-mais-de-30-dias-para-o-emitente"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-08T13:49:39Z"
rotulos: ["ERROMDFE", "MDF-e", "SEFAZ", "Transporte", "686", "MDF-e não encerrado por mais de 30 dias", "Rejeição 686 MDF-e não encerrad", "Encerre MDF-e pendentes e retransmita", "Documentos Eletrônicos"]
---

# Existe MDF-e não encerrado há mais de 30 dias para o emitente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16512663565079) MENSAGEM:**

[686 - Rejeição]: Existe MDF-e não encerrado há mais de 30 dias para o emitente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16512639169559) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Rotinas » Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/article_attachments/16512639171863) Acesse: Comercial » Rotinas » Viagens de Transporte (MDF-e)

Efetue uma pesquisa usando os filtros rápidos, para encontrar as MDF-e que estão com situação diferente de Encerrado, para ser encerrado.

**Nota¹**: Acessando o [Portal da MDF-e](https://dfe-portal.sefazvirtual.rs.gov.br/), podem ser Consultada as MDF-e não encerradas:

![Imagem 4: Nota¹ : Acessando o Portal da MDF-e , podem ser Consultada as MDF-e não encerradas:](https://ajuda.sankhya.com.br/hc/article_attachments/360059969834)

![Imagem 5: Nota¹ : Acessando o Portal da MDF-e , podem ser Consultada as MDF-e não encerradas:](https://ajuda.sankhya.com.br/hc/article_attachments/14627747587607)

![Imagem 6: Após o processo, transmita novamente a nova MDF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16512639176855) Após o processo, transmita novamente a nova MDF-e.

**Nota²:**Cada vez que a empresa ultrapassar a cota de 5 rejeições desta natureza, terá aplicada a punição pelo período de uma hora a partir da sexta rejeição.

O sistema de autorização irá suprimir esse complemento indicativo de chave e protocolo na mensagem de retorno para o CNPJ que receber mais de 5 rejeições de um destes tipos (462,610,611,686) dentro do intervalo de uma hora.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16512663575063) CAUSA:**

Quando for emitido um MDF-e e houver outro(s) MDF-e(s) ainda não encerrado pelo mesmo CNPJ emitente há mais de 30 dias, será retornada a rejeição.
