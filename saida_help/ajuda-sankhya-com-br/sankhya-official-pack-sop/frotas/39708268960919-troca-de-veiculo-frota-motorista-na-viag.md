---
id: "39708268960919"
titulo: "Troca de Veículo | Frota | Motorista na Viagem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39708268960919-Troca-de-Ve%C3%ADculo-Frota-Motorista-na-Viagem"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-07-22T13:28:05Z"
rotulos: ["MDF-e", "Veículo", "SEFAZ", "Transporte", "Viagem", "Troca de Veículo", "Motorista na Viagem", "MDF-e da viagem", "Frota", "Interrupção", "Interrupção de Viagem", "MDF-e não Encerrado", "Documentos Eletrônicos", "Motorista"]
---

# Troca de Veículo | Frota | Motorista na Viagem

Este documento descreve o comportamento do sistema ao realizar a troca de veículo e/ou motorista durante uma viagem em andamento, utilizando a aba **''Interrupção de Viagem''** na tela de **''Viagem do TMS''**.

O processo envolve o encerramento automático do MDF-e vigente e a geração automática de um novo MDF-e com os dados atualizados (placa, motorista, nova origem), mantendo os documentos fiscais originais (CT-e / NF-e).

#### Regras para Troca de Veículo e/ou Motorista

- Para efetuar a troca de veiculo ou motorista, **o MDF-e da viagem deve estar encerrado**. Caso o MDF-e esteja apenas autorizado e ainda não encerrado, o sistema exibirá uma mensagem de erro e não permitirá a troca.
- Após o encerramento do MDF-e, ao confirmar a interrupção com a nova troca, o sistema encerrará o manifesto atual e gerará automaticamente um novo MDF-e com os dados da nova etapa da viagem.

| A troca de veículo/motorista **somente é permitida** se o MDF-e vinculado à etapa atual estiver encerrado (ou ainda não emitido).  Ao confirmar a interrupção com troca, o sistema encerra automaticamente o MDF-e da etapa anterior.  Um **novo MDF-e é gerado automaticamente** para a próxima etapa, considerando como origem o ponto de interrupção.  Os documentos fiscais originais (**CT-e / NF-e**) são mantidos e reaproveitados no novo MDF-e.  O novo MDF-e reflete o local de início da nova etapa, bem como o novo veículo e/ou motorista informado. |
| --- |

#### Pré-Requisitos

**(1)** Viagem gerada com Nota Fiscal, CT-e e MDF-e devidamente associados.

**(1)** MDF-e autorizado (aprovado) pela SEFAZ.

**(1)** Acesso ao módulo **TMS** com permissão para lançar interrupções de viagem.

#### Visão Geral do Fluxo Operacional

**(1)** **Gere a Viagem**:

Crie a viagem vinculando os documentos necessários (**Nota Fiscal**, **CT-e** e **MDF-e**) e aguarde a autorização do MDF-e.

**(2)** **Acesse a aba ''Interrupção de Viagem'':**

Na tela de ''Viagem do TMS'', acesse a aba destinada ao registro de interrupções e informe o ponto de parada (origem e destino parcial da etapa).

**(3)** **Informe o novo Veículo e/ou Motorista**:

Na janela de interrupção, selecione o novo veículo e/ou motorista que dará continuidade á viagem a partir desse ponto.

**(4)** **Verifique o status do MDF-e**:

Antes de confirmar a operação, certifique-se de que o MDF-e da etapa atual está devidamente encerrado. Caso contrário, o sistema impedirá a continuidade do processo.

**(5)** **Confirme a Interrupção**:

Ao confirmar a interrupção, o sistema marca a viagem atual como interrompida, cria automaticamente um novo registro de continuidade e realiza a geração de um novo MDF-e para a próxima etapa.

**(6)** **Aprove o novo MDF-e**:

Acesse o MDF-e gerado automaticamente e realize sua aprovação antes de iniciar a próxima etapa da viagem.

**(7)** **Repita para cada troca necessária**:

