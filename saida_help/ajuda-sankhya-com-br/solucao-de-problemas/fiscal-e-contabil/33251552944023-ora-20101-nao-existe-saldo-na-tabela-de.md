---
id: "33251552944023"
titulo: "ORA-20101: Não existe saldo, na tabela de saldos por empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33251552944023-ORA-20101-N%C3%A3o-existe-saldo-na-tabela-de-saldos-por-empresa"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:29:13Z"
rotulos: ["Configuração", "Contabilidade", "Financeiro", "ORA-20101", "Lotes Contábeis", "lote", "saldo contábil", "Não existe saldo", "na tabela de saldos por empresa", "Erro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Recomposição de Saldos"]
---

# ORA-20101: Não existe saldo, na tabela de saldos por empresa

**MENSAGEM**

ORA-20101: Não existe saldo, na tabela de saldos para esta conta.

**SITUAÇÃO**

Este erro ocorre em diferentes situações relacionadas à **gestão contábil e financeira** do sistema:

- Ao tentar **alterar ou excluir lançamentos contábeis** na tela **"Lançamentos Contábeis"** (Contabilidade >> Lançamentos >> Lançamentos Contábeis)
- Ao tentar excluir lotes na tela **"Lotes Contábeis"** (Contabilidade >> Lançamentos >> Lotes Contábeis), principalmente em lotes gerados automaticamente

**SOLUÇÃO**

### Solução 1: Recomposição de Saldos Contábeis

Quando o erro ocorre em **lançamentos contábeis**, lotes ou balancetes, execute a recomposição de saldos:

Acesse a tela **"Empresa"** (Contabilidade >> Preferências >> Empresa).

No campo **"Referência p/ recomposição"**, informe a data do último mês correto. Exemplo: se janeiro está correto e fevereiro apresenta erro, informe 28/02/2025.

Clique no botão **"Outras Opções (...)"**.

Selecione a opção **"Recompor Saldos"**.

Confirme a operação e aguarde o processamento.

Após a conclusão, verifique se o problema foi resolvido gerando novamente o **"Balancete de Verificação"**.

### Solução 2: Verificação do Parâmetro CTBUTISALEMPORG

Se o erro persistir, verifique o parâmetro **"Utiliza Saldo Empresa Origem"** (**"CTBUTISALEMPORG"**) em **"Parâmetros do Sistema"** (Configurações >> Avançado >> Preferências). Para o processo padrão, este parâmetro deve permanecer desabilitado.

Onde na tela de preferências da empresa do contábil, pode ser realizado o mesmo processo de recomposição de saldos:

![Imagem 1: Onde na tela de preferências da empresa do contábil, pode ser realizado o mesmo processo de recomposição de saldos:](https://ajuda.sankhya.com.br/hc/article_attachments/40608856984983)

**CAUSA**

Este erro indica que o sistema não localizou um saldo registrado para a conta, empresa e data informadas na tabela de saldos. Isso é necessário para garantir a integridade das informações contábeis durante exclusões ou novos lançamentos.

- **Ausência de saldo implantado:** A conta não possui saldo inicial para o período.
- **Inconsistência nos saldos acumulados:** Desatualização devido a alterações manuais em lançamentos.
- **Data de movimentação anterior à implantação:** A operação tenta afetar um período sem controle de saldo.
- **Configuração de parâmetro:"CTBUTISALEMPORG"** habilitado indevidamente.
