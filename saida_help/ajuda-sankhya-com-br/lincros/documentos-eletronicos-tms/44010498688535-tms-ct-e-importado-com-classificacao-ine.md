---
id: "44010498688535"
titulo: "[TMS] - CT-e importado com classificação inesperada (documento fiscal e/ou pré-conhecimento)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010498688535--TMS-CT-e-importado-com-classifica%C3%A7%C3%A3o-inesperada-documento-fiscal-e-ou-pr%C3%A9-conhecimento"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T18:39:04Z"
rotulos: ["sync_hc", "lincros", "lincros_16961645", "sync_hash_54287db0a152"]
---

# [TMS] - CT-e importado com classificação inesperada (documento fiscal e/ou pré-conhecimento)

Ao importar um CT-e, dois campos diferentes podem receber uma classificação que você não esperava: (1) o tipo do próprio documento fiscal (aparece em CT-es x Nfs-es) e (2) o "Tipo" do pré-conhecimento vinculado (Serviço x Eletrônico). Os dois compartilham parte da mesma lógica de decisão, mas são campos distintos, em telas distintas, com regras próprias de edição — este artigo trata os dois pontos separadamente para evitar que o ajuste de um seja confundido com o do outro.

## PONTO 1 — Classificação do documento fiscal (CT-e aparece como Nfs-e, ou vice-versa)

**Onde aparece:** telas "Documentos Eletrônicos > CT-es" / "Documentos Eletrônicos > Nfs-es".

**Causa:** definida no momento da importação do CT-e. As duas rotas mais comuns e mais fáceis de diagnosticar são:

1. **CT-e com ISS destacado (maior que zero):** classificação direta — o documento é classificado como **Serviço** (aparece em Nfs-es). Essa é a rota mais simples de diagnosticar.
2. **CT-e sem ISS destacado, mas com mesma localização + cadastro da transportadora:** o sistema verifica:

   - Se origem e destino da operação correspondem à **mesma localização** (não necessariamente o mesmo texto de município exibido na tela — pode envolver uma localização/praça já cadastrada no pré-conhecimento, recorrendo ao CEP apenas quando essa localização não está definida); **e**
   - Se a transportadora responsável está cadastrada (configuração geral, ou uma configuração específica por transportadora + cliente) com a opção de emitir documento de serviço para frete municipal habilitada.

   Se as duas condições acima se confirmarem, o documento também é classificado como **Serviço** — mesmo sem ISS destacado no XML. Caso contrário, o documento permanece como **Frete/Eletrônico** (CT-e padrão).
3. **Outros fatores de validação:** essas duas rotas não esgotam a lógica. Já identificamos casos em que o sistema considera também a **presença de chave de acesso vinculada** e outras validações do documento para decidir a classificação — inclusive casos de CT-e **intermunicipal** (origem e destino diferentes) importado como Nfs-e mesmo sem ISS destacado ou configuração de transportadora que expliquem o resultado. Se o seu caso não se encaixa nas rotas 1 e 2, entre em contato com o suporte Lincros informando o CT-e, o XML e o trajeto da operação, para que possamos avaliar o caso específico.

**Ponto de atenção para diagnóstico:** um CT-e sem ISS e com chave de acesso de transporte pode legitimamente aparecer como "Serviço" — isso não é, por si só, indício de erro no XML de origem. Antes de solicitar reemissão à transportadora, verifique se a operação tem origem e destino na mesma localização e se a transportadora está com essa configuração habilitada para o cliente em questão. Se a classificação não se explica por nenhuma dessas rotas conhecidas — por exemplo, uma operação claramente intermunicipal que ainda assim saiu como Serviço/Nfs-e — não assuma automaticamente que há erro de ISS no XML: pode ser um dos "outros fatores" do item 3. Nesse caso, antes de solicitar reemissão à transportadora, reúna o CT-e, o XML e o trajeto da operação e abra um chamado com o suporte Lincros para avaliação.

**Editável?** Não. Esse campo (do documento CT-e/NFS-e em si) não tem opção de ajuste manual na tela — é sempre resultado direto da importação, seja pela rota do ISS, seja pela rota de município + cadastro da transportadora.

**Como corrigir:**

1. **Se a causa for o cadastro da transportadora** (mesma localização + opção habilitada indevidamente): revisar essa configuração no cadastro da transportadora corrige a classificação de **novos** CT-es importados a partir daí. Não corrige retroativamente os documentos já importados.
2. **Se a causa for um valor de ISS incorreto no XML:** a transportadora precisa corrigir e reemitir o documento fiscal; o Lincros reimporta e a classificação sai certa automaticamente, aplicando a mesma regra sobre o dado correto.
3. **Se a transportadora não puder reemitir** (documento já autorizado na SEFAZ, com o valor fiscal real sendo esse mesmo que gerou a classificação): abra um chamado com o suporte Lincros para avaliação de reprocessamento manual — não é um ajuste de tela.

