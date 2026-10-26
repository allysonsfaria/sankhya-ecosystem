---
id: "44010094505495"
titulo: "Como configurar as entradas DNS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010094505495-Como-configurar-as-entradas-DNS"
trilha: "Flowbiz > Dúvidas Frequentes"
atualizado_em: "2026-10-05T18:29:36Z"
rotulos: ["sync_hc", "flowbiz", "sync_hash_6e71f2aeefa4", "flowbiz_30"]
---

# Como configurar as entradas DNS

A **autenticação do DNS** é extremamente importante para o e-mail marketing, pois essa configuração influencia diretamente na **entregabilidade** **de suas campanhas**.

Esta autenticação permite que os principais ISPs (Outlook, Gmail e etc.) identifiquem que a **Flowbiz** está autorizada a realizar envios em seu nome.

Sem o DNS seu envio poderá ser interpretado pelos provedores como SPAM ou até mesmo Phishing, que é um dos tipos de golpe mais comuns da internet. Ele é usado para **roubar** informações pessoais de usuários.

No total, são 3 entradas que precisam ser inseridas. Para realizar as configurações das entradas é necessário acessar o **painel de hospedagem** do seu domínio e inserir as **entradas abaixo:**

\*Se o seu domínio aponta para mais de uma hospedagem, é preciso realizar as alterações igualmente em todas.

## As entradas são:

**• ENTRADA 01 (DKIM):**
**Nome da entrada:** mailbiz.\_domainkey
**Tipo:** TXT
**Conteudo:** v=DKIM1; k=rsa; t=s; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDqgysd/TI0iPUocxYQd+Yb6XnmyA/97dusMtf/maiDiFAbxhfk1w5X3GFgUA5Q0sTdE6yN6np9h8GiHS2i8/pQv9cW9bK26SaHta2gd1RzZvwuadZGFeRV+5KE5/B43mIZuJP58vUJb1I4smpYTqK4DPHv9FgLogYKaOYVwFy/wIDAQAB

**• ENTRADA 02 (DKIM):**
**Nome da entrada:** \_domainkey
**Tipo:** TXT
**Conteudo:** o=~;

## Configuração da Entrada DMARC

Além do DKIM, é altamente recomendável configurar a entrada **DMARC**, pois ela melhora a autenticidade dos seus envios e ajuda a evitar que seus e-mails sejam classificados como SPAM. Essa configuração permite que os provedores validem se os e-mails enviados em nome do seu domínio estão devidamente autenticados.

## • ENTRADA 03 (DMARC):

**Nome:** \_dmarc

**Tipo:** TXT

**Conteúdo:** v=DMARC1; p=none; [rua=mailto:abuse@mailbiz.com.br](mailto:rua=mailto:abuse@mailbiz.com.br); [ruf=mailto:abuse@mailbiz.com.br](mailto:ruf=mailto:abuse@mailbiz.com.br)

🔹 Caso seu domínio utilize o Cloudflare, lembre-se de configurar essa entrada como ➡ **DNS only**.

Abaixo temos alguns artigos sobre diferentes painéis:

Atualmente temos muito painéis de hospedagem e o local de configuração pode variar. Confira as instruções específicas dos principais serviços de domínio ou provedor de hospedagem:

- [RegistroBR](https://popconvert.com/pt-br/como-configurar-dkim-e-spf-no-registro-br/)
- [Go Daddy](https://br.godaddy.com/help/adicionar-um-registro-cname-19236)
- [Locaweb](https://ajuda.locaweb.com.br/wiki/como-criar-as-entradas-de-dns-na-zona-de-dns-hospedagem-de-sites-2/)
- [Wordpress](https://br.godaddy.com/help/adicionar-um-registro-cname-19236)
- [Hostgator](https://suporte.hostgator.com.br/hc/pt-br/articles/115000389554-Como-criar-ou-alterar-um-registro-na-zona-DNS-)
- [Wix](https://support.wix.com/pt/article/adicionando-ou-atualizando-registros-cname-em-sua-conta-wix)
- [Hostinger](https://www.hostinger.com.br/tutoriais/como-usar-editor-de-zona-dns-hostinger/)
- [Uol](https://faq.uolhost.uol.com.br/content/como-criar-entradas-de-dns-dentro-do-meu-dominio)
- [Cloudfare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records)

## Importante!

## Se você utiliza Cloudflare nas entradas CNAME mude a proxy para ➡  DNS only

## Se você utiliza a plataforma Magazord, pode ser necessário solicitar a inclusão das entradas DNS diretamente pelo chat de suporte da Magazord.

⚠️ Antes de editar o DNS, consulte o que está pendente para evitar duplicidade. Se precisar de ajuda, chame um especialista para conferir!
