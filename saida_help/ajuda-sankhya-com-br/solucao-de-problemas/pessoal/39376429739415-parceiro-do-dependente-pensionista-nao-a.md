---
id: "39376429739415"
titulo: "Parceiro do dependente pensionista não aparece na integração financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39376429739415-Parceiro-do-dependente-pensionista-n%C3%A3o-aparece-na-integra%C3%A7%C3%A3o-financeira"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:16Z"
rotulos: ["Parceiro", "Movimentação Financeira", "Financeiro", "eSocial", "Gerenciador de Folhas", "Configuração Funcionários", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Parceiro do dependente pensionista não aparece na integração financeira

**Mensagem**

O sistema não apresenta o parceiro responsável pelo recebimento da pensão na tela "Gerenciador de Folhas" no icone **"Integração Financeira por Eventos"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas), mesmo com todas as parametrizações corretamente realizadas.

![Imagem 1: O sistema não apresenta o parceiro responsável pelo recebimento da pensão na tela "Gerenciador de Folhas" no icone…](https://ajuda.sankhya.com.br/hc/article_attachments/41184175404567)

**Situação**

Ao realizar o processamento de pensão alimentícia utilizando o evento 522 (Pensão sobre Férias) ou **qualquer outro evento de desconto de pensão**, o sistema não vincula automaticamente o parceiro responsável pelo recebimento da pensão.

Nessa situação, o campo **"Usar parceiro responsável pelo recebimento da pensão"** permanece desabilitado, impedindo que o lançamento financeiro seja gerado com o favorecido correto.

**Solução**

Para resolver o problema, siga os passos abaixo:

**(1)** Acesse a tela **"Configuração Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários), localize o colaborador e acesse a aba **"Dependentes"**.

![Imagem 2: Selecione o dependente marcado como pensionista e remova temporariamente o código do parceiro responsável pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/41185216845463)

**(2)** Selecione o dependente marcado como pensionista e remova temporariamente o código do parceiro responsável pelo recebimento da pensão.

**(3)** Inclua novamente o código do parceiro responsável no campo correspondente e salve o cadastro. Esta ação força o sistema a replicar corretamente as informações nos campos necessário para realizar o processo da integração.

[GIF animado: Imagem 3: Certifique-se de que o campo "Percentual de repasse" está preenchido no cadastro do dependente pensionista.](https://ajuda.sankhya.com.br/hc/article_attachments/41185233028503)

 

**(4)** Certifique-se de que o campo **"Percentual de repasse"** está preenchido no cadastro do dependente pensionista.

**(5)** Acesse novamente a rotina de Gerenciador de Folhas (Pessoal+ » Rotinas Folha » Gerenciador de Folhas), no ícone de **"Integração Financeira por Eventos"** busque o colaborador e verifique se o campo **"Usar parceiro responsável pelo recebimento da pensão"** está habilitado e se o parceiro correto está sendo apresentado.

**(6)**  Verifique se na rotina de ' Configuração de integração financeira' () o item de pensionista, existe parceiro cadastrado.

**Observação:** É importante que o evento de pensão seja cadastrado na configuração do funcionário, pois é por meio desse vínculo que o sistema preenche corretamente as informações exigidas referentes ao responsável pelo recebimento da pensão.

Além disso, esse cadastro permite a identificação adequada do dependente pensionista, garantindo que os dados sejam enviados corretamente ao eSocial e evitando rejeições no evento [**S-1210 relacionadas à pensão alimentícia**](https://ajuda.sankhya.com.br/hc/pt-br/articles/39372683385239-Erro-8-Grupo-Informa%C3%A7%C3%A3o-dos-benefici%C3%A1rios-da-pens%C3%A3o-aliment%C3%ADcia-deve-ser-preenchido).

**Causa**

O problema ocorre porque o campo **resposansavél em armazenar a informação do responsavél pelo recebimento** não foi alimentado corretamente nas na folha e na movimentação do colaborador. Isso pode acontecer quando:

- O evento de pensão é incluído manualmente na folha, sem passar pelo cadastro padrão de dependentes;
- O cadastro do dependente pensionista foi alterado, mas o sistema não replicou as informações para as tabelas de folha e movimento;
- O percentual de repasse da pensão não foi informado no cadastro do dependente.

Quando essas informações não estão corretamente vinculadas, o sistema não consegue identificar qual parceiro deve receber o pagamento da pensão alimentícia, impedindo a integração financeira adequada.
