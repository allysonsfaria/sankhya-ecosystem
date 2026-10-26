---
id: "40136831896983"
titulo: "Manual do Usuário: Configuração de Credenciais do Portal SISCOMEX no ERP Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40136831896983-Manual-do-Usu%C3%A1rio-Configura%C3%A7%C3%A3o-de-Credenciais-do-Portal-SISCOMEX-no-ERP-Sankhya"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-10-22T12:44:01Z"
rotulos: ["Configuração", "Integração", "Credenciais", "ERP Sankhya", "Portal SISCOMEX", "Client ID", "Client Secret", "Portal Único SISCOMEX", "Configuração PUCOMEX", "Configuração de Credenciais", "Chaves no Portal SISCOMEX", "Catalogo de Produtos", "SISCOMEX", "Impex"]
---

# Manual do Usuário: Configuração de Credenciais do Portal SISCOMEX no ERP Sankhya

| **Versão:**  1.0 | **Data:**  Abril / 2026 |
| --- | --- |
| **Sistema:**  ERP Sankhya | **Módulo:**  Impex / Portal Único Comex |

### 1. Visão Geral

Este manual orienta o usuário a configurar as credenciais de acesso (Client ID e Client Secret) do Portal Único SISCOMEX dentro do ERP Sankhya, módulo Impex. Essa configuração é necessária para que o sistema consiga se comunicar automaticamente com o governo federal e sincronizar os dados de importação e exportação.

| **Antes de iniciar a configuração no Sankhya, é necessário gerar as chaves de acesso diretamente no site do Portal Único SISCOMEX. Siga as instruções da Etapa 1 a seguir.** |
| --- |

### 2. O que são Client ID e Client Secret?

##### O Portal Único SISCOMEX utiliza um sistema de ''chaves de acesso'' para identificar e autorizar os sistemas que se conectam a ele. Pense nessas chaves como um usuário e senha especiais criados exclusivamente para que o ERP Sankhya fale com o portal do governo.

| **CAMPO** | **DESCRIÇÃO** |
| --- | --- |
| **Client ID** | Identificador único da sua chave de acesso. Funciona como um "nome de usuário" da integração. |
| **Client Secret** | Senha secreta associada ao Client ID. Deve ser guardada com segurança e nunca compartilhada por e-mail. |
| **Perfil do Operador** | Define o tipo de operação autorizada. Para importação e exportação, o perfil normalmente utilizado é IMPEXP. |

### 3. Etapa 1 - Gere as Chaves no Portal SISCOMEX

Antes de configurar o Sankhya, **crie as chaves de acesso no Portal Único (SISCOMEX)**. Siga os passos abaixo:

#### 3.1 Acesse o Portal Único

**(1)** Abra o navegador e acesse o Portal Único (SISCOMEX):

- <https://portalunico.siscomex.gov.br/portal/> **Certificado digital (e-CNPJ ou e-CPF)** válido no padrão ICP-Brasil. Sem ele, não é possível acessar o portal.

| Utilize um certificado digital do tipo **A1** ou **A3**, no padrão **ICP-Brasil**. Caso não possua o certificado ou não saiba como utilizá-lo, entre em contato com o setor de TI da empresa. |
| --- |

#### 3.2 Abra a tela de Chaves de Acesso

**(1)** Localize, no canto superior direito da tela, o ícone de **chave** (ao lado do nome do usuário ou do menu principal).

**(2)** Clique no ícone para abrir a tela de gerenciamento de chaves.

#### 3.3 Crie uma nova chave

**(1)** Clique no ícone ''+'' localizado á direita da tela.

**(2)** Preencha os campos conforme abaixo:

| **CAMPO** | **O QUE SELECIONAR / PREENCHER** | **OBSERVAÇÃO** |
| --- | --- | --- |
| **Tipo de Chave** | Pessoa Jurídica | Selecione o CNPJ da empresa |
| **Perfis** | IMPEXP | Para importação e exportação |
| **Descrição** | Ex: "Integração ERP Sankhya" | Para facilitar a identificação futura |
| **Tempo de Expiração** | Defina conforme política interna | Renove antes do vencimento |

**(3)** Clique em **“Salvar”**.

**(4)** Visualize o **Termo de Responsabilidade** exibido em tela.

**(5)** Armazene com segurança o **Client ID** e o **Client Secret** apresentados pelo sistema.

| **ATENÇÃO**: O **Client Secret** é exibido apenas uma vez no momento da criação. Armazene-o em local seguro imediatamente. Caso o perca, crie uma nova chave de acesso. |
| --- |

### 4. Etapa 2 - Configure as Credenciais no ERP Sankhya

Após gerar as credenciais, **acesse o Sankhya** e siga os passos abaixo para configurar a integração:

#### 4.1 Acesse as Configurações Pucomex

**(1)** Acesse a tela **''Configurações PUCOMEX''** (ImpEx » Rotinas » Configuração PUCOMEX).

