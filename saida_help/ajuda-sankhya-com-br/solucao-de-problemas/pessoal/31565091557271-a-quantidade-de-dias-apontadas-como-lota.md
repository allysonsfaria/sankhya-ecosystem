---
id: "31565091557271"
titulo: "A quantidade de dias apontadas como lotação do funcionário código X, na empresa X, referência XXXX-XX-XX excede a quantidade de dias da referência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31565091557271-A-quantidade-de-dias-apontadas-como-lota%C3%A7%C3%A3o-do-funcion%C3%A1rio-c%C3%B3digo-X-na-empresa-X-refer%C3%AAncia-XXXX-XX-XX-excede-a-quantidade-de-dias-da-refer%C3%AAncia"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:35Z"
rotulos: ["Folha", "Pessoal", "Configuração Funcionários", "quantidade de dias apontadas como lotação", "excede a quantidade de dias da referência", "Erro"]
---

# A quantidade de dias apontadas como lotação do funcionário código X, na empresa X, referência XXXX-XX-XX excede a quantidade de dias da referência

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31565091545751) **MENSAGEM:**

**Erro:** A quantidade de dias apontadas como lotação do funcionário código X, na empresa X, referência XXXX-XX-XX XX:XX:XX.X excede a quantidade de dias da referência. Favor verifique na tela 'Movimentação de Tomador de Serviço' se os lançamentos dessa referência estão corretos.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31565091552151)SOLUÇÃO:**

Ajuste a data de início na tela **"Movimentação de Tomador de Serviço"** (Pessoal+ » Rotinas Folha » Movimentação de Tomador de Serviço) para que esteja de acordo com a data de admissão do funcionário. Quando se tratar de uma nova lotação, a data de início deve ser sempre o dia 01 do mês de referência, conforme demonstrado no print abaixo

![Imagem 3: Ajuste a data de início na tela " Movimentação de Tomador de Serviço" (Pessoal+ » Rotinas Folha » Movimentação de…](https://ajuda.sankhya.com.br/hc/article_attachments/31571038700439)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31565091549847)CAUSA:**

O erro ocorre devido a uma inconsistência entre a data de admissão do funcionário e a data de início registrada na tela Movimentação de Tomador de Serviço, que está diferente do dia 01.
