---
id: "42427203131671"
titulo: "Saiba tudo sobre a regra de cálculo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427203131671-Saiba-tudo-sobre-a-regra-de-c%C3%A1lculo"
trilha: "PONTOTEL: Sistema de marcação de ponto > Administração"
atualizado_em: "2026-08-03T12:50:29Z"
rotulos: ["sync_hc", "pontotel_6a3328df0081a70a1de6c5bf", "sync_hash_9ae6df99a299", "pontotel"]
---

# Saiba tudo sobre a regra de cálculo

As **regras de cálculo** da Pontotel definem como o sistema interpreta as marcações de ponto e realiza o cálculo de horas, atrasos e adicionais. Essas regras são totalmente personalizáveis, permitindo que cada empresa configure o sistema conforme suas políticas internas de jornada e controle de ponto.
O sistema possibilita a criação de quantas regras de cálculo forem necessárias para atender aos diferentes cenários da organização. Como cada regra é vinculada ao cadastro do colaborador, é possível aplicar modelos distintos de cálculo dentro de um mesmo empregador ou local de trabalho, garantindo flexibilidade para adequar o sistema a diferentes contextos, cargos ou convenções coletivas.

Neste artigo, você vai entender como funcionam os principais tipos de cálculo, tolerâncias e configurações que impactam diretamente na apuração das horas dos colaboradores.

---

### ⚠️ Importante:

- A edição de regra de cálculo será aplicada a 100% dos colaboradores vinculados a essa regra, e vai gerar o recálculo de todas as folhas que estiverem **destravadas**. Antes de realizar qualquer alteração, recomendamos que todas as folhas já fechadas e pagas sejam **travadas**, evitando que apontamentos passados sejam modificados.
- Recomendamos fortemente que você entre em [contato](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0) com o nosso **time de Suporte** da Pontotel (ou com seu ponto de contato) antes de realizar qualquer alteração nas regras de cálculo. Como essas configurações impactam globalmente o processamento das horas dos colaboradores, modificações manuais podem gerar inconsistências graves e dificultar o fechamento da folha. Nossa equipe está à disposição para analisar sua necessidade e validar as mudanças com segurança.
- As alterações realizadas pelo usuário administrador da empresa são de total responsabilidade da própria empresa, que assume integralmente as mudanças e impactos que serão refletidos no sistema a partir da aplicação da nova configuração.

---

## Tipos de Cálculo

Os tipos de cálculo definem a forma como o sistema apura atrasos e horas extras da jornada de trabalho. Para configurar ou conferir o tipo de cálculo aplicado em uma regra vá no menu **Regras > Cálculo**. Clique sobre a regra de cálculo e então no ícone de lápis, para editar. O tipo de cálculo aplicado a essa regra será a primeira opção da lista em sua tela.

1. **Cálculo Flexível**

   - Considera a **duração total da jornada**, sem exigir horários fixos de entrada e saída. O sistema soma as horas efetivamente trabalhadas e os períodos abonados aplicáveis e compara o total com a jornada obrigatória. Se o total ultrapassar a jornada, a diferença é hora extra; se faltar, gera atraso ou débito.
   - O colaborador pode bater o ponto em horários diferentes, desde que cumpra a carga horária total prevista.
     🧩 Exemplo: jornada de 8h: 7h41 trabalhadas + 1h18 abonadas = 8h59 consideradas; o saldo é de 59 minutos de hora extra.
2. **Cálculo Fixo**

   - Valida os **horários exatos** de entrada, saída e intervalos. O cálculo considera a entrada e a saída cadastradas para gerar atrasos ou horas extras.
   - Nesse modelo, é possível gerar atraso e hora extra no mesmo dia se as batidas ocorrerem fora do horário configurado.
     🧩 Exemplo: jornada 09h–18h → registro antes das 09h gera hora extra; depois das 09h, atraso.
3. **Cálculo Híbrido**

   - Combina os dois modelos (fixo + flexível). Permite que o colaborador tenha liberdade para iniciar ou encerrar o expediente em horários variados, desde que cumpra sua carga horária total e respeite as **janelas de entrada e saída** configuradas na regra de cálculo.
   - Para que essa flexibilidade seja controlada, utilizamos dois conceitos fundamentais na configuração:
   - **Como o sistema processa o cálculo:**
   - **Dentro da Janela:** Enquanto o colaborador faz sua marcação dentro dos limites (para trás ou para frente), o sistema calcula a jornada por **duração** (modelo flexível).
   - **Fora da Janela:** Caso o colaborador entre antes ou depois desses limites configurados, o sistema passa a processar o cálculo como **fixo** (por horário). Isso significa que marcações fora da janela podem gerar atrasos ou horas extras automáticas, dependendo da sua configuração.
     🧩 Exemplo: jornada 09h–18h → é preciso cumprir 9h e respeitar a janela configurada pela empresa.

---

🧩 Exemplo: jornada 09h–18h → é preciso cumprir 9h e respeitar a janela configurada pela empresa.

---

## Como o intervalo e a saída antecipada afetam o saldo

