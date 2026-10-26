---
id: "36345463407127"
titulo: "Parâmetro LOGTABMAXAGE – Controle de Retenção da Tabela de Log TGLATS (LOGTABOPER) e suas dependências"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36345463407127-Par%C3%A2metro-LOGTABMAXAGE-Controle-de-Reten%C3%A7%C3%A3o-da-Tabela-de-Log-TGLATS-LOGTABOPER-e-suas-depend%C3%AAncias"
trilha: "Manual do Produto > Plataforma e Integrações > Plataforma"
atualizado_em: "2026-10-14T17:06:33Z"
rotulos: ["Configuração", "Preferências", "LOGTABOPER", "Tabela de Log TGLATS", "TGLATS", "Retenção de Tabela", "Squad Plataforma", "LOGTABMAXAGE", "Tabela de Log"]
---

# Parâmetro LOGTABMAXAGE – Controle de Retenção da Tabela de Log TGLATS (LOGTABOPER) e suas dependências

**SITUAÇÃO:**

O parâmetro **LOGTABMAXAGE** define, em dias, o período em que o sistema manterá os registros de alterações armazenados tabela **TGLATS**, responsável por consolidar o log de operações habilitando pelo parâmetro **''**[**LOGTABOPER**](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es)**''**.

O **LOGTABMAXAGE** estabelece por quanto tempo o histórico permanecerá disponível antes que o processo automático de limpeza remova os registros antigos, evitando o crescimento excessivo da tabela e contribuindo para a saúde e o desempenho do banco de dados.

Já o ''LOGTABOPER'', controla quais entidades terão os registros de alteração habilitados e estabelece o início do processo de captura desses eventos.

Ambos os parâmetros possuem funções complementares no controle de registro e retenção de logs. O **LOGTABMAXAGE** tem valor padrão de 3 dias, enquanto o **LOGTABOPER** vem desativado por padrão.

Quando ambos estão ativos, o sistema passa a registrar as operações e, posteriormente, remove automaticamente os registros antigos conforme o período definido no LOGTABMAXAGE.

**SOLUÇÃO:**

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou Descrição''** pesquise pelo parâmetro ''**LOGTABMAXAGE''.**

**(3)** Informe o número de dias desejado para retenção.

(Permitidos de **3 a 7 dias**. O sistema **não aceita valores fora desse intervalo**).

**(4)** Salve as alterações.

**(5)** O sistema aplicará o novo período de retenção no próximo ciclo automático de limpeza.

**Para entender melhor como esses parâmetros atuam na prática, é importante conhecer o fluxo de registro e processamento do log de alterações:**

- **LOGTABOPER:** quando ativado, habilita o registro de alterações nas entidades configuradas.
- **Micromódulo Instance Logs Monitor:** recebe os eventos gerados pelo LOGTABOPER e inicia o tratamento dessas informações.

As alterações capturadas **não são gravadas diretamente na TGLATS**. Primeiro, o micromódulo registra os dados na tabela temporária **Temp\_TGLATS\_V2**, que armazena os eventos recém-processados.

Periodicamente, um **job interno** transfere esses registros da Temp\_TGLATS\_V2 para a tabela final **TGLATS**, aplicando as validações e transformações necessárias. Após a importação bem-sucedida, a Temp\_TGLATS\_V2 é limpa automaticamente, mantendo apenas registros pendentes ou recém-recebidos, evitando acúmulo de dados antigos.

A **TGLATS**, por sua vez, consolida os dados definitivos e é tratada pelo processo de limpeza configurado pelo parâmetro **LOGTABMAXAGE**, que define o período de retenção.

Esse modelo **desacopla a captura do log do processamento final**, evitando bloqueios, minimizando impacto no desempenho e garantindo estabilidade mesmo em ambientes com alto volume de operações.

##### DICAS:

- Evite configurar períodos de retenção muito elevados, pois isso pode resultar no crescimento desnecessário da tabela TGLATS.
- Ambientes com grande volume de operações, uma retenção prolongada pode causar impacto direto no desempenho do banco de dados.
- Ajuste o valor conforme a necessidade operacional e de acordo com a capacidade do ambiente.
- Após realizar qualquer alteração no parâmetro, monitore o comportamento da tabela nos primeiros dias para validar o impacto e garantir que o desempenho permaneça adequado.
