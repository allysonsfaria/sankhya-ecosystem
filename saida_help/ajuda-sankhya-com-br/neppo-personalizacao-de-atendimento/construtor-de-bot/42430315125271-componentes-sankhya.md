---
id: "42430315125271"
titulo: "Componentes Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430315125271-Componentes-Sankhya"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:32Z"
rotulos: ["sync_hc", "neppo", "neppo_857998462", "sync_hash_4a06f920f674"]
---

# Componentes Sankhya

A integração entre a **Plataforma Neppo Omnichannel** e o **ERP Sankhya** viabiliza o uso de componentes inteligentes no Construtor de Bot. Esses componentes permitem consultar dados diretamente da base Sankhya, oferecendo experiências conversacionais conectadas com informações reais do ERP em tempo real.

Para garantir que essa comunicação ocorra com segurança e confiabilidade, é necessário realizar a configuração do Gateway no Sankhya e registrar o token de integração no ambiente Neppo.

- [Dados do Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42430352793239)
- [Obter pedidos](https://sankhya.zendesk.com/hc/pt-br/articles/42430345961879)
- [Itens do Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430353726743)
- [Criar Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430354191767)
- [Preço do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430386027287)
- [Estoque do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430402782487)
- [Locais de Estoque](https://sankhya.zendesk.com/hc/pt-br/articles/42430348719383)
- [Volumes Alternativos](https://sankhya.zendesk.com/hc/pt-br/articles/42430361336343)
- [Obter Preferência](https://sankhya.zendesk.com/hc/pt-br/articles/42430349855127)
- [Tabela de Preço](https://sankhya.zendesk.com/hc/pt-br/articles/42430362758935)
- [Tipo de Operação](https://sankhya.zendesk.com/hc/pt-br/articles/42430406143383)
- [Tipos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/42430364291351)
- [Detalhe do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430364864407)
- [Busca de Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430376763159)
- [Adicionar ao Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377203479)
- [Alterar Quantidade no Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377845911)
- [Obter Itens do Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430378480151)

---

## Etapa 1 – configuração do gateway na sankhya

1. **Acesse a tela**: `Configurações Gateway` no ERP Sankhya.
2. **Aba aplicações vinculadas**: vá até a aba responsável pelo gerenciamento de integrações.
3. Clique em `+` **(Cadastrar aplicação)**.

4. No campo **Buscar aplicação**, digite `Neppo`.
5. Selecione a opção:

   ```
   Neppo: Plataforma Omnichannel
   ```
6. **Vincule um usuário** com as permissões necessárias para consulta de dados (ex: TGFPAR, TGFCAB, TGFITE).
7. Confirme o cadastro.
8. Após confirmação, será gerada automaticamente uma **Chave do Cliente** (token de integração).

![Imagem 1: Após confirmação, será gerada automaticamente uma Chave do Cliente (token de integração).](https://ajuda.sankhya.com.br/hc/article_attachments/42639599808279)
> **Importante:** Copie e guarde esse token com segurança. Ele será usado para autenticar as chamadas da Neppo ao ERP.

Referência: <https://neppo-team.atlassian.net/wiki/spaces/SRV/pages/350126084/Pr+-requisitos+para+Integra+o+Sankhya+Neppo?themeState=light>

---

## Etapa 2 – registro do token na tela de Integrações

Para que os componentes da Neppo utilizem o token de forma segura e padronizada, siga os passos abaixo:

1. Acesse o **Menu → Configurações → Integrações → Sankhya**

   ![Imagem 2: Acesse o Menu → Configurações → Integrações → Sankhya](https://ajuda.sankhya.com.br/hc/article_attachments/42639596153495)
2. Você tem a opção de cadastrar um token para ambiente de produção e/ou token do ambiente de teste.

**Aviso:** Os componentes da Sankhya são configurados por padrão para o ambiente de Produção. Para realizar testes, é necessário habilitar o token do ambiente de Teste e ajustar a configuração dos componentes no fluxo para utilizar esse ambiente.

> 🛡️ Esta variável será utilizada automaticamente pelos componentes ao realizar as chamadas para a API da Sankhya via Gateway.

---

## Observações adicionais

- Certifique-se de que o usuário vinculado à aplicação Neppo no Sankhya tenha acesso às tabelas necessárias:
  `TGFPAR`, `TGFCAB`, `TGFITE`, `TGFPRO`, `TSICID`, `TGFVEN`, entre outras.
- Em ambientes com múltiplas empresas (multitenant), valide se o código de empresa está disponível nas consultas.
- Para ambientes de homologação, recomenda-se o uso de um usuário com permissões de leitura e ambiente controlado.

- [Dados do Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42430352793239)
- [Obter pedidos](https://sankhya.zendesk.com/hc/pt-br/articles/42430345961879)
- [Itens do Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430353726743)
- [Criar Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430354191767)
- [Preço do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430386027287)
- [Estoque do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430402782487)
- [Locais de Estoque](https://sankhya.zendesk.com/hc/pt-br/articles/42430348719383)
- [Volumes Alternativos](https://sankhya.zendesk.com/hc/pt-br/articles/42430361336343)
- [Obter Preferência](https://sankhya.zendesk.com/hc/pt-br/articles/42430349855127)
- [Tabela de Preço](https://sankhya.zendesk.com/hc/pt-br/articles/42430362758935)
- [Tipo de Operação](https://sankhya.zendesk.com/hc/pt-br/articles/42430406143383)
- [Tipos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/42430364291351)
- [Detalhe do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430364864407)
- [Busca de Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430376763159)
- [Adicionar ao Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377203479)
- [Alterar Quantidade no Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377845911)
- [Obter Itens do Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430378480151)
