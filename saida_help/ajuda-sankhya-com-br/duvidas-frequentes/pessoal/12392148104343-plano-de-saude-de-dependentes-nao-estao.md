---
id: "12392148104343"
titulo: "Plano de saúde de dependentes não estão sendo importados na DIRF - 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12392148104343-Plano-de-sa%C3%BAde-de-dependentes-n%C3%A3o-est%C3%A3o-sendo-importados-na-DIRF-2025"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:25:23Z"
rotulos: ["Configuração", "Eventos", "Impostos", "DIRF", "eSocial", "Gerenciador de Folhas", "Central do eSocial", "Plano de Saúde de Dependentes Não Importados na DIRF", "Artigo atualizado KCS", "Sankhya RH - KCS"]
---

# Plano de saúde de dependentes não estão sendo importados na DIRF - 2025

**MENSAGEM**

Os valores referentes a descontos de mensalidade, coparticipação e taxa do plano de saúde não estão sendo incluídos na geração do arquivo da DIRF.

**SITUAÇÃO**

Ao gerar o **"Informe de Rendimentos"** ou a **"DIRF"**, os valores de plano de saúde (mensalidade, coparticipação e taxa de inclusão) não aparecem no campo **"Plano privado coletivo de assistência à saúde"**. Quando o informe é gerado pelo cálculo, os valores aparecem corretamente, mas quando exportado pelo retorno do eSocial, os valores não são apresentados.

**SOLUÇÃO**

Para corrigir esta situação, siga os passos abaixo:

**(1)** Acesse a tela **"Eventos"** (Configurações >> Módulo Pessoal >> Eventos) e localize os eventos relacionados ao plano de saúde, como: **"Plano de Saúde Dependente"**, **"Taxa de Inclusão"**, **"Coparticipação Titular"** e **"Coparticipação Dependente"**.

**(2)** Verifique se o campo “Código de Incidência de IRRF” (CODINCIRRF) está corretamente configurado para cada evento. A natureza da rubrica no eSocial deve estar adequada para garantir que os valores sejam devidamente considerados na DIRF.

Para o ano-calendário de 2025, o código de incidência correto é 67.

**(3)** Caso seja identificado que a configuração estava incorreta e foi corrigida recentemente, será necessário realizar o reenvio das retificações do evento S-1010 – Tabela de Rubricas.

O evento S-1010 deve ser enviado com a data de início de vigência correta (início do ano-calendário). Após o envio correto do S-1010, será necessário retificar os eventos S-1210 das competências em que os valores não foram considerados no Informe de Rendimentos.

**(4)** Acesse a tela **Gerenciador de Folhas** e realize o bloqueio das folhas e referências dos funcionários que necessitam da retificação. Em seguida, acesse a Central do eSocial e gere o evento S-1210 para envio a exclusão do evento. 

**(5)** Retorne no **Gerenciador de Folhas** e realize a liberação das folhas bloqueadas anteriormente. 
Em seguida, acesse a Central do eSocial novamente e gere S-1210 para envio da nova inclusão. 

**(6)** Verifique também se os dependentes dos funcionários estão com o plano de saúde cadastrado corretamente. Acesse a tela **"Dependentes"** (Módulo Pessoal >> Cadastros >> Dependentes) e confirme se todos os dependentes que possuem o benefício estão devidamente registrados.

**(7)** Adicionalmente, acesse a tela “Geração de Guia” (Módulo Pessoal), selecione o tipo de guia “DIRF” e clique na opção “Demonstrativo de Rendimentos”.

Em seguida, informe o ano desejado para geração (por exemplo, 2025) e selecione a forma de geração, podendo ser “eSocial” ou “Folha de Pagamento”.

**CAUSA**

Este problema ocorre quando os eventos de plano de saúde estão com a natureza da rubrica incorreta no eSocial, especificamente no campo **"Código de Incidência de IRRF"** (CODINCIRRF). Quando os eventos são enviados ao eSocial com configuração inadequada, os valores não são considerados na geração da DIRF.
