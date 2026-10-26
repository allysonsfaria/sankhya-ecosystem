---
id: "360057638034"
titulo: "O CNPJ não deve estar cadastrado na Tabela de Estabelecimentos e Obras no período especificado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360057638034-O-CNPJ-n%C3%A3o-deve-estar-cadastrado-na-Tabela-de-Estabelecimentos-e-Obras-no-per%C3%ADodo-especificado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:26:48Z"
rotulos: ["#criadoRoger", "Fiscal", "Erro 398", "Erro 697", "S-1200", "S1200", "eSocial", "Configuração Funcionários", "Central do eSocial", "Erro de Cadastro de CNPJ na Tabela de Estabelecimentos e Obras", "Regra de validação", "Erro"]
---

# O CNPJ não deve estar cadastrado na Tabela de Estabelecimentos e Obras no período especificado

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16252555289623) MENSAGEM**:

[Erro 697]: O CNPJ não deve estar cadastrado na Tabela de Estabelecimentos e Obras no período especificado.
Elemento: /eSocial/evtRemun/ideTrabalhador/infoMV/remunOutrEmpr/nrInsc [02631552000123]
[Erro 398]: Deve ser informado um valor diferente do CNPJ/CPF do empregador.
Elemento: /eSocial/evtRemun/ideTrabalhador/infoMV/remunOutrEmpr/nrInsc [02631552000123]

**Erro ao enviar o evento S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social**

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16252555294743) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o Cadastro de Funcionários em: MGE Pessoal>>Arquivos>>Funcionários - Aba: "Remuneração Outras Empresas" - Campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16252563947159) Acesse o Cadastro de Funcionários em: MGE Pessoal>>Arquivos>>Funcionários
- Aba: **"Remuneração Outras Empresas"**
- Campo **"Indicador Desconto INSS"**: [0-Não se aplica]
- Na grade de CGC/CPF, exclua qualquer linha que esteja cadastrada.

![Imagem 4: MGE Pessoal>>Cálculos>>Individuais>>Folha Normal Exclua o cálculo do Autônomo.](https://ajuda.sankhya.com.br/hc/article_attachments/16252555301015) MGE Pessoal>>Cálculos>>Individuais>>Folha Normal
Exclua o cálculo do Autônomo.

![Imagem 5: MGE Pessoal>>Lançamentos>>Movimentação por Funcionários](https://ajuda.sankhya.com.br/hc/article_attachments/16252582802967) MGE Pessoal>>Lançamentos>>Movimentação por Funcionários

**3.1 -** Exclua os registros que possuem o evento 505 e 506, pois estes foram gravados com a informação do CNPJ, no campo de observação;

**3.2 -** Lançar novamente os registros 505 e 506, estes já sem a informação do CNPJ no campo de Observação.

![Imagem 6: MGE Pessoal>>Cálculos>>Individuais>>Folha Normal Realize novamente um novo cálculo e libere a folha novamente para…](https://ajuda.sankhya.com.br/hc/article_attachments/16252555304087) MGE Pessoal>>Cálculos>>Individuais>>Folha Normal
Realize novamente um novo cálculo e libere a folha novamente para envio ao e-social.

![Imagem 7: MGE Pessoal>>Avançado>>Central do E-social](https://ajuda.sankhya.com.br/hc/article_attachments/16252563955223) MGE Pessoal>>Avançado>>Central do E-social

Efetue a transmissão novamente dos eventos anteriormente liberados.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16252563961111) OBSERVAÇÃO:**

A manutenção sobredita foi realizada no cenário no qual o funcionário **possui vinculo CLT e autônomo na mesma empresa**.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16252563966871) CAUSA:**

O erro em questão foi apresentado em virtude de existir uma regra de validação no leiaute do e-social que avalia o <nrInsc> relativo a tag <remunOutrEmpr> com base nos seguintes critérios:

**Validação:**

a) Se {tpInsc} for igual a [1], deve ser um CNPJ válido, diferente do CNPJ base indicado no registro de Informações do Empregador (S-1000) e dos estabelecimentos informados através do evento S-1005.

b) Se {tpInsc} for igual a [2], deve ser um CPF válido, diferente do CPF do trabalhador e, ainda, caso o empregador seja pessoa física, diferente do CPF do empregador.

c) Se {indApuracao} = [2] e {tpInsc} = [1], é permitido informar número de inscrição igual ao CNPJ base indicado no registro de Informações do Empregador (S-1000) e aos estabelecimentos informados através do evento S1005.

d) Se {indApuracao} = [2] e {tpInsc} = [2], é permitido informar número de inscrição igual ao CPF do empregador.
