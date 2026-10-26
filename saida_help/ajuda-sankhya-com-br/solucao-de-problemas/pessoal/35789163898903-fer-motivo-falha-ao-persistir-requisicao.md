---
id: "35789163898903"
titulo: "Fer Motivo: Falha ao persistir requisição Falha ao persistir funcionário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35789163898903-Fer-Motivo-Falha-ao-persistir-requisi%C3%A7%C3%A3o-Falha-ao-persistir-funcion%C3%A1rio"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:21:06Z"
rotulos: ["Requisições", "Contrato", "Folha", "Motivo", "Configuração Funcionários", "requisição", "Pessoal+", "Erro", "Falha", "funcionário", "ao persistir"]
---

# Fer Motivo: Falha ao persistir requisição Falha ao persistir funcionário

**MENSAGEM:**

Falha
Não foi possível confirmar requisição pendente.
Motivo: Falha ao persistir requisição.
Falha ao persistir funcionário.

![Imagem 1: Falha Não foi possível confirmar requisição pendente. Motivo: Falha ao persistir requisição. Falha ao persistir…](https://ajuda.sankhya.com.br/hc/article_attachments/35789163895319)

**SITUAÇÃO:**

Ao tentar aprovar uma requisição pendente, o sistema apresenta a mensagem de falha.

**SOLUÇÃO:**

**(1)** Acesse o **''Pessoal+''** (Rotinas Folha» Requisições);

**(2)** Localize o campo ''**Vínculo''** e altere temporariamente para '**'Prazo Indeterminado**''**;**

**(3)** Retorne à tela da requisição e tente aprovar novamente, o processo será concluído com sucesso;

**(4)** Após a aprovação, volte ao cadastro do funcionário;

**(5)** Restaure o vínculo para **“Prazo Determinado”;**

**(6)** Preencha o campo **“Objeto determinante da contratação por prazo determinado”** (campo obrigatório para este tipo de vínculo).

**(7)** Salve o cadastro para que o erro não volte a ocorrer.

**Observações importantes:** 

- O campo Objeto determinante da contratação por prazo determinado é exigido pela legislação trabalhista e deve estar sempre preenchido quando o vínculo for Prazo Determinado.
- Caso o funcionário esteja realmente dispensado do período de experiência, avalie se o vínculo por prazo determinado é o mais adequado para o caso.

**CAUSA:**

O erro ocorre quando o vínculo do funcionário está definido como Prazo Determinado e, ao mesmo tempo, a opção ''**Dispensado da experiência''** está habilitada.

Essa combinação de configurações impede o sistema de registrar corretamente os dados do funcionário, ocasionando falha na gravação da requisição.

![Imagem 2: Essa combinação de configurações impede o sistema de registrar corretamente os dados do funcionário, ocasionando falha…](https://ajuda.sankhya.com.br/hc/article_attachments/36315771166871)
