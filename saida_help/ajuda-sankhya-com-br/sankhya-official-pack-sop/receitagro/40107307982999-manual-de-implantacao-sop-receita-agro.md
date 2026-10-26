---
id: "40107307982999"
titulo: "Manual de Implantação: SOP Receita Agro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40107307982999-Manual-de-Implanta%C3%A7%C3%A3o-SOP-Receita-Agro"
trilha: "Sankhya Official Pack - SOP > ReceitAgro"
atualizado_em: "2026-09-08T11:24:42Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Princípios Ativos", "Integração", "TOP", "Sankhya ID", "Implantação", "SOP Receita Agro", "Instalação do Add-on", "Web Receita", "Alvos e Pragas", "Consultas Fitossanitárias", "Culturas", "Produtores", "Agrônomos", "Receita Agro"]
---

# Manual de Implantação: SOP Receita Agro

Este manual descreve o passo a passo para a configuração e utilização da integração entre o **Sankhya** e a plataforma **Web Receita**.

### 1. Instalação do Add-on

##### A instalação deve ser realizada diretamente no ambiente do cliente.

**(1)** Acesse a tela **''Minhas Soluções''** (Comercial » Arquivo » Cadastros » Minhas Soluções).

**(2)** Utilize as credenciais de acesso do cliente (Sankhya ID).

**(3)** Em seguida, pesquise por **''Receita Agro''**.

**(4)** Localize o módulo e clique em **''Ver Detalhes''** e, posteriormente, em **''Instalar''**.

**(5)** O sistema solicitará a senha para liberação da customização (o código será enviado para o e-mail do usuário). Após a validação, o menu do módulo estará disponível para uso.

### 2. Configurações e Credenciais (Pré-requisitos)

##### Para que a integração funcione, o cliente deve possuir contrato ativo com a plataforma Web Receita.

| **Ambientes com mais de uma empresa**  Os passos abaixo configuram **uma única credencial** para todo o ambiente. Para segregar as credenciais por empresa — cada empresa emitindo receituário com a própria credencial da Web Receita — ative antes a preferência **REC\_CONFPOREMP – Configurações por empresa Receituário** e siga o artigo [Como configurar o Receituário Agro por empresa].  Nesse cenário, os cadastros de **Agrônomo** e de **Produtor Rural** passam a exigir vínculo com a credencial de cada empresa. |
| --- |

**(1)** Acesse a tela **''Configurações Receita Agro''** (Receita Agro » Cadastros).

