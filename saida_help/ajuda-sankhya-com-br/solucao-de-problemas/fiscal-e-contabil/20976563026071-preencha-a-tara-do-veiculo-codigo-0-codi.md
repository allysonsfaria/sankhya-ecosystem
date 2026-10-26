---
id: "20976563026071"
titulo: "Preencha a 'Tara' do veiculo Codigo: 0 Codigo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20976563026071-Preencha-a-Tara-do-veiculo-Codigo-0-Codigo"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:50:25Z"
rotulos: ["ERROMDFE", "MDF-e", "Veículo", "Configuração", "Transporte", "CORE_E04595"]
---

# Preencha a 'Tara' do veiculo Codigo: 0 Codigo

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/20976563014167) **MENSAGEM:**

[CORE\_E04595] Preencha a 'Tara' do veiculo Código: 0

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20976563019543)SOLUÇÃO:**

Verifique na aba Geral do MDF-e se o campo Veículo de tração esta preenchido, caso não esteja, precisa realizar o preenchimento.

Provavelmente a viagem vai estar confirmada, então ou precisa realizar uma nova viagem incluindo a informação corretamente ou alterar o STATUSDOC para E, na tabela TGFVIAG.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/20976563020695)CAUSA:**

Ausência da informação do Veiculo na aba Geral do MDF-e ou ausência da informação da tara dentro da tela Veículos.
