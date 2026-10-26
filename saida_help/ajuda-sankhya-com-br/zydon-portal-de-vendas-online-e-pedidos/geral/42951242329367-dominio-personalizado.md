---
id: "42951242329367"
titulo: "Domínio Personalizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951242329367-Dom%C3%ADnio-Personalizado"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T13:57:29Z"
rotulos: ["zydon", "sync_hc", "zydon_213266911393", "sync_hash_a4e68b10420d"]
---

# Domínio Personalizado

Um **domínio personalizado** é um endereço exclusivo na web para o seu portal B2B. Em vez de usar a URL padrão gerada pelo sistema, você pode configurar um endereço próprio como `meuportal.com.br`, tornando o acesso mais profissional e alinhado à sua marca.

## Prɩrw-requisitos

- Acesso ao **Zydon Admin** com permissão para editar Informações da loja.
- Domínio próprio já registrado em um provedor de DNS (ex.: Registro.br, GoDaddy, Cloudflare).

## Passo a passo

1. No menu lateral esquerdo, clique em **Informações da loja → Domínio**.
2. Você verá a **URL padrão** gerada automaticamente — é possível alterá-la a qualquer momento.
3. Para usar um domínio personalizado, clique no botão de ativação. O campo de preenchimento será exibido.
4. No campo **Domínio**, insira o endereço desejado no formato `subdominio.seudominio.com.br`:
   - ✒ `meuportal.portal.com.br`
   - ✒ `www.portal.com.br`
   - ✖ meuportal.com.br (domínio raiz, não aceito)
   - ✝ meuportal (inválido)
5. Clique em **Gerar Chave**. Serão exibidos Tipo, Nome e Valor para configuração.
   ![Imagem 1: Clique em Gerar Chave . Serão exibidos Tipo, Nome e Valor para configuração.](https://downloads.intercomcdn.com/i/o/jgm6ml00/1623605061/39906b48c07ea91609e7dffdd105/image.png?expires=1778889600&signature=6430165d708294e5d0eb72f31decef4827bb3f389c0ef131b96afd54a5ca145e&req=dSYlFcx2noRZXfMW3nq%2BgYp0usInAOSj3wqlKbJeb4cg0FRyWLIqM%2BwIyH%0AHk3vlUT1vMozejKvsehWYop2A%3D%0A)
6. Acesse o painel do seu provedor de DNS e crie um novo registro **CNAME** com as informações geradas.
7. Aguarde a propagação do DNS.

> **💡 Dica:** consulte o artigo **"Como configurar um domínio no meu provedor?"** para tutoriais dos provedores mais usados.

## Perguntas frequentes

**Quanto tempo leva a propagação do DNS?**
Pde variar de alguns minutos a 48 horas.

---

### 🚀 Teste grátis por 15 dias!

[admin.zydon.com.br/criacao-conta](https://admin.zydon.com.br/criacao-conta)
