---
id: "42427457920023"
titulo: "Integração com a Flowbiz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427457920023-Integra%C3%A7%C3%A3o-com-a-Flowbiz"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:03:19Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12556202", "sync_hash_1fcaa6096cb4"]
---

# Integração com a Flowbiz

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=_F80Hg5WQiY)

## 1) Sobre a integração

A integração entre o Ploomes e o Flowbiz permite sincronizar automaticamente contatos, empresas, interações e **negócios**, conectando o CRM às estratégias de marketing e captação de leads.

Além da sincronização bidirecional de dados, a integração oferece **configurações avançadas** que controlam como leads recebidos do Flowbiz são processados no Ploomes, possibilitando fluxos flexíveis de criação de contatos, empresas e oportunidades comerciais.

Essas configurações permitem adaptar a integração desde cenários simples de recebimento de leads até estratégias mais robustas de geração automática de negócios.

## 2) Pré-requisitos

Antes de ativar a integração, certifique-se de:

- Ter um **usuário administrador** no Ploomes.
- Possuir uma conta ativa no **Flowbiz** com acesso à **API Key**.

⚠️ **Atenção**: contatos sem e-mail não são sincronizados.

## 3) Ativando a integração

1. Acesse **Configurações > Integrações > Flowbiz** no Ploomes.

   ![Imagem 1: Acesse Configurações > Integrações > Flowbiz no Ploomes.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792125008/cb27eb91c2f4909fa087c65cb1d7/Screenshot_1.png?expires=1786536000&signature=81a494ee1ff13261997c16339cb89bad46ba9a5d8ca5680dccbc8a3de290d286&req=dScuFMh8mIFfUfMW3nq%2BgRRlBscUvYu6KS%2BQu9Ffei9rp8cNf9F0b9vihaaB%0AhtrpAQG1eZ0b7HFSeR7b4M0ideM%3D%0A)
2. Clique em **"Habilitar integração"** e depois **“Autorizar integração”**.

   [GIF animado: Imagem 2: Clique em "Habilitar integração" e depois “Autorizar integração” .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792130687/1a9bf1bdba709ee357067c2c51bb/habilita+e+autoriza.gif?expires=1786536000&signature=c336718f8f52b94d51cbd4228eeb1ed4a0619964ad35eaa152917ad43dacef22&req=dScuFMh9nYdXXvMW3nq%2BgahTXx6r1BzYuiwg0orrTEfWxvF5xMouL2CHL9cM%0ADqcxcMUU6sqfghV9%2FsT1SZslLdU%3D%0A)
3. Vá até o Flowbiz para gerar sua **Chave de API.**

   1. Para isso, vá até o nome do usuário no menu superior direito e selecione **"Chaves de API"**.

      [GIF animado: Imagem 3: Para isso, vá até o nome do usuário no menu superior direito e selecione "Chaves de API" .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792136054/e47dd8e9763d5ed2039ef0985951/flowbiz+credentials.gif?expires=1786536000&signature=398941e14df469c0f1b0ee475b7d46abffaadc9f62cff00a4a13bb1a93b6cbc7&req=dScuFMh9m4FaXfMW3nq%2BgaX51ICQkhCCZ6Ta95QTObo4ikJHKNTIaPAwfjEA%0AwcH7jc2imsv%2FlKXQjSaebMypOUI%3D%0A)
   2. Clique em "Criar chave de API" e coloque o nome da chave de API. **Não insira nenhum IP no campo abaixo.**

      [GIF animado: Imagem 4: Clique em "Criar chave de API" e coloque o nome da chave de API. Não insira nenhum IP no campo abaixo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792138710/7e36d2ad8514654c93781872b893/flowbiz+credentials+generation.gif?expires=1786536000&signature=336715d0c02d842f4be0f7b93af273bdfd5e70a66388091bff2544b4a233375f&req=dScuFMh9lYZeWfMW3nq%2BgfCBfs1tw4gLejOkghJqG797aAvuci8q8K%2FfTDcg%0AhBcP1ji2qy0anoHfqI58avrxBEA%3D%0A)
   3. Copie a chave, cole na aba de autorização e clique em continuar.

      [GIF animado: Imagem 5: Copie a chave, cole na aba de autorização e clique em continuar.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792139685/f22869258912a0a13a3fe1aa0bd6/colar+chave+api+no+ploo.gif?expires=1786536000&signature=84dfefa01c85bed98a368e01807702696b82196ab370587f61f443886aa70fc3&req=dScuFMh9lIdXXPMW3nq%2BgYOL9%2B%2B6k9Vqp9OFATsF2BBQmWH3ZqecWe%2BgLaVg%0AgAAbAEF9aNDR%2B7jlTj%2BgKpNVlQ8%3D%0A)
