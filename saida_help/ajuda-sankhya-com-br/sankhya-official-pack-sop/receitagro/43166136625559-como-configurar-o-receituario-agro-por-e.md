---
id: "43166136625559"
titulo: "Como configurar o Receituário Agro por empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43166136625559-Como-configurar-o-Receitu%C3%A1rio-Agro-por-empresa"
trilha: "Sankhya Official Pack - SOP > ReceitAgro"
atualizado_em: "2026-09-08T11:25:59Z"
rotulos: ["Configuração ReceitaAgro", "Produtor Rural", "produtor rural às empresas", "Receituário Agro", "Agrônomo", "REC_CONFPOREMP"]
---

# Como configurar o Receituário Agro por empresa

A preferência **''REC\_CONFPOREMP – Configurações por empresa Receituário''** permite segregar as credenciais de integração do Receituário Agro por empresa. Com a preferência ligada, cada empresa passa a utilizar a própria credencial da plataforma **WebReceita**, e os cadastros de **Agrônomo/Responsável Técnico** e de **Produtor Rural** são vinculados às credenciais ativas correspondentes.

Este artigo apresenta o passo a passo completo da configuração — da ativação da preferência até a emissão do receituário.

### Antes de começar

- Obtenha uma credencial de integração na plataforma **WebReceita** para cada empresa que emitirá receituários.
- Garanta acesso à tela **Preferências** (**Configuração > Avançado**).
- Mantenha um único cadastro por CPF/CNPJ para cada agrônomo e para cada produtor rural. A separação por empresa é feita pelas abas de vínculo, e não por cadastros duplicados.

| **IMPORTANTE**  Na emissão do receituário é utilizada a credencial da **empresa informada na nota**. Por isso, os cadastros de **Agrônomo** e de **Produtor Rural** precisam estar vinculados a essa credencial.  Sem esse vínculo, os registros não são apresentados na pesquisa dos campos correspondentes. |
| --- |

### Passo 1: Ativar a preferência

Acesse: **Configuração > Avançado**

1. No campo de pesquisa, informe ''**REC\_CONFPOREMP''** ou localize a preferência em **Configurações > Diversas > Receituário**.
2. Selecione a preferência **Configuração por empresa Receituário**.
3. No campo **Ligado/Desligado**, selecione **Ligado**.
4. Confirme a alteração.

