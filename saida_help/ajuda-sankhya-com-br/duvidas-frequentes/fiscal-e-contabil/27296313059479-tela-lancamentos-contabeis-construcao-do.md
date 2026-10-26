---
id: "27296313059479"
titulo: "Tela Lançamentos Contábeis, construção do campo \"Número do Documento\" para movimentos de BAIXA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27296313059479-Tela-Lan%C3%A7amentos-Cont%C3%A1beis-constru%C3%A7%C3%A3o-do-campo-N%C3%BAmero-do-Documento-para-movimentos-de-BAIXA"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:39:49Z"
rotulos: ["Configuração", "Movimentação Financeira", "Agendamento", "Contabilização", "Financeiro", "NFS-e", "Tela Lançamentos Contábeis construção do campo \"Número do Documento\" para movimentos de BAIXA"]
---

# Tela Lançamentos Contábeis, construção do campo "Número do Documento" para movimentos de BAIXA

Confira abaixo as validações de buscas que o sistema faz, na construção do campo **"Num. Documento"** da tela "**Lançamentos Contábeis"**, ao ser executada a rotina da tela "**Agendamento"**, quando se está filtrando o movimento de **Baixa**.

O sistema validará se o parâmetro **"NUMNFSEDOCCTBZ"** está com a opção **"Número do RPS".** Se estiver, será levado para o campo de número de documento o valor presente no campo **"Nro Nota"** da baixa financeira (movimentação financeira). Porém, se o referido parâmetro estiver com a opção **"Número da NFS-e se couber, caso contrário, número do RPS",** o sistema levará para a contabilização, o valor presente no campo **"Nro. NFS-e:"** do financeiro, desde que este campo tenha alguma informação, caso contrário, será levado o valor do campo "Nro Nota".

Veja o exemplo do parâmetro com a opção "Número da NFS-e se couber, caso contrário, número do RPS"

![Imagem 1: Veja o exemplo do parâmetro com a opção "Número da NFS-e se couber, caso contrário, número do RPS"](https://ajuda.sankhya.com.br/hc/article_attachments/27381544243479)

como o campo NRO NFS-E está preenchido levou o valor dele, lembrando que não estivesse, seria levado o valor do campo NRO NOTA.

![Imagem 2: como o campo NRO NFS-E está preenchido levou o valor dele, lembrando que não estivesse, seria levado o valor do campo…](https://ajuda.sankhya.com.br/hc/article_attachments/27381544250007)

Agora veja o exemplo do parâmetro com a opção "Número do RPS"

![Imagem 3: Agora veja o exemplo do parâmetro com a opção "Número do RPS"](https://ajuda.sankhya.com.br/hc/article_attachments/27381544261143)

Em seguida, o sistema realizará mais algumas validações:

![Imagem 4: Se o título financeiro tem Número único devolução (NUDEV) preenchido, usa-o como Num. Documento.](https://ajuda.sankhya.com.br/hc/article_attachments/27381240395799)Se o título financeiro tem Número único devolução (NUDEV) preenchido, usa-o como Num. Documento.

![Imagem 5: Se a validação anterior não for verdadeira e se o financeiro sofreu compensação (NUCOMPENS maior que zero) e Nro Único…](https://ajuda.sankhya.com.br/hc/article_attachments/27381240400279) Se a validação anterior não for verdadeira e se o financeiro sofreu compensação (NUCOMPENS maior que zero) e Nro Único Bancário está zerado (NUBCO = 0), será usado o campo "Nro Compensação/Acerto" como Num. Documento.

![Imagem 6: Se a validação anterior não for verdadeira também e se a opção "Agrupar pelo total do cheque" da tela Agendamento…](https://ajuda.sankhya.com.br/hc/article_attachments/27381240404247) Se a validação anterior não for verdadeira também e se a opção "Agrupar pelo total do cheque" da tela Agendamento estiver desmarcada **OU** Nro Único Bancário (NUBCO) for igual a zero, o sistema validará mais as seguintes questões:

**(2)** Se o campo "Nro. NFS-e" estiver vazio **OU** o campo "Núm. Documento" da tela Movimento Bancário (da baixa financeiro em questão) for **diferente** do valor do campo "Nro Nota" da tela Mov. Financeira, e o "Núm. Documento" da tela Movimento Bancário for maior que zero, o sistema utilizará como Num. Documento na contabilização, o "Núm. Documento" da tela "**Movimento Bancário";**

**(2)** Porém, se o campo "Núm. Documento" da tela Movimento Bancário, não for maior que zero (sendo apenas diferente do "Nro Nota" da tela Mov. Financeira), o sistema levará para o campo Num. Documento, o valor do campo "Nosso Número" da Mov. Financeira.

Porém, se a validação executada no item 3, for falsa nas duas etapas, o sistema tomará outro caminho para encontrar essa informação:

![Imagem 7: Se o campo "Nosso Número" da Mov. Financeira, for maior que zero, o sistema o levará como Num. Documento para…](https://ajuda.sankhya.com.br/hc/article_attachments/27381544264599) Se o campo "Nosso Número" da Mov. Financeira, for maior que zero, o sistema o levará como Num. Documento para contabilização da baixa financeira.

![Imagem 8: Se a validação do item 4 não for verdadeira, por fim, o sistema tentará usar o valor do campo "Núm. Documento" da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/27381566910231) Se a validação do item 4 não for verdadeira, por fim, o sistema tentará usar o valor do campo "Núm. Documento" da tela Movimento Bancário ligado à baixa, se este for maior que zero.

**Se ao fim de todas essas validações, nada for constatado como verdadeira, o campo Num. Documento será levado zerado para tela Lançamentos Contábeis.**