4. Clique em "Ativar a integração". Não é possível mapear campos antes da primeira ativação da integração.

   [GIF animado: Imagem 6: Clique em "Ativar a integração". Não é possível mapear campos antes da primeira ativação da integração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792140281/78a0046f1cf6979e1c8e3d16fe45/ativando.gif?expires=1786536000&signature=1e894806e30f4667a95abb894fcaae883c009f1ede501a0a331a98a59a14ff09&req=dScuFMh6nYNXWPMW3nq%2BgbhCOxdu7XATYTEFTPxa340x5AnU0KmEfvaFFOvY%0AxY2PaADeh8faVueg0fY9TShV6bk%3D%0A)

   O sistema verifica se já existe uma **lista padrão** chamada `Clientes Ploomes - {AccountID}` no Flowbiz. Se existir, ela será reutilizada. Se não existir, uma nova lista será criada automaticamente.

   ![Imagem 7: O sistema verifica se já existe uma lista padrão chamada Clientes Ploomes - {AccountID} no Flowbiz. Se existir, ela…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792142150/0d2f6ea3c5284f306ba95589120f/image.png?expires=1786536000&signature=07422450e6778add8ebd86565b859dd17490cfcb84fcf4497b72c081a07df03d&req=dScuFMh6n4BaWfMW3nq%2BgR%2Fcz9ieqWl%2BNjoojHusCgPoVNAxUXToYAjJuuym%0A6Kv%2BI6PWtNdUDnu8vQ3%2FmcnART4%3D%0A)

   Durante essa etapa, os campos fixos são criados no Flowbiz e são mapeados com os do Ploomes.
5. Agora você pode mapear seus campos que serão integrados ao Flowbiz!

   [GIF animado: Imagem 8: Agora você pode mapear seus campos que serão integrados ao Flowbiz!](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792141019/c613355bd08223ed5e04d129ae43/mapeando.gif?expires=1786536000&signature=7b627e1d71b4ba2c4af0224f8c61364ca70a6056cff15b339e80d98a39263424&req=dScuFMh6nIFeUPMW3nq%2BgbICn%2FJ4878PRbjyozZySZYTmolALrrPSFJnCI5J%0ApzG2pl6IORaJilhZbelaXhoM7JA%3D%0A)

## 3.1) Configurando o recebimento de leads e criação de entidades

Com o recebimento de leads do Flowbiz habilitado, a integração pode criar **contatos, empresas e negócios** no Ploomes, de acordo com as configurações definidas.

Sempre que um lead ainda não integrado é processado:

- Um **contato** é criado no Ploomes
- A **empresa só é criada** se não existir correspondência por **CNPJ ou nome**
- Caso exista uma empresa correspondente, ela é reutilizada e relacionada ao contato
- Opcionalmente, a integração também pode criar **negócios**, que são sempre criados no **mesmo funil e estágio configurados.**