O processo pode ser repetido quantas vezes necessários, desde que o MDF-e da etapa vigente esteja devidamente aprovado antes de realizar uma nova interrupção.

#### Exemplo Prático - Viagem Goiânia → Uberaba

Exemplo de viagem com 3 interrupções, cada uma com troca de veículo e/ou motorista.

Rota total: Goiâna → Uberaba.

- **Veículo inicial**: 3
- **Motorista inicial**: 32
- **Origem**: Goiâna - GO
- **Destino final**: Uberaba - MG

![Imagem 1: Destino final : Uberaba - MG](https://ajuda.sankhya.com.br/hc/article_attachments/39708268919575)![Imagem 2: Destino final : Uberaba - MG](https://ajuda.sankhya.com.br/hc/article_attachments/39708268920983)![Imagem 3: Destino final : Uberaba - MG](https://ajuda.sankhya.com.br/hc/article_attachments/39708268921495)

#### 1. Primeira Interrupção - Troca de Motorista

**Goiânia** **→ Goiatuba**

**Troca realizada**: Motorista

**Ponto de Interrupção**: Goiatuba - GO

**Próxima etapa**: Goiatuba - GO → Uberaba

| O registro do trecho **Goiânia → Goiatuba** é marcado como interrompido, e um novo registro de continuidade (**Goiatuba → Uberaba**) é criado com o novo motorista.  O MDF-e do trecho anterior é encerrado, e um novo MDF-e é gerado automaticamente para o trecho **Goiatuba → Uberaba**. |
| --- |

![Imagem 4: O MDF-e do trecho anterior é encerrado, e um novo MDF-e é gerado automaticamente para o trecho Goiatuba → Uberaba .](https://ajuda.sankhya.com.br/hc/article_attachments/39708307227927)![Imagem 5: O MDF-e do trecho anterior é encerrado, e um novo MDF-e é gerado automaticamente para o trecho Goiatuba → Uberaba .](https://ajuda.sankhya.com.br/hc/article_attachments/39708268925975)![Imagem 6: O MDF-e do trecho anterior é encerrado, e um novo MDF-e é gerado automaticamente para o trecho Goiatuba → Uberaba .](https://ajuda.sankhya.com.br/hc/article_attachments/39708307230615)![Imagem 7: O MDF-e do trecho anterior é encerrado, e um novo MDF-e é gerado automaticamente para o trecho Goiatuba → Uberaba .](https://ajuda.sankhya.com.br/hc/article_attachments/39708268928279)![Imagem 8: O MDF-e do trecho anterior é encerrado, e um novo MDF-e é gerado automaticamente para o trecho Goiatuba → Uberaba .](https://ajuda.sankhya.com.br/hc/article_attachments/39708268930455)![Imagem 9: O MDF-e do trecho anterior é encerrado, e um novo MDF-e é gerado automaticamente para o trecho Goiatuba → Uberaba .](https://ajuda.sankhya.com.br/hc/article_attachments/39708307234839)![Imagem 10: O MDF-e do trecho anterior é encerrado, e um novo MDF-e é gerado automaticamente para o trecho Goiatuba → Uberaba .](https://ajuda.sankhya.com.br/hc/article_attachments/39708307235607)

#### 2. Segunda Interrupção - Troca de Veículo

**Goiânia** **→ Itumbiara**

**Troca realizada**: Veículo

**Ponto de Interrupção**: Itumbiara - GO

**Próxima etapa**: Itumbiara → Uberaba

| Se o MDF-e não estiver aprovado ao tentar registrar a interrupção, o sistema exibirá uma mensagem de erro, bloqueando a operação até que a aprovação seja realizada.  Após a aprovação do MDF-e, o registro do trecho **Goiatuba → Itumbiara** é marcado como interrompido, e um novo registro (**Itumbiara → Uberaba**) é criado com o novo veículo.  O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho **Itumbiara → Uberaba**, considerando a nova placa e os dados atualizados. |
| --- |

![Imagem 11: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho Itumbiara → Uberaba , considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/39708307236119)![Imagem 12: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho Itumbiara → Uberaba , considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/39708268933527)![Imagem 13: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho Itumbiara → Uberaba , considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/39708268935447)![Imagem 14: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho Itumbiara → Uberaba , considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/39708307238039)![Imagem 15: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho Itumbiara → Uberaba , considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/39708268937239)![Imagem 16: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho Itumbiara → Uberaba , considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/39708268938135)![Imagem 17: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho Itumbiara → Uberaba , considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/39708268939287)![Imagem 18: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado para o trecho Itumbiara → Uberaba , considerando…](https://ajuda.sankhya.com.br/hc/article_attachments/39708307245335)

#### 3. Terceira Interrupção - Troca de Motorista e Veículo

**Itumbiara** **→ Uberlândia**

**Troca realizada**: Veículo + Motorista

Ponto de Interrupção: Uberlândia - MG

Próxima etapa: Uberlândia → Uberaba

| O registro do trecho **Itumbiara → Uberlândia** é marcado como interrompido, e um novo registro é criado com o novo veículo e o novo motorista.  O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista para a última etapa da viagem. |
| --- |

![Imagem 19: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista…](https://ajuda.sankhya.com.br/hc/article_attachments/39708307246871)![Imagem 20: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista…](https://ajuda.sankhya.com.br/hc/article_attachments/39708307247895)![Imagem 21: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista…](https://ajuda.sankhya.com.br/hc/article_attachments/39708307249815)![Imagem 22: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista…](https://ajuda.sankhya.com.br/hc/article_attachments/39708307250839)![Imagem 23: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista…](https://ajuda.sankhya.com.br/hc/article_attachments/39708307254039)![Imagem 24: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista…](https://ajuda.sankhya.com.br/hc/article_attachments/39708268945175)![Imagem 25: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista…](https://ajuda.sankhya.com.br/hc/article_attachments/39708268945943)![Imagem 26: O MDF-e anterior é encerrado automaticamente, e um novo MDF-e é gerado com os dados atualizados de veículo e motorista…](https://ajuda.sankhya.com.br/hc/article_attachments/39708268946583)

#### Resumo do Fluxo de Interrupções

| Trecho | Origem → Destino | Troca | MDF-e Anterior | Novo MDF-e |
| --- | --- | --- | --- | --- |
| 0 | Goiânia → Uberaba | – | – | Emitido e Autorizado |
| 1ª | Goiânia → Goiatuba | Motorista | Encerrado | Gerado automaticamente |
| 2ª | Goiatuba → Itumbiara | Veículo | Encerrado | Gerado automaticamente |
| 3ª | Itumbiara → Uberlândia | Veículo + Motorista | Encerrado | Gerado automaticamente |

#### Mensagem de Erro - MDF-e não Encerrado

Ao tentar registrar uma interrupção com troca de veículo e/ou motorista **enquanto o MDF-e estiver autorizado**, **porém não encerrado**, **o sistema exibirá uma mensagem de erro** solicitando o encerramento do MDF-e antes de prosseguir.

A operação permanecerá bloqueada até que o MDF-e seja devidamente encerrado.

![Imagem 27: A operação permanecerá bloqueada até que o MDF-e seja devidamente encerrado.](https://ajuda.sankhya.com.br/hc/article_attachments/39708268949015)

##### OBSERVAÇÃO:

- O novo MDF-e gerado automaticamente deve ser **aprovado manualmente** antes de iniciar a próxima etapa ou realizar nova interrupção.
- Cada etapa da viagem gera um **registro independente no sistema**, permitindo rastreabilidade completa do transporte.
- Os documentos fiscais (**CT-e / NF-e**) **não são reemitidos** — apenas o MDF-e é encerrado e recriado para cada etapa.
- O processo é compatível com **múltiplas trocas sequenciais** ao longo de uma mesma viagem.
