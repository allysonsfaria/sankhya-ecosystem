---
id: "28116281875863"
titulo: "Aviso e Recibo de férias esta sendo gerado com dados e valores ''null''"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28116281875863-Aviso-e-Recibo-de-f%C3%A9rias-esta-sendo-gerado-com-dados-e-valores-null"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:26:06Z"
rotulos: ["Configuração", "Relatórios", "Preferências", "Folha", "Aviso e Recibo de férias esta sendo gerado com dados e valores ''null''", "Erro"]
---

# Aviso e Recibo de férias esta sendo gerado com dados e valores ''null''

**SITUAÇÃO:**

Aviso e Recibo de férias esta sendo gerado com dados e valores ''null''.

**SOLUÇÃO:**

**1. Quando utilizado um relatório padrão:**

**(1)** Acesse a tela **Configurações » Avançado » Preferências:**

- - Configure os parâmetros abaixo com o campo inteiro definido como 0 ou deixe em branco:
  - **FPRELATAVISOFER:** Aviso de Férias
  - **FPRELATRECFE:** Holerite de Férias

**2. Quando utilizado um relatório personalizado:**

**(1)** Acesse a tela **Configurações » Avançado » Preferências:**

Configure os parâmetros abaixo com o campo inteiro definido como o código do relatório formatado inserido na tela **Configurações » Avançado » Relatórios Formatados**:

- **FPRELATAVISOFER**: Aviso de Férias
- **FPRELATRECFE**: Holerite de Férias

**(1)**Após realizar as configurações, se o problema persistir, entre em contato com o Service Desk para análise detalhada do caso junto à equipe de Manutenção.

**CAUSA:**

Os parâmetros FPRELATAVISOFER e FPRELATRECFE não estão configurados para serem emitidos a partir do modelo padrão inseridos no fonte do sistema.