[GIF animado: Imagem 9: Opcionalmente, a integração também pode criar negócios , que são sempre criados no mesmo funil e estágio configurados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2134097546/b6fe500973f4d025ea416d67b836/ativando+o+recebimento+de+leads.gif?expires=1786536000&signature=c5c0c2a6455c1922d8d9869f574f20071e646fe05a8d06d987c4a7d90b5f165e&req=diEkEsl3moRbX%2FMW3nq%2Bgfqs30GM6LM6SgAxpglOhSdDaR9hwtYdWhgF3T7K%0AoLyO29T3g6NnJomSQmwDaaCBJjU%3D%0A)

### 3.1.1) Filtro de segmentos do Flowbiz

O **filtro de segmentos do Flowbiz** permite limitar **quais leads devem ser enviados ao Ploomes**, com base em **segmentações criadas no próprio Flowbiz**.

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

[GIF animado: Imagem 10: Esse filtro é especialmente útil quando você deseja criar negócios apenas para leads qualificados, separar diferentes…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2134098280/6c32954f23fd0fda53b6b9b6baef/filtro+de+segmentos.gif?expires=1786536000&signature=81e386e43d290fc7616a527b71979997dd1b7f0eb03856a2aeab87d3c6727842&req=diEkEsl3lYNXWfMW3nq%2BgQMz8IHIllsilpAw3OxT2CimG%2BdA8%2FWycGcrtZXc%0AdpzW%2BfLql78MGhxjXE3K3fLFzLs%3D%0A)

### 3.1.2) Criação de negócios por segmento

A integração permite controlar se a criação de negócios no Ploomes deve considerar os **segmentos do Flowbiz selecionados para filtragem**. Esse comportamento é definido por uma **flag de criação de negócios por segmento**.

Quando essa flag está **desabilitada**:

- Para cada lead processado, é criado **apenas um negócio**
- O negócio é criado no **funil e estágio configurados**, independentemente dos segmentos aos quais o lead pertença

Quando a flag está **habilitada**:

- O lead pode gerar **mais de um negócio**
- É criado **um negócio para cada segmento selecionado para filtragem** no Flowbiz ao qual o lead pertença
- Segmentos não selecionados para filtragem **não geram negócios**
- Todos os negócios são criados no **mesmo funil e estágio configurados** no Ploomes

Essa opção é indicada quando cada **segmento filtrado** representa uma intenção comercial diferente, permitindo criar e acompanhar oportunidades distintas para o mesmo lead de forma organizada.

[GIF animado: Imagem 11: Essa opção é indicada quando cada segmento filtrado representa uma intenção comercial diferente, permitindo criar e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2134098672/e7600db0eba6fe36afc128688d41/negocios+por+segmento.gif?expires=1786536000&signature=7b948bfa082cc9af0346bab6ee1929d661e475a7f6aa718a76cfff3a3d349473&req=diEkEsl3lYdYW%2FMW3nq%2BgRdR9zlTKc6yKY9aEP68UGrp%2B4SMQ5RQzRG3a0IG%0AzImCNd1wonj1P0ak54QbK2pUJpE%3D%0A)

## 4) Casos de uso da integração

## 4.1) Segmentação automática no Flowbiz com base em dados do Ploomes

A integração permite utilizar **campos do Ploomes** (como marcadores, status e campos personalizados mapeados) para criar **segmentos dinâmicos no Flowbiz**.

Sempre que um contato é atualizado no Ploomes e passa a atender às regras de um segmento:

- Ele entra automaticamente no segmento correspondente no Flowbiz
- Pode ser incluído em **campanhas ou sequências de e-mails**, de forma automática

Esse uso é indicado para automatizar comunicações com base em informações atualizadas diretamente no CRM.

## 4.2) Leads provenientes de formulários do Flowbiz

Quando um lead preenche um formulário em uma landing page do Flowbiz:

- Ele pode ser incluído automaticamente na **lista padrão vinculada à integração**
- Na próxima sincronização, o lead é processado pelo Ploomes conforme as configurações ativas

