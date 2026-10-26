---
id: "7867539538967"
titulo: "Não foi possível realizar a compensação automática pois uma liberação de limites do Evento '24 - Autorização de Pagamento' foi lançada ao tentar baixar os títulos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7867539538967-N%C3%A3o-foi-poss%C3%ADvel-realizar-a-compensa%C3%A7%C3%A3o-autom%C3%A1tica-pois-uma-libera%C3%A7%C3%A3o-de-limites-do-Evento-24-Autoriza%C3%A7%C3%A3o-de-Pagamento-foi-lan%C3%A7ada-ao-tentar-baixar-os-t%C3%ADtulos"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-10-14T12:25:49Z"
rotulos: ["Configuração", "Liberação de Limites", "TOP", "Preferências", "Financeiro", "não apagar", "#validadoHugo", "CORE_E01707", "Liberação de limites bloqueia compensação", "Valor mínimo na TOP > 000", "Ajuste \"TOPBAIDESPCOMP\"", "Erro"]
---

# Não foi possível realizar a compensação automática pois uma liberação de limites do Evento '24 - Autorização de Pagamento' foi lançada ao tentar baixar os títulos

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16541526342295) MENSAGEM**:

[CORE\_E01707] Não foi possível realizar a compensação automática pois uma liberação de limites do Evento '24 - Autorização de Pagamento' foi lançada ao tentar baixar os títulos.
O processo de compensação automática não é compatível com liberação de limites. Configure o sistema para que os títulos envolvidos na compensação não necessitem de liberações para serem baixados."

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16541543084951)SOLUÇÃO:**

Verifique as seguintes configurações:

![Imagem 3: Analise qual TOP está configurada no parâmetro (tela de " Preferências" ) " TOPBAIDESPCOMP";](https://ajuda.sankhya.com.br/hc/article_attachments/16541526349719) Analise qual TOP está configurada no parâmetro (tela de **"Preferências"**) **"TOPBAIDESPCOMP";**

![Imagem 4: Analise qual TOP está configurada no parâmetro (tela de " Preferências" ) " TOPBAIDESPCOMP";](https://ajuda.sankhya.com.br/hc/article_attachments/16541543091223)

![Imagem 5: Tela de Tipo de Operação - TOP, localize a top informada no parâmetro mencionado acima;](https://ajuda.sankhya.com.br/hc/article_attachments/16541543093399)  Tela de Tipo de Operação - TOP, localize a top informada no parâmetro mencionado acima;

![Imagem 6: Tela de Tipo de Operação - TOP, localize a top informada no parâmetro mencionado acima;](https://ajuda.sankhya.com.br/hc/article_attachments/16541543095575)

![Imagem 7: Verifique a informação do campo: 'Valor mínimo p/Autorização de Pagamento:'](https://ajuda.sankhya.com.br/hc/article_attachments/16541526363543) Verifique a informação do campo: **'Valor mínimo p/Autorização de Pagamento:'**

Se estiver com valor informado ali, o sistema emite aquela mensagem solicitando a liberação.

![Imagem 8: Se estiver com valor informado ali, o sistema emite aquela mensagem solicitando a liberação.](https://ajuda.sankhya.com.br/hc/article_attachments/16541543100823)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16541543101847)CAUSA:**

O erro ocorre quando se configurou a compensação automática utilizando uma TOP de baixa que está com campo Valor mínimo p/Autorização de Pagamento diferente de 0,00.
