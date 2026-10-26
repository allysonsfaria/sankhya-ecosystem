---
id: "39355325439639"
titulo: "Como proceder quando o cálculo de rescisão não aparece no Gerenciador de Folhas?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39355325439639-Como-proceder-quando-o-c%C3%A1lculo-de-rescis%C3%A3o-n%C3%A3o-aparece-no-Gerenciador-de-Folhas"
trilha: "Melhores Práticas > Documentação de processos"
atualizado_em: "2026-07-22T13:48:26Z"
rotulos: ["Configuração", "Folha de Pagamento", "Gerenciador de Folhas", "Rescisão", "Pessoal+", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como proceder quando o cálculo de rescisão não aparece no Gerenciador de Folhas?

No sistema Sankhya,  podem ocorrer situações em que o cálculo de rescisão não aparece no **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas), especialmente quando há folhas mensais já calculadas na mesma competência ou quando existem referências anteriores em aberto. Este artigo orienta sobre as principais causas e soluções para este cenário.

### Rescisão bloqueada por folha mensal calculada

O sistema Sankhya possui um comportamento padrão que impede o cálculo de rescisão quando a folha mensal da mesma referência já foi calculada e processada. Isso ocorre porque o sistema entende que a competência já está consolidada para a folha mensal.

Por exemplo, se um funcionário foi desligado em 30/01/2026 e o salário de janeiro já havia sido pago no mesmo dia, ao tentar gerar a rescisão contratual, o sistema exibirá uma mensagem informando que não é possível calcular a rescisão, pois o funcionário possui uma folha de pagamento calculada em uma data posterior à data de demissão.

**Solução:**

**(1)** Acesse o **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas).

**(2)** Localize a folha mensal da competência em que deseja calcular a rescisão.

**(3)** Exclua o cálculo da folha mensal dessa competência.

**(4)** Após a exclusão da folha mensal, realize o cálculo da rescisão normalmente.

### Rescisão não aparece por referências anteriores abertas

Outra situação comum é quando a opção de fechamento de folha não está disponível no **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) para determinada referência. Isso ocorre porque o sistema exige uma ordem cronológica para o fechamento das competências.

Se existirem referências anteriores abertas, o sistema impedirá o fechamento ou visualização adequada da referência atual, incluindo os cálculos de rescisão.

**Solução:**

**(1)** Acesse o **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas).

**(2)** Verifique se existem referências anteriores em aberto.

**(3)** Feche todas as referências anteriores seguindo a ordem cronológica.

**(4)** Após fechar as referências mais antigas, a opção para a referência desejada aparecerá e o cálculo de rescisão poderá ser visualizado e processado normalmente.

### Considerações importantes

Ao trabalhar com rescisões coletivas ou individuais, sempre verifique:

- Se há folhas mensais calculadas na mesma competência da rescisão;
- Se todas as referências anteriores estão fechadas corretamente;
- Se o sistema está atualizado na versão mais recente do módulo pessoal.

Seguindo estas orientações, o cálculo de rescisão será processado corretamente e aparecerá no **"Gerenciador de Folhas"** conforme esperado.