A partir desse processamento, o lead pode gerar:

- Um **contato** no Ploomes
- Uma **empresa**, apenas se não existir correspondência por **CNPJ ou nome**
- Um ou mais **negócios**, dependendo das opções configuradas na integração

Esse cenário permite transformar leads de marketing em registros acionáveis no CRM sem necessidade de importações manuais.

## 4.3) Qualificação de leads com filtro de segmentos do Flowbiz

A integração permite aplicar um **filtro por segmentos do Flowbiz** para definir **quais leads devem ser enviados ao Ploomes**.

Com esse filtro ativo:

- Apenas leads pertencentes aos **segmentos selecionados** são processados
- Leads fora desses segmentos são ignorados
- As regras de criação de contato, empresa e negócio continuam valendo

Esse caso de uso é indicado quando é necessário enviar ao Ploomes apenas leads qualificados ou separar diferentes estratégias comerciais a partir de uma mesma base de leads.

## 4.4) Criação automática de negócios a partir de leads do Flowbiz

Além da criação de contatos e empresas, a integração pode criar **negócios automaticamente** no Ploomes a partir dos leads recebidos do Flowbiz.

Esse comportamento permite:

- Criar **um negócio por lead**, ou
- Criar **um negócio para cada segmento selecionado para filtragem**, quando a flag de criação de negócios por segmento estiver habilitada

Em todos os casos:

- O negócio é criado sempre no **mesmo funil e estágio configurados**
- A empresa só é criada se não existir correspondência
- Contato, empresa e negócio são relacionados entre si

Esse uso é indicado quando cada lead ou segmento representa uma **oportunidade comercial**.

## 4.5) Consulta de interações de campanhas no Ploomes

Os eventos de interação dos contatos com campanhas do Flowbiz podem ser consultados diretamente no Ploomes.

Para visualizar:

- Acesse a página do contato
- Clique na aba **Flowbiz**

Nessa aba são exibidos eventos como aberturas, bounces e demais interações registradas nas campanhas enviadas.

[GIF animado: Imagem 12: Nessa aba são exibidos eventos como aberturas, bounces e demais interações registradas nas campanhas enviadas.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1792148306/53840b7c8865d6f31247fc1a28fa/consulta+de+intera%C3%A7%C3%B5es.gif?expires=1786536000&signature=a25fb04de681e0b73589e2ebe59a279571526aba827d6001f186943776dff25a&req=dScuFMh6lYJfX%2FMW3nq%2BgQ8Uy8a6xLqLzi9xwJKleAylNJoF%2FF%2Fu8U86PH12%0A4BxrECIzS7Ky1tJF9Fmy1HmDE3s%3D%0A)

## 5) Como funciona a integração

A integração é **bidirecional**, mas **não simétrica**: cada lado tem regras claras sobre o que pode ou não ser atualizado.

## 5.1) Ploomes → Flowbiz

- O Ploomes envia dados ao Flowbiz **em tempo real**, via webhook.
- Alterações em **campos mapeados do contato** atualizam o registro no Flowbiz.
- Se o contato não existir no Flowbiz:

  - É buscado pelo **e-mail**
  - Caso não seja encontrado, um novo contato é criado.
- Alterações de e-mail no Ploomes são refletidas no Flowbiz.
- Se o e-mail for removido no Ploomes, o contato é removido da lista no Flowbiz.

## 5.2) Flowbiz → Ploomes

- O Ploomes consulta o Flowbiz **a cada 5 minutos**.
- O Flowbiz **não sobrescreve dados existentes** no Ploomes.
- Apenas **campos vazios de contatos e empresas** podem ser preenchidos.
- Campos já preenchidos **nunca são alterados**.
- **Negócios não são atualizados** em nenhuma direção.

## 5.3) Criação de entidades

