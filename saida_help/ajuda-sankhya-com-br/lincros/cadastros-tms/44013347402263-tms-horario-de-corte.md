---
id: "44013347402263"
titulo: "[TMS] - Horário de Corte"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013347402263--TMS-Hor%C3%A1rio-de-Corte"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:55:13Z"
rotulos: ["sync_hc", "lincros", "lincros_13432663", "sync_hash_0a090756ea55"]
---

# [TMS] - Horário de Corte

**Menu**: Cadastros gerais > Modelo de distribuição > Critérios de seleção > Horário de corte > Empresa/Unidade

**Objetivo:**A tela de cadastro de horários de corte da empresa, permite inserir informações para melhor cálculo dos prazos de entregas, tanto para clientes quanto para a transportadora.

## Considerações:

- Este cadastro deve ser realizado manualmente via botão novo encontrado na tela de listagem de horário de corte;

Tela de listagem:

![Imagem 1: Tela de listagem:](https://ajuda.sankhya.com.br/hc/article_attachments/44013336729367)

Tela de edição de horário de corte

![Imagem 2: Tela de edição de horário de corte](https://ajuda.sankhya.com.br/hc/article_attachments/44013322907287)

- **Descrição:** este campo determina o título definido para o horário de corte;
- **Horário inicial:** este campo determina o horário inicial da (período) de corte;
- **Horário final:** este campo determina o horário final do período de corte;
- **Unidade:** É possível selecionar uma ou mais de uma unidade para esse horário de corte. Ao deixar em branco, entende-se que o horário de corte é para a empresa toda.

## Horários de cortes passando por dois dias:

Existe uma regra neste cadastro tratando registros do mesmo dia. Para casos onde o período inicial de horário de corte é em dia e finaliza em outro, indicamos gravar dois registros, por exemplo:

Horário Inicial: 22:00h

Horário Final: 06:00h

Neste cenário é necessário que crie dois registros no sistema:

1. Horário Inicial: 22:00h → Horário Final: 23:59h
2. Horário Inicial: 00:00h → Horário Final: 06:00h

## Horários de cortes entrelaçados:

Existe também uma regra para o cadastro, verificando o entrelaçamento dos horários, por exemplo:

1. Horário Inicial: 08:00h → Horário Final: 13:00h
2. Horário Inicial: 12:00h → Horário Final: 18:00h

Neste caso o sistema irá indicar que uma faixa de horário não pode estar dentro de outra faixa de horário (como das 12 às 13 horas, no exemplo)

Além do horário é verificado se o registro 1 (08h às 13h) são para todas as unidades ou somente para alguma unidade específica, pois se o registro 2 (12h às 18h) for para outras unidades, o sistema não irá impedir a gravação do registro.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