![Imagem 1: (1) Acesse a tela ''Configurações PUCOMEX'' (ImpEx » Rotinas » Configuração PUCOMEX).](https://ajuda.sankhya.com.br/hc/article_attachments/40136816069143)

#### 4.2 Preencha os Campos Obrigatórios

Ao acessar a tela de configurações, **preencha os campos conforme descrito abaixo**:

| **CAMPO NO SANKHYA** | **O QUE INFORMAR** | **ONDE ENCONTRAR** |
| --- | --- | --- |
| **Client ID** | Cole o Client ID gerado no Portal | Tela de Chaves do Portal SISCOMEX |
| **Client Secret** | Cole o Client Secret gerado no Portal | Guardado no momento da criação da chave |
| **Perfil do Operador** | IMPEXP (para importação e exportação) | Definido conforme operação da empresa |
| **Ambiente** | HOMOL (testes) ou PROD (produção) | Comece sempre com HOMOL para testar |

| **IMPORTANTE**: Realize os testes inicialmente no ambiente **HOMOLOGAÇÃO (HOMOL)**. Após validar que tudo está funcionando corretamente, altere para o ambiente **PRODUÇÃO (PROD)**. |
| --- |

#### 4.3 Salve as Configurações

**(1)** Salve.

**(2)** O sistema validará os dados informados e realizará automaticamente a autenticação junto ao Portal SISCOMEX.

**(3)** Verifique a ativação da integração. Caso as informações estejam corretas, a integração estará pronta para uso.

### 5. Etapa 3 - Verifique se a Integração está funcionando

##### Após salvar as configurações, verifique se a integração está ativa realizando um teste de sincronização:

**(1)** Acesse a tela **''Catálogo de Produtos''** (ImpEx » Rotinas » Catálogo de Produtos).

**(2)** Informe as credenciais (**Client ID** e **Client Secret**) caso solicitado, para autenticação no Portal SISCOMEX.

**(3)** Localize o ícone de **três pontos** na tela e clique na seta ao lado para visualizar as opções disponíveis.

**(4)** Clique na opção **"Buscar Catálogo"** para realizar a consulta das informações via API do Portal SISCOMEX.

**(5)** Clique na opção **"Recarregar Atributos"** para atualizar os atributos dos produtos conforme os dados retornados pela API.

![Imagem 2: (5) Clique na opção "Recarregar Atributos" para atualizar os atributos dos produtos conforme os dados retornados pela…](https://ajuda.sankhya.com.br/hc/article_attachments/40136831885463)

| O token gerado na autenticação possui validade de 60 minutos. A renovação é realizada automaticamente pelo sistema a cada operação, sem necessidade de intervenção do usuário. |
| --- |

### 6. Problemas Comuns e Soluções

| **PROBLEMA** | **O QUE FAZER** |
| --- | --- |
| **Token Inválido / Erro de Autenticação** | O sistema tenta renovar automaticamente. Se o erro persistir, verifique se o Client ID e o Client Secret estão corretos na entidade PUCXCON. Pode ser necessário gerar novas chaves no Portal SISCOMEX. |
| **Chave expirada** | Acesse o Portal SISCOMEX, gere um novo par de chaves e atualize os campos Client ID e Client Secret no Sankhya (entidade PUCXCON). |
| **Nenhum produto retorna (arquivo ZIP vazio)** | Acesse o site do SISCOMEX e verifique se há produtos cadastrados para o CNPJ da empresa. O problema pode não estar na configuração do Sankhya. |
| **Produto não atualiza no ERP** | Verifique se a versão do produto no Portal SISCOMEX é mais recente que a versão cadastrada no Sankhya (campo VERSAO na tabela PUCXCAT). O sistema não atualiza versões iguais ou mais antigas. |
| **Nome do produto aparece cortado** | Isso é uma limitação do Portal SISCOMEX: o campo "Denominação" aceita no máximo 100 caracteres. Nomes maiores são truncados automaticamente pelo portal. |

### 7. Informações de Suporte

| **CANAL** | **COMO CONTATAR / USAR** |
| --- | --- |
| **Dúvidas sobre o Portal SISCOMEX** | Comex Responde: Assunto Geral > "Sistemas e ferramentas de apoio" > "Portal Único Siscomex" |
| **Problemas técnicos de TI (Portal)** | Central Serpro de Atendimento: selecione "PORTAL ÚNICO SISCOMEX - PUCOMEX" no campo Serviço |
| **Documentação oficial da API** | https://docs.portalunico.siscomex.gov.br/ |
| **Suporte ERP Sankhya** | Entre em contato com o suporte interno ou com o time de implantação Sankhya da sua empresa. |

### Visão Geral do Processo

##### **(1)** Gere as credenciais no Portal SISCOMEX (Client ID e Client Secret).

**(2)** Acesse a entidade **PUCXCON** no Sankhya

**(3)** Preencha os campos **Client ID**, **Client Secret**, **Perfil** e **Ambiente**.

**(4)** Em seguida, clique em **“Salvar”** e realize os testes inicialmente no ambiente **HOMOLOGAÇÃO (HOMOL)**.

**(5)** Após validar que tudo está funcionando corretamente, altere o ambiente para **PRODUÇÃO (PROD)**.
