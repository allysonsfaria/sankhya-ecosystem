---
id: "39311697185559"
titulo: "Por que o valor do DSR está incorreto na rescisão?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39311697185559-Por-que-o-valor-do-DSR-est%C3%A1-incorreto-na-rescis%C3%A3o"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:40Z"
rotulos: ["Configuração", "Eventos", "Feriados", "Folha de Pagamento", "Rescisão", "DSR", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Por que o valor do DSR está incorreto na rescisão?

Ao conferir a folha de rescisão, observa-se que o valor do Descanso Semanal Remunerado (DSR) sobre verbas variáveis, como horas extras, adicional noturno ou comissões, apresenta valor diferente do esperado, aparentemente incorreto ou muito próximo ao valor da verba utilizada como base de cálculo.

Esse comportamento pode estar relacionado ao período de apuração do ponto, à fórmula configurada para o evento, à quantidade de dias úteis e não úteis considerados no cálculo ou ao cadastro de feriados.

Por isso é necessário realizarmos algumas verificações:

### Configuração do dia de apuração do ponto

O período utilizado para calcular o DSR é definido pelo campo **Dia de apuração do ponto**, configurado na tela **Empresas** (Pessoal+ » Cadastros » Empresas).

Por exemplo, quando o dia de apuração está configurado como **21**, o sistema considera o período compreendido entre o dia **22 do mês anterior** e o dia **21 do mês atual**. Dessa forma, a apuração não necessariamente corresponde ao primeiro e ao último dia do mês.

**(1)**  Acesse a tela **"Empresas"** (Pessoal+ » Cadastros » Empresas) e selecione a empresa desejada.

**(2)**  Localize o campo **"Dia de apuração do ponto"** e se necessário ajuste para o dia correto conforme a política da empresa.

**(3)**  Caso realize alterações, recalcule a folha de rescisão.

![Imagem 1: (3) Caso realize alterações, recalcule a folha de rescisão.](https://ajuda.sankhya.com.br/hc/article_attachments/41585612248855)

### Fórmula personalizada do DSR

O **"DSR"** utiliza uma fórmula personalizada que contém variáveis específicas para apurar o período trabalhado. A fórmula padrão geralmente segue a estrutura:

**IF(&DIASUTEISTRAB 0, (@E\_HORAEXTRA50 / &DIASUTEISTRAB) \* &DIASNAOUTEISTRAB, 0)**

Esta fórmula realiza o seguinte cálculo:

- Verifica se há dias úteis trabalhados maiores que zero.
- Divide o valor das horas extras pelos dias úteis trabalhados.
- Multiplica o resultado pelos dias não úteis trabalhados.
- Retorna zero caso não haja dias úteis trabalhados.

Em rescisões, quando o colaborador trabalha poucos dias dentro do período de apuração, a proporção entre dias úteis e dias não úteis pode resultar em um valor de DSR muito próximo ou até igual ao valor da verba utilizada como base de cálculo.

### Feriados e dias não úteis no período

Os feriados existentes no período de apuração também são considerados como dias não úteis no cálculo do DSR.

Caso existam feriados cadastrados incorretamente ou que não pertençam ao período efetivamente trabalhado pelo colaborador, o valor do DSR poderá ser alterado.

Verifique o cadastro de feriados na tela **"Feriados"** (Pessoal+ » Cadastros » Feriados) e ajuste conforme necessário para apuração correta.

## ⚠️ Observações importantes

- O sistema já possui **feriados nacionais pré-cadastrados**
- Feriados **estaduais e municipais** devem ser cadastrados manualmente
- O cadastro incorreto de feriados pode gerar valores errados no cálculo do DSR
- Feriados cadastrados indevidamente devem ser removidos para evitar problemas nos cálculos

**☑️ Recorrente**: Marque se o feriado ocorre todos os anos (o sistema manterá o cadastro automaticamente para os próximos anos)

### Evento de DSR não aparece na rescisão

Se o evento de **"DSR"** não está aparecendo na folha de rescisão, verifique se o evento está configurado para aparecer também em rescisões. Para corrigir:

1. **(1)** Acesse a tela de **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento desejado.
2. **(2)** Verifique se a opção **"Rescisão"** está marcada na regra de cálculo do evento.
3. **(3)** Salve as alterações e recalcule a folha de rescisão.
