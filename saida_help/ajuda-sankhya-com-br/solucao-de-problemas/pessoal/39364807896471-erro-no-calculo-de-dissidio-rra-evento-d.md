---
id: "39364807896471"
titulo: "Erro no cálculo de dissídio (RRA) - Evento DSR ausente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39364807896471-Erro-no-c%C3%A1lculo-de-diss%C3%ADdio-RRA-Evento-DSR-ausente"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:08Z"
rotulos: ["Configuração", "Eventos", "Folha", "Erro", "DSR", "Artigo criado KCS", "RRA", "Sankhya RH - KCS"]
---

# Erro no cálculo de dissídio (RRA) - Evento DSR ausente

**MENSAGEM**

O evento de DSR (Descanso Semanal Remunerado) não está sendo considerado no cálculo de dissídio (RRA), gerando diferenças nos valores  de RRA, mesmo que o DSR exista na folha de pagamento do mês de referência.

**SITUAÇÃO**

Ao calcular a folha de dissídio com eventos de RRA configurados, o sistema não demonstra os valores de DSR correspondentes aos eventos de hora extra, mesmo com os eventos de RRA criados e vinculados corretamente. O DSR aparece calculado na folha mensal normal, mas não é considerado no cálculo do dissídio.

Os **eventos de RRA (Rendimentos Recebidos Acumuladamente)** são eventos especiais utilizados para registrar valores pagos ao trabalhador que se referem a **anos anteriores ao ano do pagamento**. Esses valores têm um **tratamento tributário diferenciado**, sendo calculados separadamente da folha mensal para evitar tributação indevida.

## Quando Utilizar Eventos de RRA

Os eventos de RRA são aplicados em situações como:

- **Dissídio coletivo** com efeito retroativo em meses anteriores
- **Diferenças salariais** de períodos passados
- **Verbas reconhecidas judicialmente**
- **Ajustes de remuneração** pagos fora da competência original
- **Pagamentos retroativos** cujo pagamento ocorre em um ano calendário posterior ao da competência original

**SOLUÇÃO**

Para corrigir o problema, siga os passos abaixo:

**(1)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento de hora extra que está sendo utilizado no cálculo da folha do funcionário.
**(2)** Verifique se existe um evento personalizado ativo que possui a mesma característica do evento padrão de hora extra.
**(3)** Caso exista um evento personalizado ativo, desative-o temporariamente.
**(4)** Reative o evento padrão de hora extra que estava desativado.
**(5)** Acesse a tela **"Cálculo de Folha"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e recalcule a folha do funcionário.
**(6)** Verifique se os valores de **"DSR"** passaram a ser demonstrados corretamente no cálculo do dissídio.

**(7)** Confira se o evento de RRA correspondente ao **"DSR"** está criado e vinculado ao evento de DSR na aba **"Avançado"** do cadastro de eventos, no campo **"Evento de Diferença - RRA"**.

Artigo :

<https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA>

**CAUSA**

O problema ocorre porque o cálculo de DSR reconhece a característica do evento, e não apenas o evento efetivamente utilizado na folha. Quando um evento padrão de hora extra está desativado e sua característica foi vinculada a um evento personalizado, o sistema continua considerando o evento original (não utilizado no cálculo atual do funcionário) para o cálculo do DSR, o que impacta incorretamente os valores no dissídio.

Além disso, se o evento de DSR estiver desativado ou se não houver um **"Evento de Diferença - RRA"** vinculado ao evento de DSR, o sistema não conseguirá calcular corretamente as diferenças no dissídio.
