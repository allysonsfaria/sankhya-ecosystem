---
id: "12607633043607"
titulo: "Erros de validação do arquivo ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12607633043607-Erros-de-valida%C3%A7%C3%A3o-do-arquivo-ECD"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:00:46Z"
rotulos: ["Configuração", "Relatórios", "ECD", "Contabilidade", "Financeiro", "Diferença no saldo final do Ativo e Passivo", "I051 obrigatório sem vínculo", "Número de ordem duplicado na DRE", "Erro"]
---

# Erros de validação do arquivo ECD

Segue abaixo orientações sobre os erros apresentados:

![Imagem 1: O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000…](https://ajuda.sankhya.com.br/hc/article_attachments/16362981188503) O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000 (COD\_PLAN\_REF).
--> O erro é apresentado quando existem contas sem o vínculo com o plano de contas referencial. Nesse caso será necessário vincular as contas no plano de contas, aba 'Conta Contábil Referencial'.

![Imagem 2: Campo obrigatório não preenchido --> No cadastro do plano de contas, existem algumas contas sem a classificação no…](https://ajuda.sankhya.com.br/hc/article_attachments/16362981191191) Campo obrigatório não preenchido
--> No cadastro do plano de contas, existem algumas contas sem a classificação no campo **'Grupo de Conta**' para informar se a conta é de ativo, passivo, resultado, etc.

![Imagem 3: Campo obrigatório não preenchido --> No cadastro do plano de contas, existem algumas contas sem a classificação no…](https://ajuda.sankhya.com.br/hc/article_attachments/16362981192855) Saldo da conta antes do encerramento não corresponde ao total dos lançamentos de encerramento.
--> Para o que o sistema gere o lote de encerramento no arquivo, será necessário acessar a tela **"Lotes contábeis"** e para o lote de zeramento das contas de resultado em Dezembro/2019, informe no campo observação a frase: Encerramento das Contas de Resultado.

Para um correto zeramento de contas de resultado, devemos recompor o saldo das contas contábeis do ano todo nas preferências da empresa da contabilidade e, somente depois, efetuar o zeramento das contas.

![Imagem 4: Para um correto zeramento de contas de resultado, devemos recompor o saldo das contas contábeis do ano todo nas…](https://ajuda.sankhya.com.br/hc/article_attachments/16362981207959) No Balanço Patrimonial, o somatório do saldo final do Ativo está diferente do somatório do saldo **final** do Passivo.

![Imagem 5: No Balanço Patrimonial, o somatório do saldo inicial do Ativo está diferente do somatório do saldo inicial do Passivo.](https://ajuda.sankhya.com.br/hc/article_attachments/16362996120471) No Balanço Patrimonial, o somatório do saldo inicial do Ativo está diferente do somatório do saldo **inicial** do Passivo.

![Imagem 6: No Balanço Patrimonial, o valor do saldo final do último nível do Ativo deve ser igual ao valor do saldo final do…](https://ajuda.sankhya.com.br/hc/article_attachments/16362996122007) No Balanço Patrimonial, o valor do saldo final do último nível do Ativo deve ser igual ao valor do saldo **final** do último nível do Passivo e Patrimônio Líquido.

![Imagem 7: No Balanço Patrimonial, o valor do saldo inicial do último nível do Ativo deve ser igual ao valor do saldo inicial do…](https://ajuda.sankhya.com.br/hc/article_attachments/16362996124183) No Balanço Patrimonial, o valor do saldo inicial do último nível do Ativo deve ser igual ao valor do saldo **inicial** do último nível do Passivo e Patrimônio Líquido.
---> Os erros acima se referem a diferenças no fechamento do saldo do Balanço Patrimonial.

**ITENS 4 ao 7:** no artigo a seguir é possível verificar como fazer as ações para solução: [No Balanço Patrimonial, o somatório do saldo final do Ativo está diferente do somatório do saldo final do Passivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/14970240850327)

![Imagem 8: ITENS 4 ao 7: no artigo a seguir é possível verificar como fazer as ações para solução: No Balanço Patrimonial, o…](https://ajuda.sankhya.com.br/hc/article_attachments/16362996136215) O mesmo número de ordem foi informado em mais de uma linha da DRE.

![Imagem 9: Na Demonstração de Resultado, o saldo do código de aglutinação totalizador está diferente do somatório do saldo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16362996139159) Na Demonstração de Resultado, o saldo do código de aglutinação totalizador está diferente do somatório do saldo de todos os registros de nível imediatamente inferior.

![Imagem 10: Valor do saldo informado na linha de detalhe da Demonstração de Resultado é diferente do resultado calculado com base…](https://ajuda.sankhya.com.br/hc/article_attachments/16362981239703) Valor do saldo informado na linha de detalhe da Demonstração de Resultado é diferente do resultado calculado com base nos registros de saldos periódicos e de saldos de resultado.
---> Na estrutura da DRE, tela **"Demonstrativos ECD"**, foram criados 3 novos campos nesse novo layout, sendo eles: 'Numero de ordem', 'Indicador de saldo inicial' e 'indicador de saldo final'.

**\*** O campo **"Número de ordem"** deverá ser preenchido em ordem crescente conforme o numero de linhas da estrutura.
**\*** Os campos **"Indicador de saldo inicial"** e **"Indicador de saldo final"** deverão ser preenchidos conforme os saldos se credor ou devedor.

![Imagem 11: É obrigatória a assinatura de, no mínimo, um contador/contabilista(qualificação 900) e de um representante legal. -->…](https://ajuda.sankhya.com.br/hc/article_attachments/16362996147863) É obrigatória a assinatura de, no mínimo, um contador/contabilista(qualificação 900) e de um representante legal.
--> No registro J930 é necessário a assinatura de um representante legal da empresa e um contador.

Para configuração, acesse a tela 'Contabilidade>preferências>empresa', aba **"Signatários"** e preencha com os dados faltantes.
