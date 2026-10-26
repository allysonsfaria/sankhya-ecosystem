---
id: "44010829846039"
titulo: "[TMS] - Integrador VTEX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010829846039--TMS-Integrador-VTEX"
trilha: "Lincros > TMS > VTEX - TMS"
atualizado_em: "2026-10-05T18:47:51Z"
rotulos: ["sync_hc", "lincros", "sync_hash_0f3ae1f04431", "lincros_13434452"]
---

# [TMS] - Integrador VTEX

Este é um artigo complementar. Para saber mais sobre a integração Lincros com VTEX acesse [este artigo](https://sankhya.zendesk.com/hc/pt-br/articles/44010754196759).

## Objetivo:

Este artigo tem como objetivo instruir como realizar as configurações iniciais da integração com a plataforma VTEX.

## Pré-requisitos:

Possuir habilitada a funcionalidade da Integração VTEX

Realizar a configuração em conjunto com o seu consultor Lincros

## Localização:

Cadastros Gerais > Configurações da Empresa > Integrador VTEX

---

## Instruções:

1 - Clicar em "novo"

![Imagem 1: 1 - Clicar em "novo"](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963624482/a3f3ecb10a5ca2aee0dad86d990e/D74F77CA07FC433189D84FDCF5773389?expires=1791331200&signature=f87fd8fe69246d97800bbe356bb6d12c690791041a116391d462d85e3b476d1a&req=dSkhFc98mYVXW%2FMW3nq%2BgWLRlsqiSolIneatXNSM5gVaGubyn6lVhgGb9qex%0Aw7vb6HnwcRqVgY5VjXnBgAVtSpo%3D%0A)

2 - Preencher os campos conforme instruções:

- **Hook Expression:** Preencher campo com valor: invoiced.

  - Este campo serve para definir os dados de autenticação na Lincros e realizar integração. Atualmente o desenvolvimento foi feito apenas para recuperar pedidos com status 'invoiced'.

    - Quando o pedido na vtex alterar o status para faturado, será disparada a integração.
  - Existem outros status que podem ser o gancho para integrar os pedidos, se houver necessidade de importar pedido com status diferente de faturado, deve ser avaliada em conjunto com equipe de produto a viabilidade.
- **Usuário WS:** Usuário de integração (Informado pelo consultor Lincros)
- **Account name:** Nome do ambiente.
- **Environment:** Por padrão sempre preencher como 'vtexcommercestable'

  - Campo referente o 'modo' do ambiente, similar a uma variável padrão para chamar a API da VTex.
- **AppKey** - Referente à sua conta VTEX
- **AppToken** - Referente à sua conta VTEX

3 - Após informar os dados e salvar, clicar em Configurar hook.

- Após o hook ser configurado, todos os campos serão bloqueados e será habilitado um botão para permitir desconfigurá-lo.

  - Esta funcionalidade irá deletar a configuração de hook na vtex e habilitar os campos para alteração.

4 - Para conferir se a integração teve sucesso, acessar a tela de Log de integração VTEX (Sistema > Envios de Integração > Log de integração Vtex).