No cálculo, o tempo trabalhado a mais durante o intervalo pode ser compensado por uma saída antecipada no mesmo dia. Por exemplo, se o intervalo previsto é de 1 hora, mas o colaborador pausa por apenas 29 minutos, há 31 minutos trabalhados a mais no intervalo. Se a saída ocorrer 51 minutos antes do horário previsto, o sistema compensa os 31 minutos e o saldo final será de 11 minutos de débito/extra positiva, conforme o fechamento do dia.

A tolerância configurada também pode alterar o resultado: uma entrada às 06h56, em uma jornada iniciada às 07h00 com tolerância de 5 minutos, não altera o cálculo.

---

## Tolerâncias

É considerado uma tolerância o período de minutos que não gera impacto no cálculo da jornada. Ela serve para desconsiderar pequenos atrasos ou adiantamentos, tanto na entrada e saída (tolerância de atraso), quanto no início ou fim da jornada (tolerância para hora extra). Se a empresa define 10 minutos de tolerância, por exemplo, o sistema ignora atrasos ou permanências de até 10 minutos, não registrando como atraso nem como hora extra.

1. **Atraso**

   - Define quantos minutos o colaborador pode se atrasar antes que o sistema gere um apontamento de atraso.
     🧩 Exemplo: Numa jornada com entrada às 09h com tolerância de 5 minutos → atraso só contabiliza a partir das 09h06.
2. **Hora Extra**

   - Determina o tempo de tolerância antes e depois da jornada para que o sistema comece a contabilizar horas extras.
     🧩 Exemplo: Numa jornada com saída às 18h com tolerância de 5 minutos → hora extra só é contabilizada após 18h06.

---

## Folha / Espelho de Ponto

Nesse menu você terá algumas opções de configuração de exibição do espelho de ponto de seus colaboradores, assim como a configuração da regra de correção automática de pontos na folha.

### Correção Automática

Define o funcionamento das correções automáticas de ponto na folha dos colaboradores em situações de esquecimento ou excesso de marcações. Quando há períodos configurados nesse menu, o sistema utiliza essas definições como critérios para lançar ou anular pontos automaticamente, reduzindo o trabalho manual de correção das folhas.

- **Adição:** completa batidas faltantes com base na jornada.
  🧩 Exemplo: jornada 08h–17h → se o colaborador registrou apenas o ponto de entrada às 08h, o sistema completa a jornada com o lançamento de um ponto manual de saída às 17h (o horário será lançado de forma britânica, de acordo com a jornada prevista no dia).
- **Anulação:** anula batidas com intervalo menor que o limite configurado.
  🧩 Exemplo: o colaborador possui dois registros de ponto com 1 min de diferença e limite configurado é de 10 min → o mais recente é anulado, mantendo apenas 1 ponto.

OBS: Caso todos os campos estejam configurados como 0 (zero) minutos, o comportamento de correção/anulação automáticos não será aplicado.

### Configurações opcionais

(Folha/Espelho de Ponto)

Essas opções ajustam o que será exibido ou calculado automaticamente na folha e no espelho de ponto:

✅ **Gerar folha com apontamentos finais:** mostra o total mensal de apontamentos no rodapé.
✅ **Mostrar apontamentos por dia:** exibe os apontamentos diários no PDF da folha.
✅ **Ignorar valores zerados:** oculta apontamentos com valor 0 no consolidado do colaborador.
✅ **Permitir cálculos com marcações faltantes:** Permite que o sistema calcule a jornada mesmo sem o registro de ponto de saída, desde que existam pontos pares registrados.
Exemplo: se houver apenas o registro de entrada e saída de pausa, o sistema considerará a saída de pausa como o fim da jornada. Quando essa opção estiver desativada, o cálculo da jornada só será realizado se houver pontos pares completos, com registros de entrada e saída.

---

## Apontamentos

No menu “Apontamentos”, é possível configurar quais registros serão exibidos no sistema e no PDF do espelho de ponto do colaborador. Cada apontamento pode ser exibido em apenas uma das telas ou ser ocultado, conforme a necessidade. Além disso, é possível personalizar a nomenclatura dos apontamentos, ajustando-os à terminologia e às práticas da sua empresa.

1. **O que mostrar**

   - Define quais apontamentos (como horas extras ou pausas) serão exibidos no sistema e/ou no PDF (Espelho de ponto). Você pode configurar cada apontamento para aparecer apenas em uma das telas ou optar por ocultá-lo. Quando um apontamento é ocultado, ele **não é considerado** nos cálculos nem exibido em relatórios consolidados, como o R05, R01 e E02.
2. **Nomear apontamentos**

   - Permite renomear os tipos de horas exibidos nos relatórios e no sistema para uma melhor adequação ao cenário da sua empresa.
     🧩 Exemplo: alterar “Horas extras extraordinárias” para “Hora Extra 100%”.

> 💡 Dica: Essas configurações são essenciais para garantir que os cálculos e relatórios (como o R01) reflitam corretamente as regras internas da empresa. Caso perceba alguma divergência nos cálculos ou na exibição dos apontamentos, revise as configurações das abas citadas acima.

---

O sistema Pontotel permite que cada empresa defina suas próprias regras de cálculo, assegurando que os apontamentos, folhas e relatórios estejam sempre em conformidade com as políticas internas e a legislação vigente. A tela de Regra de Cálculo está disponível para usuários administradores e pode ser editada conforme necessidade. No entanto, recomendamos máxima cautela ao realizar qualquer alteração nas regras já configuradas.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
