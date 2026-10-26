---
id: "39357794738711"
titulo: "Como configurar o desconto de plano de saúde por valor fixo em vez de percentual?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39357794738711-Como-configurar-o-desconto-de-plano-de-sa%C3%BAde-por-valor-fixo-em-vez-de-percentual"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:57Z"
rotulos: ["Configuração", "eSocial", "Folha de Pagamento", "Plano de Saúde", "Artigo criado KCS", "Sankhya RH - KCS", "Dependente", "Valor Fixo"]
---

# Como configurar o desconto de plano de saúde por valor fixo em vez de percentual?

No ERP Sankhya, o desconto do **"Plano de Saúde"** pode ser configurado de duas formas: por **"Percentual"** ou por **"Valor fixo"**. Quando o campo **"Percentual Empresa"** está preenchido, o sistema interpreta que a empresa custeará aquele percentual do convênio, e o restante será descontado do colaborador. Para que o desconto seja aplicado por **"Valor fixo"**, remova o percentual e configure o valor diretamente no evento correspondente.

### Ajuste no cadastro de dependentes

Quando o campo **"Percentual Empresa"** está preenchido com 100% no cadastro do dependente, o sistema entende que o custo do convênio médico será integralmente custeado pela empresa, não gerando desconto na folha do colaborador.

Para corrigir essa situação e permitir que o desconto seja aplicado corretamente:

**(1)** Acesse a tela **"Dependentes"** (Pessoal+ » Cadastros » Configuração Funcionários) e localize o cadastro do dependente vinculado ao plano de saúde.
**(2)** Remova o valor do campo **"Percentual Empresa"**, deixando-o em branco ou zerado.

![Imagem 1: Salve as alterações e recalcule a folha de pagamento para que o desconto passe a ser exibido corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/41303006963863)
**(3)** Salve as alterações e recalcule a folha de pagamento para que o desconto passe a ser exibido corretamente.

### Diferença entre movimento fixo e mensal

É importante compreender que o evento de **"Plano de Saúde"** pode ser lançado de duas formas no sistema:

**"Movimento Fixo"**: o valor é mantido automaticamente nas competências seguintes, sem necessidade de novo lançamento manual.

**"Movimento Mensal"**: o valor precisa ser ajustado manualmente a cada competência ou após alterações.

Quando o ajuste de valor é aplicado apenas ao movimento mensal, ele não reflete automaticamente nos meses seguintes. Por isso, ajuste o valor diretamente no evento após o fechamento da competência.

### Ajuste do valor do evento

Para ajustar o valor do evento de **"Plano de Saúde"** e garantir que o desconto seja aplicado corretamente nas próximas competências:

**(1)** Conclua o fechamento da competência desejada.
**(2)** Acesse a rotina **"Lançamento de Movimentos"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento).
**(3)** Localize o evento correspondente ao **"Plano de Saúde"**.

![Imagem 2: Clique no ícone de "Lápis" para editar o evento e ajuste o valor para o montante desejado.](https://ajuda.sankhya.com.br/hc/article_attachments/41303016215063)
**(4)** Clique no ícone de **"Lápis"** para editar o evento e ajuste o valor para o montante desejado.

![Imagem 3: (4) Clique no ícone de "Lápis" para editar o evento e ajuste o valor para o montante desejado.](https://ajuda.sankhya.com.br/hc/article_attachments/41303006966039)

**(5)** Salve as alterações para que o valor passe a ser descontado corretamente na folha do colaborador nas próximas competências.

### Validação da referência inicial

Outro ponto de atenção é o campo **"Referência Inicial"** no cadastro do plano de saúde. Se o colaborador já possuía o plano em uma competência anterior, mas o campo está configurado com uma data posterior, isso pode gerar erros no envio de eventos ao **"e-Social"**.

Para corrigir:

**(1)** Acesse o cadastro do **"Plano de Saúde"** (Pessoal+ » Cadastros » Configuração Funcionários).
**(2)** Verifique o campo **"Referência Inicial"** e ajuste para a competência correta em que o plano foi iniciado.

![Imagem 4: (1) Acesse o cadastro do "Plano de Saúde" (Pessoal+ » Cadastros » Configuração Funcionários). (2) Verifique o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/41303006966807)

**(3)** Salve as alterações e reenvie o evento ao e-Social, se necessário.

💡 Artigos sobre a rotina:

<https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527-Cadastro-e-V%C3%ADnculo-de-Plano-de-Sa%C3%BAde>

<https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959-Encerramento-de-Plano-de-Sa%C3%BAde-Titular-e-Dependente>

<https://ajuda.sankhya.com.br/hc/pt-br/articles/36028541845655-Hist%C3%B3rico-de-plano-de-sa%C3%BAde-n%C3%A3o-aparece-na-tela-de-Configura%C3%A7%C3%A3o-de-Funcion%C3%A1rios>

Seguindo essas orientações, o desconto do **"Plano de Saúde"** será aplicado corretamente, seja por valor fixo ou percentual, garantindo a conformidade com a folha de pagamento e os envios ao e-Social.
