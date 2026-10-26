---
id: "360044353413"
titulo: "Como ajustar data/hora através do servidor Linux?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044353413-Como-ajustar-data-hora-atrav%C3%A9s-do-servidor-Linux"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:57:52Z"
rotulos: ["#PUBLIFER", "#EnviadoporJoãoGomes", "Configuração", "Servidor", "Linux", "Ajuste de Data/Hora no Linux", "Data e Hora"]
---

# Como ajustar data/hora através do servidor Linux?

![Imagem 1: Acesse o servidor com o usuário root (senha de posse/responsabilidade da empresa) e execute o comando abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17154216514071) Acesse o servidor com o usuário root (senha de posse/responsabilidade da empresa) e execute o comando abaixo:

**# date {mmddhhmiyyyy.ss}**

Sendo:

- mm: Mês (dois dígitos ex: 04 = Abril);
- dd: Dia do mês (dois dígitos de 01 até 31);
- hh: Hora (formato de 24 horas);
- mi: Minutos (dois dígitos de 00 até 60);
- yyyy: Ano (quatro dígitos);
- ss: Segundos (dois dígitos de 00 até 60).

![Imagem 2: Para alterar a data e hora do sistema para: 8 de Abril de 2012, 15h 53min e 13seg, pode-se fazer o comando: date…](https://ajuda.sankhya.com.br/hc/article_attachments/17154216517783) Para alterar a data e hora do sistema para: 8 de Abril de 2012, 15h 53min e 13seg, pode-se fazer o comando:

**date 040815532012.13**

**Fonte**: <https://www.vivaolinux.com.br/dica/Data-e-hora-do-sistema>

**![Imagem 3: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17154184292887) IMPORTANTE:**

Recomenda-se que os comandos acima sejam executados por um profissional de T.I da empresa. Vale ressaltar que tratam-se de recomendações para facilitar/agilizar situações causadas no sistema, em que o motivo está relacionado a infra, dessa forma, uma responsabilidade da empresa.
