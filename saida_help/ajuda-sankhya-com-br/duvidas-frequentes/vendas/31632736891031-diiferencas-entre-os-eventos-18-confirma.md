---
id: "31632736891031"
titulo: "Diiferenças entre os Eventos 18 - Confirmação de Nota e  Evento 44 - Liberação Exigida pela TOP."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31632736891031-Diiferen%C3%A7as-entre-os-Eventos-18-Confirma%C3%A7%C3%A3o-de-Nota-e-Evento-44-Libera%C3%A7%C3%A3o-Exigida-pela-TOP"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-08-01T01:20:22Z"
rotulos: ["Configuração", "Eventos", "Liberação de Limites", "TOP", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "diferenças entre eventos", "Evento 44", "Eventos 18", "Confirmação de Nota", "Liberação Exigida pela TOP", "Artigo atualizado KCS", "CVE - KCS", "Plataforma - KCS"]
---

# Diiferenças entre os Eventos 18 - Confirmação de Nota e  Evento 44 - Liberação Exigida pela TOP.

No Sankhya, o controle de confirmações de lançamentos pode ser configurado por meio de eventos específicos que garantem maior segurança e aderência às regras de negócio da organização. Dois desses eventos, bastante utilizados para este controle, são o **"Evento 18 - Confirmação de Nota"** e o **"Evento 44 - Liberação Exigida pela TOP"**.

Embora ambos tenham como objetivo principal controlar a confirmação de lançamentos (compras, vendas, pedidos etc.), eles possuem características e aplicações distintas, são elas:

### Evento 18

É acionado quando está marcada a opção **"Exigir Liberação antes da Confirmação"**, disponível no cadastro de **"Tipos de Operação (TOP)"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP).

Esse evento é utilizado para impedir que um lançamento seja confirmado sem uma liberação prévia. Caso não esteja configurado corretamente para o usuário, pode impedir o faturamento e travar o processo de vendas da empresa. Tanto um lançamento de R$ 100,00 quanto um de R$ 1.000,00 podem ser liberados por qualquer usuário que possua permissão para o **"Evento 18".**

**Em resumo:**

- Não considera o valor do lançamento;
- Basta que o usuário tenha vínculo com o evento para realizar a liberação;
- Foco no controle por tipo de operação, sem restrição financeira;
- Não pode ser utilizado na Liberação de Cascata.

### Evento 44

Entra em ação quando está habilitada a opção **"Sempre exigir Liberação"** na TOP. O **"Evento 44"** considera o valor total do lançamento para definir se o usuário está apto a liberá-lo. Dessa forma, a permissão para liberação depende de o usuário possuir um limite de liberação igual ou superior ao valor do lançamento.

**Em síntese:**

- Considera o valor do lançamento;
- Requer limite de liberação compatível;
- Proporciona maior controle financeiro;
- Pode ser utilizado na Liberação em Cascata.

### Não chegou e-mail de liberação do Evento 44

Caso o e-mail de liberação do **"Evento 44"** não seja enviado, verifique:

Acesse a tela **"Usuários"** (Configurações >> Cadastros >> Usuários) e verifique se o usuário liberador possui e-mail válido.

 Confirme se o **"Servidor SMTP"** está corretamente configurado (Configurações >> Avançado >> Servidor SMTP).

 Verifique se a **"Conta SMTP"** está ativa (Configurações >> Avançado >> Conta SMTP).

 Verifique se o argumento "-Dsankhyaw.schedule.disable" está desabilitado no servidor.

 Se utilizar modelo personalizado, valide o campo **"Modelo de E-mail"** em (Comercial >> Preferências >> Empresa).

 Após os ajustes, execute um teste de envio gerando uma nova solicitação.
