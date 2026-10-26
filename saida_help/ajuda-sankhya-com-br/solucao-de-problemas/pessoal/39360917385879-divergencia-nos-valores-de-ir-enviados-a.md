---
id: "39360917385879"
titulo: "Divergência nos valores de IR enviados ao eSocial/DCTFWeb"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39360917385879-Diverg%C3%AAncia-nos-valores-de-IR-enviados-ao-eSocial-DCTFWeb"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-26T00:42:14Z"
rotulos: ["Impostos", "eSocial", "Folha de Pagamento", "Central do eSocial", "DCTFWeb", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Divergência nos valores de IR enviados ao eSocial/DCTFWeb

**Mensagem**

Valores de Imposto de Renda (IR) calculados no sistema não foram enviados corretamente para o eSocial, resultando em diferenças na guia DCTFWeb.

**Situação**

Ao conferir a **"Guia da DCTFWeb"**, foram identificadas divergências nos valores de IR de alguns colaboradores. Os valores calculados no sistema Sankhya não correspondem aos valores enviados ao eSocial, impedindo a correta emissão da guia de recolhimento. Esta inconsistência gera problemas na apuração fiscal e pode resultar em pendências junto à Receita Federal.

**Solução**

Para corrigir as divergências nos valores de IR enviados ao eSocial, siga os passos abaixo:

**(1)** Identifique os colaboradores com divergência nos valores de IR comparando os dados do sistema com a **"Guia DCTFWeb"**. A tela: **''S-5002 - Conferência de IRRF'' (**Pessoal+ » Consultas » S-5002 - Conferência IRRF) poderá ser considerada uma ferramenta auxiliar neste processo.

**Para auxilio em sua utilização, veja o link:**

<https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda-Retido-na-Fonte-por-Trabalhador>

**(2)** Acesse o **"Evento S-1210" na tela: ''central eSocial''** (Pessoal+ » Rotinas Folha » Central do eSocial) do colaborador identificado no eSocial.

**(3)** Realize a exclusão do **"Evento S-1210"** enviado anteriormente com os valores incorretos.

![Imagem 1: https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda…](https://ajuda.sankhya.com.br/hc/article_attachments/41274871057047)

![Imagem 2: https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda…](https://ajuda.sankhya.com.br/hc/article_attachments/41274871058071)

![Imagem 3: https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda…](https://ajuda.sankhya.com.br/hc/article_attachments/41274871058455)![Imagem 4: https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071-Relat%C3%B3rio-S-5002-Confer%C3%AAncia-de-Imposto-de-Renda…](https://ajuda.sankhya.com.br/hc/article_attachments/41274840613911)

Após selecionar o ícone de lixeira, o evento será transferido para a aba; pendentes e estará preparado para envio como 'exclusão'

![Imagem 5: Após selecionar o ícone de lixeira, o evento será transferido para a aba; pendentes e estará preparado para envio como…](https://ajuda.sankhya.com.br/hc/article_attachments/41274871058839)

**(4)** Verifique se os cálculos de IR estão corretos no sistema Sankhya, conferindo a folha de pagamento do colaborador.

**(5)** Realize o reenvio do **"Evento S-1210"** com os valores corretos ao eSocial.

Para suporte com este processo, veja o link:

<https://ajuda.sankhya.com.br/hc/pt-br/articles/37960826085271-Gera%C3%A7%C3%A3o-e-envio-do-evento-S-1210-para-o-eSocial>

**(6)** Aguarde o processamento do evento pelo eSocial e verifique se foi aceito sem erros.

**(7)** Consulte novamente a **"Guia DCTFWeb"** para confirmar que os valores foram atualizados corretamente.

**(8)** Caso persistam divergências em outros colaboradores, repita o processo para cada um deles ou solicite apoio da unidade de suporte para realizar uma conferência completa.

**Causa**

As divergências nos valores de IR enviados ao eSocial podem ocorrer devido a:

- Inconsistências no cálculo da folha de pagamento que não foram identificadas antes do envio;
- Eventos **"S-1210"** enviados com dados desatualizados ou incorretos;
- Alterações retroativas na folha de pagamento que não foram refletidas no eSocial;
- Problemas na integração entre o sistema Sankhya e o eSocial durante o envio dos eventos;
- Deduções ou bases de cálculo despadronizadas/configuradas incorretamente no sistema.
