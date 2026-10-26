---
id: "42951370070295"
titulo: "Como configurar um domínio no meu provedor?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951370070295-Como-configurar-um-dom%C3%ADnio-no-meu-provedor"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T14:01:55Z"
rotulos: ["zydon", "sync_hc", "sync_hash_dee9f1cedc84", "zydon_213269676410"]
---

# Como configurar um domínio no meu provedor?

Para usar um domínio personalizado no seu portal Zydon, é necessário configurar registros DNS no painel do seu provedor de hospedagem. Este artigo mostra como fazer nos provedores mais comuns.

## O que é DNS e por que preciso configurar?

O DNS traduz o nome do seu site em um endereço IP. Para apontar seu domínio ao portal Zydon, crie um registro **CNAME** com os dados fornecidos pelo Zydon Admin no artigo **Domínio Personalizado**.

## Registro.br

1. Acesse o painel do Registro.br e localize seu domínio.
   ![Imagem 1: Acesse o painel do Registro.br e localize seu domínio.](https://ajuda.sankhya.com.br/hc/article_attachments/42951377187095)
2. Verifique se o provedor de serviços está como **nenhum (0)**.
   ![Imagem 2: Verifique se o provedor de serviços está como nenhum (0) .](https://ajuda.sankhya.com.br/hc/article_attachments/42951385764631)
3. Adi a one o registro CNAME.
   ![Imagem 3: Adi a one o registro CNAME.](https://ajuda.sankhya.com.br/hc/article_attachments/42951377806487)
   ![Imagem 4: Adi a one o registro CNAME.](https://ajuda.sankhya.com.br/hc/article_attachments/42951386361879)

## Cloudflare

1. Acesse seu painel Cloudflare e selecione o domínio.
2. V¡i em DNS ₒ Registros ₒ Adicionar registro.
   ![Imagem 5: V¡i em DNS ₒ Registros ₒ Adicionar registro.](https://downloads.intercomcdn.com/i/o/jgm6ml00/1740530700/5dd05043bf2b824bff112de76972/1712327944387-1712327944387.jpeg?expires=1778889600&signature=b72cf205eb6cd7212cc86b91ede18f36cbead1f5deadb5a92a8abcf1a5e1e3a6&req=dScjFsx9nYZfWfMW3nq%2BgQfTHHN61Skt%2FvrZH3pVj83BgN6ZXmQxNW%2BxsD25%0AYD%2F5VsHo31dxzMD%2FWya6859H2P0%3D%0A)
3. Selecione tipo CNAME e preencha com os dados do Zydon.
   ![Imagem 6: Selecione tipo CNAME e preencha com os dados do Zydon.](https://ajuda.sankhya.com.br/hc/article_attachments/42951357326359)
4. Desative o proxy (nuvem laranja < cinza) para que o CNAME funcione.
   ![Imagem 7: Desative o proxy (nuvem laranja < cinza) para que o CNAME funcione.](https://ajuda.sankhya.com.br/hc/article_attachments/42951365358231)

## GoDaddy

1. Acesse o painel GoDaddy, vá em Meus Domínios ₒ Gerenciar DNS.
   ![Imagem 8: Acesse o painel GoDaddy, vá em Meus Domínios ₒ Gerenciar DNS.](https://ajuda.sankhya.com.br/hc/article_attachments/42951401563927)
2. Adicione um registro CNAME com os dados do Zydon e salve.
   ![Imagem 9: Adicione um registro CNAME com os dados do Zydon e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/42951387431703)

> Após configurar o CNAME, aguarde até 48h para propagação completa do DNS.

---

[admin.zydon.com.br/criacao-conta](https://admin.zydon.com.br/criacao-conta)
