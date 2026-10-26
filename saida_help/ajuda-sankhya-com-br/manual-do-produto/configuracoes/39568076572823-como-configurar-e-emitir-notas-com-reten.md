---
id: "39568076572823"
titulo: "Como configurar e emitir notas com retenção de PIS/COFINS (Nota Gateway)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39568076572823-Como-configurar-e-emitir-notas-com-reten%C3%A7%C3%A3o-de-PIS-COFINS-Nota-Gateway"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:01:15Z"
rotulos: ["Configuração", "Central de Vendas", "Impostos", "Financeiro", "Retenção", "NFS-e", "PIS/COFINS", "Como configurar e emitir notas com retenção de PIS/COFINS (Nota Gateway)", "Nota Gateway"]
---

# Como configurar e emitir notas com retenção de PIS/COFINS (Nota Gateway)

**Módulo:** Configuração › Cadastros
**Caminho de acesso:** **Menu Principal › Configuração › Cadastros ›** [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)
**Versão mínima:** 4.35b612 ou superior

---

## O que é e para que serve

Este artigo explica como configurar o Sankhya Om para calcular e enviar corretamente as retenções de PIS e COFINS na emissão de notas fiscais de serviço via Nota Gateway. O procedimento garante que as notas sejam autorizadas na prefeitura sem rejeições por falta de tags fiscais, cobrindo tanto o cenário de retenção direta na nota quanto a retenção via módulo Financeiro. O artigo não cobre a configuração geral de impostos no sistema — apenas as parametrizações específicas para retenção de PIS e COFINS.

---

## Antes de começar

- **Permissões necessárias:** acesso às telas de [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos), [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) e [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas).
- **Configurações relacionadas:** Tipo de Operação (TOP) vinculado e autorizado a calcular a retenção, configurada na aba **TOP** do cadastro de impostos.

---

## Como funciona a hierarquia de envio (nota x financeiro)

O sistema possui uma lógica automática para montar o arquivo enviado à prefeitura. Ele busca os dados de retenção respeitando a seguinte ordem:

1. **Prioridade na nota:** o sistema verifica se a aba [Outros Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es#outrosimpostos) possui PIS/COFINS retido. Se sim, envia esses valores.
2. **Busca no financeiro:** se a nota não possuir o imposto destacado, o sistema busca automaticamente no título gerado no módulo Financeiro. Se encontrar a retenção lá, preenche as tags corretamente e envia a nota.

**⚠️ Atenção**

O sistema nunca duplica as informações. Se houver dados calculados tanto na nota quanto no financeiro, o envio prioriza os valores da **nota fiscal**, ignorando os dados do financeiro na montagem do JSON.

---

## Passo a passo: parametrização dos impostos

Para que o sistema saiba onde aplicar a retenção (na nota ou no financeiro), configure as regras no cadastro de impostos.

1. Acesse a tela [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos).
2. Selecione ou crie o imposto desejado (ex: PIS ou COFINS).
3. No [painel principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#configuraesiniciais), preencha as definições gerais (**Nome**, **Tipo**, **Base para impostos**).
4. Navegue até as abas inferiores ([**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaempresa), [**Parceiro**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaparceiro) e [**Serviço**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaservio)).
5. Preencha as alíquotas e defina o local da retenção conforme o cenário:

**Para reter na nota fiscal:**

- Na aba [**Serviço**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaservio), no campo [**Na Nota**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos#abaservio:~:text=vinculado%20ao%20imposto%20cadastrado.-,Voc%C3%AA%20pode%20definir%20o%20campo%20%22Na%20Nota%22%20de%20acordo%20com%20as%20seguintes%20op%C3%A7%C3%B5es%3A,-Subtrair%3A%20Ocorrer%C3%A1%20a), selecione **Subtrair**.
- No campo **No Financeiro de Origem Estoque**, selecione **Nenhum**. Com essa configuração, o valor da nota na Central passa a representar o valor do serviço com a dedução dos impostos retidos, enquanto no financeiro é considerado o valor líquido.

**Para reter apenas no financeiro:**

- No campo **Na Nota**, selecione **Incluso**.
- No campo **No Financeiro de Origem Estoque**, selecione **Subtrair**. Com essa configuração, o valor da nota na Central passa a representar o valor do serviço sem a dedução dos impostos retidos, enquanto no financeiro é considerado o valor bruto, com os impostos devidamente provisionados.

**💡 Dica**

Verifique também a aba **TOP** no cadastro de impostos para garantir que o Tipo de Operação utilizado na emissão está devidamente vinculado e autorizado a calcular essa retenção.

---

## Passo a passo: emissão na Central de Vendas

Após a parametrização, realize a emissão normalmente:

1. Acesse a [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).
2. Lance o cabeçalho informando a Empresa, Parceiro e TOP configurados.
3. Insira o item (Serviço) e confirme.
4. Para validar se o cálculo ocorreu na nota, selecione o item inserido, acesse as opções secundárias da grade de itens e clique em [**Outros Impostos Item da Nota**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#outrosimpostos).
5. Verifique se os impostos aparecem com o **Tipo Imposto** igual a **Retido** e com os valores corretos de **Base**, **Alíquota** e **Valor**.

**💡 Dica**

Se você configurou a retenção para ocorrer no módulo financeiro, essa grade de impostos do item estará vazia. O valor será deduzido e demonstrado apenas na aba **Financeiro** da nota. Para saber mais sobre a emissão via Nota Gateway, acesse [NFS-e e Reforma Tributária — Configuração e Uso do IBS/CBS via Nota Gateway](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881878261143-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway).

---

## Resultado esperado

1. Acesse o [**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) e aprove a nota fiscal.
2. O sistema acionará a integração.
3. O arquivo JSON gerado nos bastidores conterá as tags obrigatórias preenchidas corretamente (ex: `"tipoRetencaoPisCofins": "PisCofinsRetido"`), acompanhadas dos valores exatos de PIS e COFINS, garantindo a aprovação do documento na prefeitura sem falhas de integração.
