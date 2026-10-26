---
id: "44010205323415"
titulo: "Como conectar o Google Analytics 4 (GA4) na Flowbiz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010205323415-Como-conectar-o-Google-Analytics-4-GA4-na-Flowbiz"
trilha: "Flowbiz > Métricas"
atualizado_em: "2026-10-05T18:32:31Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_83", "sync_hash_604719cbd472"]
---

# Como conectar o Google Analytics 4 (GA4) na Flowbiz

Para integrar a ferramenta da Flowbiz com o Google Analytics 4 e acompanhar os dados de receita, siga o passo a passo a abaixo:

**1.** Acesse a plataforma da Flowbiz e faça login em sua conta.

**2.** No menu principal, clique na opção **Analytics**. Essa opção está localizada na barra de navegação superior. **Caso você tenha o modulo Jornadas**, vá em R**elatórios** e A**nalytics**.

![Imagem 1: IMPORTANTE: Caso você já tenha o GA Universal conectado, basta clicar em desconectar antes de começar o processo de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010184789655)**IMPORTANTE:** Caso você já tenha o GA Universal conectado, basta clicar em desconectar antes de começar o processo de conexão

**3.** Clique no botão **Conectar** para iniciar o processo de integração.

**4.** Uma janela pop-up será aberta, solicitando que você faça **login com sua conta do Google Analytics**. Insira suas credenciais de login e clique em **Permitir** para **autorizar a integração** **entre as duas ferramentas**.

**5.** Após permitir o acesso, você será redirecionado de volta à plataforma da Flowbiz. Agora, **selecione a sua conta do Google Analytics na lista suspensa**. Certifique-se de **escolher a conta correta associada** ao seu **website**.

1. Na opção **Origem/Mídia Padrão Flowbiz**, você terá duas escolhas. Se você estiver utilizando o rastreamento padrão da Flowbiz, deixe essa opção selecionada. Caso esteja usando um rastreamento personalizado, insira a origem/mídia personalizada no campo indicado. Com a mudança de marca para Flowbiz, as contas novas já passam a usar automaticamente a UTM padrão flowbiz / email.

No caso de contas mais antigas, a UTM anterior mailbiz / email continua válida desde que o GA4 não seja desconectado. Se a conta for desconectada e reconectada, o sistema vai sugerir automaticamente a nova UTM flowbiz / email no campo principal, e essa sugestão não pode ser alterada nessa etapa.

Se você quiser manter a UTM antiga mailbiz / email, será necessário inseri-la manualmente nos campos adicionais de origem/mídia que aparecem logo abaixo durante a reconexão.

**Importante:** o sistema permite configurar até **3 UTMs diferentes**. Então, em contas que utilizam módulos adicionais como o **Jornadas Pro**, pode ser necessário remover uma das mídias menos utilizadas para conseguir manter a UTM mailbiz / email.

**7.** Depois de verificar as configurações, clique em **Salvar** para concluir o processo de integração.

**Parabéns! O Google Analytics foi integrado à sua conta da Flowbiz com sucesso.** Agora você poderá acompanhar os dados de receita e outras métricas relacionadas ao seu e-mail marketing.

**OBS:** É importante lembrar que o módulo de "Comércio Eletrônico" do Google Analytics deve estar ativado para que o acompanhamento de dados de receita funcione corretamente.

---

## Por que meu Google Analytics desconectou?

Se a sua integração do Google Analytics caiu, fique tranquilo! Na maioria das vezes, isso acontece de forma automática por **regras de segurança do próprio Google**, e não por erro humano ou falha no sistema.

Os motivos mais comuns são:

- **Renovação de Segurança do Google:** O Google expira as "chaves de acesso" de ferramentas externas de tempos em tempos para garantir que seus dados continuem protegidos.
- **Mudança de Senha:** Se o usuário que fez a primeira conexão mudou a senha do e-mail Google dele, o acesso é derrubado imediatamente por segurança.
- **Alteração de Permissões:** Se a pessoa que conectou perdeu o acesso de Administrador no painel do GA, a integração deixa de funcionar.

> 💡 **Dica:** Prefira fazer a conexão usando um e-mail geral da empresa (ex: `marketing@suaempresa.com`) com acesso administrador. Isso evita quedas caso um colaborador mude de senha ou saia da equipe.

---

Caso ficar com alguma dúvida, não hesite em nos chamar no chat da ferramenta!
