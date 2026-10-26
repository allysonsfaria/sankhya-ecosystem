---
id: "43546520534295"
titulo: "Mensagem de advertência crédito do trabalhador Código da natureza da rubrica: 9253"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546520534295-Mensagem-de-advert%C3%AAncia-cr%C3%A9dito-do-trabalhador-C%C3%B3digo-da-natureza-da-rubrica-9253"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-18T11:14:54Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Mensagem de advertência crédito do trabalhador Código da natureza da rubrica: 9253

**Mensagem**

Durante o envio dos eventos de remuneração "S-1200", "S-2299" ou "S-2399", foi identificado desconto de empréstimo consignado para o trabalhador, porém os dados do contrato (instituição financeira e/ou número do contrato) informados estão divergentes do registrado no Portal Emprega Brasil para a competência, ou não há parcela registrada para o desconto informado.

**Situação**

Ao processar a folha de pagamento e enviar os eventos ao eSocial, o sistema identificou que o desconto de empréstimo consignado (rubrica 9253) foi lançado para o colaborador, porém o contrato informado está incorreto ou não corresponde ao que está registrado no Portal Emprega Brasil para a competência em questão. Isso pode gerar advertências ou rejeições no eSocial, impedindo o correto processamento dos eventos.

O lançamento do empréstimo consignado (rubrica 9253) é obrigatório para registrar descontos de crédito do trabalhador, especialmente os provenientes do eConsignado (Emprega Brasil), na folha de pagamento. O correto preenchimento garante a conformidade com o eSocial e evita advertências e rejeições.

**Solução**

**(1)** Acesse a tela **"Lançamento de Movimento"** (Pessoal+ Rotinas Folha Lançamento de Movimento) e filtre a empresa, referência (mês/ano) e o funcionário indicado na advertência.

**(2)** Localize a rubrica de **"Empréstimo Consignado"** Pessoal+ » Cadastros » Eventos (rubrica 9253) e verifique a configuração da rubrica. Eventos padrões apresentam as configurações do sistema. Caso esteja personalizado necessário verificar.

- Antes de lançar o desconto, certifique-se de que a rubrica 9253 (Empréstimo eConsignado) foi enviada ao eSocial via evento S-1010.
- Isso garante que o evento de desconto será reconhecido pelo eSocial.

  **(3)** Ajuste os campos **"Instituição Financeira"** e/ou **"Contrato eConsignado"** conforme os dados corretos do Portal Emprega Brasil para a competência.
- Ao lançar ou editar o evento 9253, preencha:
  - Instituição Financeira
  - Número do Contrato eConsignado
  - Valor da Parcela (conforme arquivo do Emprega Brasil)
  - Observação (opcional, mas recomendada para controle)
- Certifique-se de que os dados informados coincidem exatamente com os do arquivo oficial.

**(4)** Salve as alterações e recalcule a folha do funcionário.

**(5)** No **"Gerenciador de Folhas"** (Pessoal+ Rotinas Folha Gerenciador de Folhas), libere a folha para o eSocial.

**(6)** Acesse a **"Central do eSocial"** (Pessoal+ Rotinas Folha Central do eSocial), gere novamente o evento de remuneração e efetue o envio.

**(7)** Após o ajuste, o evento de remuneração deverá ser recepcionado com sucesso pelo eSocial, sem advertências.

**Pontos de Atenção e Solução de Problemas**

- **Advertência 1988:**
  Ocorre quando há divergência entre os dados do sistema e os do Portal Emprega Brasil (instituição financeira ou número do contrato).
  **Solução:** Edite o lançamento, ajuste os dados conforme o arquivo oficial, salve, recalcule a folha e reenvie o evento ao eSocial.
- **Advertência 1989:**
  Indica que foi informado desconto de empréstimo, mas não há parcela prevista para a competência no Portal Emprega Brasil.
  **Solução:** Exclua o lançamento e recalcule a folha. Só lance descontos previstos no arquivo oficial.
- **Erro de Importação:**
  Se aparecer mensagem como “Não há funcionário cadastrado com o CPF, matrícula e data admissão informados”, revise os dados cadastrais do funcionário e ajuste conforme necessário.
- **Lançamentos Manuais:**
  Evite lançamentos manuais para empréstimos eConsignado. Sempre que possível, utilize o importador para garantir a correta ordenação e evitar erros.

---

**Resumo**

- Sempre utilize o arquivo oficial do Emprega Brasil para importar os descontos.
- Preencha corretamente todos os campos obrigatórios (instituição, contrato, valor).
- Valide os dados cadastrais do funcionário.
- Libere a folha para o eSocial e envie os eventos na ordem correta.
- Corrija imediatamente qualquer advertência ou erro apresentado pelo sistema.

**Causa**

A advertência ocorre quando o empregador informa um desconto de empréstimo consignado (rubrica 9253) com dados de contrato divergentes ou inexistentes em relação ao Portal Emprega Brasil para a competência informada. Isso pode acontecer por erro de digitação, atualização incorreta do contrato ou falta de importação dos dados corretos do empréstimo para o sistema.
