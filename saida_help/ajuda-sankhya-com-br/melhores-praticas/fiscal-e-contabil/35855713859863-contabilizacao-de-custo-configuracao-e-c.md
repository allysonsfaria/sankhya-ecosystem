---
id: "35855713859863"
titulo: "Contabilização de Custo – Configuração e Considerações Importantes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35855713859863-Contabiliza%C3%A7%C3%A3o-de-Custo-Configura%C3%A7%C3%A3o-e-Considera%C3%A7%C3%B5es-Importantes"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:24:30Z"
rotulos: ["Produtos", "Custos", "Configuração", "Agendamento", "Rotinas", "Contabilização", "Parâmetros", "Considerações Importantes", "Contabilização de Custo", "Usar custo", "fórmulas", "contábeis"]
---

# Contabilização de Custo – Configuração e Considerações Importantes

Para que a contabilização do custo de produtos ocorra corretamente no Sankhya, é fundamental que as fórmulas, cadastros e parâmetros estejam configurados conforme as melhores práticas.

As orientações completas sobre a configuração das fórmulas podem ser consultadas no artigo oficial:

[Melhores práticas de como utilizar a contabilização de custo de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046324753-Melhores-pr%C3%A1ticas-de-como-utilizar-a-contabiliza%C3%A7%C3%A3o-de-custo-de-produtos)

### Configuração do Agendamento da Contabilização

Além das configurações de fórmulas e contas contábeis, é indispensável que o agendamento da rotina de contabilização esteja parametrizado corretamente, garantindo que o sistema utilize os valores de custo na geração dos lançamentos.

Confira abaixo o passo a passo para a configuração:

**(1)** Acesse o menu: Contabilização» Rotinas» Agendamento >> Aba Parâmetros >> Campo Usar custo;

**(2)** Selecione o agendamento da rotina de contabilização de custo;

**(3)** Na aba Parâmetros, localize o campo;

**(4)** Marque esta opção.

**Pontos de atenção:**

- Quando o campo **“Usar custo”** estiver marcado, o sistema irá considerar os valores de custo dos produtos no momento de gerar os lançamentos contábeis.
- Caso não esteja marcado, a contabilização não irá considerar o custo.

![Imagem 1: Caso não esteja marcado, a contabilização não irá considerar o custo.](https://ajuda.sankhya.com.br/hc/article_attachments/36063518251159)

#### Importante:

- Certifique-se de que as fórmulas contábeis estejam configuradas corretamente no cadastro de fórmulas de contabilização da TOP de Contabilização**.**
- Verifique se o custo está devidamente calculado e atualizado nos produtos antes da execução da rotina, pode ser verificado na tela de Variação de Custo, ou via consulta SQL na TGFCUS.
- Após qualquer alteração nas fórmulas ou parâmetros, recomenda-se reprocessar o agendamento para garantir que as mudanças sejam aplicadas.
