---
id: "39390412112279"
titulo: "Por que as bases da folha de pagamento não batem com o eSocial?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39390412112279-Por-que-as-bases-da-folha-de-pagamento-n%C3%A3o-batem-com-o-eSocial"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:38Z"
rotulos: ["Configuração", "Impostos", "INSS", "DIRF", "eSocial", "Folha de Pagamento", "FGTS", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Por que as bases da folha de pagamento não batem com o eSocial?

É comum que os valores das **bases de cálculo** apresentados na folha de pagamento do sistema divirjam dos valores exibidos no **portal do eSocial**. Essa diferença geralmente ocorre devido a **critérios distintos de apresentação** utilizados por cada plataforma, especialmente relacionados à **data de pagamento** versus **competência de cálculo**.

Compreender essas diferenças é fundamental para realizar a **conferência correta** dos valores e evitar inconsistências no fechamento da folha e na apuração de impostos.

### Diferença entre data de pagamento e competência de cálculo

A principal causa das divergências está na forma como cada sistema apresenta os valores:

**• eSocial:** apresenta os valores de **FGTS** e **INSS** conforme a **data de pagamento dos encargos**. Por exemplo, se o pagamento de férias com adiantamento de 13º salário ocorreu em 29/01/2026, o eSocial exibirá esses valores na referência **01/2026**.

**• Sistema de Folha:** exibe os valores no resumo da folha conforme a **competência em que o cálculo foi efetivamente realizado**. Seguindo o mesmo exemplo, se o adiantamento do 13º salário nas férias foi calculado na competência **02/2025**, os valores aparecerão nesta referência no sistema, independentemente da data de pagamento.

Essa diferença de critério explica por que os valores podem não coincidir ao comparar os relatórios de ambas as plataformas.

### Eventos despadronizados não compõem as bases corretamente

Outra causa comum de divergência ocorre quando os **eventos de base** estão despadronizados. Nestes casos, alguns eventos podem não compor automaticamente as bases de **INSS** e **FGTS**, gerando diferenças nos valores totais.

Para corrigir essa situação, siga os passos abaixo:

**(1)** Identifique os eventos que estão apontando a diferença dentro da folha (por exemplo, o evento **"10191 - Complemento 13º Reaj. Salarial"**).
**(2)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e selecione os eventos identificados.
**(3)** Navegue até a aba **"Bases de Cálculo"**.
**(4)** Inclua manualmente as bases **"Base INSS 13º Salário"** e **"Base FGTS 13º Salário"** para os eventos que não as possuem.
**(5)** Recalcule a folha de pagamento e verifique se a diferença em relação ao eSocial foi eliminada.

### Incidências fiscais configuradas incorretamente

Configurações incorretas nas **incidências fiscais** das rubricas também podem causar divergências. Um exemplo comum é quando o evento de **"FGTS Normal"** está configurado com **Incidência de IR** (CODINCIRRF) código 79, o que é indevido, pois o FGTS é isento de Imposto de Renda.

Essa parametrização incorreta faz com que os valores de FGTS sejam levados ao **Informe de Rendimentos**, impactando a geração da **DIRF**.

Para corrigir:

**(1)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento de **"FGTS Normal"** (código 995).

![Imagem 1: (1) Acesse a tela "Eventos" (Pessoal+ » Cadastros » Eventos) e localize o evento de "FGTS Normal" (código 995).](https://ajuda.sankhya.com.br/hc/article_attachments/41185577141271)

**(2)** Verifique a configuração do campo **"Incidência de IR"** (CODINCIRRF) encontrado na tela: **"Eventos"** (Pessoal+ » Cadastros » Eventos) aba: ''Esocial'' e altere de código 79 para o código correto de **isenção (atualmente, 09 ante o demonstrado)**.

![Imagem 2: (2) Verifique a configuração do campo "Incidência de IR" (CODINCIRRF) encontrado na tela: "Eventos" (Pessoal+ »…](https://ajuda.sankhya.com.br/hc/article_attachments/41185577143959)

**(3)** Revise as demais rubricas vinculadas a eventos personalizados do sistema para garantir que as incidências estejam corretas.

**Para tal conferência é sugerido utilizar como referência o manual atual do eSocial (leiaute 1.3).**

**(4)** Retifique os eventos já transmitidos ao eSocial, se necessário, para regularizar as informações por meio da tela: **''Central eSocial''** (Pessoal+ » Rotinas Folha » Central do eSocial), evento que informa tais inclusões/alterações reconhecido como: **S-1010.**

- O artigo: [**https://ajuda.sankhya.com.br/hc/pt-br/articles/37880819725079-Gera%C3%A7%C3%A3o-e-envio-do-evento-S-1010-para-o-eSocial**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880819725079-Gera%C3%A7%C3%A3o-e-envio-do-evento-S-1010-para-o-eSocial) **poderá auxiliar com esta geração.**

**(5)** Exclua os eventos **S-1200** e **S-1210** e realize um novo envio ao eSocial para que as informações sejam reprocessadas com as incidências corretas.

### Como conferir os valores corretamente

Para realizar a **conferência adequada** entre a folha de pagamento e o eSocial, considere sempre:

**• Competência versus Data de Pagamento:** verifique se a diferença não é apenas uma questão de apresentação dos valores em referências distintas.

**• Composição das Bases:** certifique-se de que todos os eventos estão compondo corretamente as bases de INSS e FGTS.

**• Incidências Fiscais:** valide se as configurações de incidências (IR, INSS, FGTS) estão corretas para cada evento.

**• Eventos Específicos:** fique atento a eventos como adiantamento de 13º salário, férias, complementos salariais e reajustes, que podem ter tratamentos diferenciados.

Seguindo essas orientações, identifique e corrija as divergências, garantindo a **consistência das informações** entre o sistema de folha de pagamento e o eSocial.
