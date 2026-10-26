---
id: "10089175545751"
titulo: "Conheça quais folhas estão no S-1210 e no S-1200"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10089175545751-Conhe%C3%A7a-quais-folhas-est%C3%A3o-no-S-1210-e-no-S-1200"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:16:10Z"
rotulos: ["XML", "Pagamentos", "S-1200", "eSocial", "Folha de Pagamento", "Verifique XML para folhas mensais e adiantamentos", "Avalie XML para remunerações mensais", "Consulte e exclua documentos", "S-1210", "Remuneração"]
---

# Conheça quais folhas estão no S-1210 e no S-1200

#### Veja abaixo exemplos que vão deixar claro como avaliar:

**Para avaliar o S-1210 Pagamentos:**

![Imagem 1: Para avaliar o S-1210 Pagamentos:](https://ajuda.sankhya.com.br/hc/article_attachments/18970532423959)

**No XML do S-1210 acima demonstra a:**

**Folha Normal Mensal** do período de referência 06/2022 que foi paga no dia 02/07/2022.

**Folha de Adiantamento** do período de referência 07/2022 que foi paga dia 20/07/2022.

O XML do S-1210 de **perApur 07/2022**, quer dizer que o S-1210 está sendo gerado na referência 07/2022 e nele é montando os pagamentos que estiveram **dentro do período de 01/07 a 31/07/2022.**

Usando o SELECT abaixo, conseguirá visualizar mais fácil as folhas pagas dentro do período. Ele deverá ser executado na tela **DBExplorer** (Caminho de acesso à tela: Configurações » Avançado » DBExplorer).

![Imagem 2: Usando o SELECT abaixo, conseguirá visualizar mais fácil as folhas pagas dentro do período. Ele deverá ser executado na…](https://ajuda.sankhya.com.br/hc/article_attachments/10088933369751)

**Veja no portal do eSocial onde consultar S-1210:**

![Imagem 3: Veja no portal do eSocial onde consultar S-1210:](https://ajuda.sankhya.com.br/hc/article_attachments/18970545542807)

Caso precise gerar exclusão do S-1210, conforme exemplo citado acima:

**\*** **Bloqueie a liberaçã**o da folha de pagamento **Mensal** da referência 06/2022 e folha de **adiantamento** da referência 07/2022.

**\*** Feito isso o S1210 será gerado como exclusão na Ref 07/2022.

**Para avaliar o S-1200 Remuneração:**

O XML do S-1200 de **perApur 06/2022**, quer dizer que o S-1200 está sendo gerado na referência 06/2022 e nele é montando as remunerações (folha) que estiveram dentro da referência, ou seja de 01/06 a 30/06/2022.

![Imagem 4: O XML do S-1200 de perApur 06/2022 , quer dizer que o S-1200 está sendo gerado na referência 06/2022 e nele é montando…](https://ajuda.sankhya.com.br/hc/article_attachments/18970545547031)

Para verificar se o S-1200 da folha normal foi enviado corretamente vá ate a referência 06/2022 e verifique a remuneração enviada (S-1200).

Caso precise verificar o adiantamento, vá até a referência 07/2022 e verifique a remuneração enviada no (S-1200).

**Veja no portal do eSocial onde consultar S-1200:**

![Imagem 5: Veja no portal do eSocial onde consultar S-1200:](https://ajuda.sankhya.com.br/hc/article_attachments/18970532435991)

Caso precise gerar exclusão do S-1200, conforme exemplo citado acima:

**\* Bloqueie a liberação** da folha de pagamento Mensal da referência 06/2022.

**\*** Feito isso o S1200 será gerado como exclusão na Ref 06/2022.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10089175545751-Conhe%C3%A7a-quais-folhas-est%C3%A3o-no-S-1210-e-no-S-1200#top)
