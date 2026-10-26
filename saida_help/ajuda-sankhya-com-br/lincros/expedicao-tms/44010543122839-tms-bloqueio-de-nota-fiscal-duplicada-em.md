---
id: "44010543122839"
titulo: "[TMS] - Bloqueio de Nota Fiscal Duplicada em Ordem de Coleta (permitirMultiplasOrdensNota)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010543122839--TMS-Bloqueio-de-Nota-Fiscal-Duplicada-em-Ordem-de-Coleta-permitirMultiplasOrdensNota"
trilha: "Lincros > TMS > Expedição - TMS"
atualizado_em: "2026-10-05T18:40:43Z"
rotulos: ["sync_hc", "lincros", "sync_hash_0c1edbaa0e8e", "lincros_15293365"]
---

# [TMS] - Bloqueio de Nota Fiscal Duplicada em Ordem de Coleta (permitirMultiplasOrdensNota)

**Menu:** Expedição > Coletas > Ordem de Coleta

**Objetivo:** Configurar o sistema para que uma nota fiscal já vinculada a uma ordem de coleta não possa ser incluída em outra, evitando duplicidades e impactos operacionais.

## Visão Geral

Por padrão, o TMS permite que uma mesma nota fiscal seja adicionada a mais de uma ordem de coleta. Esse comportamento pode gerar divergências operacionais, como a mesma NF sendo coletada duas vezes ou rastreada de forma incorreta.

Para evitar isso, o sistema conta com o parâmetro **permitirMultiplasOrdensNota**, que, quando desativado, bloqueia a inserção de uma nota fiscal em uma nova ordem de coleta caso ela já esteja vinculada a outra.

## Como funciona

Quando o parâmetro **permitirMultiplasOrdensNota** está com valor **false**:

- Ao tentar adicionar uma nota fiscal em uma ordem de coleta, o sistema verifica se essa NF já pertence a outra ordem;
- Se já estiver vinculada, o sistema exibe uma mensagem de alerta/bloqueio informando que a nota já está associada a outra ordem de coleta;
- A inclusão é impedida, garantindo que cada nota fiscal esteja em apenas uma ordem de coleta por vez.

Quando o parâmetro está com valor **true** (padrão do sistema), o comportamento acima não se aplica e a duplicidade de vínculo é permitida.

## Onde configurar

A configuração é realizada em:

**Cadastros Gerais > Configurações de Empresa > Parâmetros > Empresa**

Localize o parâmetro:

→ **permitirMultiplasOrdensNota**

Para ativar o bloqueio, defina o valor como **false**.
Para permitir múltiplos vínculos (comportamento padrão), mantenha o valor como **true**.

**Importante:** A alteração desse parâmetro vale para todas as rotinas do sistema que criam ou importam documentos em ordens de coleta — tanto pela inclusão manual quanto pela importação automática.

## Quando usar essa configuração

Essa configuração é recomendada para empresas que:

- Trabalham com alto volume de ordens de coleta e precisam garantir a unicidade do vínculo de cada NF;
- Identificaram casos de uma mesma nota aparecendo em mais de uma ordem de coleta, gerando divergências operacionais;
- Desejam ter maior controle e rastreabilidade sobre as notas vinculadas a cada coleta.

## Como solicitar a configuração

A ativação ou desativação do parâmetro **permitirMultiplasOrdensNota** é realizada pelo time de Suporte da Lincros. Para solicitar, basta abrir um chamado informando:

- A empresa/unidade na qual deseja aplicar a configuração;
- O valor desejado: **false** (bloquear duplicidade) ou **true** (permitir múltiplos vínculos).

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos."
