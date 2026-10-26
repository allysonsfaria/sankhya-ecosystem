---
id: "41182140813719"
titulo: "Processo Ativação do Sankhya Pass"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41182140813719-Processo-Ativa%C3%A7%C3%A3o-do-Sankhya-Pass"
trilha: "Manual do Produto > Comece por aqui > Sankhya Pass"
atualizado_em: "2026-10-22T14:46:29Z"
rotulos: ["Produtos", "Configuração", "Segurança", "Sankhya ID", "Central de Projetos"]
---

# Processo Ativação do Sankhya Pass

**Caminho de acesso:** tela de login dos produtos Sankhya

---

## O que é e para que serve

O **Sankhya Pass** centraliza a autenticação dos usuários nas soluções do ecossistema Sankhya. Este processo descreve a ativação do Sankhya Pass no ambiente do cliente — preparação dos usuários, validação dos acessos, vínculo entre os sistemas e ativação da autenticação no **Sankhya Om** — e serve para administradores responsáveis pela implantação. A ativação final no Sankhya Om é feita pelo seu gerente de relacionamento (GR), não pelo suporte Sankhya. Este processo não cobre a criação do ambiente Sankhya Om nem a gestão cotidiana de permissões — para isso, acesse [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos).

## Antes de começar

- O ambiente Sankhya Om deve utilizar SSL, com HTTPS válido e funcional.
- Preferencialmente, o ambiente deve estar acessível publicamente pela internet.
- Os e-mails dos usuários devem estar padronizados entre os sistemas — utilize os e-mails corporativos oficiais.
- A versão do Sankhya Om deve ser, no mínimo:
  - `4.36b78`, para ambientes na versão 4.36;
  - `4.35b814`, para ambientes na versão 4.35.
- Utilize um destes navegadores: Google Chrome, Microsoft Edge, Safari ou Mozilla Firefox.

**⚠️ Atenção**

Se o ambiente não estiver exposto publicamente, libere o acesso para gravação de cookies pelo Sankhya Pass. Regras de segurança e proxy podem exigir ajustes adicionais.

**💡 Dica**

Ative o parâmetro de VM `-Dpreferir.login.sankhya.pass.ativo.web.component=true` no Sankhya Om. Assim, o Sankhya Pass aparece como a opção principal na tela de login, o que deixa a autenticação mais fluida para o usuário.

## Etapa 1 — Obter acesso administrativo na Área do Cliente

Garanta que o responsável pela ativação possua perfil de administrador na [Área do Cliente Sankhya](https://clientes.sankhya.com.br/). O perfil de administrador permite gerenciar usuários, conceder permissões e acompanhar a ativação.

![Imagem 1: Garanta que o responsável pela ativação possua perfil de administrador na Área do Cliente Sankhya . O perfil de…](https://ajuda.sankhya.com.br/hc/article_attachments/41182140811543)

**ℹ️ Nota**

Esse acesso só pode ser concedido pelo seu GR. Fale com ele diretamente — não é necessário abrir chamado de suporte para isso.

## Etapa 2 — Cadastrar os usuários na Área do Cliente

1. Acesse a gestão de usuários da Área do Cliente.
2. Cadastre todos os usuários que utilizarão o Sankhya Pass, com os e-mails corporativos oficiais.

O e-mail cadastrado é a chave de identificação entre os sistemas do ecossistema Sankhya.

## Etapa 3 — Garantir que os usuários existam no Sankhya Om

Todos os usuários cadastrados na Área do Cliente também devem existir no **Cadastro de** [**Usuários**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) do Sankhya Om. O vínculo entre os ambientes é feito pelo campo **E-mail** — o valor deve ser exatamente o mesmo nos dois cadastros. Exemplo: `usuario@empresa.com.br` na Área do Cliente e `usuario@empresa.com.br` no Sankhya Om.

**⚠️ Atenção**

Divergências entre os e-mails impedem o funcionamento da autenticação via Sankhya Pass.

## Etapa 4 — Validar o acesso dos usuários

Antes da ativação definitiva, solicite que os usuários acessem a Área do Cliente, realizem a autenticação e confirmem que conseguem gerenciar seus dados cadastrais. Essa validação antecipa problemas de cadastro, inconsistências de e-mail e dificuldades de autenticação.

## Etapa 5 — Solicitar a ativação do Sankhya Pass no Sankhya Om

**⚠️ Atenção**

Com as etapas 1 a 4 concluídas, entre em contato com seu GR e informe que o ambiente está pronto. A ativação do Sankhya Pass é feita por ele — não é necessário abrir chamado de suporte.

## Etapa 6 — Acompanhar o pós-ativação

1. Valide os acessos dos usuários.
2. Acompanhe o rollout inicial.
3. Monitore dúvidas e inconsistências de autenticação.

**💡 Dica**

Faça uma ativação gradual: isso facilita o suporte aos usuários, o acompanhamento técnico e a identificação de problemas operacionais.

## Resultado esperado

Ao final do processo:

- os usuários acessam o Sankhya Om utilizando o Sankhya Pass;
- a autenticação fica centralizada;
- o cliente tem uma gestão unificada de acessos no ecossistema Sankhya.