![Imagem 1: (1) Acesse a tela ''Configurações Receita Agro'' (Receita Agro » Cadastros).](https://ajuda.sankhya.com.br/hc/article_attachments/40107330452759)

**(2)** No campo **''Gateway''** selecione ''**WebReceita''**.

**(3)** Insira o **Client ID** e o **Client Secret** fornecidos pela Web Receita.

**(4)** Marque a opção **''Ativo''** e salve.

![Imagem 2: (4) Marque a opção ''Ativo'' e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/40107330453911)

### 3. Sincronização de Dados (API)

O sistema importa, via API, as tabelas governamentais atualizadas. A sincronização pode ser feita de duas formas: manualmente, sob demanda em cada tela, ou de forma automática, mediante configuração de rotinas periódicas.

#### 3.1 Sincronização Manual

A sincronização manual é executada diretamente na tela correspondente a cada cadastro, sempre que o usuário desejar atualizar as informações.

#### 3.1.1 Alvos e Pragas

**(1)** Acesse a tela **''Pragas''** (Receita Agro » Cadastros).

**(2)** Clique no botão **“Sincronizar Alvos”**. O sistema realizará a importação automática, via API, de todos os alvos e culturas definidos pelo governo.

![Imagem 3: (2) Clique no botão “Sincronizar Alvos” . O sistema realizará a importação automática, via API, de todos os alvos e…](https://ajuda.sankhya.com.br/hc/article_attachments/40107330455319)

#### 3.1.2 Consultas Fitossanitárias (Princípios Ativos)

**(1)** Acesse a tela **''Consulta Fitossanitária''** (Receita Agro » Cadastros » Consulta Fitossanitária).

**(2)** Clique em **''Sincronizar Produtos''**. Isso trará a lista de princípios ativos e nomes técnicos.

![Imagem 4: (2) Clique em ''Sincronizar Produtos'' . Isso trará a lista de princípios ativos e nomes técnicos.](https://ajuda.sankhya.com.br/hc/article_attachments/40107330456983)![Imagem 5: (2) Clique em ''Sincronizar Produtos'' . Isso trará a lista de princípios ativos e nomes técnicos.](https://ajuda.sankhya.com.br/hc/article_attachments/40107330460311)![Imagem 6: (2) Clique em ''Sincronizar Produtos'' . Isso trará a lista de princípios ativos e nomes técnicos.](https://ajuda.sankhya.com.br/hc/article_attachments/40107330462615)

#### 3.1.3 Culturas

**(1)** Acesse a tela **''Culturas''** (Receita Agro » Cadastros » Culturas).

**(2)** Clique em **''Sincronizar Culturas''**.

![Imagem 7: (2) Clique em ''Sincronizar Culturas'' .](https://ajuda.sankhya.com.br/hc/article_attachments/40107330463383)

#### 3.2 Sincronização Automática

Para evitar a execução manual recorrente, o sistema permite programar rotinas que atualizam os dados automaticamente em intervalos definidos pelo usuário.

**(1)** Acesse a tela **"Configuração ReceitaAgro"** (Receita Agro » Cadastros).

**(2)** Selecione a empresa desejada

**(3)** Clique no botão **"Sincronização automática"** na barra de ferramentas.

**(4)** Na janela aberta, estão disponíveis três rotinas independentes:

- **Sinc. Produtores**
- **Sinc. Alvos / Pragas**
- **Sinc. Culturas**

**(5)** Para cada rotina que deseja automatizar, habilite o campo **Ativo**.

**(6)** Informe o **Tempo de atualização (minutos)** — intervalo em que o sistema executará a busca das informações.

**(7)** Clique em **Salvar**.

**Observações:**

- As rotinas são configuradas de forma independente: é possível ativar apenas uma, duas ou todas as três.
- O campo **Última execução** exibe a data e hora do último processamento de cada rotina, permitindo acompanhar se a automação está em funcionamento. Enquanto não houver a primeira execução, o campo apresentará "Nunca executado".
- Com as rotinas ativas, não é necessário executar manualmente as sincronizações correspondentes descritas no item 3.1.
- Para interromper a automação, basta desabilitar o campo **Ativo** da respectiva rotina e salvar.

![Imagem 8: Para interromper a automação, basta desabilitar o campo Ativo da respectiva rotina e salvar.](https://ajuda.sankhya.com.br/hc/article_attachments/43167229091735)![Imagem 9: Para interromper a automação, basta desabilitar o campo Ativo da respectiva rotina e salvar.](https://ajuda.sankhya.com.br/hc/article_attachments/43167212374167)

### 4. Cadastros e Vínculos Estratégicos

#### 4.1 Produtores (Parceiros)

Para que um parceiro seja reconhecido como produtor rural:

**(1)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros), na aba **''Fiscal''**.

![Imagem 10: (1) Acesse a tela ''Parceiros'' (Configurações » Cadastros » Parceiros), na aba ''Fiscal'' .](https://ajuda.sankhya.com.br/hc/article_attachments/40107307950231)

**(2)** Verifique se o campo **''Classificação de ICMS''** está selecionado como **''Produtor Rural''**.

**(3)** Acesse a tela **''Produtores''** (Receita Agro » Cadastros » Produtores) e clique em **''Importar Produtores''** para carregar os parceiros configurados no sistema.

![Imagem 11: (3) Acesse a tela ''Produtores'' (Receita Agro » Cadastros » Produtores) e clique em ''Importar Produtores'' para…](https://ajuda.sankhya.com.br/hc/article_attachments/40109329148311)

**Nota:** com a preferência ''REC\_CONFPOREMP'' ativa, vincule o produtor à credencial de cada empresa pela aba **Produtor Rural por empresa**.

- Consulte [[Como configurar o Receituário Agro por empresa].](https://docs.google.com/document/d/1aGiI7WLl6gk7a8XGCQURh2PuS9hEmtRR/edit?usp=sharing&ouid=106392550974760669060&rtpof=true&sd=true)

#### 4.2 Agrônomos

**(1)** Acesse a tela **''Agrônomos''** (Receita Agro » Cadastros » Agrônomos).

**(2)** O cadastro de agrônomos pode ser realizado tanto no Sankhya quanto na plataforma Web Receita. Caso o cadastro seja feito no Sankhya, utilize a opção **“Exportar Agrônomos”** para enviá-los à Web Receita. Se o cadastro for realizado na plataforma, utilize a opção **“Sincronizar Agrônomos”** para importá-los ao Sankhya.

![Imagem 12: (2) O cadastro de agrônomos pode ser realizado tanto no Sankhya quanto na plataforma Web Receita. Caso o cadastro seja…](https://ajuda.sankhya.com.br/hc/article_attachments/40107330466711)

**Nota:** com a preferência ''REC\_CONFPOREMP'' ativa, exporte o agrônomo para cada empresa pela aba **Agrônomo por Empresa**. O mesmo agrônomo recebe um **Id Origem** distinto em cada credencial.

- Consulte [[Como configurar o Receituário Agro por empresa].](https://docs.google.com/document/d/1aGiI7WLl6gk7a8XGCQURh2PuS9hEmtRR/edit?usp=sharing&ouid=106392550974760669060&rtpof=true&sd=true)

**(3)** O preenchimento do CREA é obrigatório para a emissão do receituário.

![Imagem 13: (3) O preenchimento do CREA é obrigatório para a emissão do receituário.](https://ajuda.sankhya.com.br/hc/article_attachments/40107330468247)

#### 4.3 Vínculo de Produtos ERP

Este é o passo mais importante para o usuário final (geralmente o Engenheiro Agrônomo):

**(1)** Acesse a tela ''Consulta Fitossanitária'' (Receita Agro » Cadastros » Consulta Fitossanitária).

**(2)** Selecione o princípio ativo (Web Receita) e acesse a aba **''Vínculo Produto ERP''**.

**(3)** Vincule o código do produto comercial correspondente, previamente cadastrado no Sankhya.

**Nota**: O vínculo pode ser realizado no formato 1 para 1 ou 1 para muitos, conforme as marcas comerciais utilizadas.

![Imagem 14: Nota : O vínculo pode ser realizado no formato 1 para 1 ou 1 para muitos, conforme as marcas comerciais utilizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/40107307954839)

### 5. Processo de Venda e Emissão

#### 5.1 Configuração da TOP

Defina em qual momento o receituário será gerado: no **Pedido** ou na **Nota**.

**(1)** Acesse a tela **''Tipos de Operação''**, na aba **''ReceitaAgro''**.

**(2)** Marque a opção **''Emite Receiturário''**.

**IMPORTANTE**: Geralmente, a configuração é realizada na TOP de Venda, para que a emissão ocorra de forma simultânea ao faturamento.

![Imagem 15: IMPORTANTE : Geralmente, a configuração é realizada na TOP de Venda, para que a emissão ocorra de forma simultânea ao…](https://ajuda.sankhya.com.br/hc/article_attachments/40107307959063)

#### 5.2 Layout do Portal de Vendas

**(1)** Certifique-se de que o campo **''Cód. Agrônomo''** esteja visível no cabeçalho das notas/pedidos na tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas).

**(2)** Essa configuração deve ser realizada na tela **''Configurador de Layout da Nota''** (Comercial » Configuração » Configurador de Layout da Nota).

![Imagem 16: (2) Essa configuração deve ser realizada na tela ''Configurador de Layout da Nota'' (Comercial » Configuração »…](https://ajuda.sankhya.com.br/hc/article_attachments/40107330473111)

#### 5.3 Fluxo Operacional

**(1)** No momento do faturamento, caso existam produtos vinculados à receita, o sistema exibirá um **pop-up.**

**(2)** Nesse momento, o sistema irá sugerir o quantitativo de aplicação padrão (mínimo aceitável pelo governo).

**(3)** O usuário poderá confirmar ou ajustar as informações de aplicação para cada item.

**(4)** Ao salvar e confirmar a Nota Fiscal, o sistema gerará, de forma simultânea, as receitas correspondentes na plataforma integrada.

Em ambientes com configuração por empresa, o receituário é gerado na credencial da **empresa informada na nota**.