![Imagem 1: Confirme a alteração.](https://ajuda.sankhya.com.br/hc/article_attachments/43166136596119)

Tela Preferências com a preferência REC\_CONFPOREMP ligada.

Com a preferência ativa, a segregação de credenciais por empresa fica disponível nas telas de cadastro do Receita Agro.

### Passo 2: Cadastrar as credenciais de cada empresa

Acesse: **Receita Agro > Cadastros > Configuração ReceitaAgro**

1. Clique em **Incluir**.
2. Informe a **Empresa** e a **Plataforma** correspondente.
3. Preencha as credenciais de integração fornecidas pela plataforma (**Client ID**, **Client Secret** e demais campos exigidos).
4. Mantenha o campo **Ativo** como **Sim** e confirme o registro.
5. Repita o procedimento para cada empresa que emitirá receituários.

![Imagem 2: Repita o procedimento para cada empresa que emitirá receituários.](https://ajuda.sankhya.com.br/hc/article_attachments/43166136598295)

Uma linha de configuração para cada empresa, com a respectiva credencial.

| **OBSERVAÇÃO**  Cadastre apenas **uma configuração ativa por empresa**. A coluna **Cód. Configuração** identifica cada credencial registrada. |
| --- |

### Passo 3: Vincular o agrônomo às empresas

Acesse: **Receita Agro > Cadastros > Agrônomo**

Mantenha **um único cadastro por agrônomo** (um cadastro por CPF/CNPJ). O vínculo com a credencial de cada empresa é feito pela aba **Agrônomo por Empresa**.

1. Posicione no cadastro do agrônomo desejado.
2. Acesse a aba **Agrônomo por Empresa**.
3. Clique em **Exportar Agrônomo** para enviar o cadastro à credencial da empresa. Para atualizar registros já integrados, utilize **Sincronizar Agrônomos**.
4. Confirme a mensagem **“Agrônomo exportado com sucesso”**.
5. Repita o procedimento para cada empresa em que o agrônomo deve estar disponível.

![Imagem 3: Repita o procedimento para cada empresa em que o agrônomo deve estar disponível.](https://ajuda.sankhya.com.br/hc/article_attachments/43166136606359)

Aba Agrônomo por Empresa: uma linha para cada empresa integrada.

Após a exportação, a aba apresenta o **Id Origem** de cada empresa — o identificador do cadastro na plataforma externa. O mesmo agrônomo recebe um **Id Origem diferente em cada credencial**, conforme os exemplos abaixo.

![Imagem 4: Após a exportação, a aba apresenta o Id Origem de cada empresa — o identificador do cadastro na plataforma externa. O…](https://ajuda.sankhya.com.br/hc/article_attachments/43166095123607)

Credencial da EMPRESA PADRÃO (empresa 1): o agrônomo recebeu o ID 584.

![Imagem 5: Credencial da EMPRESA PADRÃO (empresa 1): o agrônomo recebeu o ID 584.](https://ajuda.sankhya.com.br/hc/article_attachments/43166136608279)

Credencial da EMPRESA 2 TESTE (empresa 2): o mesmo agrônomo recebeu o ID 585.

### Passo 4: Vincular o produtor rural às empresas

Acesse: **Receita Agro > Cadastros > Produtor**

A lógica é a mesma do agrônomo: mantenha **um único cadastro por produtor** (um cadastro por CPF/CNPJ) e realize o vínculo pela aba **Produtor Rural por empresa**.

1. Posicione no cadastro do produtor desejado.
2. Acesse a aba **Produtor Rural por empresa**.
3. Clique em **Exportar Produtores** para enviar o cadastro à credencial da empresa.
4. Observe se a aba apresenta uma linha para cada empresa integrada, com o respectivo **Id Origem**.

![Imagem 6: Observe se a aba apresenta uma linha para cada empresa integrada, com o respectivo Id Origem .](https://ajuda.sankhya.com.br/hc/article_attachments/43166095126167)

Aba Produtor Rural por empresa com o produtor integrado às empresas 1 e 2.

### Como funciona na emissão do receituário

Na emissão, o sistema utiliza a credencial da **empresa informada na nota** e apresenta apenas os cadastros já integrados a essa credencial.

#### Exemplo prático

- O receituário é emitido para a **Empresa 2 – EMPRESA 2 TESTE**.
- O **Parceiro 290** está vinculado ao **Produtor 244 – TESTE**, já integrado à credencial da empresa 2 na aba **Produtor Rural por empresa**.
- Ao abrir a pesquisa do campo **Cód. Resp. Técnico**, o sistema apresenta somente os agrônomos integrados à empresa 2.

![Imagem 7: Ao abrir a pesquisa do campo Cód. Resp. Técnico , o sistema apresenta somente os agrônomos integrados à empresa 2.](https://ajuda.sankhya.com.br/hc/article_attachments/43166136616727)

Pesquisa do campo Cód. Resp. Técnico filtrada pela empresa informada na nota.

**Resultado:** o receituário é emitido na credencial da empresa 2, com o produtor de **Id Origem 1063611** e o agrônomo de **Id Origem 585** — identificadores dos cadastros na plataforma externa.

### Dúvidas frequentes

- ##### O agrônomo não aparece na pesquisa do campo Cód. Resp. Técnico. O que verificar?

##### Confirme se o cadastro do agrônomo foi exportado para a credencial da empresa informada na nota. Acesse Receita Agro > Cadastros > Agrônomo, aba Agrônomo por Empresa, e verifique se existe uma linha com essa empresa e com o Id Origem preenchido.

- ##### É necessário criar um cadastro de agrônomo ou de produtor para cada empresa?

Não. Mantenha um único cadastro por CPF/CNPJ e realize a vinculação pelas abas **Agrônomo por Empresa** e **Produtor Rural por empresa**.

- ##### O que acontece com a preferência desligada?

Com a preferência **REC\_CONFPOREMP** desligada, não há segregação de credenciais por empresa e o comportamento anterior do Receituário Agro é mantido.
