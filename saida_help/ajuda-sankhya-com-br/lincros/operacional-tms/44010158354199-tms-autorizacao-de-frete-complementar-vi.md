---
id: "44010158354199"
titulo: "[TMS] - Autorização de Frete Complementar via Portal do Transportador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010158354199--TMS-Autoriza%C3%A7%C3%A3o-de-Frete-Complementar-via-Portal-do-Transportador"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:31:27Z"
rotulos: ["sync_hc", "lincros", "lincros_13433427", "sync_hash_76f8491cd602"]
---

# [TMS] - Autorização de Frete Complementar via Portal do Transportador

**Menu**: No acesso do transportador - Operacional > Conhecimentos de frete > Autorização de frete complementar

**Objetivo**: Esse recurso é utilizado quando o transportador precisa emitir um complemento de frete e solicita ao embarcador a validação do documento;

## Considerações:

- Ter um CT-e do tipo Normal e suas respectivas notas fiscais importadas no TMS;

## Transportador

1. Na tela inicial do menu, (Operacional > Conhecimentos de frete > Autorização de frete complementar) no portal do transportador, são listados todos os registros e suas principais informações, sendo possível acompanhar também a situação do documento em relação a sua aprovação: aguardando aprovação, deferido, indeferido, cancelado;

![Imagem 1: Na tela inicial do menu, (Operacional > Conhecimentos de frete > Autorização de frete complementar) no portal do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010189393687)

2. Para criar um conhecimento complementar, clique em "Novo" e faça o preenchimento dos campos;

![Imagem 2: 2. Para criar um conhecimento complementar, clique em "Novo" e faça o preenchimento dos campos;](https://ajuda.sankhya.com.br/hc/article_attachments/44010175230743)

**Filial**: Unidade/filial da transportadora;

**Empresa**: nome do embarcador;

**Unidade**: unidade da empresa embarcadora.

![Imagem 3: Unidade : unidade da empresa embarcadora.](https://ajuda.sankhya.com.br/hc/article_attachments/44010148260247)

**Valor total do frete**: Informe o valor do frete;

**Modal**: Selecione o modelo de transporte utilizado;

**Tipo**: Defina o tipo do documento: complementar, reentrega, diária, descarga etc;

**CT-e referência**: Informe o número do CT-e ou use a lupa para localizar o conhecimento original;

**Notas fiscais**: Selecione as notas fiscais correspondentes;

**Observação**: É possível incluir uma observação, inserir uma imagem ou link ao documento no sistema.

Finalizado o processo, clique em "Salvar".

![Imagem 4: Finalizado o processo, clique em "Salvar".](https://ajuda.sankhya.com.br/hc/article_attachments/44010159049367)

**Obs**.: Os campos que aparecem em vermelho são de preenchimento obrigatório.

Além do portal do transportador, o CT-e do tipo complementar também pode ser criado através da importação do XML.

**Atenção — CT-e complementar do tipo "Complemento de Valores" importado via XML:** nesse caso específico, o campo "Notas fiscais"/"Documentos fiscais da carga" do CT-e complementar não é preenchido diretamente — ele não recebe a nota fiscal cadastrada nele mesmo. A(s) nota(s) fiscal(is) são herdadas do CT-e original que ele referencia, e o painel só aparece preenchido quando esse vínculo com o CT-e de origem está corretamente estabelecido. Se o campo estiver vazio, não tente vincular a NF diretamente no complementar: confirme antes o número/chave do CT-e original e se a nota já está anexada a ele — o vínculo do complementar é resolvido a partir daí, não por seleção manual de nota no próprio complementar.

**Atenção — "Devolução" não é um tipo fiscal reconhecido pela SEFAZ:** o campo que define o tipo do CT-e perante a SEFAZ (tpCTe, no XML) aceita apenas 4 valores — Normal, Complemento de Valores, Anulação ou Substituto. Não existe um tipo "Devolução" nesse campo oficial. Por isso, quando uma nota de devolução referencia a nota de venda, o Lincros cria automaticamente um pré-conhecimento do tipo **Complementar** (mesmo a operação sendo, na prática, uma devolução) — o sistema está refletindo fielmente o que foi autorizado pela SEFAZ, não se trata de erro de classificação. A palavra "Devolução" que aparece em campos de observação/motivo do documento é só descritiva, não corresponde ao tipo fiscal oficial.

## Embarcador

Após o transportador realizar a solicitação do frete complementar pelo portal, é de responsabilidade do embarcador deferir/indeferir a autorização, abaixo alguns critérios que são importantes:

- Este processo utiliza alçada de aprovação, desta forma é preciso que no menu: Cadastros gerais > configurações de empresa > parâmetros > empresa conste o parâmetro: usarAlcadaAprovacaoConhecimento = true;
- No menu Cadastros gerais > configurações da empresa > workflow > alçadas de aprovação, realizar o cadastro da alçada marcando o Tipo de restrição Conhecimento (maiores informações sobre alçada de aprovação, consultar o artigo '[[TMS] - Como configurar a alçada de aprovação](https://intercom.help/ajudalincros/pt-BR/articles/13439012-tms-como-configurar-a-alcada-de-aprovacao)');
- Quando o transportador salvar a solicitação de autorização de frete, é criado um pré conhecimento do tipo informado pela transportadora, vinculado à nota fiscal;
- É criada uma cotação spot para este conhecimento, já com situação confirmada com a determinada transportadora. É criada uma cotação, pois não há uma tabela de frete vinculado, sendo um preço informado pelo usuário;
- Devido ao vínculo com a cotação spot, não é possível realizar modificações no mesmo;
- O pré-conhecimento criado fica com situação 'Aguardando aprovação'. O usuário que possui alçada de aprovação deverá 'deferir' ou 'indeferir' o pré conhecimento;

Caso seja indeferido o pré conhecimento: o pré-conhecimento perde o vínculo com a nota fiscal; a cotação spot é cancelada; a situação de aprovação é alterada para 'Indeferido'.

Caso seja deferido o pré conhecimento: a situação de aprovação é alterada para 'Deferido'.

## Envio de e-mail

Para disparar emails nesta rotina, é necessário habilitar os parâmetros, conforme desejado:

- enviarEmailAberturaSolicitacaoAutorizacaoFrete - envia e-mail para o usuário da transportadora que está criando a solicitação e para os prováveis aprovadores da alçada de aprovação do frete;
- enviarEmailTranspDeferirSolicitacaoAutorizacaoFrete - envia e-mail para os usuários da filial da transportadora do conhecimento informando que o mesmo foi deferido;
- enviarEmailTranspIndeferirSolicitacaoAutorizacaoFrete - envia e-mail para os usuários da filial da transportadora do conhecimento informando que o mesmo foi indeferido;

**Obs.:** Para que estes parâmetros sejam habilitados, entrar em contato com o HelpDesk.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