## Como localizar um CT-e classificado como Serviço

Um CT-e classificado como **Serviço** (Ponto 1) já foi importado com sucesso e está integrado normalmente — mas, na tela padrão **"Documentos Eletrônicos > CT-es"**, ele pode não aparecer na busca por número/chave se o filtro de coluna "Tipo" não estiver configurado para incluir "Serviço". Isso é frequentemente confundido com erro de importação ou de indexação, quando na verdade é apenas um ajuste de filtro. Para localizar esse documento, use uma das opções abaixo:

- **Na própria tela "Documentos Eletrônicos > CT-es":** adicione a coluna/filtro "Tipo" e informe o valor "Serviço" ao buscar. Sem esse filtro explícito, a busca padrão pode não retornar documentos desse tipo.
- **Tela alternativa (já traz o filtro por padrão):** acesse Operacional > Conhecimentos de frete, onde a coluna "Tipo" já vem habilitada na busca por padrão, facilitando a localização de CT-es de Serviço sem configuração adicional.

Se, mesmo com o filtro de Tipo = Serviço aplicado, o documento não aparecer em nenhuma das duas telas, aí sim pode se tratar de um problema de importação (ver artigo de erros de importação de EDI) — não de busca/filtro.

## PONTO 2 — "Tipo" do pré-conhecimento (Serviço x Eletrônico)

**Onde aparece:** campo "Tipo" na tela de edição do pré-conhecimento.

**Causa:** definida por uma sequência de critérios avaliados na importação do CT-e vinculado:

1. Transportadora é Correios? → classificação especial própria, não segue as demais regras.
2. Origem e destino da operação são a mesma localização **e** a transportadora está configurada (cadastro geral ou cadastro específico por cliente) com a opção de emitir documento de serviço para frete municipal habilitada → Serviço.
3. Se nenhuma condição acima se aplicar → Eletrônico.

Atenção: assim como no Ponto 1, a comparação de "mesma localização" não é necessariamente uma comparação simples de texto de município — pode envolver uma localização/praça já vinculada ao pré-conhecimento, recorrendo ao CEP/município só quando essa localização não estiver definida. Isso explica por que dois casos com município aparentemente igual podem ter resultados diferentes.

**Importante — origem/destino é da Nota Fiscal, não do trajeto do CT-e:** a comparação de "mesma localização" usada nesse critério é feita a partir do **endereço de origem/entrega informado na Nota Fiscal vinculada** ao pré-conhecimento — não a partir do trajeto real percorrido pela transportadora no CT-e. Isso gera um mal-entendido recorrente: você pode notar que "o CT-e passou por outro município" e mesmo assim o pré-conhecimento sair como Serviço, porque o endereço de entrega da NF está no mesmo município da origem. Ao diagnosticar, confirme sempre o endereço da NF vinculada (não apenas o trajeto do CT-e) antes de considerar a classificação um erro.

**Editável?** Sim — é um campo de seleção na tela do pré-conhecimento, e a alteração manual persiste após salvar.

**Como corrigir:**

- **Pontual:** ajuste manualmente o campo "Tipo" na tela do pré-conhecimento já represado. Correção imediata, não depende de reimportação.
- **Preventivo** (para padrões recorrentes, ex. muitos casos do mesmo município/transportadora): revise o cadastro da transportadora responsável — a opção de emissão de documento de serviço para frete municipal pode estar habilitada indevidamente para aquele contexto. Desabilitá-la evita que **novos** CT-es do mesmo padrão continuem sendo classificados como Serviço. Não corrige retroativamente os pré-conhecimentos já represados na fila — esses ainda precisam do ajuste manual pontual.

## Relação entre os dois pontos

Os dois pontos **não são totalmente independentes**: quando o CT-e não tem ISS destacado, tanto a classificação do documento (Ponto 1) quanto a do pré-conhecimento (Ponto 2) são decididas pela **mesma verificação** — mesma localização de origem/destino + cadastro da transportadora. Por isso, é comum que os dois apareçam classificados como "Serviço" ao mesmo tempo nesse cenário.

Ainda assim, são **campos distintos, em telas distintas, com regras de edição diferentes**:

- O campo do documento (Ponto 1) não é editável.
- O campo do pré-conhecimento (Ponto 2) é editável, e a edição não afeta o campo do documento.

Ajustar o cadastro da transportadora (opção "emite documento de serviço para frete municipal") afeta **ambos** os pontos de forma preventiva para novos CT-es, mas não corrige retroativamente nenhum dos dois para os casos já importados.