- Contatos podem ser criados a partir de leads do Flowbiz.
- Empresas só são criadas após validação por **CNPJ e nome**.
- Negócios podem ser criados automaticamente, conforme configuração:

  - **1 negócio por lead**, ou
  - **1 negócio por segmento selecionado para filtragem**.
- Todos os negócios são criados no **mesmo funil e estágio configurados**.

## 5.4) Compatibilização de campos de opções

- Ao ativar ou atualizar a integração, as **opções pré-cadastradas** dos campos mapeados são sincronizadas.
- Em campos do tipo lista ou seletor:

  - O Ploomes cria automaticamente no Flowbiz as opções correspondentes.
  - Caso alguma opção não exista, ela é criada durante a atualização.
- Problemas de opções faltantes ou divergentes geralmente são resolvidos **atualizando a integração**.

## 5.5) Limitações importantes

- Descadastros no Flowbiz **não removem contatos** no Ploomes.
- Exclusões no Flowbiz **não são refletidas** no Ploomes.
- Atualizações de negócios **não acontecem** após a criação.

## 6) FAQ

## 6.1) A integração é automática ou precisa ser atualizada manualmente?

A sincronização é **automática**.
O Ploomes envia **webhooks em tempo real** para o Flowbiz sempre que há alterações em contatos, e também realiza **consultas periódicas (a cada 5 minutos)** para processar atualizações e novos leads vindos do Flowbiz.

## 6.2) O que acontece se eu editar o e-mail de um contato no Ploomes?

O e-mail é atualizado imediatamente no Flowbiz via webhook.
Se o novo e-mail já existir em outra lista ou registro, o comportamento segue as **regras de duplicidade**, podendo gerar conflitos ou impedir a atualização.

## 6.3) Posso criar campanhas automáticas no Flowbiz com dados do Ploomes?

Sim.
Campos mapeados do Ploomes podem ser usados para criar **segmentos dinâmicos no Flowbiz**, que alimentam campanhas e sequências de e-mails automaticamente.

## 6.4) Leads capturados por formulários no Flowbiz aparecem no Ploomes?

Sim.
Após a sincronização, o lead é processado no Ploomes conforme as configurações da integração, podendo gerar:

- Um **contato**
- Uma **empresa** (apenas se não existir correspondência por CNPJ ou nome)
- Um ou mais **negócios**, se essa opção estiver habilitada

## 6.5) Onde vejo as interações de campanhas no Ploomes?

Na página do contato, na aba **Flowbiz**, onde são exibidos eventos como aberturas, bounces e interações com campanhas.

## 6.6) O Flowbiz atualiza informações já preenchidas no Ploomes?

Não.
O Flowbiz **não sobrescreve dados existentes** no Ploomes.
Ele apenas **preenche campos que já estejam vazios**, e isso se aplica somente a **contatos e empresas**.

## 6.7) A integração atualiza negócios no Ploomes?

Não.
Negócios podem ser **criados automaticamente**, conforme configuração, mas **não recebem atualizações da integração** após a criação.

## 6.8) Um lead pode gerar mais de um negócio?

Sim, dependendo da configuração.
Se a opção de **criação de negócios por segmento selecionado para filtragem** estiver habilitada, um mesmo lead pode gerar **mais de um negócio**, um para cada segmento selecionado ao qual ele pertença.

## 6.9) O que acontece se um contato for descadastrado ou excluído no Flowbiz?

- **Descadastro (unsubscribe):** o contato permanece no Ploomes
- **Exclusão no Flowbiz:** não é refletida no Ploomes

Para remover um contato do CRM, a exclusão deve ser feita diretamente no Ploomes.

## 6.10) Como resolver problemas com opções de campos que não aparecem corretamente no Flowbiz?

Basta **atualizar a integração**.
Durante a atualização, o Ploomes sincroniza automaticamente as **opções de campos do tipo lista ou seletor**, criando no Flowbiz aquelas que estiverem faltando.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com)
