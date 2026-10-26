---
id: "360043792914"
titulo: "Como emitir NFC-e para Consumidor Padrão Identificado via FAST SERVICE?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043792914-Como-emitir-NFC-e-para-Consumidor-Padr%C3%A3o-Identificado-via-FAST-SERVICE"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:58:58Z"
rotulos: ["Configuração", "Fiscal", "Fast Service", "SEFAZ", "NFC-e", "Vendas identificadas/sem identificação", "NFC-e para Consumidor Padrão", "Cupom Fiscal NFC-e e SAT", "Documentos Eletrônicos"]
---

# Como emitir NFC-e para Consumidor Padrão Identificado via FAST SERVICE?

Como configurar o Fast para que seja feito o controle de vendas identificadas/sem identificação no ponto de venda. **Válido para Cupom Fiscal, NFC-e e SAT.**

Neste documento, vamos indicar a melhor forma de adaptar o seu PDV para o controle de identificação de CPF/CNPJ nas vendas.

Conforme estabelecido pela Secretaria da Fazenda, existem algumas validações referentes a identificação de consumidor final na NFC-e que devemos nos atentar e a que vamos enaltecer hoje é a citada na [**NT\_2015\_002\_v141**](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hDS5co/qWOc=).

Este, cita:
"NFC-e com valor total superior a R$ 10.000,00: – Código do Destinatário não informado(tag:dest/CNPJ, dest/CPF oudest/idEstrang) Observação: Valor definido a critério da UF." 

750- Rejeição: NFC-e com valor total superior ao permitido para destinatário não identificado (Código) [Limite] 

**(1)** Considere o comportamento da aplicação, conforme abaixo:

(2)** 1º Cenário:**

Solicitar o CPF/CNPJ no lançamento do Cupom Fiscal pelo Fast.

Acesse o FastService

Avançado » Preferencias » Todas as Preferencias

Aba: **Miscelânea**

Parâmetro: **"UFs que solicitam CPF na venda com cupom fiscal":**

Este parâmetro irá solicitar que seja digitado o CPF da venda no momento da inclusão do primeiro item, caso a UF da empresa emitente esteja informada no parâmetro.

![Imagem 1: O pop-up solicitando os dados do cliente será apresentado ao gravar o primeiro item(produto) no Cupom Fiscal.](https://ajuda.sankhya.com.br/hc/article_attachments/16201464980631) O pop-up solicitando os dados do cliente será apresentado ao gravar o primeiro item(produto) no Cupom Fiscal.

(2)** 2º Cenário:**

Exigir que seja informado o CPF/CNPJ no Cupom, caso a venda seja acima de um determinado valor.

Acesse o FastService

Avançado » Preferências » Todas as Preferências

Aba: **Parâmetros de Telas**

Parâmetro: **"Exigir CPF/CNPJ no Cupom acima de":**

Este parâmetro irá exigir que seja digitado o CPF/CNPJ do parceiro na conclusão da venda, caso o total da venda seja maior que o informado no parâmetro em questão.

**![Imagem 2: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201426881303) OBSERVAÇÃO:**

Vale ressaltar que os parâmetros destacados (**"UFCAPTURACPF", "EXIGECPFCNPJVLR"**) solicitados acima são no início e no fim da venda, respectivamente.

E podem ser utilizados em conjunto ou não, de acordo com o processo e exigência fiscal da SEFAZ Estadual.
