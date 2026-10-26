---
id: "360043995274"
titulo: "Como inserir os eventos que não apresentaram no relatório de Termo de Rescisão?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043995274-Como-inserir-os-eventos-que-n%C3%A3o-apresentaram-no-relat%C3%B3rio-de-Termo-de-Rescis%C3%A3o"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-09-29T12:12:22Z"
rotulos: ["#criadoRoger", "#revisadohugnei", "Configuração", "Eventos", "Relatórios", "MGEPessoal", "Eventos que não apresentaram no relatório de Termo de Rescisão", "Preencha eventos na aba \"Eventos\"", "Verifique e imprima", "Recibos", "Termo de Rescisão"]
---

# Como inserir os eventos que não apresentaram no relatório de Termo de Rescisão?

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17126968762903) SOLUÇÃO:**

![Imagem 2: Acesse: MGEPessoal > Relatórios > Recibos > Rescisões.](https://ajuda.sankhya.com.br/hc/article_attachments/17126968767255) Acesse: MGEPessoal > Relatórios > Recibos > Rescisões.

Antes de extrair o relatório, acesse a aba **"Eventos"** e informe nos campos (espaços) em branco disponíveis os eventos do cálculo da rescisão, que não são informativos, de acordo com seu tipo (Proventos/Descontos).

Alguns campos dessa relação tem sua descrição padrão, pois segue a Portaria 1057 do MTE. Os campos que podem ter sua descrição alterada estão em branco, e neles podem ser informados qualquer descrição e código de um evento que não está previsto na Portaria.

Quando o usuário tentar emitir um TRCT - Termo de Rescisão do Contrato de Trabalho o qual falta algum evento do cálculo ser informado na aba Eventos, automaticamente o sistema irá emitir a mensagem e a impressão não se conclui:

---------------------------
MGE - Pessoal

Informe os eventos: XXXX na aba Eventos desta tela.
---------------------------

Se for inserido um evento que é um Provento na relação de Desconto, o sistema emite a critica e vice-e-versa:
---------------------------
Atenção!
 O evento XXXX que você está lançando é um Provento e você está tentando informar seu código no local destinado aos Descontos.
---------------------------

Deve ser observado um detalhe, que são os eventos de Faltas e Descontos DSR, o qual possui um campo específico nessa aba para serem informados. Uma vez informados nos seus respectivos campos, esses eventos não devem constar na relação 'Descontos' desta aba.

![Imagem 3: Após os ajustes, salve o registro e clique em "Visualizar/Imprimir" .](https://ajuda.sankhya.com.br/hc/article_attachments/17126968771607) Após os ajustes, salve o registro e clique em **"Visualizar/Imprimir"**.
