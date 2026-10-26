---
id: "44011038430743"
titulo: "Como integrar a Ploomes com a Flowbiz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011038430743-Como-integrar-a-Ploomes-com-a-Flowbiz"
trilha: "Flowbiz > Integrações"
atualizado_em: "2026-10-05T18:54:55Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_281", "sync_hash_96fee82c04c1"]
---

# Como integrar a Ploomes com a Flowbiz

A integração da Ploomes com a Flowbiz permite sincronizar automaticamente contatos, empresas, interações e **negócios**, conectando o CRM às estratégias de marketing e captação de leads. A integração oferece **configurações avançadas** que controlam como leads recebidos aqui na Flowbiz são processados na Ploomes, possibilitando fluxos flexíveis de criação de contatos, empresas e oportunidades comerciais. Essas configurações permitem adaptar a integração desde cenários simples de recebimento de leads até estratégias mais robustas de geração automática de negócios.

Para realizar a Integração é necessário que você tenha

- **Usuário administrador** no Ploomes.
- Conta ativa aqui na Flowbiz com acesso a **API Key**

## Iniciando o processo de ativação da Integração

1. No painel da Ploomes, acesse **Configurações > Integrações > Flowbiz**
2. ![Imagem 1: Clique em "Habilitar integração" e depois “Autorizar integração” .](https://ajuda.sankhya.com.br/hc/article_attachments/44011038700439)Clique em **"Habilitar integração"** e depois **“Autorizar integração”**.

   ![Imagem 2: Clique em "Habilitar integração" e depois “Autorizar integração” .](https://ajuda.sankhya.com.br/hc/article_attachments/44011068069527)
3. Na sequência acesse sua conta Flowbiz para gerar a **Chave de API.**
   Para isso, vá até o nome do usuário no menu superior direito e selecione **"Chaves de API"**.

![Imagem 3: 3.1 Clique em "Criar chave de API" e coloque o nome da chave de API. Não insira nenhum IP no campo abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/44011068514839)3.1 Clique em "Criar chave de API" e coloque o nome da chave de API. **Não insira nenhum IP no campo abaixo.**

![Imagem 4: 3.2 Copie a chave, cole na aba de autorização e clique em continuar.](https://ajuda.sankhya.com.br/hc/article_attachments/44011040041879)3.2 Copie a chave, cole na aba de autorização e clique em continuar.

![Imagem 5: 3.2 Copie a chave, cole na aba de autorização e clique em continuar.](https://ajuda.sankhya.com.br/hc/article_attachments/44011040403863)

3.3 Clique em "Ativar a integração". Não é possível mapear campos antes da primeira ativação da integração.

![Imagem 6: 3.4 O sistema verifica se já existe uma lista padrão chamada Clientes Ploomes - {AccountID} na Flowbiz. Se existir, ela…](https://ajuda.sankhya.com.br/hc/article_attachments/44011058185367)3.4 O sistema verifica se já existe uma **lista padrão** chamada `Clientes Ploomes - {AccountID}` na Flowbiz. Se existir, ela será reutilizada. Se não existir, uma nova lista será criada automaticamente.

![Imagem 7: Durante essa etapa, os campos fixos são criados na Flowbiz e são mapeados com os da Ploomes.](https://ajuda.sankhya.com.br/hc/article_attachments/44011083192087)Durante essa etapa, os campos fixos são criados na Flowbiz e são mapeados com os da Ploomes.

1. Agora você deve mapear seus campos que serão integrados na Flowbiz!

![Imagem 8: Agora você deve mapear seus campos que serão integrados na Flowbiz!](https://ajuda.sankhya.com.br/hc/article_attachments/44011086667799)

## Configurando o recebimento de leads e criação de entidades

Com o recebimento de leads habilitado, a integração pode criar **contatos, empresas e negócios** na Ploomes, de acordo com as configurações definidas.

Sempre que um lead ainda não integrado é processado:

- Um **contato** é criado no Ploomes
- A **empresa só é criada** se não existir correspondência por **CNPJ ou nome**
- Caso exista uma empresa correspondente, ela é reutilizada e relacionada ao contato
- Opcionalmente, a integração também pode criar **negócios**, que são sempre criados no **mesmo funil e estágio configurados.**

![Imagem 9: Opcionalmente, a integração também pode criar negócios , que são sempre criados no mesmo funil e estágio configurados.](https://ajuda.sankhya.com.br/hc/article_attachments/44011070910999)

## Filtro de segmentos da Flowbiz

O **filtro de segmentos da Flowbiz** permite limitar **quais leads devem ser enviados ao Ploomes**, com base em **segmentações criadas na própria Flowbiz**.

Segmentos são agrupamentos dinâmicos de leads definidos por regras, como:

- origem do lead
- preenchimento de formulários
- comportamento em campanhas
- campos e propriedades do contato

Quando o filtro por segmentos está ativado:

- **Apenas leads que pertencem aos segmentos selecionados** são processados pela integração
- Leads fora desses segmentos são ignorados
- As regras de criação de contato, empresa e negócio continuam as mesmas

Esse filtro é especialmente útil quando você deseja criar negócios apenas para leads qualificados, separar diferentes estratégias comerciais a partir de uma mesma lista e controlar com mais precisão quais leads entram no CRM

## Imagem 10: Criação de negócios por segmentoCriação de negócios por segmento

A integração permite controlar se a criação de negócios no Ploomes deve considerar os **segmentos da Flowbiz selecionados para filtragem**. Esse comportamento é definido por uma **flag de criação de negócios por segmento**.

Quando essa flag está **desabilitada**:

- Para cada lead processado, é criado **apenas um negócio**
- O negócio é criado no **funil e estágio configurados**, independentemente dos segmentos aos quais o lead pertença

Quando a flag está **habilitada**:

- O lead pode gerar **mais de um negócio**
- É criado **um negócio para cada segmento selecionado para filtragem** aqui na Flowbiz ao qual o lead pertença
- Segmentos não selecionados para filtragem **não geram negócios**
- Todos os negócios são criados no **mesmo funil e estágio configurados** no Ploomes

Essa opção é indicada quando cada **segmento filtrado** representa uma intenção comercial diferente, permitindo criar e acompanhar oportunidades distintas para o mesmo lead de forma organizada.

## Imagem 11: Casos de uso da integraçãoCasos de uso da integração

**4.1 Segmentação automática na Flowbiz com base em dados da Ploomes**

A integração permite utilizar **campos da Ploomes** (como marcadores, status e campos personalizados mapeados) para criar **segmentos dinâmicos na Flowbiz**.

Sempre que um contato é atualizado no Ploomes e passa a atender às regras de um segmento:

- Ele entra automaticamente no segmento correspondente na Flowbiz
- Pode ser incluído em **campanhas ou sequências de e-mails**, de forma automática

Esse uso é indicado para automatizar comunicações com base em informações atualizadas diretamente no CRM.

**4.2 Leads provenientes de formulários da Flowbiz**

Quando um lead preenche um formulário em uma landing page da Flowbiz:

- Ele pode ser incluído automaticamente na **lista padrão vinculada à integração**
- Na próxima sincronização, o lead é processado pelo Ploomes conforme as configurações ativas

A partir desse processamento, o lead pode gerar:

- Um **contato** na Ploomes
- Uma **empresa**, apenas se não existir correspondência por **CNPJ ou nome**
- Um ou mais **negócios**, dependendo das opções configuradas na integração

Esse cenário permite transformar leads de marketing em registros acionáveis no CRM sem necessidade de importações manuais.

**4.3 Qualificação de leads com filtro de segmentos da Flowbiz**

A integração permite aplicar um **filtro por segmentos da Flowbiz** para definir **quais leads devem ser enviados a Ploomes**.

Com esse filtro ativo:

- Apenas leads pertencentes aos **segmentos selecionados** são processados
- Leads fora desses segmentos são ignorados
- As regras de criação de contato, empresa e negócio continuam valendo

Esse caso de uso é indicado quando é necessário enviar ao Ploomes apenas leads qualificados ou separar diferentes estratégias comerciais a partir de uma mesma base de leads.

**4.4 Criação automática de negócios a partir de leads da Flowbiz**

Além da criação de contatos e empresas, a integração pode criar **negócios automaticamente** na Ploomes a partir dos leads recebidos da Flowbiz.

Esse comportamento permite:

- Criar **um negócio por lead**, ou
- Criar **um negócio para cada segmento selecionado para filtragem**, quando a flag de criação de negócios por segmento estiver habilitada

Em todos os casos:

- O negócio é criado sempre no **mesmo funil e estágio configurados**
- A empresa só é criada se não existir correspondência
- Contato, empresa e negócio são relacionados entre si

Esse uso é indicado quando cada lead ou segmento representa uma **oportunidade comercial**.

**4.5 Consulta de interações de campanhas no Ploomes**

Os eventos de interação dos contatos com campanhas da Flowbiz podem ser consultados diretamente na Ploomes.

Para visualizar:

- Acesse a página do contato
- Clique na aba **Flowbiz**

Nessa aba são exibidos eventos como aberturas, bounces e demais interações registradas nas campanhas enviadas.

## Imagem 12: Como funciona a integraçãoComo funciona a integração

A integração é **bidirecional**, mas **não simétrica**: cada lado tem regras claras sobre o que pode ou não ser atualizado.

## Ploomes → Flowbiz

- A Ploomes envia dados a Flowbiz **em tempo real**, via webhook.
- Alterações em **campos mapeados do contato** atualizam o registro na Flowbiz.
- Se o contato não existir na Flowbiz:
- É buscado pelo **e-mail**
- Caso não seja encontrado, um novo contato é criado.
- Alterações de e-mail na Ploomes são refletidas na Flowbiz.
- Se o e-mail for removido da Ploomes, o contato é removido da lista na Flowbiz.

## Flowbiz → Ploomes

- A Ploomes consulta a Flowbiz **a cada 5 minutos**.
- A Flowbiz **não sobrescreve dados existentes** na Ploomes.
- Apenas **campos vazios de contatos e empresas** podem ser preenchidos.
- Campos já preenchidos **nunca são alterados**.
- **Negócios não são atualizados** em nenhuma direção.

## Criação de entidades

- Contatos podem ser criados a partir de leads da Flowbiz.
- Empresas só são criadas após validação por **CNPJ e nome**.
- Negócios podem ser criados automaticamente, conforme configuração:
- **1 negócio por lead**, ou
- **1 negócio por segmento selecionado para filtragem**.
- Todos os negócios são criados no **mesmo funil e estágio configurados**.

## Compatibilização de campos de opções

- Ao ativar ou atualizar a integração, as **opções pré-cadastradas** dos campos mapeados são sincronizadas.
- Em campos do tipo lista ou seletor:
- A Ploomes cria automaticamente na Flowbiz as opções correspondentes.
- Caso alguma opção não exista, ela é criada durante a atualização.
- Problemas de opções faltantes ou divergentes geralmente são resolvidos **atualizando a integração**.

## Limitações importantes

- Descadastros na Flowbiz **não removem contatos** na Ploomes.
- Exclusões na Flowbiz **não são refletidas** na Ploomes.
- Atualizações de negócios **não acontecem** após a criação.

## Dúvidas frequentes

- **A integração é automática ou precisa ser atualizada manualmente?**

A sincronização é **automática**.
A Ploomes envia **webhooks em tempo real** para Flowbiz sempre que há alterações em contatos, e também realiza **consultas periódicas (a cada 5 minutos)** para processar atualizações e novos leads vindos da Flowbiz.

- **O que acontece se eu editar o e-mail de um contato no Ploomes?**

O e-mail é atualizado imediatamente na Flowbiz via webhook.
Se o novo e-mail já existir em outra lista ou registro, o comportamento segue as **regras de duplicidade**, podendo gerar conflitos ou impedir a atualização.

- **Posso criar campanhas automáticas no Flowbiz com dados do Ploomes?**

Sim. Campos mapeados da Ploomes podem ser usados para criar **segmentos dinâmicos na Flowbiz**, que alimentam campanhas e sequências de e-mails automaticamente.

- **Leads capturados por formulários no Flowbiz aparecem no Ploomes?**

Sim. Após a sincronização, o lead é processado na Ploomes conforme as configurações da integração, podendo gerar:

- Um **contato**
- Uma **empresa** (apenas se não existir correspondência por CNPJ ou nome)
- Um ou mais **negócios**, se essa opção estiver habilitada
- **Onde vejo as interações de campanhas na Ploomes?**

Na página do contato, na aba **Flowbiz**, onde são exibidos eventos como aberturas, bounces e interações com campanhas.

- **A Flowbiz atualiza informações já preenchidas na Ploomes?**

Não. A Flowbiz **não sobrescreve dados existentes** na Ploomes.
Ele apenas **preenche campos que já estejam vazios**, e isso se aplica somente a **contatos e empresas**.

- **O que acontece se um contato for descadastrado ou excluído na Flowbiz?**

**Descadastro (unsubscribe):** o contato permanece na Ploomes

**Exclusão no Flowbiz:** não é refletida na Ploomes

Para remover um contato do CRM, a exclusão deve ser feita diretamente na Ploomes.

- **Como resolver problemas com opções de campos que não aparecem corretamente na Flowbiz?**

Basta **atualizar a integração**. Durante a atualização, a Ploomes sincroniza automaticamente as **opções de campos do tipo lista ou seletor**, criando na Flowbiz aquelas que estiverem faltando.

Caso fique com dúvidas, entre em contato com nosso time de suporte via chat da ferramenta.
