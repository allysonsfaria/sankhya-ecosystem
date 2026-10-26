---
id: "37362619505047"
titulo: "Falha. Não foi possível realizar a finalização da referência.  Motivo: ORA-01427: a subconsulta de uma única linha retorna mais de uma linha."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37362619505047-Falha-N%C3%A3o-foi-poss%C3%ADvel-realizar-a-finaliza%C3%A7%C3%A3o-da-refer%C3%AAncia-Motivo-ORA-01427-a-subconsulta-de-uma-%C3%BAnica-linha-retorna-mais-de-uma-linha"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:17Z"
rotulos: ["Configuração", "Portal RH", "Carga Horária", "ORA-01427", "Erro", "Finalização da referência", "Escala real de trabalho", "inconsistência na carga horária", "Parametrização correta de horários turnos e descansos"]
---

# Falha. Não foi possível realizar a finalização da referência.  Motivo: ORA-01427: a subconsulta de uma única linha retorna mais de uma linha.

**MENSAGEM:**

“Falha. Não foi possível realizar a finalização da referência.

Motivo: ORA-01427: a subconsulta de uma única linha retorna mais de uma linha.”

![Imagem 1: Motivo: ORA-01427: a subconsulta de uma única linha retorna mais de uma linha.”](https://ajuda.sankhya.com.br/hc/article_attachments/37362619501591)

**SOLUÇÃO:**

**(1)** Acesse a tela **''Carga Horária''** (Pessoal+ » Cadastros » Carga Horária).

**(2)** Busque o colaborador desejado.

**(3)** Verifique os dias e turnos de trabalho, conferindo se algum dia foi marcado incorretamente como descanso ou feriado.

**(4)** Corrija a quarta-feira (ou outro dia com erro) para refletir a jornada real de trabalho.

**(5)** Salve as alterações e tente novamente finalizar a referência.

##### OBSERVAÇÃO:

- A parametrização correta de **horários, turnos e descansos** é essencial para o funcionamento do Portal RH.
- Inconsistências na jornada podem gerar erros técnicos e impedir o fechamento de referências.
- Sempre valide se os dias e turnos estão configurados conforme a **escala real de trabalho**.

##### CAUSA:

O erro ocorre devido a uma **inconsistência na carga horária**, na qual a quarta-feira estava configurada como dia de descanso no turno da tarde, quando, na realidade, trata-se de um dia normal de trabalho.

Essa divergência entre a jornada real e a parametrização do horário gera conflito nas validações do sistema, ocasionando o erro durante a finalização da referência no Portal RH.

![Imagem 2: Essa divergência entre a jornada real e a parametrização do horário gera conflito nas validações do sistema,…](https://ajuda.sankhya.com.br/hc/article_attachments/37450965352727)
