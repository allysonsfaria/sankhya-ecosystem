---
id: "7270116254359"
titulo: "S-1210 - Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7270116254359-S-1210-Erro-724-N%C3%A3o-foi-localizado-um-evento-de-remunera%C3%A7%C3%A3o-do-trabalhador-para-o-per%C3%ADodo-e-com-mesmo-demonstrativo-de-pagamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-02T14:20:19Z"
rotulos: ["não apagar", "S-1200", "eSocial", "Folha de Pagamento", "Erro 724", "Central do eSocial", "Erro 724: Evento de Remuneração Não Encontrado", "Erro", "S-1210", "Remuneração"]
---

# S-1210 - Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento.

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16513197779223) MENSAGEM**:

Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento. Ação Sugerida:
Deve ser um valor atribuído pela fonte pagadora em S-1200, S-1202 ou S-1207 no campo "Identificador de Recibo de Pagamento", obedecendo a relação:
.Se Tipo de Pagamento = [1], em S-1200;
.Se Tipo de Pagamento = [4], em S-1202;
.Se Tipo de Pagamento = [5], em S-1207

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513222286487) SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo:

![Imagem 3: Acesse a central do e-Social e verifique se o evento de remuneração (S-1200/S-2299) foi enviado sem erros ao portal do…](https://ajuda.sankhya.com.br/hc/article_attachments/16513222288535) Acesse a central do e-Social e verifique se o evento de remuneração (S-1200/S-2299) foi enviado sem erros ao portal do eSocial;

**(2)**S-1200 enviado, para conferência acesse o Portal do eSocial na opção: **Folha de Pagamento >> Gestão de folha >> Trabalhadores >> Remuneração devida** e confira se todas as folhas que o funcionário teve no mês constam no portal (Exemplo: adiantamento, férias, normal);

**(2)**S-2299 enviado, para conferência acesse o Portal do eSocial na opção: **Empregado >> Gestão de Empregados >> Desligamento** e verifique se a rubricas da rescisão foram enviadas (se tiver folha de adiantamento precisa constar aí também);

![Imagem 4: Caso não tenha enviado o evento de remuneração, envie e depois gere o S-1210 para envio;](https://ajuda.sankhya.com.br/hc/article_attachments/16513197789975) Caso não tenha enviado o evento de remuneração, envie e depois gere o S-1210 para envio;

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16513222302871)CAUSA:**

Essa mensagem de erro de validação ocorre no retorno do Evento S-1210 quando o evento de remuneração (S-1200 /S-2299) deste funcionário não foi enviado ou retornou com erros.
