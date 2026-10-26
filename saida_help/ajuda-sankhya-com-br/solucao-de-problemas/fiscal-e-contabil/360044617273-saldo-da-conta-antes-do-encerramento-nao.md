---
id: "360044617273"
titulo: "Saldo da conta antes do encerramento não corresponde ao total dos lançamentos de encerramento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617273-Saldo-da-conta-antes-do-encerramento-n%C3%A3o-corresponde-ao-total-dos-lan%C3%A7amentos-de-encerramento"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:11Z"
rotulos: ["#criadoRoger", "Configuração", "ECD", "Contabilidade", "Preferências", "Financeiro", "Problema: Saldo da conta antes do encerramento não confere com os lançamentos.", "Solução: Ajuste as configurações de período nas preferências da empresa e gere o arquivo ECD novamente.", "Causas: Configurações de período diferentes entre empresas datas incorretas zeramento inadequado ou lançamentos fora dos lotes de zeramento.", "Erro"]
---

# Saldo da conta antes do encerramento não corresponde ao total dos lançamentos de encerramento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18664709538455) MENSAGEM:**

Saldo da conta antes do encerramento não corresponde ao total dos lançamentos de encerramento.

**SOLUÇÃO:**

![Imagem 2: Contabilidade » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/18664709544855) Contabilidade » Preferências » Empresa

- Selecione as empresas que participam da consolidação de dados, e na aba: ECD-Escrituração Contábil Digital
- Campo: **Período de Geração das Demonstrações Contábeis** =  [marque uma unica opção, para todas as empresas da Consolidação.
- Ou seja se a empresa, 1, 2 e 3, participam da consolidação, todas devem ter uma unica opção neste campo.

![Imagem 3: Contabilidade » Conexão » ECD » Geração de Arquivo - ECD](https://ajuda.sankhya.com.br/hc/article_attachments/18664677158679)Contabilidade » Conexão » ECD » Geração de Arquivo - ECD

- Gere o arquivo novamente e transmiti-lo.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18664709552663) CAUSA:**

Ao tentar transmitir o arquivo ECD, o incidente ocorre. Quando a empresa é consolidada e as empresas de origem estão com a configuração do campo "Período de geração das demonstrações contábeis" localizado no menu Contabilidade>> Preferências>> Empresa>> aba ECD Escrituração fiscal digital está diferente entre as empresas por exemplo: uma empresa anual outra trimestral.

#### Outras causas que podem ensejar o erro são:

- A data de inicio da conta de resultado e/ou encerramento está superior a data dos lançamentos do I250;

Nesse caso, vá até o Plano de Contas e defina o campo **"Referência de ativação"** com uma data igual ao menor a data de geração do ECD.

- O zeramento das contas de resultado não foi executado corretamente, onde as contas permaneceram com saldos, mesmo após o encerramento.

Nesse caso, devemos **excluir os lotes de zeramento**, recompor os saldos do ano todo da empresa geradora do ECD e zerar novamente, nessa ordem.

- A forma de geração dos lotes de encerramento das contas de resultado, não bateu com a forma que foi configurado nas preferências da empresa na aba > ECD > campo "Período de Geração das Demonstrações Contábeis."

**Exemplo:** Fiz o zeramento trimestral das contas de resultado, ou seja, tenho 4 lotes de zeramento, informei no campo citado, a forma "anual".

- Quando há lançamentos para a conta de encerramento/apuração do resultado do exercício, fora dos lotes de zeramento das contas, o que não pode acontecer, visto que essa conta é exclusiva para os lançamentos de zeramento, não podendo ser usada para outros lançamentos/contabilizações;

Analise se alguma dessas possibilidade se encaixam com a situação atual da empresa geradora do ECD, e siga as instruções sugeridas.
