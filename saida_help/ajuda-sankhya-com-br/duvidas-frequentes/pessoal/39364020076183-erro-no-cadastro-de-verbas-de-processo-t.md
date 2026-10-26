---
id: "39364020076183"
titulo: "Erro no cadastro de verbas de processo trabalhista S-2501 - Não é possível cadastrar verbas sem incidências"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39364020076183-Erro-no-cadastro-de-verbas-de-processo-trabalhista-S-2501-N%C3%A3o-%C3%A9-poss%C3%ADvel-cadastrar-verbas-sem-incid%C3%AAncias"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:03Z"
rotulos: ["Configuração", "Impostos", "Folha", "eSocial", "Processo Trabalhista", "Artigo criado KCS", "Sankhya RH - KCS", "S-2501"]
---

# Erro no cadastro de verbas de processo trabalhista S-2501 - Não é possível cadastrar verbas sem incidências

**MENSAGEM**

Não é possível cadastrar verbas sem incidências para o evento S-2501

**SITUAÇÃO**

Ao tentar cadastrar verbas no **"Processo Trabalhista"** (Pessoal+ » Rotinas Folha » Processo Trabalhista) para envio do evento **S-2501** ao eSocial, o sistema impede o cadastro quando as rubricas não possuem incidências fiscais configuradas corretamente. Esta situação ocorre durante o preenchimento das informações de tributos decorrentes de processo trabalhista, especialmente quando há valores tributáveis que precisam ser informados ao eSocial.

**SOLUÇÃO**

Para resolver este erro, siga os passos abaixo:

**(1)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize as rubricas que serão utilizadas no processo trabalhista.

**(2)** Verifique se as rubricas possuem as **"Incidências Fiscais"** configuradas corretamente, especialmente para **"INSS"**, **"FGTS"** e **"Imposto de Renda"**.

![Imagem 1: Configure as incidências de acordo com a natureza da verba do processo trabalhista. Certifique-se de que as rubricas…](https://ajuda.sankhya.com.br/hc/article_attachments/41263575813655)

**(3)** Configure as incidências de acordo com a natureza da verba do processo trabalhista. Certifique-se de que as rubricas estejam parametrizadas conforme as regras do eSocial.

Neste link externo, constam as informações fornecidas pelo leiaute 1.3 do eSocial pertinente as rúbricas:

<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-nt-06-2026-rev-09-04-2026/index.html#evtTabRubrica>

**(4)** Após configurar as incidências, caso tenha havido alguma alteração, efetue por meio da tela: **''Central eSocial''** (Pessoal+ » Rotinas Folha » Central do eSocial) a geração e envio do S-1010 para adequação das informações que serão transmitidas no processo.

Para suporte com este envio, veja o link a seguir:

<https://ajuda.sankhya.com.br/hc/pt-br/articles/37880819725079-Gera%C3%A7%C3%A3o-e-envio-do-evento-S-1010-para-o-eSocial>

Após o envio do S-1010, caso seja necessário, retorne ao cadastro do **"Processo Trabalhista"** e realize novamente o cadastro das verbas.

**(5)** Envie o evento **"S-2500"** primeiro, seguido do evento **"S-2501"**, respeitando a ordem de envio estabelecida pelo eSocial.

**CAUSA**

O erro ocorre porque o eSocial exige que todas as verbas informadas no evento **"S-2501"** possuam incidências fiscais devidamente configuradas. As rubricas utilizadas em processos trabalhistas devem ter suas bases de cálculo e incidências tributárias definidas para que o sistema possa calcular corretamente os valores de **"INSS"**, **"FGTS"** e **"Imposto de Renda"** decorrentes da decisão judicial. Sem essas configurações, o sistema não consegue gerar as informações necessárias para os eventos **"S-2500 e S-2501"**.
