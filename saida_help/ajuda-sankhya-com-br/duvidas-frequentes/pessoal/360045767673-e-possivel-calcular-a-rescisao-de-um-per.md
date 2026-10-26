---
id: "360045767673"
titulo: "É possível calcular a rescisão de um período que já houve cálculo mensal da folha?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045767673-%C3%89-poss%C3%ADvel-calcular-a-rescis%C3%A3o-de-um-per%C3%ADodo-que-j%C3%A1-houve-c%C3%A1lculo-mensal-da-folha"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:27:54Z"
rotulos: ["#criadoRoger", "#textmining", "#validadorogerXlorrana28102020", "Folha de Pagamento", "Gerenciador de Folhas", "Rescisão", "Configuração Funcionários", "Excluir cálculo mensal para calcular rescisão.", "Cálculo só na competência do mês.", "Duplicidade ocorre se calcular duas folhas.", "Erro", "Artigo atualizado KCS", "Sankhya RH - KCS"]
---

# É possível calcular a rescisão de um período que já houve cálculo mensal da folha?

**MENSAGEM**

Não é possível calcular a rescisão, pois o funcionário possui uma folha de pagamento calculada em uma data posterior à data de demissão.

**SITUAÇÃO**

Esta situação ocorre quando o usuário tenta gerar o **"Cálculo de Rescisão"**  de um funcionário que já possui a folha de pagamento mensal calculada na mesma competência da data de demissão. Por exemplo, um funcionário desligado em 30/01/2026 que já teve o salário de janeiro/2026 calculado e processado anteriormente.

**SOLUÇÃO**

Siga os passos abaixo:

**(1)** Acesse a tela de **"Gerenciador de folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e localize o cálculo mensal da competência em que ocorreu a demissão para o funcionário. 

**(2)** Exclua o cálculo da folha mensal referente à competência da rescisão. Esta exclusão é necessária para liberar o sistema para processar a rescisão.

**(3)** Após a exclusão da folha mensal, acesse a tela de **"Cálculos"** (Pessoal+ » Rotinas Folha » Cálculos) e realize o cálculo da rescisão normalmente.

**CAUSA**

O sistema Sankhya possui um comportamento padrão de bloqueio que impede o cálculo de rescisão quando a folha mensal da mesma competência já foi calculada e processada. Este controle existe porque o sistema entende que a competência já está em processamento ou consolidada para a folha mensal, evitando assim conflitos de cálculo e inconsistências nos valores processados.
